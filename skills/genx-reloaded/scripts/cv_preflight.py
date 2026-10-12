#!/usr/bin/env python3
"""Inspect local CV extraction; never predict ATS acceptance or hiring outcomes."""

import argparse
import json
import re
import sys
import unicodedata
import zipfile
from pathlib import Path
from urllib.parse import unquote
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
CONTENT_TYPES = "{http://schemas.openxmlformats.org/package/2006/content-types}"
COMMENTS_TYPE = "application/vnd.openxmlformats-officedocument.wordprocessingml.comments+xml"
XML_LIMIT = 20_000_000
EMAIL = re.compile(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", re.UNICODE)
LIMITATION = (
    "Local extraction and structural observations only. No ATS emulation, "
    "hiring prediction, OCR, or visual certification. Review reading order "
    "and the rendered document separately. Not a complete metadata or privacy audit."
)


def normalise(value):
    value = unicodedata.normalize("NFKC", value).casefold()
    value = value.translate(str.maketrans({
        "\u2010": "-", "\u2011": "-", "\u2012": "-",
        "\u2013": "-", "\u2014": "-", "\u2212": "-",
        "\u2018": "'", "\u2019": "'",
    }))
    return " ".join(value.split())


def word_text(root):
    """Extract body order, excluding deletions and directly hidden runs.

    This is not Word's layout or style-inheritance engine. Style-based hidden
    settings are flagged separately and still need rendered inspection.
    """
    def visible_chunks(element):
        if element.tag in (W + "del", W + "moveFrom"):
            return
        if element.tag == W + "r":
            properties = element.find(W + "rPr")
            if properties is not None and any(
                item.tag in (W + "vanish", W + "webHidden") and active_switch(item)
                for item in properties
            ):
                return
        if element.tag == W + "t":
            yield element.text or ""
        elif element.tag == W + "tab":
            yield "\t"
        elif element.tag in (W + "br", W + "cr"):
            yield "\n"
        else:
            for child in element:
                yield from visible_chunks(child)

    parents = {child: parent for parent in root.iter() for child in parent}
    lines = []
    for paragraph in root.iter(W + "p"):
        ancestor = parents.get(paragraph)
        nested = False
        while ancestor is not None:
            if ancestor.tag == W + "p":
                nested = True
                break
            ancestor = parents.get(ancestor)
        if nested:
            continue
        if any(a.tag in (W + "del", W + "moveFrom") for a in ancestors(paragraph, parents)):
            continue
        lines.append("".join(visible_chunks(paragraph)))
    return "\n".join(lines)


def ancestors(element, parents):
    current = parents.get(element)
    while current is not None:
        yield current
        current = parents.get(current)


def contains_phrase(text, phrase):
    """Match normalised literal text without accepting a substring of a word."""
    start = r"(?<!\w)" if phrase[0].isalnum() or phrase[0] == "_" else ""
    end = r"(?!\w)" if phrase[-1].isalnum() or phrase[-1] == "_" else ""
    return re.search(start + re.escape(phrase) + end, text) is not None


def active_switch(element):
    return element.get(W + "val", "true").lower() not in ("0", "false", "off")


def add_finding(findings, code, detail):
    findings.append({"code": code, "detail": detail})


def inspect_docx(path, findings):
    with zipfile.ZipFile(path) as archive:
        # Comments are separate package parts, not visible main-body text.
        # Inspect even unanchored/resolved stored comments without reporting
        # their contents or authors. Do not extract package paths to disk.
        comment_parts = {"word/comments.xml"} & set(archive.namelist())
        metadata_size = 0
        if "[Content_Types].xml" in archive.namelist():
            metadata_size = archive.getinfo("[Content_Types].xml").file_size
            if metadata_size > XML_LIMIT:
                raise ValueError("DOCX XML is too large for this bounded inspection.")
            types = ET.fromstring(archive.read("[Content_Types].xml"))
            for item in types.findall(CONTENT_TYPES + "Override"):
                if item.get("ContentType") == COMMENTS_TYPE:
                    name = unquote(item.get("PartName", "")).lstrip("/")
                    if not name or name not in archive.namelist():
                        raise ValueError("DOCX declares a missing comments part.")
                    comment_parts.add(name)
        # Protect inspection from very large decompressed XML packages.
        names = [
            name for name in archive.namelist()
            if name in ("word/document.xml", "word/styles.xml")
            or re.fullmatch(r"word/(header|footer)\d+\.xml", name)
        ]
        if "word/document.xml" not in names:
            raise ValueError("DOCX has no word/document.xml.")
        selected = set(names) | comment_parts
        if metadata_size + sum(archive.getinfo(name).file_size for name in selected) > XML_LIMIT:
            raise ValueError("DOCX XML is too large for this bounded inspection.")
        roots = {name: ET.fromstring(archive.read(name)) for name in names}
        comments = sum(
            len(list(ET.fromstring(archive.read(name)).iter(W + "comment")))
            for name in sorted(comment_parts)
        )

    document = roots["word/document.xml"]
    body = document.find(W + "body")
    if body is None:
        raise ValueError("DOCX has no main document body.")
    text = word_text(body)
    supplemental = "\n".join(
        word_text(root) for name, root in roots.items()
        if re.fullmatch(r"word/(header|footer)\d+\.xml", name)
    )
    tables = len(list(body.iter(W + "tbl")))
    boxes = sum(len(list(root.iter(W + "txbxContent"))) for root in roots.values())
    hidden = sum(
        1 for root in roots.values()
        for item in root.iter()
        if item.tag in (W + "vanish", W + "webHidden") and active_switch(item)
    )
    tracked = sum(
        1 for root in roots.values()
        for item in root.iter()
        if item.tag in (W + "ins", W + "del", W + "moveFrom", W + "moveTo")
    )
    comment_markers = sum(
        1 for root in roots.values() for item in root.iter()
        if item.tag in (W + "commentRangeStart", W + "commentRangeEnd", W + "commentReference")
    )
    columns = 1
    for item in body.iter(W + "cols"):
        try:
            columns = max(columns, int(item.get(W + "num", "1")), len(item.findall(W + "col")))
        except ValueError:
            add_finding(findings, "invalid_column_metadata", "Inspect Word section settings.")
    observations = [
        (tables, "docx_tables", f"{tables} table(s); inspect reading order and associations."),
        (boxes, "docx_text_boxes", f"{boxes} text box(es); check essential content."),
        (hidden, "docx_hidden_text", f"{hidden} hidden-text setting(s); resolve before use."),
        (tracked, "docx_tracked_changes", f"{tracked} tracked-change element(s); resolve before use."),
        (comments or comment_markers, "docx_comments",
         f"{comments} stored comment(s), {comment_markers} comment marker(s); "
         "review and delete private comments from a submission copy. Hiding or resolving is not deletion."),
        (columns > 1, "docx_columns", f"Up to {columns} configured columns; inspect extraction order."),
    ]
    for present, code, detail in observations:
        if present:
            add_finding(findings, code, detail)
    extra_emails = set(EMAIL.findall(supplemental.casefold())) - set(EMAIL.findall(text.casefold()))
    if extra_emails:
        add_finding(
            findings, "header_footer_only_email",
            f"{len(extra_emails)} email address(es) appear only in a header or footer."
        )
    return text, supplemental, {
        "method": "DOCX main-body XML", "tables": tables, "text_boxes": boxes,
        "configured_columns": columns, "hidden_settings": hidden,
        "tracked_change_elements": tracked, "pages": None,
        "stored_comments": comments, "comment_markers": comment_markers,
    }


def inspect_pdf(path, findings):
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise ValueError("PDF inspection requires pypdf in the selected Python runtime.") from exc
    reader = PdfReader(str(path))
    if reader.is_encrypted and not reader.decrypt(""):
        raise ValueError("PDF requires a password; provide an accessible copy.")
    extracted = []
    page_chars = []
    for index, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ""
        extracted.append(text)
        count = len(normalise(text))
        page_chars.append(count)
        if count < 40:
            add_finding(
                findings, "sparse_pdf_page",
                f"Page {index} has {count} extracted characters; inspect for scans or missing text."
            )
    return "\n\n".join(extracted), "", {
        "method": "pypdf", "pages": len(extracted),
        "characters_per_page": page_chars,
    }


def inspect(path, required):
    findings = []
    extension = path.suffix.lower()
    if extension == ".docx":
        text, supplemental, structure = inspect_docx(path, findings)
    elif extension == ".pdf":
        text, supplemental, structure = inspect_pdf(path, findings)
    elif extension in (".txt", ".md"):
        text = path.read_text(encoding="utf-8-sig")
        supplemental = ""
        structure = {"method": "UTF-8 text", "pages": None}
    else:
        raise ValueError("Supported formats: .pdf, .docx, .txt, .md.")
    body_normalised = normalise(text)
    extra_normalised = normalise(supplemental)
    if len(body_normalised) < 80:
        add_finding(findings, "little_extracted_text", "Fewer than 80 characters extracted; inspect source.")
    expected = []
    for phrase in required:
        key = normalise(phrase)
        if not key:
            raise ValueError("--require values must contain visible text.")
        found = contains_phrase(body_normalised, key)
        supplemental_only = not found and contains_phrase(extra_normalised, key)
        expected.append({
            "text": phrase, "found_in_main_text": found,
            "found_only_in_header_footer": supplemental_only,
        })
        if not found:
            add_finding(
                findings,
                "header_footer_only_expected_text" if supplemental_only else "missing_expected_text",
                f"Expected text not found in main extraction: {phrase}",
            )
    return {
        "status": "review_needed" if findings else "no_local_flags",
        "file": str(path), "format": extension.lstrip("."),
        "characters": len(text), "words": len(text.split()),
        "structure": structure, "expected_text": expected,
        "findings": findings, "limitations": LIMITATION,
    }, text


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--require", action="append", default=[], metavar="TEXT")
    parser.add_argument("--report", type=Path)
    parser.add_argument("--text-out", type=Path)
    args = parser.parse_args(argv)
    if any(not normalise(phrase) for phrase in args.require):
        parser.error("--require values must contain visible text.")
    source = args.file.resolve()
    outputs = [p.resolve() for p in (args.report, args.text_out) if p is not None]
    paths = [source] + outputs
    collisions = any(
        a == b or (a.exists() and b.exists() and a.samefile(b))
        for index, a in enumerate(paths) for b in paths[index + 1:]
    )
    if collisions:
        parser.error("Outputs must be different from the input and from each other.")
    skill_root = Path(__file__).resolve().parents[1]
    if any(path.is_relative_to(skill_root) for path in outputs):
        parser.error("Store CV reports and extracted text outside the reusable skill.")
    try:
        if not source.is_file():
            raise ValueError("Input must be an existing regular file.")
        report, text = inspect(source, args.require)
        if args.text_out:
            args.text_out.write_text(text, encoding="utf-8")
        payload = json.dumps(report, ensure_ascii=False, indent=2)
        if args.report:
            args.report.write_text(payload + "\n", encoding="utf-8")
        print(payload)
        return 0
    except Exception as exc:
        print(json.dumps({
            "status": "inspection_failed", "file": str(source),
            "error": f"{type(exc).__name__}: {exc}", "limitations": LIMITATION,
        }, ensure_ascii=False, indent=2))
        return 1


if __name__ == "__main__":
    sys.exit(main())
