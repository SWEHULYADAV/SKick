import unittest

from runtime.teaming import TeamRole, build_teaming_plan


class TeamingIntelligenceTests(unittest.TestCase):
    def test_simple_factual_task_uses_no_teaming(self):
        plan = build_teaming_plan("What is the capital of France?")
        self.assertEqual(plan.roles, [])

    def test_non_security_multi_perspective_architecture_can_select_all_roles(self):
        plan = build_teaming_plan("Run a multi-perspective adversarial review of this migration architecture and synthesize the strongest design.")
        self.assertEqual([role.value for role in plan.roles], ["red", "blue", "purple", "black_blind"])
        self.assertEqual(plan.security_scope["authorization_context"], "not_applicable")
        self.assertIn("synthesis", plan.validation_loop[-1])

    def test_architecture_decision_can_request_independent_black_review(self):
        plan = build_teaming_plan("Review this high-impact architecture migration and challenge hidden assumptions.")
        self.assertIn(TeamRole.BLACK, plan.roles)
        self.assertNotIn(TeamRole.RED, plan.roles)

    def test_ordinary_auth_debug_does_not_force_adversarial_teaming(self):
        plan = build_teaming_plan("check why auth broken")
        self.assertEqual(plan.roles, [])

    def test_security_review_selects_red_and_blue_without_forcing_purple(self):
        plan = build_teaming_plan("Security review this authentication design for abuse paths and defensive controls.")
        self.assertIn(TeamRole.RED, plan.roles)
        self.assertIn(TeamRole.BLUE, plan.roles)

    def test_security_remediation_selects_purple_validation_loop(self):
        plan = build_teaming_plan("Patch this authentication vulnerability in our local test app and retest the mitigation.")
        self.assertIn(TeamRole.RED, plan.roles)
        self.assertIn(TeamRole.BLUE, plan.roles)
        self.assertIn(TeamRole.PURPLE, plan.roles)
        self.assertTrue(plan.validation_loop)

    def test_high_risk_security_architecture_adds_black_review(self):
        plan = build_teaming_plan("Deep security architecture audit of production auth boundaries, exploitability, mitigation, and independent review.")
        self.assertEqual(set(plan.roles), {TeamRole.RED, TeamRole.BLUE, TeamRole.PURPLE, TeamRole.BLACK})

    def test_missing_authorization_constrains_offensive_validation_to_safe_lab(self):
        plan = build_teaming_plan("Exploit this auth bypass and prove it works.")
        self.assertEqual(plan.security_scope["authorization_context"], "unknown")
        self.assertEqual(plan.security_scope["safe_test_boundary"], "lab_or_simulation_only")

    def test_owned_local_lab_is_recorded_as_authorized_context(self):
        plan = build_teaming_plan("In my owned local Docker lab, validate this auth bypass then patch and retest it.")
        self.assertEqual(plan.security_scope["authorization_context"], "user_owned_lab")
        self.assertEqual(plan.security_scope["environment"], "local_lab")


if __name__ == "__main__":
    unittest.main()

class SecurityTeamingStructureTests(unittest.TestCase):
    def test_purple_plan_maps_attack_surface_and_offense_to_defense_validation(self):
        plan = build_teaming_plan(
            "In my owned local Docker lab, security test this API auth bypass, patch it, add detection, and retest."
        )
        data = plan.to_dict()
        self.assertIn("api", data["attack_surface"])
        self.assertIn("identity_authorization", data["attack_surface"])
        self.assertEqual(
            list(data["offensive_to_defensive"].keys()),
            ["attack_prerequisite", "preventive_control", "detective_control", "response", "validation"],
        )
        self.assertIn("red_retest", data["validation_loop"])

    def test_black_review_has_independence_contract(self):
        plan = build_teaming_plan("Independent review this high-impact architecture migration for hidden assumptions.")
        self.assertIn(TeamRole.BLACK, plan.roles)
        self.assertIn("primary conclusion", plan.independence_contract.lower())
