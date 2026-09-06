import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / "scripts" / "run_evals.py"
COMPARE = ROOT / "scripts" / "compare_evals.py"
BAD = ROOT / "tests" / "fixtures" / "eval_runner_self_reports_pass.py"
GOOD = ROOT / "tests" / "fixtures" / "eval_runner_good.py"
JUDGE = ROOT / "tests" / "fixtures" / "eval_judge_pass.py"


class EvalHarnessTests(unittest.TestCase):
    def _suite(self, directory: Path, checks):
        path = directory / "suite.json"
        path.write_text(json.dumps({"cases": [{"id": "safety", "prompt": "Return a safe answer", "checks": checks}]}), encoding="utf-8")
        return path

    def test_candidate_self_report_cannot_override_deterministic_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            suite = self._suite(d, [
                {"type": "contains", "field": "response", "value": "SAFE verified"},
                {"type": "not_contains", "field": "response", "value": "UNSAFE"}
            ])
            output = d / "out.json"
            proc = subprocess.run([sys.executable, str(RUN), str(suite), "--output", str(output), "--runner", sys.executable, str(BAD)], text=True, capture_output=True)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            data = json.loads(output.read_text())
        self.assertEqual(data["summary"]["candidate_reported_pass_rate"], 1.0)
        self.assertEqual(data["summary"]["pass_rate"], 0.0)
        self.assertFalse(data["results"][0]["scored_passed"])
        self.assertTrue(data["results"][0]["candidate_result"]["passed"])

    def test_deterministic_checks_can_pass_even_when_candidate_self_reports_false(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            suite = self._suite(d, [{"type": "contains", "field": "response", "value": "SAFE verified"}])
            output = d / "out.json"
            proc = subprocess.run([sys.executable, str(RUN), str(suite), "--output", str(output), "--runner", sys.executable, str(GOOD)], text=True, capture_output=True)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            data = json.loads(output.read_text())
        self.assertEqual(data["summary"]["pass_rate"], 1.0)
        self.assertFalse(data["results"][0]["candidate_result"]["passed"])
        self.assertTrue(data["results"][0]["scored_passed"])

    def test_optional_judge_is_separate_from_candidate_result(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            suite = self._suite(d, [])
            output = d / "out.json"
            proc = subprocess.run([
                sys.executable, str(RUN), str(suite), "--output", str(output),
                "--judge-command", f"{sys.executable} {JUDGE}",
                "--runner", sys.executable, str(GOOD)
            ], text=True, capture_output=True)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            data = json.loads(output.read_text())
        result = data["results"][0]
        self.assertIn("candidate_result", result)
        self.assertIn("judge_result", result)
        self.assertTrue(result["scored_passed"])
        self.assertEqual(result["score_source"], "judge")


    def test_windows_judge_command_preserves_backslashes(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location("run_evals", RUN)
        module = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(module)
        command = r"C:\Python314\python.exe C:\Users\Admin\judge.py"
        self.assertEqual(
            module.split_command(command, platform="nt"),
            [r"C:\Python314\python.exe", r"C:\Users\Admin\judge.py"],
        )

    def test_unscored_run_is_not_treated_as_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            suite = self._suite(d, [])
            output = d / "out.json"
            proc = subprocess.run([sys.executable, str(RUN), str(suite), "--output", str(output), "--runner", sys.executable, str(GOOD)], text=True, capture_output=True)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            data = json.loads(output.read_text())
        self.assertIsNone(data["summary"]["pass_rate"])
        self.assertEqual(data["summary"]["unscored_runs"], 1)
        self.assertIsNone(data["results"][0]["scored_passed"])


class CompareEvalTests(unittest.TestCase):
    def _write(self, path: Path, rows):
        path.write_text(json.dumps({
            "schema_version": 2,
            "summary": {"pass_rate": None},
            "results": [
                {"case_id": case, "run_index": run, "scored_passed": passed, "duration_seconds": 1.0}
                for case, run, passed in rows
            ]
        }), encoding="utf-8")

    def test_task_level_regressions_and_win_loss_tie_are_visible(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            base = d / "base.json"; cand = d / "cand.json"
            self._write(base, [("a", 0, True), ("b", 0, True)])
            self._write(cand, [("a", 0, True), ("b", 0, False)])
            proc = subprocess.run([sys.executable, str(COMPARE), str(base), str(cand)], text=True, capture_output=True)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            data = json.loads(proc.stdout)
        self.assertEqual(data["paired"]["wins"], 0)
        self.assertEqual(data["paired"]["losses"], 1)
        self.assertEqual(data["paired"]["ties"], 1)
        self.assertEqual(data["paired"]["success_delta"], -0.5)
        self.assertEqual(data["regressions"], ["b"])
        self.assertIsNone(data["paired"]["success_delta_ci95"])
        self.assertIn("a", data["tasks"])
        self.assertIn("b", data["tasks"])


if __name__ == "__main__":
    unittest.main()
