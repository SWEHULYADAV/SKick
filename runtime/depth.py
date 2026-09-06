from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path

from .model import DepthDecision

DEPTHS = ("quick", "standard", "deep", "exhaustive")
MODES = ("research", "build", "debug", "review", "security", "design", "install", "maintain")


@lru_cache(maxsize=1)
def _model() -> dict:
    path = Path(__file__).with_name("depth_model.json")
    return json.loads(path.read_text(encoding="utf-8"))


def _explicit_depth_from_text(text: str) -> str | None:
    lower = text.lower()
    for depth in DEPTHS:
        if re.search(rf"\b{depth}\s+(?:mode|depth)\b|\bin\s+{depth}\s+(?:mode|depth)\b", lower):
            return depth
    return None


def _mode(text: str) -> str:
    lower = text.lower()
    if re.search(r"\b(?:vulnerab\w*|security|exploit\w*|threat|purple[- ]team|hardening)\b", lower):
        return "security"
    if re.search(r"\b(debug|failing|failure|regression|intermittent|root cause|bug)\b", lower):
        return "debug"
    if re.search(r"\b(install|setup|set up|doctor)\b", lower):
        return "install"
    if re.search(r"\b(maintain|release|port|upgrade skick|update skick)\b", lower):
        return "maintain"
    if re.search(r"\b(review|audit)\b", lower):
        return "review"
    if re.search(r"\b(design|ux|ui|architecture)\b", lower):
        return "design"
    if re.search(r"\b(fix|implement|build|patch|refactor|migrate|change|edit|typo)\b", lower):
        return "build"
    return "research"


def _explicit_skick(text: str) -> bool:
    return bool(re.search(r"(?:@skick\b|/skick\b|\buse\s+skick\b|\bskick\s+in\s+(?:quick|standard|deep|exhaustive)\b)", text, re.I))


def classify_task(task: str, *, explicit_depth: str | None = None) -> DepthDecision:
    if not isinstance(task, str) or not task.strip():
        raise ValueError("task must be a non-empty string")
    model = _model()
    lower = task.lower()
    reasons: list[str] = []
    score = 0

    explicit_from_text = _explicit_depth_from_text(task)
    chosen_explicit = explicit_depth or explicit_from_text
    if chosen_explicit is not None and chosen_explicit not in DEPTHS:
        raise ValueError(f"invalid explicit depth: {chosen_explicit}")

    trivial = any(re.search(pattern, lower, re.I) for pattern in model.get("trivial_patterns", []))
    for feature in model.get("features", []):
        if any(re.search(pattern, lower, re.I) for pattern in feature.get("patterns", [])):
            weight = int(feature.get("weight", 0))
            score += weight
            reasons.append(f"{feature['id']} (+{weight})")

    explicit_invocation = _explicit_skick(task)
    if explicit_invocation:
        reasons.append("explicit SKick invocation")

    if chosen_explicit:
        depth = chosen_explicit
        reasons.append(f"explicit depth override: {chosen_explicit}")
    elif trivial:
        depth = "quick"
        reasons.append("trivial/single-step pattern keeps minimum sufficient process")
    else:
        thresholds = model["thresholds"]
        if score >= int(thresholds["exhaustive"]):
            depth = "exhaustive"
        elif score >= int(thresholds["deep"]):
            depth = "deep"
        elif score >= int(thresholds["standard"]):
            depth = "standard"
        else:
            depth = "quick"

    # Automatic activation is conservative. Explicit depth is itself a caller signal
    # that the runtime is intentionally being used.
    activate = bool(explicit_invocation or explicit_depth is not None or (not trivial and score >= int(model["thresholds"]["standard"])))
    return DepthDecision(
        activate=activate,
        mode=_mode(task),
        depth=depth,
        score=score,
        reasons=reasons or ["no complexity/risk feature matched"],
        explicit_depth=chosen_explicit,
    )
