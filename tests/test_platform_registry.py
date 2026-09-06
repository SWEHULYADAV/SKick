import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'INSTALLATION_MANIFEST.json'

VERIFICATION_STATUSES = {
    'LIVE_TESTED', 'DOC_VERIFIED', 'COMMUNITY_VERIFIED', 'HOST_DEPENDENT',
    'GENERIC_PROMPT_FALLBACK', 'BROKEN_UNSUPPORTED', 'UNKNOWN'
}
NATIVE_SKILL = {'yes', 'no', 'unknown', 'host_dependent'}
ACTIVATION_STATE = {'supported', 'unsupported', 'unknown', 'host_dependent'}
RUNTIME_TIERS = {'full_runtime', 'partial_runtime', 'declarative', 'prompt_fallback', 'unknown'}


class PlatformRegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(MANIFEST.read_text(encoding='utf-8'))
        cls.platforms = cls.data['platforms']

    def test_every_route_has_normalized_truth_fields(self):
        required = {
            'entity_type', 'native_skill_support', 'activation', 'runtime_tier',
            'capabilities', 'verification_status', 'last_verified',
            'official_evidence', 'live_test', 'limitations'
        }
        for pid, entry in self.platforms.items():
            with self.subTest(pid=pid):
                self.assertFalse(required - set(entry), f"missing {sorted(required - set(entry))}")
                self.assertIn(entry['native_skill_support'], NATIVE_SKILL)
                self.assertIn(entry['verification_status'], VERIFICATION_STATUSES)
                self.assertIn(entry['runtime_tier'], RUNTIME_TIERS)
                self.assertRegex(entry['last_verified'], r'^\d{4}-\d{2}-\d{2}$')
                self.assertIsInstance(entry['capabilities'], list)
                self.assertIsInstance(entry['official_evidence'], list)
                activation = entry['activation']
                self.assertIn(activation['explicit'], ACTIVATION_STATE)
                self.assertIn(activation['automatic'], ACTIVATION_STATE)
                self.assertIn(activation['literal_at_skick'], {'yes', 'no', 'unknown'})
                self.assertIsInstance(activation['native_equivalent'], str)

    def test_live_tested_requires_reproducible_live_metadata(self):
        for pid, entry in self.platforms.items():
            with self.subTest(pid=pid):
                if entry.get('verification_status') != 'LIVE_TESTED':
                    continue
                live = entry.get('live_test')
                self.assertIsInstance(live, dict)
                for key in ('skick_version', 'host_version', 'tested_on', 'activation', 'result'):
                    self.assertTrue(live.get(key), f'{pid}: live_test.{key} required')
                self.assertEqual(live['result'], 'passed')

    def test_model_providers_are_not_misrepresented_as_skill_hosts(self):
        for pid, entry in self.platforms.items():
            if entry.get('kind') != 'model_provider_only':
                continue
            with self.subTest(pid=pid):
                self.assertEqual(entry['entity_type'], 'model_provider')
                self.assertIn(entry['verification_status'], {'HOST_DEPENDENT', 'GENERIC_PROMPT_FALLBACK', 'UNKNOWN'})
                self.assertIn(entry['native_skill_support'], {'no', 'host_dependent', 'unknown'})
                self.assertNotEqual(entry['activation']['literal_at_skick'], 'yes')

    def test_doc_verified_requires_current_official_evidence(self):
        for pid, entry in self.platforms.items():
            if entry.get('verification_status') != 'DOC_VERIFIED':
                continue
            with self.subTest(pid=pid):
                evidence = entry.get('official_evidence', [])
                self.assertTrue(evidence, f'{pid}: DOC_VERIFIED requires evidence')
                self.assertTrue(any(e.get('source_type') in {'first_party_docs', 'first_party_release_notes', 'official_repository', 'official_support'} and e.get('checked_on') == entry['last_verified'] for e in evidence))

    def test_registry_has_no_minimum_route_count_quality_invariant(self):
        audit = (ROOT / 'scripts' / 'audit_release.py').read_text(encoding='utf-8')
        self.assertNotIn('len(platforms) < 40', audit)
        self.assertNotIn('required platform routes missing', audit)


if __name__ == '__main__':
    unittest.main()

class PlatformGenerationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.platforms = json.loads(MANIFEST.read_text(encoding='utf-8'))['platforms']

    def test_installation_manifest_schema_declares_normalized_fields(self):
        schema_path = ROOT / 'schemas' / 'installation-manifest.schema.json'
        self.assertTrue(schema_path.is_file())
        schema = json.loads(schema_path.read_text(encoding='utf-8'))
        platform_schema = schema['properties']['platforms']['additionalProperties']
        required = set(platform_schema['required'])
        for key in ('entity_type', 'native_skill_support', 'activation', 'runtime_tier', 'verification_status', 'last_verified', 'official_evidence', 'live_test'):
            self.assertIn(key, required)

    def test_generated_platform_reports_cover_every_route(self):
        for rel in ('docs/PLATFORM_CATALOG.md', 'docs/PLATFORM_AUDIT.md', 'docs/ACTIVATION_MATRIX.md'):
            text = (ROOT / rel).read_text(encoding='utf-8')
            for pid in self.platforms:
                self.assertIn(f'`{pid}`', text, f'{rel} missing {pid}')

    def test_platform_generator_check_mode(self):
        import subprocess, sys
        result = subprocess.run([sys.executable, str(ROOT / 'scripts' / 'generate_platform_catalog.py'), '--check'], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

class FreshnessAuditTests(unittest.TestCase):
    def test_structured_platform_dates_are_checked_without_network(self):
        import subprocess, sys
        result = subprocess.run([
            sys.executable, str(ROOT / 'scripts' / 'audit_freshness.py'), str(ROOT),
            '--as-of', '2026-09-05', '--max-age-days', '20', '--fail-stale'
        ], text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('Platform routes older than 20 days: 0', result.stdout)

    def test_stale_platform_evidence_can_fail_ci(self):
        import subprocess, sys, tempfile
        with tempfile.TemporaryDirectory() as td:
            temp = Path(td)
            (temp / 'INSTALLATION_MANIFEST.json').write_text(json.dumps({
                'platforms': {'x': {'last_verified': '2026-01-01', 'official_evidence': []}}
            }), encoding='utf-8')
            result = subprocess.run([
                sys.executable, str(ROOT / 'scripts' / 'audit_freshness.py'), str(temp),
                '--as-of', '2026-09-05', '--max-age-days', '30', '--fail-stale'
            ], text=True, capture_output=True)
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertIn('STALE_ROUTE x', result.stdout)

class AdapterBlockTests(unittest.TestCase):
    def test_generated_adapter_blocks_surface_proof_and_activation(self):
        for rel in ('adapters/chatgpt/README.md', 'adapters/codex/README.md', 'adapters/model-provider/README.md'):
            text = (ROOT / rel).read_text(encoding='utf-8')
            self.assertIn('Verification status:', text, rel)
            self.assertIn('Runtime tier:', text, rel)
            self.assertIn('Literal `@SKick`:', text, rel)

class PlatformAuditShapeTests(unittest.TestCase):
    def test_generated_audit_contains_requested_truth_columns(self):
        text = (ROOT / 'docs' / 'PLATFORM_AUDIT.md').read_text(encoding='utf-8')
        self.assertIn('Required plan/tier if known', text)
        self.assertIn('Notes', text)

class CommunityEvidenceTruthTests(unittest.TestCase):
    def test_community_routes_do_not_fill_official_evidence_column_from_legacy_source(self):
        data = json.loads((ROOT / 'INSTALLATION_MANIFEST.json').read_text(encoding='utf-8'))
        for pid in ('aider-desk', 'continue', 'neovate'):
            route = data['platforms'][pid]
            self.assertEqual(route['verification_status'], 'COMMUNITY_VERIFIED')
            self.assertEqual(route.get('official_evidence'), [])
            self.assertIn('vercel-labs/skills', route.get('source', ''))
        audit = (ROOT / 'docs/PLATFORM_AUDIT.md').read_text(encoding='utf-8')
        for pid in ('aider-desk', 'continue', 'neovate'):
            line = next(line for line in audit.splitlines() if line.startswith(f'| `{pid}` |'))
            self.assertNotIn('auth0.github.io', line)
