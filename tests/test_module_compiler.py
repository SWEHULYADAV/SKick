import tempfile
import unittest
from pathlib import Path

from runtime.capabilities import discover_capabilities
from runtime.depth import classify_task
from runtime.modules import compile_modules


ROOT = Path(__file__).resolve().parents[1]


class ModuleCompilerTests(unittest.TestCase):
    def test_trivial_typo_task_loads_no_heavy_module_bundle(self):
        with tempfile.TemporaryDirectory() as tmp:
            caps = discover_capabilities(Path(tmp))
            decision = classify_task("Fix this typo in one README line only.")
            plan = compile_modules("Fix this typo in one README line only.", ROOT, caps, decision=decision)
        self.assertFalse(decision.activate)
        self.assertEqual(plan.selected, [])
        self.assertEqual(plan.total_estimated_tokens, 0)
        self.assertEqual(plan.plan_kind, "minimal")

    def test_oauth_debug_selects_repo_debug_security_testing_and_skips_unrelated_domains(self):
        task = "Fix an intermittent Next.js OAuth callback failure in this repo and review the patch for auth security regressions with tests."
        caps = discover_capabilities(ROOT, declared={"web_search": {"state": "available", "provider": "host"}})
        plan = compile_modules(task, ROOT, caps, decision=classify_task(task), budget_tokens=12000)
        selected = {item.path for item in plan.selected}
        self.assertIn("core/repository-research.md", selected)
        self.assertIn("core/engineering-feedback-loops.md", selected)
        self.assertIn("core/security-research.md", selected)
        self.assertIn("core/evidence-verification.md", selected)
        self.assertIn("core/verified-review-and-simplification.md", selected)
        self.assertNotIn("core/financial-and-economic-research.md", selected)
        self.assertNotIn("extensions/web3d-experience-design.md", selected)

    def test_missing_semantic_search_uses_generic_repository_fallback_and_does_not_force_serena(self):
        task = "Map this repository, trace callers and references, then fix the regression and test it."
        caps = discover_capabilities(ROOT, declared={"semantic_code_search": {"state": "unavailable", "provider": "host"}})
        plan = compile_modules(task, ROOT, caps, decision=classify_task(task), budget_tokens=8000)
        selected = {item.path for item in plan.selected}
        self.assertIn("core/repository-research.md", selected)
        self.assertNotIn("core/serena-integration.md", selected)
        self.assertTrue(any("fallback" in reason.lower() for reason in plan.routing_notes))

    def test_serena_module_is_selected_only_when_semantic_capability_provider_is_serena(self):
        task = "Deeply map this large repository and trace symbol references before changing code."
        caps = discover_capabilities(ROOT, declared={"semantic_code_search": {"state": "available", "provider": "Serena"}})
        plan = compile_modules(task, ROOT, caps, decision=classify_task(task), budget_tokens=12000)
        self.assertIn("core/serena-integration.md", {item.path for item in plan.selected})

    def test_budget_drops_optional_modules_before_mandatory_truth_and_trust_modules(self):
        task = "Deeply audit this repository security design, research current evidence, trace failure modes, and verify conclusions."
        caps = discover_capabilities(ROOT, declared={"web_search": {"state": "available", "provider": "host"}})
        plan = compile_modules(task, ROOT, caps, decision=classify_task(task), budget_tokens=2600)
        selected = {item.path for item in plan.selected}
        self.assertIn("core/untrusted-content-boundary.md", selected)
        self.assertIn("core/evidence-verification.md", selected)
        self.assertLessEqual(plan.total_estimated_tokens, plan.budget_tokens)
        self.assertTrue(plan.dropped_for_budget)

    def test_explicit_ablation_can_remove_evidence_module_for_experiments_only(self):
        task = "Deeply audit this repository and verify the evidence."
        caps = discover_capabilities(ROOT)
        full = compile_modules(task, ROOT, caps, decision=classify_task(task), budget_tokens=8000)
        ablated = compile_modules(task, ROOT, caps, decision=classify_task(task), budget_tokens=8000, ablations={"evidence-verification"})
        self.assertIn("core/evidence-verification.md", {item.path for item in full.selected})
        self.assertNotIn("core/evidence-verification.md", {item.path for item in ablated.selected})
        self.assertLess(ablated.total_estimated_tokens, full.total_estimated_tokens)
        self.assertTrue(any("ABLATION" in note for note in ablated.routing_notes))

    def test_plan_exposes_transparent_estimation_method_and_skips(self):
        task = "Research this repository architecture and verify the implementation evidence."
        caps = discover_capabilities(ROOT)
        plan = compile_modules(task, ROOT, caps, decision=classify_task(task), budget_tokens=7000)
        data = plan.to_dict()
        self.assertEqual(data["estimate_method"], "utf8_bytes_div_4")
        self.assertIn("skipped", data)
        self.assertIn("budget_tokens", data)
        self.assertGreaterEqual(data["root_control_plane_estimated_tokens"], 1)


if __name__ == "__main__":
    unittest.main()
