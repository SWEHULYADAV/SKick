from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from .budget import DEFAULT_MODULE_BUDGETS, ESTIMATE_METHOD, estimate_file_tokens
from .model import CapabilitySnapshot, CapabilityState, DepthDecision


@dataclass(slots=True)
class ModuleSelection:
    id: str
    path: str
    priority: int
    mandatory: bool
    estimated_tokens: int
    reasons: list[str]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class ModulePlan:
    plan_kind: str
    selected: list[ModuleSelection]
    optional: list[ModuleSelection]
    skipped: list[dict[str, Any]]
    dropped_for_budget: list[dict[str, Any]]
    routing_notes: list[str]
    budget_tokens: int
    total_estimated_tokens: int
    root_control_plane_estimated_tokens: int
    estimate_method: str = ESTIMATE_METHOD
    required_capabilities: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": 1,
            "plan_kind": self.plan_kind,
            "selected": [item.to_dict() for item in self.selected],
            "optional": [item.to_dict() for item in self.optional],
            "skipped": self.skipped,
            "dropped_for_budget": self.dropped_for_budget,
            "routing_notes": self.routing_notes,
            "budget_tokens": self.budget_tokens,
            "total_estimated_tokens": self.total_estimated_tokens,
            "root_control_plane_estimated_tokens": self.root_control_plane_estimated_tokens,
            "estimate_method": self.estimate_method,
            "required_capabilities": self.required_capabilities,
        }


def _catalog(root: Path) -> list[dict[str, Any]]:
    path = root / "runtime" / "module_catalog.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    modules = data.get("modules")
    if not isinstance(modules, list):
        raise ValueError("runtime/module_catalog.json needs a modules array")
    return modules


def _policy(root: Path, supplied: dict[str, Any] | None) -> dict[str, Any]:
    if supplied is not None:
        return supplied
    path = root / "runtime" / "project_policy.json"
    return json.loads(path.read_text(encoding="utf-8"))


def _policy_value(policy: dict[str, Any], dotted: str | None) -> Any:
    if not dotted:
        return None
    value: Any = policy
    for part in dotted.split("."):
        if not isinstance(value, dict) or part not in value:
            return None
        value = value[part]
    return value


def _provider_matches(entry: dict[str, Any], caps: CapabilitySnapshot) -> bool:
    required = entry.get("required_provider")
    if not isinstance(required, dict):
        return True
    name = required.get("capability")
    record = caps.capabilities.get(str(name))
    if record is None or record.state != CapabilityState.AVAILABLE or not record.provider:
        return False
    return bool(re.search(str(required.get("provider_pattern", ".*")), record.provider))


def _capabilities_satisfied(entry: dict[str, Any], caps: CapabilitySnapshot) -> bool:
    for name in entry.get("required_capabilities", []):
        record = caps.capabilities.get(name)
        if record is None or record.state != CapabilityState.AVAILABLE:
            return False
    return True


def _activation_reasons(entry: dict[str, Any], task: str, decision: DepthDecision, policy: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    if decision.depth not in entry.get("depths", []):
        return []
    if entry.get("always_for_activated"):
        reasons.append("required by active SKick branch")
    if decision.mode in entry.get("modes", []):
        reasons.append(f"mode={decision.mode}")
    for pattern in entry.get("task_patterns", []):
        if re.search(pattern, task, re.I):
            reasons.append(f"task matched {pattern}")
            break
    project_policy = entry.get("project_policy")
    if project_policy:
        if _policy_value(policy, project_policy) is True:
            reasons.append(f"project policy enabled: {project_policy}")
        else:
            # Policy-gated modules cannot be selected merely by task keywords.
            return []
    return reasons


def compile_modules(
    task: str,
    root: Path,
    capabilities: CapabilitySnapshot,
    *,
    decision: DepthDecision,
    budget_tokens: int | None = None,
    project_policy: dict[str, Any] | None = None,
    ablations: set[str] | None = None,
    forced_modules: dict[str, str] | None = None,
) -> ModulePlan:
    root = root.resolve()
    budget = int(budget_tokens if budget_tokens is not None else DEFAULT_MODULE_BUDGETS[decision.depth])
    root_tokens = estimate_file_tokens(root / "SKILL.md")
    if not decision.activate:
        return ModulePlan(
            plan_kind="minimal",
            selected=[],
            optional=[],
            skipped=[{"path": entry["path"], "reason": "SKick auto-activation not warranted for this task"} for entry in _catalog(root)],
            dropped_for_budget=[],
            routing_notes=["minimum sufficient process: no additional SKick modules compiled"],
            budget_tokens=budget,
            total_estimated_tokens=0,
            root_control_plane_estimated_tokens=root_tokens,
        )

    policy = _policy(root, project_policy)
    ablations = set(ablations or set())
    forced_modules = dict(forced_modules or {})
    candidates: list[ModuleSelection] = []
    skipped: list[dict[str, Any]] = []
    routing_notes: list[str] = []
    required_capabilities: set[str] = set()

    semantic = capabilities.capabilities.get("semantic_code_search")
    if semantic is None or semantic.state != CapabilityState.AVAILABLE:
        routing_notes.append("semantic_code_search unavailable/unknown: use repository-search and targeted file-read fallback")
    elif semantic.provider:
        routing_notes.append(f"semantic_code_search available via {semantic.provider}; provider selected only when module policy matches")

    for entry in _catalog(root):
        if str(entry.get("id")) in ablations:
            skipped.append({"path": entry["path"], "reason": "explicit experimental ablation"})
            routing_notes.append(f"ABLATION: skipped {entry['id']}")
            continue
        reasons = _activation_reasons(entry, task, decision, policy)
        forced_reason = forced_modules.get(str(entry.get("id")))
        if forced_reason and decision.depth in entry.get("depths", []):
            reasons = list(dict.fromkeys([*reasons, f"intelligence plan: {forced_reason}"]))
        if not reasons:
            skipped.append({"path": entry["path"], "reason": "activation conditions not met"})
            continue
        if not _provider_matches(entry, capabilities):
            skipped.append({"path": entry["path"], "reason": "required capability provider not available"})
            continue
        if not _capabilities_satisfied(entry, capabilities):
            skipped.append({"path": entry["path"], "reason": "required capability unavailable"})
            continue
        for name in entry.get("required_capabilities", []):
            required_capabilities.add(name)
        candidates.append(ModuleSelection(
            id=str(entry["id"]),
            path=str(entry["path"]),
            priority=max(int(entry.get("priority", 0)), 90 if forced_reason else 0),
            mandatory=bool(entry.get("mandatory", False)),
            estimated_tokens=int(entry.get("estimated_context_tokens", 1)),
            reasons=reasons,
        ))

    candidates.sort(key=lambda item: (not item.mandatory, -item.priority, item.path))
    selected: list[ModuleSelection] = []
    dropped: list[dict[str, Any]] = []
    used = 0
    for item in candidates:
        if item.mandatory:
            selected.append(item)
            used += item.estimated_tokens
            continue
        if used + item.estimated_tokens <= budget:
            selected.append(item)
            used += item.estimated_tokens
        else:
            dropped.append({"path": item.path, "estimated_tokens": item.estimated_tokens, "reason": "module budget exceeded; optional module dropped"})
            skipped.append({"path": item.path, "reason": "dropped for instruction budget"})

    if used > budget:
        routing_notes.append("mandatory module cost exceeds configured module budget; mandatory truth/safety modules were retained")
    optional = [item for item in selected if not item.mandatory]
    return ModulePlan(
        plan_kind="compiled",
        selected=selected,
        optional=optional,
        skipped=skipped,
        dropped_for_budget=dropped,
        routing_notes=routing_notes,
        budget_tokens=budget,
        total_estimated_tokens=used,
        root_control_plane_estimated_tokens=root_tokens,
        required_capabilities=sorted(required_capabilities),
    )
