from __future__ import annotations

from enum import Enum
from typing import Any
from uuid import uuid4

from .state import evidence_index, utc_now


class FindingKind(str, Enum):
    FACT = "fact"
    INFERENCE = "inference"
    HYPOTHESIS = "hypothesis"
    OPINION = "opinion"
    UNKNOWN = "unknown"


CONFIDENCE_LEVELS = {"high", "medium", "low", "unresolved"}
COVERAGE_STATES = {"unexplored", "partial", "covered", "blocked"}


class ResearchLedgerError(ValueError):
    pass


def add_research_finding(
    state: dict[str, Any],
    question: str,
    claim: str,
    *,
    kind: str | FindingKind,
    evidence_ids: list[str] | None = None,
    source_class: str | None = None,
    freshness: str | None = None,
    confidence: str | None = None,
    contradictions: list[str] | None = None,
) -> str:
    if not question.strip() or not claim.strip():
        raise ResearchLedgerError("question and claim must be non-empty")
    try:
        finding_kind = kind if isinstance(kind, FindingKind) else FindingKind(kind)
    except ValueError as exc:
        raise ResearchLedgerError(f"unsupported finding kind: {kind}") from exc
    ids = list(evidence_ids or [])
    index = evidence_index(state)
    missing = [item for item in ids if item not in index]
    if missing:
        raise ResearchLedgerError(f"unknown evidence ids: {', '.join(missing)}")
    if finding_kind is FindingKind.FACT:
        if not ids:
            raise ResearchLedgerError("FACT requires supporting evidence")
        if all(index[item].get("type") == "inference" for item in ids):
            raise ResearchLedgerError("FACT cannot be supported only by inference evidence")
    if confidence is None:
        confidence = "unresolved" if finding_kind in {FindingKind.HYPOTHESIS, FindingKind.UNKNOWN} else "medium"
    if confidence not in CONFIDENCE_LEVELS:
        raise ResearchLedgerError(f"unsupported confidence: {confidence}")
    contradiction_list = list(contradictions or [])
    if finding_kind is FindingKind.FACT and confidence == "high" and contradiction_list:
        raise ResearchLedgerError("high-confidence FACT cannot retain unresolved contradictions")
    finding_id = f"rf-{uuid4().hex[:12]}"
    state.setdefault("research_findings", []).append({
        "id": finding_id,
        "question": question,
        "claim": claim,
        "kind": finding_kind.value,
        "evidence_ids": ids,
        "source_class": source_class,
        "freshness": freshness,
        "confidence": confidence,
        "contradictions": contradiction_list,
        "recorded_at": utc_now(),
    })
    state["updated_at"] = utc_now()
    return finding_id


def evidence_independence_groups(state: dict[str, Any], evidence_ids: list[str]) -> dict[str, list[str]]:
    index = evidence_index(state)
    groups: dict[str, list[str]] = {}
    for evidence_id in evidence_ids:
        if evidence_id not in index:
            raise ResearchLedgerError(f"unknown evidence id: {evidence_id}")
        record = index[evidence_id]
        metadata = record.get("metadata") if isinstance(record.get("metadata"), dict) else {}
        lineage = metadata.get("lineage_root") or record.get("source") or evidence_id
        key = str(lineage)
        groups.setdefault(key, []).append(evidence_id)
    return groups


def summarize_research_evidence(state: dict[str, Any], evidence_ids: list[str]) -> dict[str, Any]:
    """Summarize source independence and triangulation without inflating copied sources."""
    index = evidence_index(state)
    if not evidence_ids:
        return {
            "classification": "NO_EVIDENCE",
            "independent_path_count": 0,
            "lineage_group_sizes": [],
        }
    groups = evidence_independence_groups(state, evidence_ids)
    records = []
    for evidence_id in evidence_ids:
        if evidence_id not in index:
            raise ResearchLedgerError(f"unknown evidence id: {evidence_id}")
        records.append(index[evidence_id])
    has_primary = any(
        record.get("type") == "first_party_documentation"
        or (isinstance(record.get("metadata"), dict) and record["metadata"].get("authority") == "primary")
        for record in records
    )
    has_implementation = any(record.get("type") in {"source_code", "source_file", "runtime_observation", "live_platform_test"} for record in records)
    has_independent = any(
        isinstance(record.get("metadata"), dict) and record["metadata"].get("authority") == "independent"
        for record in records
    )
    community_only = all(
        isinstance(record.get("metadata"), dict) and record["metadata"].get("authority") == "community"
        for record in records
    )
    independent_paths = len(groups)
    if has_primary and has_implementation and independent_paths >= 2:
        classification = "PRIMARY_PLUS_IMPLEMENTATION"
    elif community_only:
        classification = "COMMUNITY_ONLY"
    elif has_primary and has_independent and independent_paths >= 2:
        classification = "PRIMARY_PLUS_INDEPENDENT_CONFIRMATION"
    elif has_primary and independent_paths >= 2:
        classification = "MULTIPLE_PRIMARY_PATHS"
    elif has_primary:
        classification = "SINGLE_PRIMARY_SOURCE"
    else:
        classification = "MIXED_OR_OTHER"
    return {
        "classification": classification,
        "independent_path_count": independent_paths,
        "lineage_group_sizes": [len(items) for items in groups.values()],
    }


def update_research_frontier(
    state: dict[str, Any],
    *,
    resolved: list[str] | None = None,
    unresolved: list[str] | None = None,
) -> None:
    frontier = state.setdefault("research_frontier", {"resolved": [], "unresolved": []})
    if resolved is not None:
        frontier["resolved"] = list(dict.fromkeys(str(item) for item in resolved if str(item).strip()))
    if unresolved is not None:
        frontier["unresolved"] = list(dict.fromkeys(str(item) for item in unresolved if str(item).strip()))
    state["updated_at"] = utc_now()


def set_research_coverage(state: dict[str, Any], dimension: str, status: str) -> None:
    if status not in COVERAGE_STATES:
        raise ResearchLedgerError(f"unsupported coverage status: {status}")
    if not dimension.strip():
        raise ResearchLedgerError("coverage dimension must be non-empty")
    state.setdefault("research_coverage", {})[dimension] = status
    state["updated_at"] = utc_now()
