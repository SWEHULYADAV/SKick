import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class DocumentationTruthTests(unittest.TestCase):
    def test_readme_describes_runtime_without_hard_coded_route_marketing(self):
        text = (ROOT / 'README.md').read_text(encoding='utf-8')
        required = [
            '## What SKick is', '## What SKick is not', '## Architecture',
            '## Execution modes', '## Capability discovery', '## Progressive loading',
            '## Evidence and claim verification', '## Installation', '## Activation',
            '## Platform compatibility', '## Benchmarks', '## Security',
            '## Limitations', '## Versioning', '## Updating', '## Uninstalling',
            '## Contributing',
        ]
        for heading in required:
            self.assertIn(heading, text)
        lower = text.lower()
        self.assertNotIn('works everywhere', lower)
        self.assertNotIn('62 routes', lower)
        self.assertIn('doc_verified', lower)
        self.assertIn('live_tested', lower)
        self.assertLess(len(text.splitlines()), 700)

    def test_runtime_guarantee_doc_distinguishes_four_tiers(self):
        path = ROOT / 'docs' / 'RUNTIME_AND_GUARANTEE_LEVELS.md'
        text = path.read_text(encoding='utf-8')
        for tier in ('FULL RUNTIME', 'PARTIAL RUNTIME', 'DECLARATIVE MODE', 'PROMPT FALLBACK'):
            self.assertIn(tier, text)
        self.assertIn('Claim firewall', text)
        self.assertIn('Capability probe', text)

    def test_migration_guide_preserves_v1_and_explains_rollback(self):
        text = (ROOT / 'docs' / 'VNEXT_MIGRATION.md').read_text(encoding='utf-8')
        self.assertIn('v1', text)
        self.assertIn('backup', text.lower())
        self.assertIn('rollback', text.lower())
        self.assertIn('project-local', text.lower())

    def test_security_threat_model_is_local_first_and_has_no_phone_home(self):
        text = (ROOT / 'docs' / 'SECURITY_THREAT_MODEL.md').read_text(encoding='utf-8').lower()
        for marker in ('prompt injection', 'mcp', 'symlink', 'secret', 'local-first', 'opt-in'):
            self.assertIn(marker, text)
        self.assertIn('repository content is data', text)

    def test_contributing_requires_evidence_for_platforms_and_modules(self):
        text = (ROOT / 'CONTRIBUTING.md').read_text(encoding='utf-8').lower()
        for marker in ('literal `@skick`', 'verification status', 'estimated context cost', 'activation conditions', 'eval'):
            self.assertIn(marker, text)

    def test_changelog_has_v11_release_entry_with_proof_boundaries(self):
        text = (ROOT / 'CHANGELOG.md').read_text(encoding='utf-8')
        self.assertIn('## v1.1 — 2026-09-05', text)
        for heading in ('### Added', '### Improved', '### Fixed', '### Changed', '### Deprecated', '### Removed', '### Security', '### Compatibility', '### Testing'):
            self.assertIn(heading, text)
        self.assertIn('NOT_MEASURED', text)


if __name__ == '__main__':
    unittest.main()

class ReleaseAuditTruthTests(unittest.TestCase):
    def test_release_audit_describes_v1_failure_and_v11_proof_layers(self):
        text = (ROOT / "docs/RELEASE_AUDIT.md").read_text(encoding="utf-8")
        self.assertIn("v1.1", text)
        self.assertIn("assets/icon.svg", text)
        self.assertIn("BASELINE_BLOCKED", text)
        self.assertIn("LIVE_TESTED", text)
        self.assertIn("BEHAVIORAL", text)
        self.assertNotIn("Serena-first repository-intelligence", text)
        self.assertNotIn("Canonical package validation | PASS — 73 core modules", text)

    def test_package_validator_requires_new_runtime_truth_sources(self):
        text = (ROOT / "scripts/validate_package.py").read_text(encoding="utf-8")
        for required in [
            "docs/PLATFORM_AUDIT.md",
            "docs/ACTIVATION_MATRIX.md",
            "docs/RUNTIME_AND_GUARANTEE_LEVELS.md",
            "docs/VNEXT_MIGRATION.md",
            "docs/SECURITY_THREAT_MODEL.md",
            "docs/EVALUATION_STRATEGY.md",
            "runtime/versioning.py",
            "evals/benchmark-partitions.json",
        ]:
            self.assertIn(f'"{required}"', text)
