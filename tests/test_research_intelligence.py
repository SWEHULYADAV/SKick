import unittest

from runtime.research import ResearchLevel, build_research_plan, route_source_classes, transform_queries


class ResearchIntelligenceTests(unittest.TestCase):
    def test_trivial_stable_question_needs_no_external_research(self):
        plan = build_research_plan("What is 2 + 2?")
        self.assertEqual(plan.level, ResearchLevel.NONE)
        self.assertEqual(plan.query_classes, {})

    def test_current_compatibility_gets_question_map_freshness_and_disconfirmation(self):
        plan = build_research_plan("Deep research whether platform X currently supports Agent Skills and explicit activation.")
        self.assertIn(plan.level, {ResearchLevel.DEEP, ResearchLevel.LATERAL})
        self.assertTrue(plan.freshness_required)
        self.assertTrue(plan.question_map["decision_critical_questions"])
        self.assertIn("disconfirmation", plan.strategies)
        self.assertIn("historical", plan.strategies)
        self.assertIn("first_party_documentation", plan.expected_source_types)
        self.assertGreater(plan.budget["max_queries"], 1)

    def test_platform_source_router_prioritizes_first_party_before_community(self):
        sources = route_source_classes("product_platform")
        self.assertEqual(sources[0], "first_party_documentation")
        self.assertLess(sources.index("official_release_notes"), sources.index("community_reports"))

    def test_security_source_router_includes_advisory_and_patch_evidence(self):
        sources = route_source_classes("security")
        self.assertIn("vendor_security_advisory", sources)
        self.assertIn("patch_commit_or_source", sources)
        self.assertIn("known_exploitation_catalog", sources)

    def test_query_transformation_branches_by_evidence_neighborhood(self):
        queries = transform_queries("Codex supports Skills", entity="Codex", feature="Skills")
        self.assertEqual(set(queries), {"direct", "negative", "failure", "historical", "implementation", "change", "discussion"})
        self.assertNotEqual(queries["direct"], queries["failure"])
        self.assertIn("unsupported", queries["negative"].lower())

    def test_deep_research_plan_exposes_graph_branches(self):
        plan = build_research_plan("Deep research whether platform X currently supports Agent Skills.")
        self.assertEqual(plan.graph["root"], plan.question_map["primary_question"])
        self.assertIn("implementation", plan.graph["branches"])
        self.assertIn("contradicting_evidence", plan.graph["branches"])
        self.assertIn("historical_version", plan.graph["branches"])

    def test_explicit_research_output_mode_is_respected(self):
        self.assertEqual(build_research_plan("Research this and return an evidence matrix.").output_mode, "evidence_matrix")
        self.assertEqual(build_research_plan("Research this as a decision memo.").output_mode, "decision_memo")
        self.assertEqual(build_research_plan("Research this and give an investigation log.").output_mode, "investigation_log")

    def test_research_plan_exposes_frontier_coverage_and_stop_rules(self):
        plan = build_research_plan("Research whether a library's latest release fixes a security regression.")
        self.assertTrue(plan.frontier["unresolved"])
        self.assertIn("official_docs", plan.coverage)
        self.assertEqual(plan.coverage["official_docs"], "unexplored")
        self.assertTrue(any("decision-critical" in item.lower() for item in plan.stopping_criteria))


if __name__ == "__main__":
    unittest.main()

class ResearchPlanningDepthTests(unittest.TestCase):
    def test_deep_research_exposes_pivots_terminology_and_information_gain_rule(self):
        plan = build_research_plan("Deep research whether platform X currently supports Agent Skills.")
        data = plan.to_dict()
        self.assertTrue(data["pivot_rules"])
        self.assertTrue(any("documentation" in item and "source" in item for item in data["pivot_rules"]))
        self.assertIn("agent skill", data["terminology_expansion"])
        self.assertIn("information", data["information_gain_rule"].lower())
        self.assertIn(data["output_mode"], {"research_brief", "deep_dive", "evidence_matrix"})

    def test_security_research_generates_mechanism_hypothesis_dimensions(self):
        plan = build_research_plan("Deep research an intermittent authentication security failure and possible bypass.")
        self.assertIn("configuration", plan.hypothesis_dimensions)
        self.assertIn("timing", plan.hypothesis_dimensions)
        self.assertIn("authorization", plan.hypothesis_dimensions)

class ResearchFailureTaxonomyTests(unittest.TestCase):
    def test_research_failure_taxonomy_includes_paywall_without_guessing_through_it(self):
        plan = build_research_plan("Research the latest implementation details for this platform.")
        self.assertIn("PAYWALL", plan.failure_taxonomy)
