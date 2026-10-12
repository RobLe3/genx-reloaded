import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location("eval_record", Path(__file__).resolve().parents[1] / "scripts/eval_record.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class EvaluationRecordTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.runtime = self.root / "skill"
        self.runtime.mkdir()
        (self.runtime / "SKILL.md").write_text("A fictional skill.\n", encoding="utf-8")
        self.snapshot = self.root / "snapshot.json"
        MODULE.write_new(self.snapshot, MODULE.capture(self.runtime))
        self.prompt = self.root / "prompt.txt"
        self.response = self.root / "response.md"
        self.prompt.write_text("A fictional request.\n", encoding="utf-8")
        self.response.write_text("A fictional response.\n", encoding="utf-8")

    def record(self, target=None):
        return MODULE.record(self.snapshot, self.prompt, self.response, target or self.root / "run", "GX-01", "fictional-agent", wrapper="Fictional test wrapper")

    def test_roundtrip_preserves_raw_artifacts_and_unknown_metadata(self):
        result = self.record()
        self.assertEqual("unknown", result["model"])
        self.assertEqual("unassessed", result["assessment"])
        self.assertEqual(self.response.read_bytes(), (self.root / "run/response.md").read_bytes())
        self.assertEqual(result, MODULE.verify(self.root / "run"))

    def test_changed_response_is_detected(self):
        self.record()
        (self.root / "run/response.md").write_text("Changed after recording", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "artifact changed"):
            MODULE.verify(self.root / "run")

    def test_no_skill_comparison_does_not_invent_a_runtime(self):
        result = MODULE.record(None, self.prompt, self.response, self.root / "control", "GX-01", "control-agent")
        self.assertEqual("no-skill", result["skill_condition"])
        self.assertIsNone(result["runtime_inventory_sha256"])
        self.assertFalse((self.root / "control/runtime.json").exists())
        self.assertEqual(result, MODULE.verify(self.root / "control"))

    def test_changed_snapshot_content_is_detected(self):
        data = json.loads(self.snapshot.read_text())
        data["files"][0]["content"] = "Tampered"
        with self.assertRaisesRegex(ValueError, "content changed"):
            MODULE.validate_snapshot(data)

    def test_parent_path_and_duplicate_path_are_rejected(self):
        for bad_name in ("../escape", "/absolute", "a/../../escape", "a\\escape"):
            data = MODULE.capture(self.runtime)
            data["files"][0]["path"] = bad_name
            with self.assertRaises(ValueError):
                MODULE.validate_snapshot(data)
        data = MODULE.capture(self.runtime)
        data["files"].append(data["files"][0].copy())
        with self.assertRaises(ValueError):
            MODULE.validate_snapshot(data)

    def test_symlink_cannot_capture_external_private_data(self):
        (self.runtime / "private.txt").symlink_to(self.response)
        with self.assertRaisesRegex(ValueError, "Symlink"):
            MODULE.capture(self.runtime)

    def test_existing_output_is_preserved(self):
        self.record()
        before = (self.root / "run/response.md").read_bytes()
        with self.assertRaises(FileExistsError):
            self.record()
        self.assertEqual(before, (self.root / "run/response.md").read_bytes())
        with self.assertRaises(FileExistsError):
            MODULE.write_new(self.snapshot, {})

    def test_blank_output_does_not_become_a_run(self):
        self.response.write_text(" \n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Empty response"):
            self.record()
        self.assertFalse((self.root / "run").exists())


if __name__ == "__main__":
    unittest.main()
