import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from contextlib import redirect_stdout


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("correction_effort", ROOT / "scripts/correction_effort.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def study_record(phase="confirmatory", participants=36):
    conditions = list(MODULE.PHASE_CONDITIONS[phase])
    families = ["long-history", "multiple-fields", "portal-correction"][:len(conditions)]
    permutations = (
        ("none", "released-0.4.2", "candidate"),
        ("none", "candidate", "released-0.4.2"),
        ("released-0.4.2", "none", "candidate"),
        ("released-0.4.2", "candidate", "none"),
        ("candidate", "none", "released-0.4.2"),
        ("candidate", "released-0.4.2", "none"),
    )
    outputs = []
    for participant in range(participants):
        if len(conditions) == 3:
            sequence = permutations[participant % len(permutations)]
        else:
            sequence = tuple(conditions if participant % 2 == 0 else reversed(conditions))
        for position, condition in enumerate(sequence, start=1):
            action = []
            if condition != "candidate":
                action = [{
                    "action_id": "A1",
                    "reviewer_1": "consequential",
                    "reviewer_2": "consequential",
                    "adjudicated": "consequential",
                }]
            outputs.append({
                "output_id": f"O{participant:03d}-{position}",
                "participant_id": f"P{participant:03d}",
                "task_id": f"T{participant:03d}-{position}",
                "task_family": families[position - 1],
                "condition": condition,
                "condition_order": position,
                "elapsed_seconds": 600,
                "completion_status": "completed",
                "requested_deliverable_complete": True,
                "blocking_questions": 0,
                "effort_rating": 3,
                "accurate_representation": "yes",
                "disclosure_control": "yes",
                "reviewer_ids": ["R1", "R2"],
                "actions": action,
            })
    return {
        "schema_version": 1,
        "study_id": "correction-effort-v1",
        "phase": phase,
        "generated_on": "2026-10-12",
        "protocol_frozen": phase == "confirmatory",
        "review_complete_before_unblinding": True,
        "accessibility_time_exception": {"applies": False, "basis": ""},
        "regressions": {name: "pass" for name in MODULE.REGRESSIONS},
        "outputs": outputs,
    }


def calibration_record():
    severities = ["critical", "consequential", "minor", "preference"] * 3
    return {
        "schema_version": 1,
        "study_id": "correction-effort-v1",
        "calibration_id": "CAL-01",
        "completed_on": "2026-10-13",
        "reviewer_ids": ["R1", "R2"],
        "condition_blinded": True,
        "items": [
            {"item_id": f"I{index:02d}", "reviewer_1": severity, "reviewer_2": severity}
            for index, severity in enumerate(severities, start=1)
        ],
    }


class CorrectionEffortTests(unittest.TestCase):
    def test_reviewer_calibration_passes_fixed_gate(self):
        record = calibration_record()
        self.assertEqual([], MODULE.validate_calibration(record))
        result = MODULE.analyse_calibration(record)
        self.assertTrue(result["passed"])
        self.assertEqual(1.0, result["exact_severity_agreement"])

    def test_reviewer_calibration_requires_scope_and_boundary_agreement(self):
        record = calibration_record()
        record["items"][0]["reviewer_2"] = "minor"
        result = MODULE.analyse_calibration(record)
        self.assertFalse(result["passed"])
        self.assertLess(result["critical_or_consequential_boundary_agreement"], 1.0)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "calibration.json"
            path.write_text(json.dumps(record), encoding="utf-8")
            output = io.StringIO()
            with redirect_stdout(output):
                status = MODULE.main(["calibrate", str(path)])
        self.assertEqual(2, status)
        self.assertEqual("fail", json.loads(output.getvalue())["status"])
        record["items"] = record["items"][:4]
        self.assertTrue(any("at least 12" in error for error in MODULE.validate_calibration(record)))

    def test_confirmatory_record_validates_and_passes_gate(self):
        record = study_record()
        self.assertEqual([], MODULE.validate_record(record))
        analysis = MODULE.analyse(record)
        self.assertTrue(analysis["release_gate"]["passed"])
        self.assertEqual(1.0, analysis["condition_summaries"]["candidate"]["usable_without_critical_or_consequential_correction_rate"])
        self.assertTrue(all(contrast["primary_gate"] for contrast in analysis["contrasts"]))

    def test_sample_assignment_and_packet_errors_fail(self):
        record = study_record()
        record["outputs"][1]["condition"] = record["outputs"][0]["condition"]
        record["outputs"][2]["task_id"] = record["outputs"][0]["task_id"]
        errors = MODULE.validate_record(record)
        self.assertTrue(any("condition set" in error for error in errors))
        self.assertTrue(any("source packet" in error for error in errors))

    def test_review_and_privacy_safe_contract_errors_fail(self):
        record = study_record()
        record["review_complete_before_unblinding"] = False
        record["outputs"][0]["reviewer_ids"] = ["R1", "R1"]
        record["outputs"][0]["actions"][0]["adjudicated"] = "unknown"
        errors = MODULE.validate_record(record)
        self.assertTrue(any("before condition unblinding" in error for error in errors))
        self.assertTrue(any("two distinct" in error for error in errors))
        self.assertTrue(any("invalid severity" in error for error in errors))

    def test_critical_failure_and_time_regression_block_release(self):
        record = study_record()
        candidates = [output for output in record["outputs"] if output["condition"] == "candidate"]
        for candidate in candidates:
            candidate["elapsed_seconds"] = 1200
        candidate = candidates[0]
        candidate["actions"].append({
            "action_id": "C1",
            "reviewer_1": "critical",
            "reviewer_2": "critical",
            "adjudicated": "critical",
        })
        analysis = MODULE.analyse(record)
        self.assertFalse(analysis["release_gate"]["passed"])
        self.assertFalse(analysis["release_gate"]["checks"]["no_candidate_critical_failures"])
        self.assertFalse(analysis["release_gate"]["checks"]["time_vs_none"])

    def test_pilot_power_resamples_participant_blocks(self):
        record = study_record("candidate-pilot", 6)
        self.assertEqual([], MODULE.validate_record(record))
        result = MODULE.simulate_power(record, iterations=100, seed=7)
        self.assertEqual(36, result["recommended_completers"])
        self.assertTrue(result["within_protocol_bounds"])

    def test_baseline_uses_two_conditions(self):
        record = study_record("baseline", 12)
        self.assertEqual([], MODULE.validate_record(record))
        analysis = MODULE.analyse(record)
        self.assertFalse(analysis["release_gate"]["evaluated"])
        self.assertEqual([], analysis["contrasts"])

    def test_cli_does_not_echo_private_identifiers_on_validation_error(self):
        record = study_record("candidate-pilot", 6)
        private_id = "PRIVATE-PERSON-NAME"
        record["outputs"][0]["participant_id"] = private_id
        record["outputs"][0]["reviewer_ids"] = ["R1", "R1"]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "record.json"
            path.write_text(json.dumps(record), encoding="utf-8")
            output = io.StringIO()
            with redirect_stdout(output):
                status = MODULE.main(["validate", str(path)])
        self.assertEqual(1, status)
        self.assertNotIn(private_id, output.getvalue())


if __name__ == "__main__":
    unittest.main()
