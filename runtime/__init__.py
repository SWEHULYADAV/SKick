"""Optional executable runtime for SKick.

The runtime is intentionally dependency-free and optional. Declarative Skill hosts do
not need to import this package.
"""
from pathlib import Path

from .versioning import normalize_semver, read_package_version

__version__ = normalize_semver(read_package_version(Path(__file__).resolve().parents[1]))
