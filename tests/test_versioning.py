import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class VersioningTests(unittest.TestCase):
    def test_distribution_builder_does_not_hardcode_current_release(self):
        text = (ROOT / 'scripts' / 'build_distributions.py').read_text(encoding='utf-8')
        self.assertNotIn('LABEL = "v1.0"', text)
        self.assertNotIn('PLUGIN_VERSION = "1.0.0"', text)
        self.assertIn('read_package_version', text)

    def test_package_validator_reads_version_file(self):
        text = (ROOT / 'scripts' / 'validate_package.py').read_text(encoding='utf-8')
        self.assertNotIn('RELEASE = "1.0"', text)
        self.assertIn('read_package_version', text)

    def test_distribution_validator_derives_wrapper_version(self):
        text = (ROOT / 'scripts' / 'validate_distributions.py').read_text(encoding='utf-8')
        self.assertNotIn('m.get("version") != "1.0.0"', text)
        self.assertIn('normalize_semver', text)

    def test_version_helper_normalizes_semver_for_plugin_wrappers(self):
        from runtime.versioning import normalize_semver
        self.assertEqual(normalize_semver('1.0'), '1.0.0')
        self.assertEqual(normalize_semver('2.1.3'), '2.1.3')

    def test_other_executable_release_checks_are_derived_from_version(self):
        for rel in [
            'scripts/validate_mcp_catalog.py',
            'scripts/build_handoff_bundle.py',
            'scripts/validate_package.py',
        ]:
            text = (ROOT / rel).read_text(encoding='utf-8')
            self.assertNotRegex(text, r'\bv1\.0\b')
        self.assertIn('read_package_version', (ROOT / 'scripts/validate_mcp_catalog.py').read_text(encoding='utf-8'))
        self.assertIn('read_package_version', (ROOT / 'scripts/build_handoff_bundle.py').read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
