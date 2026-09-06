import unittest

from runtime.research_ledger import (
    FindingKind,
    ResearchLedgerError,
    add_research_finding,
    evidence_independence_groups,
    summarize_research_evidence,
    set_research_coverage,
    update_research_frontier,
)
from runtime.state import add_evidence, new_run_state, validate_state


class ResearchLedgerTests(unittest.TestCase):
    def test_fact_requires_non_inference_evidence(self):
        state = new_run_state("research")
        with self.assertRaises(ResearchLedgerError):
            add_research_finding(state, "Does X work?", "X works", kind="fact", evidence_ids=[])
        ev = add_evidence(state, "first_party_documentation", "Official support docs", status="verified", source="https://example.invalid/docs")
        finding_id = add_research_finding(state, "Does X work?", "Docs state X works", kind="fact", evidence_ids=[ev])
        self.assertTrue(finding_id.startswith("rf-"))

    def test_hypothesis_does_not_silently_become_fact(self):
        state = new_run_state("debug")
        finding_id = add_research_finding(state, "Why failing?", "Clock skew may explain the failure", kind="hypothesis")
        finding = next(item for item in state["research_findings"] if item["id"] == finding_id)
        self.assertEqual(finding["kind"], FindingKind.HYPOTHESIS.value)
        self.assertEqual(finding["confidence"], "unresolved")

    def test_source_independence_groups_shared_lineage(self):
        state = new_run_state("research")
        a = add_evidence(state, "external_documentation", "Blog A", status="observed", source="https://a.example", metadata={"lineage_root": "vendor-release"})
        b = add_evidence(state, "external_documentation", "Blog B", status="observed", source="https://b.example", metadata={"lineage_root": "vendor-release"})
        c = add_evidence(state, "source_code", "Implementation", status="observed", source="repo://src", metadata={"lineage_root": "implementation"})
        groups = evidence_independence_groups(state, [a, b, c])
        self.assertEqual(len(groups), 2)
        self.assertEqual(sorted(len(group) for group in groups.values()), [1, 2])

    def test_triangulation_distinguishes_lineage_from_independent_paths(self):
        state = new_run_state("research")
        docs_a = add_evidence(state, "first_party_documentation", "Official docs copy A", status="verified", source="https://vendor.example/docs", metadata={"lineage_root": "vendor-doc", "authority": "primary"})
        docs_b = add_evidence(state, "external_documentation", "Syndicated copy", status="observed", source="https://blog.example/copy", metadata={"lineage_root": "vendor-doc", "authority": "independent"})
        code = add_evidence(state, "source_code", "Loader implementation", status="observed", source="repo://loader", metadata={"lineage_root": "implementation", "authority": "primary"})
        summary = summarize_research_evidence(state, [docs_a, docs_b, code])
        self.assertEqual(summary["independent_path_count"], 2)
        self.assertEqual(summary["classification"], "PRIMARY_PLUS_IMPLEMENTATION")
        self.assertEqual(summary["lineage_group_sizes"], [2, 1])

    def test_frontier_and_coverage_updates_are_explicit(self):
        state = new_run_state("research", research_plan={"frontier": {"unresolved": ["live invocation"]}})
        update_research_frontier(state, resolved=["docs support"], unresolved=["live invocation", "plan availability"])
        set_research_coverage(state, "official_docs", "covered")
        set_research_coverage(state, "live_test", "blocked")
        self.assertIn("docs support", state["research_frontier"]["resolved"])
        self.assertEqual(state["research_coverage"]["live_test"], "blocked")
        self.assertEqual(validate_state(state), [])

    def test_invalid_evidence_reference_is_rejected(self):
        state = new_run_state("research")
        with self.assertRaises(ResearchLedgerError):
            add_research_finding(state, "q", "claim", kind="inference", evidence_ids=["ev-missing"])


if __name__ == "__main__":
    unittest.main()
