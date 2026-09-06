from __future__ import annotations

import re
from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any


class EnhancementMode(str, Enum):
    SILENT = "silent"
    VISIBLE = "visible"
    EXECUTION = "execution"
    STRICT_SPEC = "strict_spec"


@dataclass(slots=True)
class PromptInterpretation:
    original_request: str
    interpreted_goal: str
    enhancement_mode: EnhancementMode
    constraints: list[str] = field(default_factory=list)
    assumptions: list[str] = field(default_factory=list)
    unknowns: list[str] = field(default_factory=list)
    success_criteria: list[str] = field(default_factory=list)
    research_needs: list[str] = field(default_factory=list)
    verification_needs: list[str] = field(default_factory=list)
    domains: list[str] = field(default_factory=list)
    contradictions: list[str] = field(default_factory=list)
    outputs: list[str] = field(default_factory=list)
    evidence_requirements: list[str] = field(default_factory=list)
    non_goals: list[str] = field(default_factory=list)
    failure_conditions: list[str] = field(default_factory=list)
    quality: dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["enhancement_mode"] = self.enhancement_mode.value
        return data

    def render_spec(self) -> str:
        lines = [
            f"Original request: {self.original_request}",
            f"Interpreted goal: {self.interpreted_goal}",
            f"Enhancement mode: {self.enhancement_mode.value}",
        ]
        sections = [
            ("Constraints", self.constraints),
            ("Assumptions", self.assumptions),
            ("Unknowns", self.unknowns),
            ("Success criteria", self.success_criteria),
            ("Research needs", self.research_needs),
            ("Verification needs", self.verification_needs),
            ("Contradictions", self.contradictions),
            ("Outputs", self.outputs),
            ("Evidence requirements", self.evidence_requirements),
            ("Non-goals", self.non_goals),
            ("Failure conditions", self.failure_conditions),
        ]
        for title, items in sections:
            if items:
                lines.append(f"\n{title}:")
                lines.extend(f"- {item}" for item in items)
        return "\n".join(lines)


def _contains(text: str, pattern: str) -> bool:
    return bool(re.search(pattern, text, re.I))


def _extract_constraints(text: str) -> list[str]:
    """Extract explicit user constraints without inventing new requirements.

    Negative constraints are obvious, but positive imperatives such as "Use Python"
    and scope locks such as "Only modify this file" are equally binding. Keep the
    user's wording so downstream planning can preserve it verbatim.
    """
    constraints: list[str] = []
    clauses = re.split(r"(?<=[.!?])\s+|\s+but\s+|;", text, flags=re.I)
    patterns = (
        r"\b(?:do not|don't|must not|never|without changing|keep .* unchanged|preserve|no new|no additional)\b",
        r"^(?:use|using|must use|required to use)\b",
        r"^only\b",
        r"\b(?:only modify|only change|only edit|only touch|limit (?:changes|edits) to)\b",
        r"\b(?:must remain|must stay|must be|must use|must keep)\b",
    )
    for clause in clauses:
        cleaned = clause.strip(" .")
        if not cleaned:
            continue
        if any(_contains(cleaned, pattern) for pattern in patterns):
            constraints.append(cleaned)
    return list(dict.fromkeys(constraints))


def _detect_contradictions(text: str) -> list[str]:
    lower = text.lower()
    findings: list[str] = []
    if re.search(r"\b(?:exhaustive|exhaustively|deep(?:ly)?)\b", lower) and re.search(
        r"\b(?:almost no|very few|minimal|tiny|near[- ]zero)\s+(?:tokens?|context|tool calls?|search(?:es)?)\b",
        lower,
    ):
        findings.append("Exhaustive depth conflicts with the requested near-minimal token/resource budget; depth and budget must be prioritized explicitly.")
    if re.search(r"\b(?:complete(?:ly)?|full)\s+refactor\b", lower) and re.search(r"\bchange nothing\b", lower):
        findings.append("A complete refactor conflicts with the requirement to change nothing.")
    if re.search(r"\b(?:latest|current|today|up[- ]to[- ]date)\b", lower) and re.search(
        r"\b(?:no|without)\s+(?:web|external|outside)\s+(?:research|sources?|access)\b",
        lower,
    ):
        findings.append("Current-state verification conflicts with the prohibition on external/current evidence.")
    return findings


def analyze_prompt_quality(text: str) -> dict[str, str]:
    if not isinstance(text, str) or not text.strip():
        raise ValueError("prompt must be a non-empty string")
    words = re.findall(r"\b\w+\b", text)
    vague = bool(re.fullmatch(r"\s*(?:fix|check|research|compare|review|make|do)\s+(?:this|it)\s*[.!?]?\s*", text, re.I))
    intent = "low" if vague or len(words) <= 2 else ("medium" if len(words) < 7 else "high")
    has_success = _contains(text, r"\b(?:success|done when|acceptance|should pass|expected result|must produce)\b")
    has_verification = _contains(text, r"\b(?:test|verify|validate|reproduce|benchmark|prove|check)\b") and not vague
    has_constraints = bool(_extract_constraints(text)) or _contains(text, r"\b(?:must|only|under|within|using|without)\b")
    freshness = "required" if _contains(text, r"\b(?:latest|current|today|pricing|version|supported|compatib)\b") else "not_indicated"
    research = "required" if _contains(text, r"\b(?:research|latest|current|documentation|standard|vulnerab|compatib|pricing)\b") else "not_indicated"
    repository_need = _contains(text, r"\b(?:repo|repository|code|implementation|fix|debug|auth|oauth|test)\b")
    external_need = research == "required" or freshness == "required"
    if repository_need and external_need:
        tool_need = "repository_and_external_evidence"
    elif repository_need:
        tool_need = "repository_or_runtime"
    elif external_need:
        tool_need = "external_evidence"
    else:
        tool_need = "not_indicated"
    security = "present" if _contains(text, r"\b(?:auth|security|vulnerab|exploit|credential|secret|permission|privilege)\b") else "not_indicated"
    output_defined = _contains(text, r"\b(?:return|produce|output|report|table|json|patch|answer|summary|memo)\b")
    missing_context = "likely" if vague or (repository_need and not _contains(text, r"\b(?:local|dev|test|staging|production|version|branch|file)\b")) else "limited"
    assumption_risk = "high" if vague else ("medium" if research == "required" or security == "present" else "low")
    failure_signal = "present" if vague or freshness == "required" or security == "present" or bool(_detect_contradictions(text)) else "not_indicated"
    return {
        "intent_clarity": intent,
        "scope_clarity": "low" if vague else ("medium" if len(words) < 10 else "high"),
        "constraints": "present" if has_constraints else "missing",
        "missing_context": missing_context,
        "output_definition": "present" if output_defined else "missing",
        "success_criteria": "present" if has_success else "missing",
        "verification_requirements": "present" if has_verification else "missing",
        "freshness_requirements": freshness,
        "research_requirements": research,
        "tool_requirements": tool_need,
        "safety_security_implications": security,
        "hidden_assumption_risk": assumption_risk,
        "likely_failure_modes": failure_signal,
        "ambiguity": "high" if vague else ("medium" if intent == "medium" else "low"),
    }


def _domains(text: str) -> list[str]:
    domains: list[str] = []
    checks = [
        ("security", r"\b(?:auth|security|secure|harden|vulnerab|exploit|threat|permission|authorization|authentication)\b"),
        ("software_engineering", r"\b(?:auth|code|repo|repository|project|bug|broken|failure|fix|debug|test|api|library|framework|variable|oauth|callback|build|refactor)\b"),
        ("research", r"\b(?:research|investigate|compare|evidence|source|documentation|find everything|find all)\b"),
        ("product_platform", r"\b(?:platform|product|plan|tier|pricing|supported|compatib|skill|plugin|host)\b"),
        ("data", r"\b(?:dataset|sql|metric|analytics|data quality)\b"),
        ("academic", r"\b(?:paper|study|journal|conference|meta-analysis)\b"),
        ("legal", r"\b(?:law|legal|regulation|statute|court|patent)\b"),
    ]
    for name, pattern in checks:
        if _contains(text, pattern):
            domains.append(name)
    return domains or ["general"]


def _goal(text: str) -> str:
    lower = text.lower().strip()
    if _contains(lower, r"\bauth\b|\boauth\b|authentication") and _contains(lower, r"\bbroken\b|\bfail|\bwhy\b|\bcheck\b"):
        return "Identify the root cause of the authentication failure and determine the smallest safe corrective action without changing the user's stated objective."
    if re.fullmatch(r"make\s+secure[.!]?", lower):
        return "Assess the user-supplied target's security posture and identify the smallest evidence-backed hardening actions; keep the target and authorization context explicit when they are not yet known."
    if re.fullmatch(r"check\s+this\s+project[.!]?", lower):
        return "Inspect the provided project for material issues relevant to correctness, maintainability, security, and the stated goal without turning the request into an unrelated redesign."
    if re.fullmatch(r"why\s+broken[.!]?", lower):
        return "Identify the failure mechanism/root cause from the available context, keep competing explanations until evidence separates them, and avoid claiming a fix without validation."
    if re.fullmatch(r"find\s+everything\s+about\s+this[.!]?", lower):
        return "Research the supplied subject broadly enough to answer the user's real decision, prioritizing high-value evidence neighborhoods rather than treating 'everything' as unbounded scope."
    if re.fullmatch(r"fix\s+(?:this|it)[.!]?", lower):
        return "Identify what is wrong with the supplied target and apply the smallest justified correction while preserving any explicit constraints and avoiding unrelated changes."
    if re.fullmatch(r"make\s+better[.!]?", lower):
        return "Improve the supplied target against its apparent purpose and explicit constraints, using the minimum sufficient change rather than inventing a broader redesign."
    if re.fullmatch(r"compare\s+(?:these|this|them)[.!]?", lower):
        return "Compare the supplied items on decision-relevant criteria, keep missing comparison context explicit, and avoid inventing attributes that were not provided or researched."
    if _contains(lower, r"\brename\b"):
        return text.strip().rstrip(".")
    if lower.startswith("improve this prompt:"):
        payload = text.split(":", 1)[1].strip()
        return _goal(payload)
    if _contains(lower, r"\bresearch\b|\bfind everything\b"):
        return f"Research the requested subject and produce an evidence-backed answer while preserving the requested scope: {text.strip()}"
    return text.strip().rstrip(".")


def _success_criteria(text: str, domains: list[str]) -> list[str]:
    lower = text.lower()
    if _contains(lower, r"\brename\b"):
        return ["Apply the requested rename without unrelated changes."]
    criteria: list[str] = []
    if "security" in domains and re.fullmatch(r"\s*make\s+secure[.!]?\s*", lower):
        criteria.extend([
            "Identify the relevant security risk/control boundary without inventing an unspecified target or authorization context.",
            "Recommend proportionate defensive changes and state what evidence would be required to call them verified.",
        ])
    elif "software_engineering" in domains and _contains(lower, r"\bbroken\b|\bfail|\bbug\b|\bdebug\b|\bfix\b"):
        criteria.extend([
            "Identify the failure mechanism/root cause with repository or runtime evidence.",
            "Use the smallest change that satisfies the request and preserves explicit constraints.",
            "Verify the changed behavior with the strongest available relevant test or reproduction.",
        ])
    elif "software_engineering" in domains and _contains(lower, r"\bproject\b|\brepo(?:sitory)?\b"):
        criteria.extend([
            "Inspect the supplied project/repository and surface material findings supported by project evidence.",
            "Avoid unrelated refactoring or architecture changes unless a finding makes them necessary.",
        ])
    elif "research" in domains or "product_platform" in domains:
        criteria.extend([
            "Answer the decision-critical question with source-appropriate evidence.",
            "Keep unresolved uncertainty and source freshness visible.",
        ])
    else:
        criteria.append("Produce the requested result without unnecessary scope expansion.")
    return criteria[:5]


def _research_needs(text: str, domains: list[str]) -> list[str]:
    lower = text.lower()
    if _contains(lower, r"\brename\b|\btypo\b") and not _contains(lower, r"\bresearch\b|\blatest\b|\bcurrent\b"):
        return []
    needs: list[str] = []
    if _contains(lower, r"\b(?:research|find everything|latest|current|today|supported|compatib|pricing|version|vulnerab|documentation|standard)\b"):
        needs.append("Determine whether current/external evidence is required and route to the appropriate source class.")
    if "software_engineering" in domains and _contains(lower, r"\bauth\b|\boauth\b|\bfail|\bbug\b"):
        needs.append("Inspect project-local implementation, configuration, tests, and recent relevant changes before externalizing the hypothesis.")
    return needs


def _verification_needs(text: str, domains: list[str]) -> list[str]:
    lower = text.lower()
    needs: list[str] = []
    if "software_engineering" in domains and _contains(lower, r"\b(?:broken|fail|bug|fix|patch|debug|auth|oauth)\b"):
        needs.extend([
            "Reproduce or otherwise establish the observed failure when feasible.",
            "Run focused regression tests or an equivalent discriminating validation after any change.",
        ])
    if _contains(lower, r"\b(?:latest|current|supported|compatib|pricing|version)\b"):
        needs.append("Use sufficiently fresh evidence and do not promote documentation proof to live verification.")
    if "security" in domains and _contains(lower, r"\b(?:secure|security|harden|fix|mitigat)\b"):
        needs.append("Do not call the target secure from inspection alone; validate the relevant control in an authorized or safe environment when feasible.")
    return needs


def _unknowns(text: str, domains: list[str]) -> list[str]:
    lower = text.lower()
    unknowns: list[str] = []
    if "software_engineering" in domains and _contains(lower, r"\b(?:broken|fail|bug|auth|oauth)\b"):
        if not _contains(lower, r"\b(?:production|staging|local|test|dev)\b"):
            unknowns.append("Runtime/environment in which the failure occurs.")
        unknowns.append("Exact failing flow, reproduction conditions, and most recent relevant change.")
    if _contains(lower, r"\b(?:platform|product|supported|compatib)\b"):
        unknowns.append("Exact host/product version and distinction between documented, installed, invoked, and live-tested support.")
    if "security" in domains and re.fullmatch(r"\s*make\s+secure[.!]?\s*", lower):
        unknowns.extend(["Target/system to secure.", "Authorization context and safe validation environment."])
    return list(dict.fromkeys(unknowns))


def interpret_task(text: str, *, mode: str | EnhancementMode = EnhancementMode.SILENT) -> PromptInterpretation:
    if not isinstance(text, str) or not text.strip():
        raise ValueError("task must be a non-empty string")
    try:
        enhancement_mode = mode if isinstance(mode, EnhancementMode) else EnhancementMode(mode)
    except ValueError as exc:
        raise ValueError(f"unsupported enhancement mode: {mode}") from exc

    domains = _domains(text)
    constraints = _extract_constraints(text)
    contradictions = _detect_contradictions(text)
    assumptions: list[str] = []
    if "software_engineering" in domains and not constraints:
        assumptions.append("Preserve the existing project architecture unless evidence or the user requires otherwise.")

    verification_needs = _verification_needs(text, domains)
    outputs: list[str] = []
    evidence_requirements: list[str] = []
    non_goals: list[str] = []
    failure_conditions: list[str] = []
    if re.search(r"\bfind everything\b", text, re.I):
        non_goals.append("Do not treat 'everything' as infinite scope; prioritize decision-relevant evidence and report valuable out-of-scope branches separately.")
    if enhancement_mode is EnhancementMode.STRICT_SPEC:
        outputs = ["Produce the requested deliverable and a concise verification/result-status report."]
        evidence_requirements = list(verification_needs) or ["Attach evidence appropriate to any completion or factual claim that materially affects the result."]
        non_goals = ["Do not broaden the task into unrelated refactoring, research, or technology changes."]
        failure_conditions = [
            "An explicit user constraint would be violated.",
            "A required verification step cannot be performed but the result would otherwise be reported as verified.",
        ]
        if contradictions:
            failure_conditions.append("A material contradiction remains unresolved and changes the feasible outcome.")

    return PromptInterpretation(
        original_request=text,
        interpreted_goal=_goal(text),
        enhancement_mode=enhancement_mode,
        constraints=constraints,
        assumptions=assumptions,
        unknowns=_unknowns(text, domains),
        success_criteria=_success_criteria(text, domains),
        research_needs=_research_needs(text, domains),
        verification_needs=verification_needs,
        domains=domains,
        contradictions=contradictions,
        outputs=outputs,
        evidence_requirements=evidence_requirements,
        non_goals=non_goals,
        failure_conditions=failure_conditions,
        quality=analyze_prompt_quality(text),
    )
