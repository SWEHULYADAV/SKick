from __future__ import annotations

import re
from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any


class TeamRole(str, Enum):
    RED = "red"
    BLUE = "blue"
    PURPLE = "purple"
    BLACK = "black_blind"


@dataclass(slots=True)
class TeamingPlan:
    roles: list[TeamRole]
    security_scope: dict[str, str]
    challenge_questions: list[str] = field(default_factory=list)
    validation_loop: list[str] = field(default_factory=list)
    disagreement_policy: str = "Preserve disagreement and identify the next discriminating evidence/experiment rather than forcing consensus."
    attack_surface: list[str] = field(default_factory=list)
    offensive_to_defensive: dict[str, str] = field(default_factory=dict)
    independence_contract: str = "Black/blind review receives the problem and necessary evidence but does not inherit the primary conclusion as a premise."

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["roles"] = [role.value for role in self.roles]
        return data


def _security_scope(text: str) -> dict[str, str]:
    lower = text.lower()
    user_owned = bool(re.search(r"\b(?:my|our|owned|i own|we own)\b", lower) and re.search(r"\b(?:local|lab|docker|ctf|sandbox|test app|test environment)\b", lower))
    local_lab = bool(re.search(r"\b(?:local|docker|lab|ctf|sandbox|test app)\b", lower))
    if user_owned:
        authorization = "user_owned_lab"
        safe_boundary = "authorized_local_scope"
    else:
        authorization = "unknown"
        safe_boundary = "lab_or_simulation_only"
    return {
        "target": "user_supplied_target" if re.search(r"\b(?:app|system|auth|target|service|repo)\b", lower) else "unspecified",
        "authorization_context": authorization,
        "environment": "local_lab" if local_lab else "unknown",
        "goal": "defensive_validation" if re.search(r"\b(?:patch|mitigat|fix|defen|hardening|retest|security review)\b", lower) else "analysis",
        "safe_test_boundary": safe_boundary,
    }


def build_teaming_plan(text: str) -> TeamingPlan:
    if not isinstance(text, str) or not text.strip():
        raise ValueError("task must be a non-empty string")
    lower = text.lower()
    explicit_security = bool(re.search(r"\b(?:security|vulnerab\w*|exploit\w*|attack\w*|bypass\w*|threat\w*|abuse\w*|red team|blue team|purple team)\b", lower))
    auth_security_context = bool(re.search(r"\bauth(?:entication|orization)?\b", lower) and re.search(r"\b(?:security|vulnerab\w*|exploit\w*|bypass\w*|abuse\w*|hardening|threat\w*)\b", lower))
    security = explicit_security or auth_security_context
    remediation = bool(re.search(r"\b(?:patch|fix|mitigat\w*|remediat\w*|hardening|retest|regression)\b", lower))
    architecture = bool(re.search(r"\b(?:architecture|migration|design|proposal)\b", lower))
    high_impact = bool(re.search(r"\b(?:high[- ]impact|production|deep|critical|independent review|hidden assumptions)\b", lower))
    explicit_black = bool(re.search(r"\b(?:black(?:/blind)? review|blind review|independent review|challenge hidden assumptions)\b", lower))
    multi_perspective = bool(re.search(r"\b(?:multi[- ]perspective|adversarial review|challenge (?:the )?proposal|synthesize the strongest)\b", lower))

    roles: list[TeamRole] = []
    if security:
        roles.extend([TeamRole.RED, TeamRole.BLUE])
        if remediation or re.search(r"\bpurple\b", lower):
            roles.append(TeamRole.PURPLE)
        if (architecture and high_impact) or explicit_black:
            roles.append(TeamRole.BLACK)
    elif architecture and multi_perspective:
        roles.extend([TeamRole.RED, TeamRole.BLUE, TeamRole.PURPLE, TeamRole.BLACK])
    elif architecture and (high_impact or explicit_black):
        roles.append(TeamRole.BLACK)

    # Stable unique order.
    roles = list(dict.fromkeys(roles))
    scope = _security_scope(text) if security else {
        "target": "not_security_scoped",
        "authorization_context": "not_applicable",
        "environment": "not_applicable",
        "goal": "independent_challenge" if TeamRole.BLACK in roles else "none",
        "safe_test_boundary": "not_applicable",
    }
    challenge = []
    if roles:
        challenge = [
            "What assumption would make the leading conclusion wrong?",
            "What evidence is independent of the primary investigation path?",
            "What safe discriminating experiment would resolve the most important disagreement?",
        ]
    attack_surface: list[str] = []
    if security:
        if re.search(r"\bapi\b", lower):
            attack_surface.append("api")
        if re.search(r"\b(?:browser|web)\b", lower):
            attack_surface.append("browser")
        if re.search(r"\b(?:upload|file)\b", lower):
            attack_surface.append("uploaded_file")
        if re.search(r"\bwebhook\b", lower):
            attack_surface.append("webhook")
        if re.search(r"\b(?:dependency|package|plugin)\b", lower):
            attack_surface.append("dependency_supply_chain")
        if re.search(r"\b(?:mcp|agent tool|prompt|context)\b", lower):
            attack_surface.append("agent_tool_context")
        if re.search(r"\b(?:ci|build|installer)\b", lower):
            attack_surface.append("build_ci_installer")
        if re.search(r"\b(?:secret|credential|token)\b", lower):
            attack_surface.append("secrets")
        if re.search(r"\b(?:auth|identity|permission|privilege)\b", lower):
            attack_surface.append("identity_authorization")
        if not attack_surface:
            attack_surface.append("trust_boundary_unspecified")
    offensive_to_defensive = {}
    if security:
        offensive_to_defensive = {
            "attack_prerequisite": "Record the prerequisite/reachability condition demonstrated or hypothesized by Red evidence.",
            "preventive_control": "Identify the smallest control that removes or constrains that prerequisite/root cause.",
            "detective_control": "Identify observable telemetry or a detection opportunity for attempted boundary violation.",
            "response": "Define containment/recovery action proportionate to the demonstrated impact.",
            "validation": "Retest the same safe stimulus plus legitimate functionality; do not claim mitigation from inspection alone.",
        }
    validation_loop: list[str] = []
    if TeamRole.PURPLE in roles and security:
        validation_loop = [
            "red_hypothesis",
            "authorized_or_safe_test",
            "observation",
            "blue_control",
            "detection_or_mitigation",
            "red_retest",
            "residual_risk",
        ]
    elif TeamRole.PURPLE in roles:
        validation_loop = [
            "proposal",
            "red_challenge",
            "blue_hardening",
            "black_blind_review",
            "purple_synthesis",
        ]
    return TeamingPlan(roles=roles, security_scope=scope, challenge_questions=challenge, validation_loop=validation_loop, attack_surface=attack_surface, offensive_to_defensive=offensive_to_defensive)
