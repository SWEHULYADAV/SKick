from __future__ import annotations

import re
from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any


class ResearchLevel(str, Enum):
    NONE = "none"
    LIGHT = "light"
    STANDARD = "standard"
    DEEP = "deep"
    EXHAUSTIVE = "exhaustive"
    LATERAL = "lateral"
    ADVERSARIAL = "adversarial"


SOURCE_ROUTES: dict[str, list[str]] = {
    "product_platform": [
        "first_party_documentation", "official_support", "official_repository",
        "official_release_notes", "official_issue_tracker", "official_announcements",
        "credible_independent_evidence", "community_reports",
    ],
    "software_library": [
        "official_documentation", "source_repository", "source_code", "releases_tags",
        "changelog", "issues", "pull_requests", "maintainer_discussions", "package_registry",
        "technical_community",
    ],
    "technical_standard": [
        "standards_body", "normative_specification", "official_reference_implementation", "working_group_material",
    ],
    "academic": [
        "original_paper", "journal_or_conference", "author_publication", "replication_studies",
        "systematic_review", "datasets", "implementation_repository", "later_citations", "critiques",
    ],
    "security": [
        "vendor_security_advisory", "project_security_advisory", "cve_record", "known_exploitation_catalog",
        "cert_advisory", "patch_commit_or_source", "security_mailing_list", "reputable_security_research",
        "detection_guidance", "controlled_exploitability_evidence",
    ],
    "open_source_project": [
        "source_repository", "source_code", "issues", "discussions", "pull_requests", "commits",
        "blame_history", "releases", "maintainer_comments", "package_registry", "downstream_reports",
    ],
    "user_experience": ["issue_tracker", "support_forum", "stack_overflow", "reddit", "community_forum", "bug_reports", "reviews"],
    "general": ["primary_source", "authoritative_secondary_source", "high_quality_independent_source", "community_evidence"],
}


RESEARCH_BUDGETS: dict[ResearchLevel, dict[str, int]] = {
    ResearchLevel.NONE: {"max_queries": 0, "max_sources": 0, "max_source_classes": 0},
    ResearchLevel.LIGHT: {"max_queries": 2, "max_sources": 3, "max_source_classes": 2},
    ResearchLevel.STANDARD: {"max_queries": 5, "max_sources": 8, "max_source_classes": 4},
    ResearchLevel.DEEP: {"max_queries": 10, "max_sources": 18, "max_source_classes": 7},
    ResearchLevel.LATERAL: {"max_queries": 12, "max_sources": 22, "max_source_classes": 8},
    ResearchLevel.ADVERSARIAL: {"max_queries": 14, "max_sources": 24, "max_source_classes": 8},
    ResearchLevel.EXHAUSTIVE: {"max_queries": 20, "max_sources": 40, "max_source_classes": 10},
}


@dataclass(slots=True)
class ResearchPlan:
    level: ResearchLevel
    question_map: dict[str, Any]
    expected_source_types: list[str]
    strategies: list[str]
    query_classes: dict[str, str]
    freshness_required: bool
    coverage: dict[str, str]
    frontier: dict[str, list[str]]
    stopping_criteria: list[str]
    budget: dict[str, int]
    failure_taxonomy: list[str] = field(default_factory=list)
    next_best_evidence: str | None = None
    pivot_rules: list[str] = field(default_factory=list)
    terminology_expansion: list[str] = field(default_factory=list)
    information_gain_rule: str = ""
    output_mode: str = "answer"
    hypothesis_dimensions: list[str] = field(default_factory=list)
    graph: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["level"] = self.level.value
        return data


def route_source_classes(domain: str) -> list[str]:
    return list(SOURCE_ROUTES.get(domain, SOURCE_ROUTES["general"]))


def _research_level(text: str) -> ResearchLevel:
    lower = text.lower()
    if re.search(r"\b(?:2\s*\+\s*2|capital of france|rename variable|fix typo)\b", lower):
        return ResearchLevel.NONE
    if re.search(r"\bexhaustive(?:ly)?\b", lower):
        return ResearchLevel.EXHAUSTIVE
    if re.search(r"\b(?:red team|adversarial research|exploitability|threat intelligence)\b", lower):
        return ResearchLevel.ADVERSARIAL
    if re.search(r"\blateral research\b", lower):
        return ResearchLevel.LATERAL
    if re.search(r"\bdeep(?:ly)?\s+(?:research|investigat)|\bdeep dive\b", lower):
        return ResearchLevel.DEEP
    if re.search(r"\b(?:latest|current|supported|compatib|pricing|release|version|vulnerab|security advisory)\b", lower):
        return ResearchLevel.STANDARD
    if re.search(r"\b(?:research|look up|documentation|standard|specification|paper|study)\b", lower):
        return ResearchLevel.STANDARD
    if re.search(r"\b(?:why|how does|compare)\b", lower):
        return ResearchLevel.LIGHT
    return ResearchLevel.NONE


def _domain(text: str) -> str:
    lower = text.lower()
    if re.search(r"\b(?:vulnerab\w*|security|cve|exploit\w*|attack\w*|auth bypass)\b", lower):
        return "security"
    if re.search(r"\b(?:platform|product|supported|compatib|pricing|plan|tier|agent skills?|plugin|host)\b", lower):
        return "product_platform"
    if re.search(r"\b(?:library|framework|package|api|source code|repository|repo)\b", lower):
        return "software_library"
    if re.search(r"\b(?:rfc|standard|specification|ietf|w3c)\b", lower):
        return "technical_standard"
    if re.search(r"\b(?:paper|journal|conference|study|meta-analysis|dataset)\b", lower):
        return "academic"
    return "general"


def transform_queries(claim: str, *, entity: str | None = None, feature: str | None = None) -> dict[str, str]:
    subject = " ".join(part for part in [entity, feature] if part) or claim
    return {
        "direct": f"{subject} official documentation",
        "negative": f"{subject} unsupported limitation",
        "failure": f"{subject} not working regression issue",
        "historical": f"{subject} deprecated renamed historical",
        "implementation": f"{subject} source code implementation",
        "change": f"{subject} release notes changelog",
        "discussion": f"{subject} issue maintainer discussion",
    }


def _question_map(text: str, domain: str) -> dict[str, Any]:
    subquestions = ["What directly answers the user's question?", "Which claim(s) require external verification?"]
    decision: list[str] = []
    unknowns: list[str] = []
    disconfirm = ["What authoritative, implementation, historical, failure, or live-test evidence would make the leading conclusion wrong?"]
    if domain == "product_platform":
        subquestions.extend([
            "Does the product/host document the claimed capability?",
            "Is installation distinct from discovery, explicit invocation, automatic activation, and real task success?",
            "What version/plan/host limitations apply?",
        ])
        decision.extend([
            "Is the capability native to this host or only host-dependent?",
            "What proof level is justified: documentation, installation, invocation, or live task execution?",
        ])
        unknowns.extend(["Current product version", "Current plan/tier limitations", "Live-test availability"])
    elif domain == "security":
        subquestions.extend([
            "What versions/configurations are affected?",
            "Is the vulnerable path reachable under the target's actual configuration?",
            "What patch/control changes the mechanism?",
        ])
        decision.extend(["Is the issue reachable/exploitable in scope?", "What evidence proves the mitigation blocks the path?"])
        unknowns.extend(["Target version", "Reachability", "Authorization/test environment"])
    else:
        decision.append("Which unresolved fact could materially change the final answer or action?")
    return {
        "primary_question": text.strip(),
        "subquestions": subquestions,
        "decision_critical_questions": decision,
        "unknown_variables": unknowns,
        "claims_requiring_verification": ["Any current, version-sensitive, compatibility, security, or implementation claim used in the conclusion."],
        "disconfirming_evidence_to_seek": disconfirm,
    }


def _research_graph(text: str, domain: str, *, deep: bool) -> dict[str, Any]:
    branches = ["entity", "official_docs"]
    if domain in {"product_platform", "software_library", "security", "open_source_project"}:
        branches.append("implementation")
    if domain == "security":
        branches.append("security_evidence")
    if deep or domain == "product_platform":
        branches.extend(["historical_version", "failure_reports", "contradicting_evidence", "alternative_or_dependency"])
    return {"root": text.strip(), "branches": list(dict.fromkeys(branches))}


def _select_output_mode(text: str, level: ResearchLevel) -> str:
    lower = text.lower()
    explicit = [
        ("evidence_matrix", r"\bevidence matrix\b"),
        ("investigation_log", r"\binvestigation log\b"),
        ("decision_memo", r"\bdecision memo\b"),
        ("research_brief", r"\bresearch brief\b"),
        ("deep_dive", r"\bdeep dive\b"),
    ]
    for mode, pattern in explicit:
        if re.search(pattern, lower):
            return mode
    if level in {ResearchLevel.DEEP, ResearchLevel.LATERAL, ResearchLevel.ADVERSARIAL, ResearchLevel.EXHAUSTIVE}:
        return "deep_dive"
    if level is ResearchLevel.STANDARD:
        return "research_brief"
    return "answer"


def build_research_plan(
    text: str,
    *,
    strategy_allowlist: set[str] | None = None,
    disabled_strategies: set[str] | None = None,
) -> ResearchPlan:
    if not isinstance(text, str) or not text.strip():
        raise ValueError("research task must be a non-empty string")
    level = _research_level(text)
    domain = _domain(text)
    freshness = bool(re.search(r"\b(?:latest|current(?:ly)?|today|supported|compatib|pricing|version|release|vulnerab)\b", text, re.I))
    if level is ResearchLevel.NONE:
        return ResearchPlan(
            level=level,
            question_map=_question_map(text, domain),
            expected_source_types=[],
            strategies=[],
            query_classes={},
            freshness_required=freshness,
            coverage={},
            frontier={"resolved": [], "unresolved": []},
            stopping_criteria=["No external research is required for the requested result."],
            budget=dict(RESEARCH_BUDGETS[level]),
            graph=_research_graph(text, domain, deep=False),
        )

    sources = route_source_classes(domain)
    strategies = ["direct"]
    if level in {ResearchLevel.STANDARD, ResearchLevel.DEEP, ResearchLevel.LATERAL, ResearchLevel.ADVERSARIAL, ResearchLevel.EXHAUSTIVE}:
        strategies.append("cross_check")
    if domain in {"software_library", "security", "product_platform"}:
        strategies.append("implementation")
    if level in {ResearchLevel.DEEP, ResearchLevel.LATERAL, ResearchLevel.ADVERSARIAL, ResearchLevel.EXHAUSTIVE}:
        strategies.extend(["lateral", "disconfirmation", "failure_oriented"])
    if freshness or domain == "product_platform":
        strategies.append("historical")
    if domain == "security" and level in {ResearchLevel.DEEP, ResearchLevel.ADVERSARIAL, ResearchLevel.EXHAUSTIVE}:
        strategies.append("adversarial_challenge")
    # preserve order while deduplicating, then apply explicit experimental ablations.
    strategies = list(dict.fromkeys(strategies))
    disabled = set(disabled_strategies or set())
    if strategy_allowlist is not None:
        allow = set(strategy_allowlist)
        strategies = [item for item in strategies if item in allow]
    strategies = [item for item in strategies if item not in disabled]

    query_classes = transform_queries(text)
    if level is ResearchLevel.LIGHT:
        query_classes = {k: query_classes[k] for k in ("direct", "negative")}
    elif level is ResearchLevel.STANDARD:
        query_classes = {k: query_classes[k] for k in ("direct", "negative", "failure", "implementation", "change")}
    query_strategy = {
        "direct": "direct",
        "negative": "disconfirmation",
        "failure": "failure_oriented",
        "historical": "historical",
        "implementation": "implementation",
        "change": "historical",
        "discussion": "cross_check",
    }
    if strategy_allowlist is not None or disabled:
        query_classes = {
            name: query
            for name, query in query_classes.items()
            if query_strategy.get(name, "direct") in strategies
        }

    coverage = {
        "official_docs": "unexplored",
        "implementation": "unexplored",
        "release_history": "unexplored",
        "failure_reports": "unexplored",
        "independent_evidence": "unexplored",
        "contradiction_search": "unexplored",
        "live_test": "unexplored",
    }
    qmap = _question_map(text, domain)
    unresolved = list(qmap["decision_critical_questions"]) + list(qmap["unknown_variables"])
    pivot_rules = [
        "keyword -> entity when repeated keyword searches stop adding evidence",
        "documentation -> source_code when actual implementation behavior is load-bearing",
        "source_code -> issues when implementation intent/failure history is unclear",
        "current -> historical when a rename, deprecation, or migration may explain conflicting claims",
        "claim -> contradiction_search before high-confidence/high-impact promotion",
        "entity -> dependency_or_underlying_protocol when the named surface does not explain the mechanism",
        "direct -> analogous_system when direct evidence remains weak; analogy generates hypotheses, not proof",
    ]
    terminology_expansion: list[str] = []
    if domain == "product_platform" and re.search(r"\bskills?\b", text, re.I):
        terminology_expansion = ["skill", "agent skill", "command", "rule", "instruction", "plugin", "extension", "workflow", "agent", "prompt package", "capability"]
    hypothesis_dimensions: list[str] = []
    if domain == "security" or re.search(r"\b(?:failure|failing|broken|intermittent|debug)\b", text, re.I):
        hypothesis_dimensions = [
            "data", "state", "timing", "concurrency", "environment", "dependency", "configuration",
            "network", "cache", "authentication", "authorization", "permissions", "version_mismatch",
        ]
    output_mode = _select_output_mode(text, level)
    return ResearchPlan(
        level=level,
        question_map=qmap,
        expected_source_types=sources,
        strategies=strategies,
        query_classes=query_classes,
        freshness_required=freshness,
        coverage=coverage,
        frontier={"resolved": [], "unresolved": unresolved},
        stopping_criteria=[
            "Stop when decision-critical questions are answered with evidence appropriate to the claim impact.",
            "Stop when material contradictions are resolved or explicitly remain unresolved.",
            "Stop when additional search is repetitive/diminishing-return or the declared budget is reached.",
        ],
        budget=dict(RESEARCH_BUDGETS[level]),
        failure_taxonomy=[
            "NO_AUTHORITATIVE_SOURCE", "STALE_EVIDENCE", "CONFLICTING_SOURCES", "INSUFFICIENT_ACCESS", "PAYWALL",
            "RUNTIME_TEST_UNAVAILABLE", "VERSION_UNKNOWN", "SOURCE_CODE_UNAVAILABLE", "NETWORK_UNAVAILABLE", "AMBIGUOUS_ENTITY",
        ],
        next_best_evidence="Prefer the cheapest safe evidence source or experiment that most reduces decision-relevant uncertainty.",
        pivot_rules=pivot_rules,
        terminology_expansion=terminology_expansion,
        information_gain_rule="Prioritize the safe next source or experiment with the highest decision-relevant information value per cost, not the easiest additional search.",
        output_mode=output_mode,
        hypothesis_dimensions=hypothesis_dimensions,
        graph=_research_graph(text, domain, deep=level in {ResearchLevel.DEEP, ResearchLevel.LATERAL, ResearchLevel.ADVERSARIAL, ResearchLevel.EXHAUSTIVE}),
    )
