import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCTOR = ROOT / "scripts" / "skick_doctor.py"


class InstallDoctorTests(unittest.TestCase):
    def test_doctor_separates_detected_inferred_and_unverified_facts(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            (project / ".opencode").mkdir()
            proc = subprocess.run([sys.executable, str(DOCTOR), "--project", str(project), "--target", "opencode", "--json"], text=True, capture_output=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        data = json.loads(proc.stdout)
        self.assertIn("detected", data)
        self.assertIn("inferred", data)
        self.assertIn("unverified", data)
        self.assertEqual(data["target"], "opencode")
        self.assertTrue(any("discovery" in item.lower() for item in data["unverified"]))


if __name__ == "__main__":
    unittest.main()
