import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class DeclarativePolicyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')

    def test_capability_fit_not_vendor_brand_is_root_rule(self):
        lower = self.skill.lower()
        self.assertIn('capability fit', lower)
        self.assertNotIn('prefer serena automatically', lower)
        self.assertNotIn('check serena first', lower)

    def test_existing_project_architecture_outranks_starter_profiles(self):
        lower = self.skill.lower()
        self.assertIn('existing project architecture', lower)
        self.assertIn('starter profile', lower)
        self.assertNotIn('for the preferred python web profile', lower)
        self.assertNotIn('prefer the host-neutral `python backend + semantic html + css + vanilla javascript` profile', lower)

    def test_executable_runtime_is_optional_not_mandatory(self):
        lower = self.skill.lower()
        self.assertIn('optional executable runtime', lower)
        self.assertIn('declarative fallback', lower)
        self.assertIn('runtime/', self.skill)
        self.assertIn('scripts/skick_runtime.py', self.skill)

    def test_root_skill_remains_compact(self):
        self.assertLess(len(self.skill.splitlines()), 500)

    def test_declarative_references_exist_without_executing_runtime(self):
        links = re.findall(r'\]\(([^)#]+\.md)(?:#[^)]+)?\)', self.skill)
        self.assertGreater(len(links), 10)
        for rel in links:
            self.assertTrue((ROOT / rel).is_file(), rel)
        self.assertNotIn('MUST run `scripts/skick_runtime.py`', self.skill)

    def test_vendor_and_starter_modules_are_policy_scoped(self):
        serena = (ROOT / 'core/serena-integration.md').read_text(encoding='utf-8').lower()
        web = (ROOT / 'core/python-vanilla-web-stack.md').read_text(encoding='utf-8').lower()
        self.assertIn('capability', serena)
        self.assertIn('not a constitutional preference', serena)
        self.assertIn('optional starter profile', web)
        self.assertNotIn('cross-platform agent rule', web)

    def test_core_policy_has_no_serena_first_vendor_privilege(self):
        offenders = []
        for path in (ROOT / 'core').glob('*.md'):
            text = path.read_text(encoding='utf-8').lower()
            if 'serena-first' in text or 'prefer serena' in text or 'check serena availability first' in text:
                offenders.append(path.relative_to(ROOT).as_posix())
        self.assertEqual(offenders, [])

    def test_bootstrap_does_not_grant_special_serena_install_authority(self):
        paths = [ROOT / 'BOOTSTRAP_PROMPTS.md', ROOT / 'START_HERE.md', ROOT / 'docs' / 'GITHUB_BOOTSTRAP.md', ROOT / 'docs' / 'INSTALLATION.md', ROOT / 'docs' / 'RUNTIME_COMPATIBILITY.md']
        offenders = []
        for path in paths:
            text = path.read_text(encoding='utf-8').lower()
            if 'serena-first' in text or 'authorizes canonical serena' in text or 'configure canonical serena' in text or 'check serena first' in text:
                offenders.append(path.relative_to(ROOT).as_posix())
        self.assertEqual(offenders, [])

    def test_engineering_lifecycle_does_not_force_python_starter_profile(self):
        text = (ROOT / 'core' / 'engineering-lifecycle.md').read_text(encoding='utf-8').lower()
        self.assertNotIn('for ordinary new web products without a stronger constraint', text)
        self.assertIn('existing project', text)


if __name__ == '__main__':
    unittest.main()

class ThinAdapterPolicyTests(unittest.TestCase):
    def test_adapters_do_not_duplicate_global_vendor_or_stack_policy(self):
        offenders = []
        for path in (ROOT / 'adapters').rglob('README.md'):
            text = path.read_text(encoding='utf-8').lower()
            if 'prefer serena automatically' in text or 'v1.0 preferred web profile' in text:
                offenders.append(path.relative_to(ROOT).as_posix())
        self.assertEqual(offenders, [])

class ActivePolicyResidueTests(unittest.TestCase):
    def test_handoff_and_user_docs_do_not_reintroduce_vendor_or_stack_defaults(self):
        files = [
            ROOT / 'AI_HANDOFF.md',
            ROOT / 'docs/USAGE_PLAYBOOK.md',
            ROOT / 'docs/TROUBLESHOOTING.md',
        ]
        forbidden = [
            'repository engineering is serena-first',
            'default to a minimal `app.py`',
            'only placement is invariant',
        ]
        for path in files:
            text = path.read_text(encoding='utf-8').lower()
            for needle in forbidden:
                self.assertNotIn(needle, text, f'{path}: {needle}')

class EvaluationPolicyResidueTests(unittest.TestCase):
    def test_behavioral_evals_do_not_reward_global_serena_preference(self):
        text = (ROOT / 'evals/evals.json').read_text(encoding='utf-8').lower()
        for needle in [
            'serena first',
            'prefer serena',
            'check and use serena before broad file reads',
            'serena-first-architecture-gate',
        ]:
            self.assertNotIn(needle, text)
