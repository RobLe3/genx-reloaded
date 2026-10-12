#!/usr/bin/env python3
"""Validate the private launch record for the correction-effort study.

The record contains operational details and stays outside Git. This validator
reports field-level errors without echoing private values.
"""

from datetime import date
import argparse
import json
from pathlib import Path
import re
import sys

FIELDS = {
    "schema_version",
    "study_id",
    "study_owner",
    "encrypted_storage_location",
    "access_list",
    "contact_route",
    "recruitment_source",
    "withdrawal_contact",
    "compensation_method",
    "ethics_review_status",
    "ethics_review_basis",
    "privacy_review_status",
    "privacy_review_basis",
    "deletion_tested_on",
    "invitation_approved",
}


def _text(record, key, errors):
    value = record.get(key)
    if not isinstance(value, str) or not value.strip():
        errors.append(f"Missing private operations field: {key}")


def validate_operations(record):
    errors = []
    if not isinstance(record, dict):
        return ["Private operations record must be an object."]
    if set(record) != FIELDS:
        errors.append("Private operations fields differ from the launch contract.")
    if record.get("schema_version") != 1 or record.get("study_id") != "correction-effort-v1":
        errors.append("Private operations study identity or schema is invalid.")
    for key in FIELDS - {"schema_version", "access_list", "ethics_review_status", "privacy_review_status", "deletion_tested_on", "invitation_approved"}:
        _text(record, key, errors)
    access = record.get("access_list")
    if not isinstance(access, list) or not access or not all(isinstance(value, str) and value.strip() for value in access):
        errors.append("Access list must name at least one authorised person or role.")
    if record.get("ethics_review_status") not in {"approved", "not-required"}:
        errors.append("Ethics review must be approved or documented as not required.")
    if record.get("privacy_review_status") != "approved":
        errors.append("Privacy review must be approved before recruitment.")
    checked = record.get("deletion_tested_on")
    try:
        if not isinstance(checked, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", checked):
            raise ValueError
        date.fromisoformat(checked)
    except (TypeError, ValueError):
        errors.append("Deletion test date must be a valid ISO calendar date.")
    if record.get("invitation_approved") is not True:
        errors.append("Participant invitation must be approved before recruitment.")
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description="Validate a private correction-effort study launch record without printing its values.")
    parser.add_argument("record", type=Path)
    args = parser.parse_args(argv)
    try:
        record = json.loads(args.record.read_text(encoding="utf-8"))
        errors = validate_operations(record)
    except (OSError, ValueError, TypeError) as exc:
        errors = [str(exc)]
    print(json.dumps({"status": "fail" if errors else "pass", "errors": errors}, indent=2))
    return bool(errors)


if __name__ == "__main__":
    sys.exit(main())
