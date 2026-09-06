import unittest

from runtime.prompt_intelligence import EnhancementMode, analyze_prompt_quality, interpret_task


class PromptIntelligenceTests(unittest.TestCase):
    def test_weak_auth_prompt_preserves_original_and_adds_execution_structure(self):
        task = interpret_task("check why auth broken")
        self.assertEqual(task.original_request, "check why auth broken")
        self.assertIn("authentication", task.interpreted_goal.lower())
        self.assertIn("software_engineering", task.domains)
        self.assertTrue(any("root cause" in item.lower() for item in task.success_criteria))
        self.assertTrue(any("test" in item.lower() or "reproduce" in item.lower() for item in task.verification_needs))
        self.assertLessEqual(len(task.success_criteria), 5)

    def test_explicit_user_constraint_is_locked_not_rewritten_as_assumption(self):
        task = interpret_task("Fix the OAuth callback but do not change the public API.")
        self.assertTrue(any("do not change the public api" in item.lower() for item in task.constraints))
        self.assertFalse(any("public api" in item.lower() for item in task.assumptions))

    def test_tiny_rename_does_not_expand_into_research_project(self):
        task = interpret_task("Rename variable foo to bar.")
        self.assertEqual(task.research_needs, [])
        self.assertLessEqual(len(task.success_criteria), 2)
        self.assertEqual(task.enhancement_mode, EnhancementMode.SILENT)

    def test_visible_enhancement_is_explicit_and_reusable(self):
        task = interpret_task("Improve this prompt: check why auth broken", mode="visible")
        self.assertEqual(task.enhancement_mode, EnhancementMode.VISIBLE)
        rendered = task.render_spec()
        self.assertIn("Original request", rendered)
        self.assertIn("Success criteria", rendered)

    def test_contradiction_detection_keeps_tradeoff_visible(self):
        task = interpret_task("Research this exhaustively but use almost no tokens.")
        self.assertTrue(task.contradictions)
        self.assertTrue(any("exhaust" in item.lower() and "token" in item.lower() for item in task.contradictions))

    def test_quality_analyzer_exposes_execution_relevant_dimensions(self):
        quality = analyze_prompt_quality("Research the current auth behavior in this repo and verify the fix.")
        for key in (
            "missing_context", "output_definition", "hidden_assumption_risk",
            "tool_requirements", "safety_security_implications", "likely_failure_modes",
        ):
            self.assertIn(key, quality)
        self.assertEqual(quality["freshness_requirements"], "required")
        self.assertEqual(quality["safety_security_implications"], "present")

    def test_quality_analyzer_identifies_missing_success_and_verification(self):
        quality = analyze_prompt_quality("fix this")
        self.assertEqual(quality["intent_clarity"], "low")
        self.assertEqual(quality["success_criteria"], "missing")
        self.assertEqual(quality["verification_requirements"], "missing")


if __name__ == "__main__":
    unittest.main()

class StrictSpecPromptTests(unittest.TestCase):
    def test_strict_spec_exposes_outputs_evidence_non_goals_and_failure_conditions(self):
        task = interpret_task(
            "Implement the smallest safe auth fix without changing the public API and verify it.",
            mode="strict_spec",
        )
        data = task.to_dict()
        self.assertTrue(data["outputs"])
        self.assertTrue(data["evidence_requirements"])
        self.assertTrue(data["non_goals"])
        self.assertTrue(data["failure_conditions"])
        self.assertIn("public API", "\n".join(data["constraints"]))
