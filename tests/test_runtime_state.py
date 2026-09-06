import json
import unittest

from runtime.claims import add_claim
from runtime.state import add_evidence, new_run_state, validate_state


class RuntimeStateTests(unittest.TestCase):
    def test_new_state_is_json_serializable_and_has_no_chain_of_thought_field(self):
        state = new_run_state("Audit this repository")
        encoded = json.dumps(state)
        self.assertIn('"task"', encoded)
        forbidden = {"chain_of_thought", "reasoning", "scratchpad", "private_reasoning"}
        self.assertTrue(forbidden.isdisjoint(state))
        self.assertEqual(validate_state(state), [])

    def test_evidence_ids_are_unique_and_append_only(self):
        state = new_run_state("Test task")
        a = add_evidence(state, "source_file", "a.py", status="observed", source="a.py")
        b = add_evidence(state, "test_result", "unit tests", status="passed", source="unittest")
        self.assertNotEqual(a, b)
        self.assertEqual([item["id"] for item in state["evidence"]], [a, b])

    def test_validation_catches_missing_required_runtime_fields(self):
        state = new_run_state("Test task")
        del state["claims"]
        errors = validate_state(state)
        self.assertTrue(any("claims" in error for error in errors))

    def test_claims_reference_existing_evidence_when_supplied(self):
        state = new_run_state("Test task")
        ev = add_evidence(state, "source_file", "a.py", status="observed", source="a.py")
        claim_id = add_claim(state, "a.py was inspected", status="inspected", evidence_ids=[ev])
        self.assertEqual(state["claims"][0]["id"], claim_id)
        self.assertEqual(validate_state(state), [])


if __name__ == "__main__":
    unittest.main()
