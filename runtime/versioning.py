from __future__ import annotations

import re
from pathlib import Path

_VERSION_RE = re.compile(r'^\d+(?:\.\d+){1,2}(?:[-+][0-9A-Za-z.-]+)?$')


def read_package_version(root: Path) -> str:
    path = root / 'VERSION'
    if not path.is_file():
        raise ValueError(f'VERSION missing: {path}')
    value = path.read_text(encoding='utf-8').strip()
    if not _VERSION_RE.fullmatch(value):
        raise ValueError(f'invalid SKick VERSION: {value!r}')
    return value


def normalize_semver(value: str) -> str:
    core, *suffix = re.split(r'(?=[-+])', value, maxsplit=1)
    parts = core.split('.')
    if len(parts) == 2:
        core = core + '.0'
    elif len(parts) != 3:
        raise ValueError(f'cannot normalize semantic version: {value!r}')
    return core + (suffix[0] if suffix else '')
