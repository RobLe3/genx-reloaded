#!/usr/bin/env python3
"""Validate research record structure and case references, not source truth."""

from datetime import date
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
FIELDS = set("id workstream statement source_url source_title publisher publication_date checked_on evidence_type scope inspection limitations candidate_action mitigation_tested status review_trigger reviewer related_cases".split())
STATUSES = {"supported-within-scope", "promising-untested-here", "mixed", "outdated", "unknown"}
TYPES = {"study", "synthesis", "official-guidance", "law", "vendor-documentation", "retrieval-lead"}


def valid_date(value):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ValueError("Expected ISO calendar date.")
    date.fromisoformat(value)


def validate(claims, catalogue):
    errors = []
    if not isinstance(claims, dict) or not isinstance(catalogue, dict):
        return ["Record roots must be objects."]
    if claims.get("schema_version") != 1 or catalogue.get("schema_version") != 1:
        errors.append("Unsupported schema version.")
    try:
        valid_date(claims.get("checked_on"))
    except (ValueError, TypeError):
        errors.append("Invalid register check date.")
    if not isinstance(claims.get("review_kind"), str) or not claims["review_kind"].strip():
        errors.append("Missing review kind.")
    cases = catalogue.get("cases", [])
    if not isinstance(cases, list) or not isinstance(claims.get("claims"), list):
        return errors + ["Claims and cases must be lists."]
    ids = []
    for c in cases:
        if not isinstance(c, dict):
            errors.append("Each case must be an object.")
            continue
        ident = c.get("id", "")
        ids.append(ident)
        if not re.fullmatch(r"GX-\d{2}", ident):
            errors.append(f"Invalid case ID: {ident}")
        if c.get("split") not in {"development", "reserved"} or not isinstance(c.get("prompt"), str) or not c["prompt"].strip():
            errors.append(f"Invalid case prompt/split: {ident}")
        if not isinstance(c.get("checks"), list) or not c["checks"] or not all(isinstance(s, str) and s.strip() for s in c["checks"]):
            errors.append(f"Missing case criteria: {ident}")
    if not cases or len(ids) != len(set(ids)):
        errors.append("Empty or duplicate case IDs.")
    seen = set()
    for c in claims.get("claims", []):
        if not isinstance(c, dict):
            errors.append("Each claim must be an object.")
            continue
        ident = c.get("id", "")
        if set(c) != FIELDS:
            errors.append(f"Claim fields differ: {ident}")
            continue
        if ident in seen or not re.fullmatch(r"GX-C\d{2}", ident):
            errors.append(f"Invalid/duplicate claim ID: {ident}")
        seen.add(ident)
        valid_strings = True
        for key in FIELDS - {"publication_date", "related_cases"}:
            if not isinstance(c[key], str) or not c[key].strip():
                errors.append(f"Empty claim field: {ident}.{key}")
                valid_strings = False
        if not valid_strings:
            continue
        try:
            valid_date(c["checked_on"])
            published = c["publication_date"]
            if published is not None:
                if not isinstance(published, str) or not re.fullmatch(r"\d{4}(-\d{2}){0,2}", published):
                    raise ValueError("Invalid publication date.")
                valid_date(published + ("-01-01" if len(published) == 4 else "-01" if len(published) == 7 else ""))
        except (ValueError, TypeError):
            errors.append(f"Invalid claim date: {ident}")
        if c["status"] not in STATUSES or c["evidence_type"] not in TYPES:
            errors.append(f"Invalid evidence classification: {ident}")
        if not re.fullmatch(r"R(0[1-9]|1[0-2])", c["workstream"]):
            errors.append(f"Invalid workstream: {ident}")
        parsed = urlparse(c["source_url"])
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            errors.append(f"Invalid source URL: {ident}")
        if not isinstance(c["related_cases"], list) or any(case not in ids for case in c["related_cases"]):
            errors.append(f"Unknown related case: {ident}")
    if not seen:
        errors.append("No claims.")
    return errors


def main():
    try:
        claims = json.loads((ROOT / "research/claims.json").read_text(encoding="utf-8"))
        cases = json.loads((ROOT / "evals/catalogue/cases.json").read_text(encoding="utf-8"))
        errors = validate(claims, cases)
    except (OSError, ValueError, TypeError, KeyError) as exc:
        errors = [str(exc)]
    print(json.dumps({"status": "fail" if errors else "pass", "errors": errors, "limits": "Structure and references only; no source-truth or behavioural grading."}, indent=2))
    return bool(errors)


if __name__ == "__main__":
    sys.exit(main())
