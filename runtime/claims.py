from __future__ import annotations

from typing import Any
from uuid import uuid4

from .state import evidence_index, utc_now


CLAIM_STATUSES = {
    "planned",
    "inspected",
    "changed",
    "implemented",
    "executed",
    "tested",
    "verified",
    "docs_verified",
    "live_verified",
    "inferred",
    "likely",
    "blocked",
    "unknown",
    "not_tested",
}

CLAIM_TYPES = {
    "general",
    "code_change",
    "current_fact",
    "platform_compatibility",
    "security",
}

SUCCESS_STATUSES = {"passed", "verified"}
PROOF_STATUSES = {"executed", "tested", "verified", "docs_verified", "live_verified"}


class ClaimFirewallError(ValueError):
    pass


def _claim(state: dict[str, Any], claim_id: str) -> dict[str, Any]:
    for claim in state.get("claims", []):
        if claim.get("id") == claim_id:
            return claim
    raise KeyError(f"unknown claim id: {claim_id}")


def _selected_evidence(state: dict[str, Any], evidence_ids: list[str]) -> list[dict[str, Any]]:
    index = evidence_index(state)
    missing = [evidence_id for evidence_id in evidence_ids if evidence_id not in index]
    if missing:
        raise ClaimFirewallError(f"claim references unknown evidence ids: {missing}")
    return [index[evidence_id] for evidence_id in evidence_ids]


def _bound_evidence(claim: dict[str, Any], evidence: list[dict[str, Any]]) -> list[dict[str, Any]]:
    claim_id = str(claim.get("id", ""))
    bound: list[dict[str, Any]] = []
    for item in evidence:
        metadata = item.get("metadata") if isinstance(item.get("metadata"), dict) else {}
        supported = metadata.get("supports_claim_ids", [])
        if isinstance(supported, str):
            supported = [supported]
        if claim_id and isinstance(supported, list) and claim_id in {str(value) for value in supported}:
            bound.append(item)
    return bound


def _fresh(item: dict[str, Any]) -> bool:
    metadata = item.get("metadata") if isinstance(item.get("metadata"), dict) else {}
    return str(metadata.get("freshness", "")).lower() in {"current", "fresh", "live"}


def _default_claim_type(text: str) -> str:
    lower = text.lower()
    if any(token in lower for token in ("today", "current", "latest", "right now")):
        return "current_fact"
    if any(token in lower for token in ("works on platform", "supports skill", "supported on", "compatible with")):
        return "platform_compatibility"
    if any(token in lower for token in ("vulnerability", "secure", "security", "exploit", "authorization", "authentication bypass")):
        return "security"
    if any(token in lower for token in ("fixed", "regression", "patch", "bug is resolved", "implemented fix")):
        return "code_change"
    return "general"


def status_supported(
    status: str,
    evidence: list[dict[str, Any]],
    *,
    claim: dict[str, Any] | None = None,
) -> tuple[bool, str | None]:
    if status not in CLAIM_STATUSES:
        return False, f"unsupported claim status: {status}"

    claim_type = str((claim or {}).get("claim_type", "general"))
    relevant = evidence
    if status in PROOF_STATUSES and claim is not None:
        relevant = _bound_evidence(claim, evidence)
        if not relevant:
            return False, f"{status.upper()} requires evidence explicitly bound to claim {claim.get('id')}"

    if status == "tested":
        if any(item.get("type") == "test_result" and item.get("status") in SUCCESS_STATUSES for item in relevant):
            return True, None
        return False, "TESTED requires passing claim-bound test_result evidence"

    if status == "docs_verified":
        if any(
            item.get("type") == "first_party_documentation"
            and item.get("status") in {"observed", "verified", "passed"}
            for item in relevant
        ):
            return True, None
        return False, "DOCS_VERIFIED requires claim-bound first_party_documentation evidence"

    if status == "live_verified":
        allowed_types = {"live_platform_test"} if claim_type == "platform_compatibility" else {"runtime_observation", "live_platform_test"}
        if any(item.get("type") in allowed_types and item.get("status") in SUCCESS_STATUSES for item in relevant):
            return True, None
        if claim_type == "platform_compatibility":
            return False, "LIVE_VERIFIED platform compatibility requires successful claim-bound live_platform_test evidence"
        return False, "LIVE_VERIFIED requires successful claim-bound runtime_observation or live_platform_test evidence"

    if status == "verified":
        if claim_type == "current_fact":
            allowed = {"first_party_documentation", "external_documentation", "browser_result", "runtime_observation", "live_platform_test"}
            if any(item.get("type") in allowed and item.get("status") in {"observed", "verified", "passed"} and _fresh(item) for item in relevant):
                return True, None
            return False, "VERIFIED current facts require claim-bound current/fresh external or runtime evidence"
        if claim_type == "platform_compatibility":
            if any(item.get("type") == "live_platform_test" and item.get("status") in SUCCESS_STATUSES for item in relevant):
                return True, None
            return False, "VERIFIED platform compatibility requires claim-bound live_platform_test evidence; use DOCS_VERIFIED for documentation-only proof"
        if claim_type in {"code_change", "security"}:
            allowed = {"test_result", "runtime_observation", "live_platform_test", "benchmark"}
            if any(item.get("type") in allowed and item.get("status") in SUCCESS_STATUSES for item in relevant):
                return True, None
            return False, f"VERIFIED {claim_type} claims require successful claim-bound behavioral/test evidence"
        strong_types = {"test_result", "runtime_observation", "live_platform_test", "static_analysis", "browser_result", "benchmark", "command_output"}
        if any(item.get("type") in strong_types and item.get("status") in SUCCESS_STATUSES for item in relevant):
            return True, None
        return False, "VERIFIED requires successful claim-bound verification evidence, not inference alone"

    if status == "executed":
        if any(
            item.get("type") in {"command_output", "runtime_observation", "test_result"}
            and item.get("status") in {"passed", "failed", "verified", "observed"}
            for item in relevant
        ):
            return True, None
        return False, "EXECUTED requires claim-bound command/runtime/test execution evidence"

    return True, None


def add_claim(
    state: dict[str, Any],
    text: str,
    *,
    status: str = "planned",
    evidence_ids: list[str] | None = None,
    claim_type: str | None = None,
) -> str:
    if not text:
        raise ValueError("claim text must not be empty")
    claim_type = claim_type or _default_claim_type(text)
    if claim_type not in CLAIM_TYPES:
        raise ValueError(f"unsupported claim type: {claim_type}")
    evidence_ids = list(evidence_ids or [])
    evidence = _selected_evidence(state, evidence_ids)
    claim_id = f"cl-{uuid4().hex[:12]}"
    claim = {
        "id": claim_id,
        "text": text,
        "claim_type": claim_type,
        "status": status,
        "evidence_ids": evidence_ids,
        "updated_at": utc_now(),
    }
    ok, reason = status_supported(status, evidence, claim=claim)
    if not ok:
        raise ClaimFirewallError(reason or "claim status is not supported")
    state.setdefault("claims", []).append(claim)
    state["updated_at"] = utc_now()
    return claim_id


def set_claim_status(
    state: dict[str, Any],
    claim_id: str,
    status: str,
    *,
    evidence_ids: list[str] | None = None,
) -> None:
    claim = _claim(state, claim_id)
    selected_ids = list(claim.get("evidence_ids", [])) if evidence_ids is None else list(evidence_ids)
    evidence = _selected_evidence(state, selected_ids)
    ok, reason = status_supported(status, evidence, claim=claim)
    if not ok:
        raise ClaimFirewallError(reason or "claim status is not supported")
    claim["status"] = status
    claim["evidence_ids"] = selected_ids
    claim["updated_at"] = utc_now()
    state["updated_at"] = utc_now()
