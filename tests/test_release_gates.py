import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ProvenanceCompletenessTests(unittest.TestCase):
    def test_unlisted_canonical_file_fails_provenance(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / 'tracked.txt').write_text('ok', encoding='utf-8')
            import hashlib
            content = b'ok'
            (root / 'ARTIFACT_MANIFEST.json').write_text(json.dumps({
                'artifacts': [{'path': 'tracked.txt', 'sha256': hashlib.sha256(content).hexdigest(), 'size': len(content)}]
            }), encoding='utf-8')
            (root / 'SHA256SUMS.txt').write_text('', encoding='utf-8')
            (root / 'surprise.txt').write_text('not covered', encoding='utf-8')
            result = subprocess.run([sys.executable, str(ROOT / 'scripts' / 'verify_provenance.py'), str(root)], text=True, capture_output=True)
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertIn('unlisted canonical file: surprise.txt', result.stdout)

    def test_generated_platform_docs_check_is_side_effect_free(self):
        before = (ROOT / 'docs' / 'PLATFORM_CATALOG.md').read_bytes()
        result = subprocess.run([sys.executable, str(ROOT / 'scripts' / 'generate_platform_catalog.py'), '--check'], cwd=ROOT, text=True, capture_output=True)
        after = (ROOT / 'docs' / 'PLATFORM_CATALOG.md').read_bytes()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(before, after)


class ReleasePolicyTests(unittest.TestCase):
    def test_ci_has_named_proof_layers(self):
        text = (ROOT / '.github' / 'workflows' / 'validate.yml').read_text(encoding='utf-8')
        for job in ('static:', 'unit:', 'integration:'):
            self.assertIn(job, text)
        self.assertIn('run_local_evals.py', text)
        self.assertIn('generate_platform_catalog.py --check', text)

    def test_validator_does_not_constitutionalize_vendor_or_starter_stack(self):
        text = (ROOT / 'scripts' / 'validate_package.py').read_text(encoding='utf-8')
        self.assertNotIn('must explicitly preserve automatic Serena preference', text)
        self.assertNotIn('Preferred web-stack profile must be first-class and cross-platform', text)
        self.assertNotIn('SKILL.md must directly reference the Python/vanilla web profile', text)


if __name__ == '__main__':
    unittest.main()

class ReleaseTruthOutputTests(unittest.TestCase):
    def test_release_audit_reports_compatibility_proof_counts(self):
        result = subprocess.run([sys.executable, str(ROOT / 'scripts' / 'audit_release.py')], cwd=ROOT, text=True, capture_output=True)
        # This test targets reporting shape; the current source may still have other
        # release blockers while the vNext branch is under construction.
        combined = result.stdout + result.stderr
        self.assertIn('compatibility_proof=', combined)
        self.assertIn('LIVE_TESTED=', combined)
        self.assertIn('DOC_VERIFIED=', combined)

    def test_ci_checks_module_catalog_generation(self):
        text = (ROOT / '.github' / 'workflows' / 'validate.yml').read_text(encoding='utf-8')
        self.assertIn('generate_module_catalog.py --check', text)

    def test_ci_checks_package_manifest_generation(self):
        text = (ROOT / '.github' / 'workflows' / 'validate.yml').read_text(encoding='utf-8')
        self.assertIn('generate_package_manifest.py --check', text)

    def test_package_manifest_generator_detects_current_staleness_or_sync(self):
        script = ROOT / 'scripts' / 'generate_package_manifest.py'
        self.assertTrue(script.is_file(), 'package manifest must have a deterministic generator')
        result = subprocess.run([sys.executable, str(script), '--check'], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_package_manifest_order_is_platform_independent(self):
        import runpy

        module = runpy.run_path(str(ROOT / 'scripts' / 'generate_package_manifest.py'))

        class FakeRel:
            def __init__(self, name):
                self.parts = (name,)
                self._name = name

            def as_posix(self):
                return self._name

        class WindowsOrderedPath:
            def __init__(self, name):
                self.name = name

            def __lt__(self, other):
                return self.name.lower() < other.name.lower()

            def is_file(self):
                return True

            def relative_to(self, root):
                return FakeRel(self.name)

        class FakeRoot:
            def rglob(self, pattern):
                return [WindowsOrderedPath('a.txt'), WindowsOrderedPath('Z.txt')]

        self.assertEqual(module['canonical_paths'](FakeRoot()), ['Z.txt', 'a.txt'])

class IntelligenceReleaseGateTests(unittest.TestCase):
    def test_ci_runs_prompt_research_teaming_and_research_ablation_evals(self):
        workflow = (ROOT / ".github" / "workflows" / "validate.yml").read_text(encoding="utf-8")
        for suite in (
            "prompt-intelligence-evals.json",
            "research-intelligence-evals.json",
            "teaming-evals.json",
            "research-ablation-evals.json",
        ):
            self.assertIn(suite, workflow)

    def test_ci_actions_are_pinned_to_immutable_commit_shas(self):
        workflow = (ROOT / ".github" / "workflows" / "validate.yml").read_text(encoding="utf-8")
        import re
        refs = re.findall(r"uses:\s+(actions/(?:checkout|setup-python))@([^\s#]+)", workflow)
        self.assertTrue(refs)
        for action, ref in refs:
            self.assertRegex(ref, r"^[0-9a-f]{40}$", f"{action} must be SHA-pinned")

    def test_ci_loads_controlled_security_behavioral_fixture_without_calling_it_passed(self):
        workflow = (ROOT / ".github" / "workflows" / "validate.yml").read_text(encoding="utf-8")
        self.assertIn("security-behavioral-fixture.json", workflow)
        self.assertIn("Legacy eval definition load checks", workflow)

    def test_package_validator_requires_intelligence_runtime_and_schemas(self):
        source = (ROOT / "scripts" / "validate_package.py").read_text(encoding="utf-8")
        for required in (
            "runtime/prompt_intelligence.py",
            "runtime/research.py",
            "runtime/research_ledger.py",
            "runtime/teaming.py",
            "runtime/orchestrator.py",
            "schemas/task-interpretation.schema.json",
            "schemas/research-plan.schema.json",
            "schemas/teaming-plan.schema.json",
            "schemas/research-finding.schema.json",
        ):
            self.assertIn(required, source)
