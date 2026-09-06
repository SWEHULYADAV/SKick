import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / "tests" / "fixtures" / "security_auth_lab" / "lab.py"


def load_lab():
    spec = importlib.util.spec_from_file_location("security_auth_lab", LAB)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


class SecurityAuthLabFixtureTests(unittest.TestCase):
    def test_fixture_has_reproducible_cross_tenant_failure_and_fixed_control(self):
        lab = load_lab()
        records = lab.sample_records()
        leaked = lab.vulnerable_get_project("tenant-a", "project-b", records)
        self.assertEqual(leaked["secret"], "tenant-b-secret")
        with self.assertRaises(PermissionError):
            lab.fixed_get_project("tenant-a", "project-b", records)
        own = lab.fixed_get_project("tenant-a", "project-a", records)
        self.assertEqual(own["secret"], "tenant-a-secret")


if __name__ == "__main__":
    unittest.main()
