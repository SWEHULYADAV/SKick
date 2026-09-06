import unittest

from runtime.depth import classify_task


class DepthSelectionTests(unittest.TestCase):
    def test_trivial_arithmetic_is_quick_and_does_not_auto_activate(self):
        decision = classify_task("2 + 2")
        self.assertFalse(decision.activate)
        self.assertEqual(decision.depth, "quick")
        self.assertEqual(decision.mode, "research")

    def test_tiny_typo_edit_uses_quick_minimum_process(self):
        decision = classify_task("Fix this typo in one README line only.")
        self.assertFalse(decision.activate)
        self.assertEqual(decision.depth, "quick")
        self.assertEqual(decision.mode, "build")

    def test_repository_bug_activates_standard_or_deeper(self):
        decision = classify_task("Fix the failing payment webhook in this repo and add a regression test.")
        self.assertTrue(decision.activate)
        self.assertIn(decision.depth, {"standard", "deep"})
        self.assertEqual(decision.mode, "debug")

    def test_intermittent_production_auth_failure_is_deep(self):
        decision = classify_task("Debug an intermittent authentication failure in production across the API and worker, find the mechanism, patch it, and verify the fix.")
        self.assertTrue(decision.activate)
        self.assertIn(decision.depth, {"deep", "exhaustive"})
        self.assertEqual(decision.mode, "debug")
        self.assertTrue(any("production" in reason.lower() or "security" in reason.lower() for reason in decision.reasons))

    def test_current_vulnerability_research_patch_and_validation_escalates(self):
        decision = classify_task("Research the current vulnerability, identify affected code in this repository, patch it, and validate the patch with security regression tests.")
        self.assertTrue(decision.activate)
        self.assertIn(decision.depth, {"deep", "exhaustive"})
        self.assertEqual(decision.mode, "security")

    def test_auth_exploitability_audit_is_security_and_deep(self):
        decision = classify_task("Audit this authentication system and prove whether this vulnerability is exploitable.")
        self.assertTrue(decision.activate)
        self.assertIn(decision.depth, {"deep", "exhaustive"})
        self.assertEqual(decision.mode, "security")

    def test_explicit_depth_and_skick_invocation_override_heuristics(self):
        decision = classify_task("Use SKick in exhaustive mode to review this one line.")
        self.assertTrue(decision.activate)
        self.assertEqual(decision.depth, "exhaustive")
        self.assertEqual(decision.explicit_depth, "exhaustive")

    def test_explicit_function_argument_wins(self):
        decision = classify_task("Summarize this tiny config file.", explicit_depth="deep")
        self.assertTrue(decision.activate)
        self.assertEqual(decision.depth, "deep")


if __name__ == "__main__":
    unittest.main()
