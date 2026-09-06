from __future__ import annotations

from dataclasses import replace
from pathlib import Path
from typing import Any

from .model import CapabilitySnapshot
from .depth import classify_task
from .modules import compile_modules
from .prompt_intelligence import EnhancementMode, interpret_task
from .research import ResearchLevel, build_research_plan
from .teaming import TeamRole, build_teaming_plan


def _forced_modules(research_plan, teaming_plan) -> dict[str, str]:
    forced: dict[str, str] = {}
    if research_plan.level is not ResearchLevel.NONE:
        forced["research-core"] = f"research level={research_plan.level.value}"
    if "lateral" in research_plan.strategies or "disconfirmation" in research_plan.strategies:
        forced["query-mutation"] = "lateral/disconfirmation query branching is required"
        forced["coverage-and-lateral-search"] = "research coverage and pivot rules are required"
    roles = set(teaming_plan.roles)
    if TeamRole.RED in roles or TeamRole.BLUE in roles:
        forced["security-research"] = "security teaming requires scoped security research guidance"
    if TeamRole.PURPLE in roles:
        forced["offensive-defensive"] = "purple validation requires offensive-to-defensive translation"
        forced["purple-team-research-and-validation"] = "purple retest loop is selected"
    if TeamRole.BLACK in roles:
        forced["verified-review-and-simplification"] = "independent skeptical review is selected"
    return forced



def _reconcile_decision(decision, research_plan, *, explicit_depth: str | None):
    if explicit_depth is not None:
        return decision
    depth = decision.depth
    reasons = list(decision.reasons)
    activate = decision.activate
    if research_plan.level in {ResearchLevel.STANDARD, ResearchLevel.DEEP, ResearchLevel.LATERAL, ResearchLevel.ADVERSARIAL, ResearchLevel.EXHAUSTIVE}:
        activate = True
        reasons.append(f"research intelligence selected {research_plan.level.value}")
    if research_plan.level in {ResearchLevel.DEEP, ResearchLevel.LATERAL, ResearchLevel.ADVERSARIAL} and depth in {"quick", "standard"}:
        depth = "deep"
        reasons.append("research intelligence escalated execution depth to deep")
    elif research_plan.level is ResearchLevel.EXHAUSTIVE and depth != "exhaustive":
        depth = "exhaustive"
        reasons.append("research intelligence escalated execution depth to exhaustive")
    return replace(decision, activate=activate, depth=depth, reasons=list(dict.fromkeys(reasons)))


def build_execution_plan(
    task: str,
    root: Path,
    capabilities: CapabilitySnapshot,
    *,
    explicit_depth: str | None = None,
    budget_tokens: int | None = None,
    project_policy: dict[str, Any] | None = None,
    ablations: set[str] | None = None,
    enhancement_mode: str | EnhancementMode = EnhancementMode.SILENT,
) -> dict[str, Any]:
    interpretation = interpret_task(task, mode=enhancement_mode)
    decision = classify_task(task, explicit_depth=explicit_depth)
    research_plan = build_research_plan(task)
    decision = _reconcile_decision(decision, research_plan, explicit_depth=explicit_depth)
    teaming_plan = build_teaming_plan(task)
    module_plan = compile_modules(
        task,
        root,
        capabilities,
        decision=decision,
        budget_tokens=budget_tokens,
        project_policy=project_policy,
        ablations=ablations,
        forced_modules=_forced_modules(research_plan, teaming_plan),
    )
    return {
        "schema_version": 1,
        "task": task,
        "task_interpretation": interpretation.to_dict(),
        "decision": decision.to_dict(),
        "research_plan": research_plan.to_dict(),
        "teaming_plan": teaming_plan.to_dict(),
        "capability_snapshot": capabilities.to_dict(),
        "module_plan": module_plan.to_dict(),
    }
