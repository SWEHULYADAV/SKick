from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import uuid4

from .schema_validation import validate_schema_instance
from .versioning import read_package_version


EVIDENCE_TYPES = {
    "source_code",
    "source_file",
    "command_output",
    "test_result",
    "runtime_observation",
    "live_platform_test",
    "first_party_documentation",
    "external_documentation",
    "benchmark",
    "static_analysis",
    "browser_result",
    "user_provided_evidence",
    "inference",
}

EVIDENCE_STATUSES = {"passed", "failed", "observed", "verified", "blocked", "unknown"}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def new_run_state(
    task: str,
    *,
    skick_version: str | None = None,
    host: str | None = None,
    model: str | None = None,
    mode: str | None = None,
    depth: str | None = None,
    capabilities: dict[str, Any] | None = None,
    module_plan: dict[str, Any] | None = None,
    task_interpretation: dict[str, Any] | None = None,
    research_plan: dict[str, Any] | None = None,
    teaming_plan: dict[str, Any] | None = None,
) -> dict[str, Any]:
    if not isinstance(task, str) or not task.strip():
        raise ValueError("task must be a non-empty string")
    if skick_version is None:
        skick_version = read_package_version(Path(__file__).resolve().parents[1])
    return {
        "schema_version": 1,
        "run_id": f"run-{uuid4().hex[:16]}",
        "skick_version": skick_version,
        "created_at": utc_now(),
        "updated_at": utc_now(),
        "task": task,
        "host": host,
        "model": model,
        "mode": mode,
        "depth": depth,
        "capabilities": capabilities or {},
        "module_plan": module_plan,
        "task_interpretation": task_interpretation,
        "research_plan": research_plan,
        "teaming_plan": teaming_plan,
        "research_findings": [],
        "research_frontier": dict((research_plan or {}).get("frontier", {"resolved": [], "unresolved": []})),
        "research_coverage": dict((research_plan or {}).get("coverage", {})),
        "budget": {},
        "evidence": [],
        "claims": [],
        "tests": [],
        "blockers": [],
        "trace": [],
        "result_status": "running",
    }


def add_evidence(
    state: dict[str, Any],
    evidence_type: str,
    subject: str,
    *,
    status: str,
    source: str | None = None,
    command: str | None = None,
    version: str | None = None,
    sha256: str | None = None,
    notes: str | None = None,
    metadata: dict[str, Any] | None = None,
) -> str:
    if evidence_type not in EVIDENCE_TYPES:
        raise ValueError(f"unsupported evidence type: {evidence_type}")
    if status not in EVIDENCE_STATUSES:
        raise ValueError(f"unsupported evidence status: {status}")
    if not subject:
        raise ValueError("evidence subject must not be empty")
    evidence_id = f"ev-{uuid4().hex[:12]}"
    record = {
        "id": evidence_id,
        "type": evidence_type,
        "subject": subject,
        "status": status,
        "source": source,
        "command": command,
        "version": version,
        "sha256": sha256,
        "notes": notes,
        "metadata": metadata or {},
        "recorded_at": utc_now(),
    }
    state.setdefault("evidence", []).append(record)
    state["updated_at"] = utc_now()
    return evidence_id


def evidence_index(state: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(item.get("id")): item for item in state.get("evidence", []) if isinstance(item, dict) and item.get("id")}


def validate_state(state: dict[str, Any]) -> list[str]:
    errors: list[str] = [f"schema: {item}" for item in validate_schema_instance(state, "runtime-state.schema.json")]
    required = [
        "schema_version", "run_id", "skick_version", "created_at", "task", "evidence",
        "claims", "tests", "blockers", "trace", "result_status",
    ]
    for key in required:
        if key not in state:
            errors.append(f"missing required field: {key}")
    if state.get("schema_version") != 1:
        errors.append("schema_version must equal 1")
    for key in ("evidence", "claims", "tests", "blockers", "trace", "research_findings"):
        if key in state and not isinstance(state[key], list):
            errors.append(f"{key} must be an array")
    ids = []
    for item in state.get("evidence", []) if isinstance(state.get("evidence"), list) else []:
        if not isinstance(item, dict) or not item.get("id"):
            errors.append("each evidence record needs an id")
            continue
        ids.append(item["id"])
        if item.get("type") not in EVIDENCE_TYPES:
            errors.append(f"evidence {item['id']} has unsupported type")
        if item.get("status") not in EVIDENCE_STATUSES:
            errors.append(f"evidence {item['id']} has unsupported status")
    if len(ids) != len(set(ids)):
        errors.append("evidence ids must be unique")
    evidence_ids = set(ids)
    claim_ids: list[str] = []
    for claim in state.get("claims", []) if isinstance(state.get("claims"), list) else []:
        if not isinstance(claim, dict) or not claim.get("id"):
            errors.append("each claim needs an id")
            continue
        claim_ids.append(claim["id"])
        for evidence_id in claim.get("evidence_ids", []):
            if evidence_id not in evidence_ids:
                errors.append(f"claim {claim['id']} references unknown evidence id {evidence_id}")
    if len(claim_ids) != len(set(claim_ids)):
        errors.append("claim ids must be unique")
    research_ids: list[str] = []
    allowed_kinds = {"fact", "inference", "hypothesis", "opinion", "unknown"}
    for finding in state.get("research_findings", []) if isinstance(state.get("research_findings"), list) else []:
        if not isinstance(finding, dict) or not finding.get("id"):
            errors.append("each research finding needs an id")
            continue
        research_ids.append(str(finding["id"]))
        if finding.get("kind") not in allowed_kinds:
            errors.append(f"research finding {finding['id']} has unsupported kind")
        for evidence_id in finding.get("evidence_ids", []):
            if evidence_id not in evidence_ids:
                errors.append(f"research finding {finding['id']} references unknown evidence id {evidence_id}")
    if len(research_ids) != len(set(research_ids)):
        errors.append("research finding ids must be unique")
    if "research_frontier" in state and not isinstance(state["research_frontier"], dict):
        errors.append("research_frontier must be an object")
    if "research_coverage" in state and not isinstance(state["research_coverage"], dict):
        errors.append("research_coverage must be an object")
    return errors
