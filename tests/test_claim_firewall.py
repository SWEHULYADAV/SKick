import unittest

from runtime.claims import ClaimFirewallError, add_claim, set_claim_status
from runtime.report import render_report
from runtime.state import add_evidence, new_run_state


class ClaimFirewallTests(unittest.TestCase):
    def setUp(self):
        self.state = new_run_state("Fix the auth regression")
        self.claim_id = add_claim(
            self.state,
            "The authentication regression is fixed",
            status="implemented",
            claim_type="code_change",
        )

    def _bound(self, evidence_type, subject, *, status, source=None, claim_id=None, **metadata):
        target = claim_id or self.claim_id
        return add_evidence(
            self.state,
            evidence_type,
            subject,
            status=status,
            source=source,
            metadata={"supports_claim_ids": [target], **metadata},
        )

    def test_tested_requires_passing_test_evidence(self):
        with self.assertRaises(ClaimFirewallError):
            set_claim_status(self.state, self.claim_id, "tested")
        failed = self._bound("test_result", "auth regression", status="failed", source="pytest")
        with self.assertRaises(ClaimFirewallError):
            set_claim_status(self.state, self.claim_id, "tested", evidence_ids=[failed])
        passed = self._bound("test_result", "auth regression", status="passed", source="pytest")
        set_claim_status(self.state, self.claim_id, "tested", evidence_ids=[passed])
        self.assertEqual(self.state["claims"][0]["status"], "tested")

    def test_docs_verified_requires_first_party_documentation(self):
        docs_claim = add_claim(
            self.state,
            "Platform X documents native Skill support",
            status="implemented",
            claim_type="platform_compatibility",
        )
        external = self._bound(
            "external_documentation", "host skill support", status="observed", source="blog", claim_id=docs_claim
        )
        with self.assertRaises(ClaimFirewallError):
            set_claim_status(self.state, docs_claim, "docs_verified", evidence_ids=[external])
        official = self._bound(
            "first_party_documentation", "host skill support", status="verified", source="official docs", claim_id=docs_claim
        )
        set_claim_status(self.state, docs_claim, "docs_verified", evidence_ids=[official])
        claim = next(item for item in self.state["claims"] if item["id"] == docs_claim)
        self.assertEqual(claim["status"], "docs_verified")

    def test_live_verified_requires_successful_live_runtime_observation(self):
        docs = self._bound(
            "first_party_documentation", "auth implementation docs", status="verified", source="official docs"
        )
        with self.assertRaises(ClaimFirewallError):
            set_claim_status(self.state, self.claim_id, "live_verified", evidence_ids=[docs])
        live = self._bound("runtime_observation", "auth regression reproduction", status="passed", source="real runtime")
        set_claim_status(self.state, self.claim_id, "live_verified", evidence_ids=[live])
        self.assertEqual(self.state["claims"][0]["status"], "live_verified")

    def test_verified_cannot_be_created_from_inference_or_static_analysis_alone(self):
        inference = self._bound("inference", "likely root cause", status="observed", source="analysis")
        with self.assertRaises(ClaimFirewallError):
            set_claim_status(self.state, self.claim_id, "verified", evidence_ids=[inference])
        static = self._bound("static_analysis", "package manifest integrity", status="passed", source="validator")
        with self.assertRaises(ClaimFirewallError):
            set_claim_status(self.state, self.claim_id, "verified", evidence_ids=[static])
        regression = self._bound("test_result", "auth regression test", status="passed", source="pytest")
        set_claim_status(self.state, self.claim_id, "verified", evidence_ids=[regression])
        self.assertEqual(self.state["claims"][0]["status"], "verified")

    def test_renderer_never_promotes_tampered_claim_without_evidence(self):
        self.state["claims"][0]["status"] = "verified"
        self.state["claims"][0]["evidence_ids"] = []
        report = render_report(self.state)
        self.assertNotIn("[VERIFIED] The authentication regression is fixed", report)
        self.assertIn("[UNKNOWN] The authentication regression is fixed", report)
        self.assertIn("claim firewall", report.lower())

    def test_not_tested_is_visible(self):
        set_claim_status(self.state, self.claim_id, "not_tested")
        report = render_report(self.state)
        self.assertIn("[NOT TESTED] The authentication regression is fixed", report)


if __name__ == "__main__":
    unittest.main()
