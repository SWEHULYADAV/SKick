import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "skick_runtime.py"


class RuntimeCliTests(unittest.TestCase):
    def test_status_reports_observed_and_unknown_capabilities(self):
        with tempfile.TemporaryDirectory() as tmp:
            proc = subprocess.run([sys.executable, str(CLI), "status", "--project", tmp, "--json"], text=True, capture_output=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        data = json.loads(proc.stdout)
        self.assertEqual(data["capabilities"]["filesystem_read"]["state"], "available")
        self.assertEqual(data["capabilities"]["network"]["state"], "unknown")
        self.assertIn("runtime_candidates", data)

    def test_compile_outputs_task_depth_modules_and_budget(self):
        task = "Fix the failing OAuth callback in this repo and add security regression tests."
        proc = subprocess.run([sys.executable, str(CLI), "compile", "--project", str(ROOT), "--task", task, "--budget", "9000"], text=True, capture_output=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        data = json.loads(proc.stdout)
        self.assertIn(data["decision"]["depth"], {"standard", "deep", "exhaustive"})
        self.assertEqual(data["module_plan"]["budget_tokens"], 9000)
        self.assertTrue(data["module_plan"]["selected"])

    def test_state_evidence_claim_and_report_round_trip(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = Path(tmp) / "run.json"
            create = subprocess.run([sys.executable, str(CLI), "new-state", "--task", "Fix auth", "--output", str(state)], text=True, capture_output=True)
            self.assertEqual(create.returncode, 0, create.stderr)
            add_claim = subprocess.run([sys.executable, str(CLI), "set-claim", "--state", str(state), "--text", "Auth patch implemented", "--status", "not_tested"], text=True, capture_output=True)
            self.assertEqual(add_claim.returncode, 0, add_claim.stderr)
            report = subprocess.run([sys.executable, str(CLI), "report", "--state", str(state)], text=True, capture_output=True)
            self.assertEqual(report.returncode, 0, report.stderr)
            self.assertIn("[NOT TESTED] Auth patch implemented", report.stdout)


if __name__ == "__main__":
    unittest.main()
