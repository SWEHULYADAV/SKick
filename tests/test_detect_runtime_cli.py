import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "detect_runtime.py"


class DetectRuntimeCliTests(unittest.TestCase):
    def test_original_json_candidate_shape_is_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            proc = subprocess.run([sys.executable, str(SCRIPT), "--project", tmp, "--json"], text=True, capture_output=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        data = json.loads(proc.stdout)
        self.assertEqual(set(data), {"project", "candidates"})

    def test_capabilities_flag_adds_structured_snapshot_without_environment_dump(self):
        with tempfile.TemporaryDirectory() as tmp:
            proc = subprocess.run([sys.executable, str(SCRIPT), "--project", tmp, "--json", "--capabilities"], text=True, capture_output=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        data = json.loads(proc.stdout)
        self.assertIn("candidates", data)
        self.assertIn("capability_snapshot", data)
        self.assertEqual(data["capability_snapshot"]["capabilities"]["network"]["state"], "unknown")
        self.assertNotIn("environment", data["capability_snapshot"])


if __name__ == "__main__":
    unittest.main()
