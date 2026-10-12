#!/usr/bin/env python3
"""Check repository structure offline; do not evaluate CV or hiring quality."""

import ast
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

import yaml

ROOT = Path(__file__).resolve().parents[1]


def main():
    errors = []
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    version = (ROOT / "VERSION").read_text().strip()
    skill = ROOT / manifest["runtime_root"]
    if manifest["version"] != version:
        errors.append("Manifest and VERSION differ.")
    if f"Version {version}" not in (ROOT / "README.md").read_text():
        errors.append("README version does not match VERSION.")
    if f"## {version}," not in (ROOT / "CHANGELOG.md").read_text():
        errors.append("Current version is missing from CHANGELOG.md.")
    declared = {entry["path"]: entry["sha256"] for entry in manifest["files"]}
    actual = {
        str(p.relative_to(ROOT)): p
        for p in skill.rglob("*")
        if p.is_file() and "__pycache__" not in p.parts
    }
    if set(declared) != set(actual):
        errors.append("Runtime inventory differs from manifest.")
    for relative, path in actual.items():
        if declared.get(relative) != hashlib.sha256(path.read_bytes()).hexdigest():
            errors.append(f"Runtime digest mismatch: {relative}")

    content = (skill / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\n(.*?)\n---\n", content, re.S)
    if not frontmatter:
        errors.append("Missing skill frontmatter.")
        metadata = {}
    else:
        metadata = yaml.safe_load(frontmatter.group(1))
    if set(metadata) != {"name", "description"}:
        errors.append("Skill frontmatter must contain name and description only.")
    if metadata.get("name") != skill.name or skill.name != manifest["name"]:
        errors.append("Skill name, runtime folder and manifest name differ.")
    description = metadata.get("description", "")
    if not isinstance(description, str) or not 1 <= len(description) <= 1024:
        errors.append("Skill description must contain 1-1024 characters.")
    if len(content.splitlines()) > 500:
        errors.append("SKILL.md exceeds the project's 500-line limit.")
    interface = yaml.safe_load((skill / "agents/openai.yaml").read_text())["interface"]
    if f"${manifest['name']}" not in interface["default_prompt"]:
        errors.append("Default prompt uses the wrong invocation.")
    if not 25 <= len(interface["short_description"]) <= 64:
        errors.append("Short description is outside 25-64 characters.")
    for key in ("icon_small", "icon_large"):
        if key in interface and not (skill / interface[key]).is_file():
            errors.append(f"Missing {key} asset.")

    checked_links = 0
    markdown = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]
    for path in markdown:
        text = path.read_text(encoding="utf-8")
        for raw in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", text):
            parsed = urlparse(raw)
            if parsed.scheme or not parsed.path:
                continue
            target = (path.parent / unquote(parsed.path)).resolve()
            checked_links += 1
            if not target.is_relative_to(ROOT) or not target.exists():
                errors.append(f"Broken or out-of-repository link: {path.relative_to(ROOT)} -> {raw}")
    python_files = [p for p in ROOT.rglob("*.py") if ".git" not in p.parts and ".venv" not in p.parts]
    for path in python_files:
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path.relative_to(ROOT)))
        except SyntaxError as exc:
            errors.append(str(exc))

    result = {
        "status": "fail" if errors else "pass",
        "version": version,
        "runtime_files": len(actual),
        "local_markdown_links": checked_links,
        "python_files": len(python_files),
        "errors": errors,
        "limits": "Structural checks only; no live URL, agent behaviour, visual, ATS or hiring validation.",
    }
    print(json.dumps(result, indent=2))
    return bool(errors)


if __name__ == "__main__":
    sys.exit(main())
