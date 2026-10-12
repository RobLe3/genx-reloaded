import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]


class CorrectionEffortRehearsalTests(unittest.TestCase):
    def test_ephemeral_synthetic_rehearsal_completes_and_deletes_records(self):
        completed = subprocess.run(
            [sys.executable, str(ROOT / "scripts/rehearse_correction_effort.py")],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        result = json.loads(completed.stdout)
        self.assertEqual("pass", result["status"])
        self.assertTrue(result["synthetic_only"])
        self.assertFalse(result["candidate_outcome_claim"])
        self.assertTrue(result["steps"]["temporary_records_deleted"])
        self.assertTrue(all(result["steps"].values()))


if __name__ == "__main__":
    unittest.main()
