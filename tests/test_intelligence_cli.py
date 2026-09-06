import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "skick_runtime.py"


class IntelligenceCliTests(unittest.TestCase):
    def _json(self, *args):
        proc = subprocess.run([sys.executable, str(CLI), *args], text=True, capture_output=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        return json.loads(proc.stdout)

    def test_enhance_visible_returns_reusable_spec_and_structured_intent(self):
        data = self._json("enhance", "--task", "check why auth broken", "--mode", "visible")
        self.assertEqual(data["enhancement_mode"], "visible")
        self.assertIn("interpreted_goal", data)
        self.assertIn("rendered_spec", data)

    def test_research_plan_command_exposes_question_map_and_budget(self):
        data = self._json("research-plan", "--task", "Deep research current platform Skill support")
        self.assertEqual(data["level"], "deep")
        self.assertTrue(data["question_map"]["decision_critical_questions"])
        self.assertGreater(data["budget"]["max_queries"], 0)

    def test_research_finding_cli_records_lineage_and_fact_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = Path(tmp) / "run.json"
            create = subprocess.run([sys.executable, str(CLI), "new-state", "--task", "Research support", "--output", str(state)], text=True, capture_output=True)
            self.assertEqual(create.returncode, 0, create.stderr)
            evidence = subprocess.run([sys.executable, str(CLI), "add-evidence", "--state", str(state), "--type", "first_party_documentation", "--subject", "Official docs", "--status", "verified", "--source", "https://example.invalid/docs", "--lineage-root", "vendor-doc", "--authority", "primary"], text=True, capture_output=True)
            self.assertEqual(evidence.returncode, 0, evidence.stderr)
            evidence_id = evidence.stdout.strip()
            finding = subprocess.run([sys.executable, str(CLI), "add-finding", "--state", str(state), "--question", "Does it work?", "--claim", "Docs state it works", "--kind", "fact", "--evidence", evidence_id], text=True, capture_output=True)
            self.assertEqual(finding.returncode, 0, finding.stderr)
            data = json.loads(state.read_text(encoding="utf-8"))
            self.assertEqual(data["evidence"][0]["metadata"]["lineage_root"], "vendor-doc")
            self.assertEqual(data["research_findings"][0]["kind"], "fact")

    def test_team_plan_command_keeps_unknown_authorization_safe(self):
        data = self._json("team-plan", "--task", "Exploit this auth bypass and prove it works")
        self.assertIn("red", data["roles"])
        self.assertEqual(data["security_scope"]["authorization_context"], "unknown")
        self.assertEqual(data["security_scope"]["safe_test_boundary"], "lab_or_simulation_only")


if __name__ == "__main__":
    unittest.main()
