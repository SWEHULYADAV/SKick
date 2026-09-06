import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

from runtime.capabilities import discover_capabilities
from runtime.model import CapabilityState


class CapabilityDiscoveryTests(unittest.TestCase):
    def test_filesystem_read_write_are_observed_and_network_stays_unknown_by_default(self):
        with tempfile.TemporaryDirectory() as tmp:
            snapshot = discover_capabilities(Path(tmp))
        self.assertEqual(snapshot.capabilities["filesystem_read"].state, CapabilityState.AVAILABLE)
        self.assertEqual(snapshot.capabilities["filesystem_write"].state, CapabilityState.AVAILABLE)
        self.assertEqual(snapshot.capabilities["network"].state, CapabilityState.UNKNOWN)
        self.assertEqual(snapshot.capabilities["web_search"].state, CapabilityState.UNKNOWN)

    def test_git_executable_and_git_repository_are_distinct_capabilities(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            before = discover_capabilities(root)
            if before.capabilities["git"].state != CapabilityState.AVAILABLE:
                self.skipTest("git executable is not available in this environment")
            self.assertEqual(before.capabilities["git_repository"].state, CapabilityState.UNAVAILABLE)
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            after = discover_capabilities(root)
            self.assertEqual(after.capabilities["git_repository"].state, CapabilityState.AVAILABLE)

    def test_trusted_host_declaration_can_resolve_unknown_without_overwriting_observed_local_facts(self):
        with tempfile.TemporaryDirectory() as tmp:
            snapshot = discover_capabilities(
                Path(tmp),
                declared={
                    "web_search": {"state": "available", "provider": "host"},
                    "filesystem_read": {"state": "unavailable", "provider": "bad declaration"},
                },
            )
        self.assertEqual(snapshot.capabilities["web_search"].state, CapabilityState.AVAILABLE)
        self.assertEqual(snapshot.capabilities["web_search"].provider, "host")
        self.assertEqual(snapshot.capabilities["filesystem_read"].state, CapabilityState.AVAILABLE)
        self.assertIn("observed locally", snapshot.capabilities["filesystem_read"].evidence[0])

    def test_snapshot_serialization_never_dumps_environment_secrets(self):
        os.environ["SKICK_TEST_SECRET"] = "do-not-leak-this-value"
        try:
            with tempfile.TemporaryDirectory() as tmp:
                snapshot = discover_capabilities(Path(tmp))
            encoded = json.dumps(snapshot.to_dict())
            self.assertNotIn("do-not-leak-this-value", encoded)
            self.assertNotIn("SKICK_TEST_SECRET", encoded)
        finally:
            os.environ.pop("SKICK_TEST_SECRET", None)

    def test_host_only_capabilities_are_unknown_not_false_when_unobservable(self):
        with tempfile.TemporaryDirectory() as tmp:
            snapshot = discover_capabilities(Path(tmp))
        for name in ["browser_automation", "subagents", "approval_request", "secret_access", "mcp"]:
            self.assertEqual(snapshot.capabilities[name].state, CapabilityState.UNKNOWN, name)


if __name__ == "__main__":
    unittest.main()
