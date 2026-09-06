from __future__ import annotations

from typing import Any

from .claims import status_supported
from .state import evidence_index


LABELS = {
    "planned": "PLANNED",
    "inspected": "INSPECTED",
    "changed": "CHANGED",
    "implemented": "IMPLEMENTED",
    "executed": "EXECUTED",
    "tested": "TESTED",
    "verified": "VERIFIED",
    "docs_verified": "DOC VERIFIED",
    "live_verified": "LIVE VERIFIED",
    "inferred": "INFERRED",
    "likely": "LIKELY",
    "blocked": "BLOCKED",
    "unknown": "UNKNOWN",
    "not_tested": "NOT TESTED",
}


def _effective_status(claim: dict[str, Any], index: dict[str, dict[str, Any]]) -> tuple[str, str | None]:
    status = str(claim.get("status", "unknown"))
    evidence = [index[eid] for eid in claim.get("evidence_ids", []) if eid in index]
    ok, reason = status_supported(status, evidence, claim=claim)
    if ok:
        return status, None
    return "unknown", f"claim firewall downgraded unsupported status {status}: {reason}"


def render_report(state: dict[str, Any]) -> str:
    index = evidence_index(state)
    lines = [
        f"SKick run: {state.get('run_id', 'unknown')}",
        f"Result status: {state.get('result_status', 'unknown')}",
        f"Mode/depth: {state.get('mode') or 'unknown'} / {state.get('depth') or 'unknown'}",
        "",
        "Claims:",
    ]
    if not state.get("claims"):
        lines.append("- [UNKNOWN] No explicit completion claim recorded.")
    for claim in state.get("claims", []):
        status, note = _effective_status(claim, index)
        lines.append(f"- [{LABELS.get(status, status.upper())}] {claim.get('text', '')}")
        if claim.get("evidence_ids"):
            lines.append("  Evidence: " + ", ".join(str(x) for x in claim["evidence_ids"]))
        if note:
            lines.append(f"  Note: {note}")
    if state.get("blockers"):
        lines.extend(["", "Blockers:"])
        for blocker in state["blockers"]:
            lines.append(f"- {blocker}")
    return "\n".join(lines).rstrip() + "\n"
