import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class IntelligenceSchemaTests(unittest.TestCase):
    def test_structured_intelligence_schemas_exist_and_runtime_state_references_them(self):
        expected = [
            "task-interpretation.schema.json",
            "research-plan.schema.json",
            "teaming-plan.schema.json",
            "research-finding.schema.json",
        ]
        for name in expected:
            self.assertTrue((ROOT / "schemas" / name).is_file(), name)
        runtime_state = json.loads((ROOT / "schemas" / "runtime-state.schema.json").read_text())
        props = runtime_state["properties"]
        self.assertEqual(props["task_interpretation"]["$ref"], "task-interpretation.schema.json")
        self.assertEqual(props["research_plan"]["$ref"], "research-plan.schema.json")
        self.assertEqual(props["teaming_plan"]["$ref"], "teaming-plan.schema.json")

    def test_schemas_do_not_request_private_chain_of_thought(self):
        combined = "\n".join(path.read_text().lower() for path in (ROOT / "schemas").glob("*.json"))
        self.assertNotIn("chain_of_thought", combined)
        self.assertNotIn("chain-of-thought", combined)


if __name__ == "__main__":
    unittest.main()
