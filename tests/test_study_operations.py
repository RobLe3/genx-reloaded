import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_study_operations", ROOT / "scripts/validate_study_operations.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def valid_record():
    return {
        "schema_version": 1,
        "study_id": "correction-effort-v1",
        "study_owner": "Named owner",
        "encrypted_storage_location": "Approved encrypted private store",
        "access_list": ["Study owner", "Named researcher"],
        "contact_route": "Approved participant contact route",
        "recruitment_source": "Approved recruitment source",
        "withdrawal_contact": "Approved withdrawal contact",
        "compensation_method": "Approved payment method",
        "ethics_review_status": "not-required",
        "ethics_review_basis": "Documented review basis",
        "privacy_review_status": "approved",
        "privacy_review_basis": "Documented privacy review",
        "deletion_tested_on": "2026-10-12",
        "invitation_approved": True,
    }


class StudyOperationsTests(unittest.TestCase):
    def test_valid_launch_record_passes(self):
        self.assertEqual([], MODULE.validate_operations(valid_record()))

    def test_missing_storage_and_access_fail(self):
        record = valid_record()
        record["encrypted_storage_location"] = ""
        record["access_list"] = []
        errors = MODULE.validate_operations(record)
        self.assertTrue(any("encrypted_storage_location" in error for error in errors))
        self.assertTrue(any("Access list" in error for error in errors))

    def test_unapproved_reviews_and_invitation_fail(self):
        record = valid_record()
        record["ethics_review_status"] = "pending"
        record["privacy_review_status"] = "pending"
        record["invitation_approved"] = False
        errors = MODULE.validate_operations(record)
        self.assertTrue(any("Ethics" in error for error in errors))
        self.assertTrue(any("Privacy" in error for error in errors))
        self.assertTrue(any("invitation" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
