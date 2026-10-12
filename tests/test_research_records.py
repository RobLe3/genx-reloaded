import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_research", ROOT / "scripts/validate_research.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ResearchRecordTests(unittest.TestCase):
    def setUp(self):
        self.claims = json.loads((ROOT / "research/claims.json").read_text())
        self.cases = json.loads((ROOT / "evals/catalogue/cases.json").read_text())

    def test_release_records_validate(self):
        self.assertEqual([], MODULE.validate(self.claims, self.cases))

    def test_missing_provenance_and_invalid_date_fail(self):
        del self.claims["claims"][0]["inspection"]
        self.claims["claims"][1]["checked_on"] = "2026-02-31"
        errors = MODULE.validate(self.claims, self.cases)
        self.assertTrue(any("fields" in e for e in errors))
        self.assertTrue(any("date" in e for e in errors))

    def test_unknown_case_and_duplicate_claim_fail(self):
        self.claims["claims"][0]["related_cases"] = ["GX-99"]
        self.claims["claims"].append(copy.deepcopy(self.claims["claims"][0]))
        errors = MODULE.validate(self.claims, self.cases)
        self.assertTrue(any("Unknown related" in e for e in errors))
        self.assertTrue(any("duplicate claim" in e for e in errors))

    def test_missing_register_date_and_wrong_root_fail(self):
        del self.claims["checked_on"]
        self.assertTrue(MODULE.validate(self.claims, self.cases))
        self.assertTrue(MODULE.validate([], self.cases))


if __name__ == "__main__":
    unittest.main()
