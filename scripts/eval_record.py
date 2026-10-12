#!/usr/bin/env python3
"""Capture a text skill and record fictional evaluation artifacts, offline.

No model is called and no behavioural pass is inferred. Existing output paths
are never overwritten. Snapshots contain reusable skill files, not user CVs.
"""

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import sys


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def inventory_digest(files):
    return digest(canonical([{k: f[k] for k in ("path", "sha256")} for f in files]))


def capture(runtime):
    root = Path(runtime)
    if root.is_symlink() or not root.is_dir():
        raise ValueError("Runtime must be a real directory, not a symlink.")
    files = []
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if any(p in {".git", "__pycache__"} for p in relative.parts):
            continue
        if path.is_symlink():
            raise ValueError(f"Symlink in runtime: {relative}")
        if path.is_file():
            data = path.read_bytes()
            files.append({"path": relative.as_posix(), "sha256": digest(data), "content": data.decode("utf-8")})
    if not any(f["path"] == "SKILL.md" for f in files):
        raise ValueError("Runtime has no SKILL.md.")
    result = {"schema_version": 1, "files": files, "inventory_sha256": inventory_digest(files)}
    validate_snapshot(result)
    return result


def validate_snapshot(snapshot):
    if snapshot.get("schema_version") != 1 or not isinstance(snapshot.get("files"), list):
        raise ValueError("Invalid snapshot format.")
    paths = set()
    for entry in snapshot["files"]:
        name = entry["path"]
        p = PurePosixPath(name)
        if not name or p.is_absolute() or ".." in p.parts or "\\" in name or p.as_posix() != name or name in paths:
            raise ValueError("Unsafe or duplicate snapshot path.")
        paths.add(name)
        if digest(entry["content"].encode("utf-8")) != entry["sha256"]:
            raise ValueError(f"Snapshot content changed: {name}")
    if "SKILL.md" not in paths or inventory_digest(snapshot["files"]) != snapshot.get("inventory_sha256"):
        raise ValueError("Snapshot inventory mismatch.")


def write_new(path, data):
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("x", encoding="utf-8") as stream:
        json.dump(data, stream, ensure_ascii=False, indent=2)
        stream.write("\n")


def record(snapshot_path, prompt_path, response_path, output, case_id, agent_id, model="unknown", wrapper="unknown"):
    if not re.fullmatch(r"GX-\d{2}", case_id):
        raise ValueError("Case ID must have the form GX-01.")
    snapshot = None
    if snapshot_path is not None:
        snapshot = json.loads(Path(snapshot_path).read_text(encoding="utf-8"))
        validate_snapshot(snapshot)
    prompt = Path(prompt_path).read_bytes()
    response = Path(response_path).read_bytes()
    for label, data in (("prompt", prompt), ("response", response)):
        if not data.decode("utf-8").strip():
            raise ValueError(f"Empty {label}.")
    target = Path(output)
    target.mkdir(parents=True, exist_ok=False)
    try:
        (target / "prompt.txt").write_bytes(prompt)
        (target / "response.md").write_bytes(response)
        if snapshot is not None:
            write_new(target / "runtime.json", snapshot)
        metadata = {
            "schema_version": 1,
            "case_id": case_id,
            "agent_id": agent_id,
            "model": model,
            "sampling_settings": "unknown",
            "host": "Codex Work Mode fresh agent context",
            "execution_started_at": None,
            "recorded_at": datetime.now(timezone.utc).isoformat(),
            "wrapper": wrapper,
            "tools": "Host tools available; complete tool transcript not archived.",
            "data_kind": "fictional",
            "assessment": "unassessed",
            "files": {"prompt.txt": digest(prompt), "response.md": digest(response)},
            "skill_condition": "captured-runtime" if snapshot is not None else "no-skill",
            "runtime_inventory_sha256": snapshot["inventory_sha256"] if snapshot is not None else None,
            "limits": "Artifact capture, not automatic grading, independent adjudication, or deterministic model reproduction.",
        }
        write_new(target / "record.json", metadata)
    except Exception:
        shutil.rmtree(target)
        raise
    return metadata


def verify(directory):
    root = Path(directory)
    metadata = json.loads((root / "record.json").read_text(encoding="utf-8"))
    if metadata.get("schema_version") != 1 or metadata.get("data_kind") != "fictional":
        raise ValueError("Unsupported run record.")
    if set(metadata.get("files", {})) != {"prompt.txt", "response.md"}:
        raise ValueError("Unexpected run artifact inventory.")
    condition = metadata.get("skill_condition")
    if condition == "captured-runtime":
        snapshot = json.loads((root / "runtime.json").read_text(encoding="utf-8"))
        validate_snapshot(snapshot)
        if metadata["runtime_inventory_sha256"] != snapshot["inventory_sha256"]:
            raise ValueError("Run and snapshot disagree.")
    elif condition != "no-skill" or metadata.get("runtime_inventory_sha256") is not None or (root / "runtime.json").exists():
        raise ValueError("Invalid no-skill comparison record.")
    for name, expected in metadata["files"].items():
        if digest((root / name).read_bytes()) != expected:
            raise ValueError(f"Run artifact changed: {name}")
    return metadata


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    cap = commands.add_parser("capture")
    cap.add_argument("runtime", type=Path)
    cap.add_argument("output", type=Path)
    rec = commands.add_parser("record")
    rec.add_argument("--snapshot", help="Omit only for a no-skill comparison.")
    for name in ("prompt", "response", "output", "case-id", "agent-id", "wrapper"):
        rec.add_argument("--" + name, required=True)
    rec.add_argument("--model", default="unknown")
    ver = commands.add_parser("verify")
    ver.add_argument("directory", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "capture":
            result = capture(args.runtime)
            write_new(args.output, result)
            result = {"files": len(result["files"]), "inventory_sha256": result["inventory_sha256"]}
        elif args.command == "record":
            result = record(args.snapshot, args.prompt, args.response, args.output, args.case_id, args.agent_id, args.model, args.wrapper)
        else:
            result = verify(args.directory)
        print(json.dumps({"status": "recorded" if args.command != "verify" else "verified", "case_id": result.get("case_id"), "inventory_sha256": result.get("inventory_sha256", result.get("runtime_inventory_sha256"))}))
        return 0
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(json.dumps({"status": "error", "message": str(exc)}))
        return 1


if __name__ == "__main__":
    sys.exit(main())
