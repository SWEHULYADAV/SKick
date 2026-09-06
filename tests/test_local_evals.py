import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "scripts" / "run_local_evals.py"


class LocalEvalTests(unittest.TestCase):
    def _run(self, suite_name: str):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "out.json"
            proc = subprocess.run([sys.executable, str(RUNNER), str(ROOT / "evals" / suite_name), "--output", str(output), "--root", str(ROOT)], text=True, capture_output=True)
            self.assertEqual(proc.returncode, 0, proc.stderr + proc.stdout)
            data = json.loads(output.read_text())
        return data

    def test_routing_suite_passes_all_deterministic_cases(self):
        data = self._run("runtime-routing-evals.json")
        self.assertEqual(data["summary"]["pass_rate"], 1.0)
        self.assertGreaterEqual(data["summary"]["runs"], 8)
        self.assertTrue(all(r["score_source"] == "local_deterministic" for r in data["results"]))

    def test_output_uses_package_relative_suite_path(self):
        data = self._run("runtime-routing-evals.json")
        self.assertEqual(data["suite"], "evals/runtime-routing-evals.json")
        self.assertNotIn("/mnt/", json.dumps(data))
        self.assertNotIn("/home/", json.dumps(data))

    def test_routing_suite_reports_activation_confusion_and_depth_accuracy(self):
        data = self._run("runtime-routing-evals.json")
        activation = data["summary"]["activation_confusion"]
        self.assertEqual(activation, {"tp": 4, "tn": 3, "fp": 0, "fn": 0})
        self.assertEqual(data["summary"]["activation_accuracy"], 1.0)
        self.assertEqual(data["summary"]["depth_accuracy"], 1.0)

    def test_claim_honesty_suite_includes_rejection_cases_as_expected_passes(self):
        data = self._run("claim-honesty-evals.json")
        self.assertEqual(data["summary"]["pass_rate"], 1.0)
        rejected = {r["case_id"]: r["candidate_result"] for r in data["results"]}
        self.assertFalse(rejected["verified-without-evidence-rejected"]["allowed"])

    def test_security_injection_suite_passes_without_active_network_probe(self):
        data = self._run("security-injection-evals.json")
        self.assertEqual(data["summary"]["pass_rate"], 1.0)
        cap = next(r for r in data["results"] if r["case_id"] == "web-instruction-does-not-enable-network")
        self.assertEqual(cap["candidate_result"]["capabilities"]["network"], "unknown")

    def test_ablation_suite_exposes_token_savings_and_guard_regression(self):
        data = self._run("ablation-evals.json")
        self.assertEqual(data["summary"]["pass_rate"], 1.0)
        for row in data["results"]:
            result = row["candidate_result"]
            self.assertGreater(result["full_tokens"], result["ablated_tokens"])
            self.assertTrue(result["required_guard_missing"])

    def test_prompt_intelligence_suite_checks_structure_and_over_expansion(self):
        data = self._run("prompt-intelligence-evals.json")
        self.assertEqual(data["summary"]["pass_rate"], 1.0)
        self.assertEqual(data["summary"]["proof_type"], "deterministic_local_runtime")

    def test_research_intelligence_suite_checks_freshness_sources_and_disconfirmation(self):
        data = self._run("research-intelligence-evals.json")
        self.assertEqual(data["summary"]["pass_rate"], 1.0)

    def test_teaming_suite_checks_minimum_process_and_safe_scope(self):
        data = self._run("teaming-evals.json")
        self.assertEqual(data["summary"]["pass_rate"], 1.0)

    def test_research_ablation_is_labeled_planner_only(self):
        data = self._run("research-ablation-evals.json")
        self.assertEqual(data["summary"]["pass_rate"], 1.0)
        self.assertEqual(data["summary"]["behavioral_quality_measurement"], "NOT_MEASURED")
        for row in data["results"]:
            result = row["candidate_result"]
            self.assertGreater(result["full_query_classes"], result["direct_only_query_classes"])
            self.assertIn("disconfirmation", result["removed_without_disconfirmation"])


if __name__ == "__main__":
    unittest.main()
