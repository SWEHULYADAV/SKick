import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "scripts" / "install_skick.py"


class InstallerStatusTests(unittest.TestCase):
    def test_dry_run_json_does_not_claim_install_or_discovery(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            (project / ".opencode").mkdir()
            proc = subprocess.run([
                sys.executable, str(INSTALLER), "--source", str(ROOT), "--target", "opencode",
                "--scope", "project", "--project", str(project), "--dry-run", "--json"
            ], text=True, capture_output=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        data = json.loads(proc.stdout)
        self.assertEqual(data["copy_state"], "not_performed")
        self.assertEqual(data["install_state"], "planned")
        self.assertEqual(data["discovered"], "unknown")
        self.assertEqual(data["invokable"], "unknown")
        self.assertEqual(data["live_tested"], "unknown")

    def test_actual_copy_reports_copied_installed_but_not_discovered(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "project"
            project.mkdir()
            destination = Path(tmp) / "installed" / "skick"
            proc = subprocess.run([
                sys.executable, str(INSTALLER), "--source", str(ROOT), "--target", "agents",
                "--scope", "project", "--project", str(project), "--destination", str(destination), "--json"
            ], text=True, capture_output=True)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            data = json.loads(proc.stdout)
            self.assertEqual(data["copy_state"], "copied")
            self.assertEqual(data["install_state"], "installed")
            self.assertEqual(data["discovered"], "unknown")
            self.assertTrue((destination / "SKILL.md").is_file())


if __name__ == "__main__":
    unittest.main()
