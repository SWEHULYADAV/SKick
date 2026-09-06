import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / 'scripts' / 'install_skick.py'


class MigrationInstallTests(unittest.TestCase):
    def _old_install(self, root: Path) -> Path:
        dest = root / 'installed' / 'skick'
        dest.mkdir(parents=True)
        (dest / 'VERSION').write_text('1.0\n', encoding='utf-8')
        (dest / 'SKILL.md').write_text('local v1 skill\n', encoding='utf-8')
        (dest / 'LOCAL_CUSTOMIZATION.md').write_text('keep me\n', encoding='utf-8')
        return dest

    def test_existing_v1_install_is_not_overwritten_without_force(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            dest = self._old_install(root)
            project = root / 'project'; project.mkdir()
            proc = subprocess.run([
                sys.executable, str(INSTALLER), '--source', str(ROOT), '--target', 'agents',
                '--scope', 'project', '--project', str(project), '--destination', str(dest), '--json'
            ], text=True, capture_output=True)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn('Destination already exists', proc.stderr)
            self.assertEqual((dest / 'LOCAL_CUSTOMIZATION.md').read_text(encoding='utf-8'), 'keep me\n')

    def test_explicit_force_replacement_creates_backup_with_customization(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            dest = self._old_install(root)
            project = root / 'project'; project.mkdir()
            proc = subprocess.run([
                sys.executable, str(INSTALLER), '--source', str(ROOT), '--target', 'agents',
                '--scope', 'project', '--project', str(project), '--destination', str(dest), '--force', '--json'
            ], text=True, capture_output=True)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            data = json.loads(proc.stdout)
            self.assertEqual(data['install_state'], 'installed')
            backups = list(dest.parent.glob('skick.backup-*'))
            self.assertEqual(len(backups), 1)
            self.assertEqual((backups[0] / 'LOCAL_CUSTOMIZATION.md').read_text(encoding='utf-8'), 'keep me\n')
            self.assertTrue((dest / 'SKILL.md').is_file())
            self.assertEqual(data['discovered'], 'unknown')
            self.assertEqual(data['live_tested'], 'unknown')


if __name__ == '__main__':
    unittest.main()
