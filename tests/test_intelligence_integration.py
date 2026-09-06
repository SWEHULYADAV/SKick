import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from runtime.capabilities import discover_capabilities
from runtime.orchestrator import build_execution_plan
from runtime.state import new_run_state, validate_state

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "skick_runtime.py"


class IntelligenceIntegrationTests(unittest.TestCase):
    def test_deep_platform_research_forces_research_intelligence_modules(self):
        caps = discover_capabilities(ROOT, active_network_probe=False)
        plan = build_execution_plan(
            "Deep research whether platform X currently supports Agent Skills and explicit activation.",
            ROOT,
            caps,
        )
        selected = {item["path"] for item in plan["module_plan"]["selected"]}
        self.assertNotIn("core/prompt-enhancement.md", selected)
        self.assertIn("core/research-core.md", selected)
        self.assertNotIn("core/research-source-router.md", selected)
        self.assertIn("core/query-mutation.md", selected)
        self.assertTrue(plan["research_plan"]["expected_source_types"])
        self.assertIn("core/coverage-and-lateral-search.md", selected)
        self.assertIn("core/evidence-verification.md", selected)
        self.assertIn("disconfirmation", plan["research_plan"]["strategies"])

    def test_purple_security_task_forces_security_and_validation_modules(self):
        caps = discover_capabilities(ROOT, active_network_probe=False)
        plan = build_execution_plan(
            "In my owned local Docker lab, security test this auth bypass, patch it, and retest the mitigation.",
            ROOT,
            caps,
            explicit_depth="deep",
        )
        selected = {item["path"] for item in plan["module_plan"]["selected"]}
        self.assertIn("red", plan["teaming_plan"]["roles"])
        self.assertIn("blue", plan["teaming_plan"]["roles"])
        self.assertIn("purple", plan["teaming_plan"]["roles"])
        self.assertIn("core/security-research.md", selected)
        self.assertIn("core/offensive-defensive.md", selected)
        self.assertIn("core/purple-team-research-and-validation.md", selected)

    def test_ordinary_auth_debug_stays_non_adversarial(self):
        caps = discover_capabilities(ROOT, active_network_probe=False)
        plan = build_execution_plan("check why auth broken", ROOT, caps, explicit_depth="standard")
        self.assertEqual(plan["teaming_plan"]["roles"], [])

    def test_runtime_state_can_persist_intelligence_without_hidden_reasoning(self):
        state = new_run_state(
            "research platform support",
            task_interpretation={"original_request": "research platform support", "interpreted_goal": "research platform support"},
            research_plan={"level": "standard", "frontier": {"unresolved": ["live test"]}},
            teaming_plan={"roles": []},
        )
        self.assertEqual(validate_state(state), [])
        self.assertIn("task_interpretation", state)
        self.assertIn("research_plan", state)
        self.assertIn("teaming_plan", state)
        self.assertNotIn("chain_of_thought", json.dumps(state).lower())

    def test_compile_cli_exposes_intelligence_plans(self):
        proc = subprocess.run(
            [sys.executable, str(CLI), "compile", "--project", str(ROOT), "--task", "Deep research current Agent Skills support"],
            text=True,
            capture_output=True,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        data = json.loads(proc.stdout)
        self.assertIn("task_interpretation", data)
        self.assertIn("research_plan", data)
        self.assertIn("teaming_plan", data)
        self.assertIn("module_plan", data)


if __name__ == "__main__":
    unittest.main()
