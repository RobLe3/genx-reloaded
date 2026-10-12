#!/usr/bin/env python3
"""Run an ephemeral, entirely fictional correction-effort workflow rehearsal."""

from datetime import date
import json
from pathlib import Path
import tempfile

from correction_effort import (
    PHASE_CONDITIONS,
    REGRESSIONS,
    analyse,
    analyse_calibration,
    simulate_power,
    validate_calibration,
    validate_record,
)
from validate_study_operations import validate_operations


TODAY = date.today().isoformat()


def _calibration():
    severities = ["critical", "consequential", "minor", "preference"] * 3
    return {
        "schema_version": 1,
        "study_id": "correction-effort-v1",
        "calibration_id": "SYNTHETIC-CALIBRATION",
        "completed_on": TODAY,
        "reviewer_ids": ["SYNTHETIC-R1", "SYNTHETIC-R2"],
        "condition_blinded": True,
        "items": [
            {"item_id": f"SYNTHETIC-I{index:02d}", "reviewer_1": severity, "reviewer_2": severity}
            for index, severity in enumerate(severities, start=1)
        ],
    }


def _study_record(phase, participant_count):
    conditions = list(PHASE_CONDITIONS[phase])
    families = ["history", "application-fields", "portal-repair"][:len(conditions)]
    permutations = (
        ("none", "released-0.4.2", "candidate"),
        ("none", "candidate", "released-0.4.2"),
        ("released-0.4.2", "none", "candidate"),
        ("released-0.4.2", "candidate", "none"),
        ("candidate", "none", "released-0.4.2"),
        ("candidate", "released-0.4.2", "none"),
    )
    outputs = []
    for participant in range(participant_count):
        sequence = (
            permutations[participant % len(permutations)]
            if len(conditions) == 3
            else tuple(conditions if participant % 2 == 0 else reversed(conditions))
        )
        for order, condition in enumerate(sequence, start=1):
            actions = [] if condition == "candidate" else [{
                "action_id": "SYNTHETIC-A1",
                "reviewer_1": "consequential",
                "reviewer_2": "consequential",
                "adjudicated": "consequential",
            }]
            outputs.append({
                "output_id": f"SYNTHETIC-O{participant:03d}-{order}",
                "participant_id": f"SYNTHETIC-P{participant:03d}",
                "task_id": f"SYNTHETIC-T{participant:03d}-{order}",
                "task_family": families[order - 1],
                "condition": condition,
                "condition_order": order,
                "elapsed_seconds": 600,
                "completion_status": "completed",
                "requested_deliverable_complete": True,
                "blocking_questions": 0,
                "effort_rating": 3,
                "accurate_representation": "yes",
                "disclosure_control": "yes",
                "reviewer_ids": ["SYNTHETIC-R1", "SYNTHETIC-R2"],
                "actions": actions,
            })
    return {
        "schema_version": 1,
        "study_id": "correction-effort-v1",
        "phase": phase,
        "generated_on": TODAY,
        "protocol_frozen": phase == "confirmatory",
        "review_complete_before_unblinding": True,
        "accessibility_time_exception": {"applies": False, "basis": ""},
        "regressions": {name: "pass" for name in REGRESSIONS},
        "outputs": outputs,
    }


def _operations():
    return {
        "schema_version": 1,
        "study_id": "correction-effort-v1",
        "study_owner": "Synthetic rehearsal owner",
        "encrypted_storage_location": "Synthetic temporary rehearsal store",
        "access_list": ["Synthetic study owner", "Synthetic reviewer"],
        "contact_route": "Synthetic contact route",
        "recruitment_source": "Synthetic recruitment source",
        "withdrawal_contact": "Synthetic withdrawal route",
        "compensation_method": "Synthetic compensation route",
        "ethics_review_status": "not-required",
        "ethics_review_basis": "Synthetic rehearsal contains no participants",
        "privacy_review_status": "approved",
        "privacy_review_basis": "Synthetic rehearsal uses temporary fictional records",
        "deletion_tested_on": TODAY,
        "invitation_approved": True,
    }


def _write_json(path, value):
    path.write_text(json.dumps(value, indent=2), encoding="utf-8")
    return json.loads(path.read_text(encoding="utf-8"))


def run_rehearsal():
    steps = {}
    rehearsal_root = None
    with tempfile.TemporaryDirectory(prefix="genx-correction-effort-rehearsal-") as directory:
        rehearsal_root = Path(directory)
        contacts = rehearsal_root / "contact-and-consent"
        coded = rehearsal_root / "coded-study"
        contacts.mkdir()
        coded.mkdir()

        _write_json(contacts / "synthetic-contact.json", {
            "notice": "Fictional rehearsal only",
            "contact": "participant@example.invalid",
        })
        steps["contact_and_coded_storage_separated"] = contacts.parent == coded.parent and contacts != coded

        operations = _write_json(rehearsal_root / "operations.json", _operations())
        steps["operations_record_valid"] = not validate_operations(operations)

        calibration = _write_json(coded / "calibration.json", _calibration())
        steps["reviewer_calibration_valid"] = not validate_calibration(calibration)
        steps["reviewer_calibration_passed"] = analyse_calibration(calibration)["passed"]

        baseline = _write_json(coded / "baseline.json", _study_record("baseline", 12))
        steps["baseline_record_valid"] = not validate_record(baseline)
        steps["baseline_aggregate_created"] = analyse(baseline)["participants"] == 12

        pilot = _write_json(coded / "pilot.json", _study_record("candidate-pilot", 6))
        steps["pilot_record_valid"] = not validate_record(pilot)
        power = simulate_power(pilot, iterations=5000, seed=20261012)
        steps["pilot_power_completed"] = power["recommended_completers"] is not None

        confirmatory = _write_json(coded / "confirmatory.json", _study_record("confirmatory", 36))
        steps["confirmatory_record_valid"] = not validate_record(confirmatory)
        steps["confirmatory_gate_exercised"] = analyse(confirmatory)["release_gate"]["evaluated"]

    steps["temporary_records_deleted"] = rehearsal_root is not None and not rehearsal_root.exists()
    return {
        "status": "pass" if all(steps.values()) else "fail",
        "synthetic_only": True,
        "candidate_outcome_claim": False,
        "steps": steps,
    }


def main():
    result = run_rehearsal()
    print(json.dumps(result, indent=2, sort_keys=True))
    return result["status"] != "pass"


if __name__ == "__main__":
    raise SystemExit(main())
