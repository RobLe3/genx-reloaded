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
STUDY_PHASES = {"discovery", "baseline", "candidate-pilot", "confirmatory"}
STUDY_CONDITIONS = ["none", "released-0.4.2", "candidate"]
STUDY_FIELDS = {
    "schema_version", "study_id", "status", "prepared_on", "runtime_baseline_version",
    "objective", "conditions", "mutation_trigger", "phases", "design", "analysis",
    "primary_outcome", "secondary_outcomes", "release_gate", "privacy",
}
STUDY_ANALYSIS_FIELDS = {
    "record_schema_version", "contrast_estimand", "one_sided_test", "multiplicity",
    "simultaneous_interval", "power_simulation", "simulation_iterations", "simulation_seed",
}


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


def validate_study(study):
    errors = []
    if not isinstance(study, dict):
        return ["Study protocol root must be an object."]
    if set(study) != STUDY_FIELDS:
        errors.append("Correction-effort study fields differ from the approved protocol.")
    if study.get("schema_version") != 1 or study.get("study_id") != "correction-effort-v1":
        errors.append("Unsupported correction-effort study identity or schema.")
    if study.get("status") not in {"prepared", "active", "complete"}:
        errors.append("Invalid correction-effort study status.")
    try:
        valid_date(study.get("prepared_on"))
    except (ValueError, TypeError):
        errors.append("Invalid correction-effort preparation date.")
    if study.get("runtime_baseline_version") != "0.4.2":
        errors.append("Correction-effort baseline must remain released 0.4.2 for this protocol.")
    if study.get("conditions") != STUDY_CONDITIONS:
        errors.append("Correction-effort conditions or order changed.")

    trigger = study.get("mutation_trigger", {})
    if trigger.get("minimum_participants") != 3 or trigger.get("minimum_occupations") != 2 or trigger.get("required_severity") != "consequential":
        errors.append("Mutation trigger differs from the approved participant and severity gate.")

    phases = study.get("phases", [])
    phase_ids = [p.get("id") for p in phases if isinstance(p, dict)] if isinstance(phases, list) else []
    if len(phases) != 4 or len(phase_ids) != 4 or set(phase_ids) != STUDY_PHASES or len(set(phase_ids)) != 4:
        errors.append("Correction-effort phases are missing or duplicated.")
    else:
        by_id = {p["id"]: p for p in phases}
        if by_id["discovery"].get("target_participants") != 10 or by_id["baseline"].get("target_participants") != 12:
            errors.append("Discovery or baseline participant target changed.")
        pilot = by_id["candidate-pilot"]
        confirmatory = by_id["confirmatory"]
        if pilot.get("minimum_participants") != 6 or pilot.get("maximum_participants") != 8:
            errors.append("Candidate-pilot range changed.")
        if confirmatory.get("minimum_completers") != 36 or confirmatory.get("maximum_completers") != 120:
            errors.append("Confirmatory sample bounds changed.")
        expected_sessions = {
            "discovery": (30, 25),
            "baseline": (60, 40),
            "candidate-pilot": (60, 40),
            "confirmatory": (60, 40),
        }
        for ident, (minutes, compensation) in expected_sessions.items():
            phase = by_id[ident]
            if phase.get("duration_minutes") != minutes or phase.get("compensation_eur") != compensation:
                errors.append(f"Duration or compensation changed: {ident}")

    design = study.get("design", {})
    if design.get("tasks_per_participant") != 3 or design.get("conditions_per_participant") != 3:
        errors.append("Confirmatory task or condition count changed.")
    if design.get("power") != 0.8 or design.get("familywise_alpha") != 0.05:
        errors.append("Power or family-wise alpha changed.")
    for key in ("condition_order_counterbalanced", "reviewers_blinded", "adjudication_required", "fresh_confirmatory_participants"):
        if design.get(key) is not True:
            errors.append(f"Required study control disabled: {key}")
    if design.get("confirmatory_assignment") != "balanced-incomplete-block" or design.get("same_packet_repeated_for_participant") is not False or design.get("reviewers_per_output") != 2:
        errors.append("Confirmatory assignment, packet reuse or reviewer count changed.")

    analysis = study.get("analysis", {})
    if not isinstance(analysis, dict) or set(analysis) != STUDY_ANALYSIS_FIELDS:
        errors.append("Correction-effort analysis fields differ from the approved protocol.")
    if analysis.get("record_schema_version") != 1:
        errors.append("Correction-effort data contract version changed.")
    if analysis.get("contrast_estimand") != "Participant-paired mean of candidate minus control consequential correction counts.":
        errors.append("Correction-effort contrast estimand changed.")
    if analysis.get("one_sided_test") != "Normal approximation on participant-paired differences.":
        errors.append("Correction-effort test method changed.")
    if analysis.get("multiplicity") != "Holm adjustment across the two candidate comparisons.":
        errors.append("Correction-effort multiplicity method changed.")
    if analysis.get("simultaneous_interval") != "Bonferroni-adjusted one-sided 95% upper bounds.":
        errors.append("Correction-effort simultaneous interval changed.")
    if analysis.get("power_simulation") != "Empirical participant-block resampling of candidate-pilot contrasts.":
        errors.append("Correction-effort power method changed.")
    if analysis.get("simulation_iterations") != 5000 or analysis.get("simulation_seed") != 20261012:
        errors.append("Correction-effort simulation defaults changed.")

    primary = study.get("primary_outcome", {})
    if primary.get("name") != "consequential-correction-actions" or primary.get("minimum_mean_reduction") != 0.5 or primary.get("confidence_level") != 0.95:
        errors.append("Primary correction-effort outcome or threshold changed.")

    gate = study.get("release_gate", {})
    if gate.get("minimum_zero_correction_rate_gain") != 0.15 or gate.get("maximum_time_regression") != 0.1 or gate.get("critical_failures_allowed") != 0:
        errors.append("Correction-effort release threshold changed.")
    if gate.get("release_version") != "0.5.0":
        errors.append("Correction-effort release version changed.")
    expected_regressions = {"privacy", "historical-evidence", "modern-product-boundary", "low-energy-interaction", "deliverable-completion", "document-safety"}
    if not isinstance(gate.get("required_regressions"), list) or set(gate["required_regressions"]) != expected_regressions:
        errors.append("Required regression set changed.")

    privacy = study.get("privacy", {})
    if privacy.get("repository_contains_participant_data") is not False:
        errors.append("Participant data must remain outside the repository.")
    if privacy.get("raw_retention_days_after_adjudication") != 90 or privacy.get("coded_retention_days") != 365:
        errors.append("Study retention period changed.")
    if privacy.get("default_material") != "fictional":
        errors.append("Fictional material must remain the participant default.")
    for key in ("real_document_requires_separate_consent", "recording_optional", "notes_only_route", "contact_and_consent_stored_separately", "withdrawal_available_until_aggregation"):
        if privacy.get(key) is not True:
            errors.append(f"Required privacy control disabled: {key}")
    return errors


def main():
    try:
        claims = json.loads((ROOT / "research/claims.json").read_text(encoding="utf-8"))
        cases = json.loads((ROOT / "evals/catalogue/cases.json").read_text(encoding="utf-8"))
        study = json.loads((ROOT / "research/correction-effort-study.json").read_text(encoding="utf-8"))
        errors = validate(claims, cases) + validate_study(study)
    except (OSError, ValueError, TypeError, KeyError) as exc:
        errors = [str(exc)]
    print(json.dumps({"status": "fail" if errors else "pass", "errors": errors, "limits": "Structure and references only; no source-truth or behavioural grading."}, indent=2))
    return bool(errors)


if __name__ == "__main__":
    sys.exit(main())
