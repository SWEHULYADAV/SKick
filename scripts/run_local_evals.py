#!/usr/bin/env python3
"""Dependency-free deterministic SKick runtime evaluations.

These suites test SKick's own executable routing/state/claim/compiler behavior. They are
not substitutes for model behavioral evaluations or live platform tests.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime.capabilities import discover_capabilities
from runtime.claims import ClaimFirewallError, add_claim, set_claim_status
from runtime.depth import classify_task
from runtime.modules import compile_modules
from runtime.report import render_report
from runtime.prompt_intelligence import interpret_task
from runtime.research import build_research_plan
from runtime.teaming import build_teaming_plan
from runtime.state import add_evidence, new_run_state


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def check(name: str, actual: Any, expected: Any, passed: bool | None = None) -> dict[str, Any]:
    return {"name": name, "actual": actual, "expected": expected, "passed": bool(actual == expected if passed is None else passed)}


def eval_classify(case: dict[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    decision = classify_task(case["task"], explicit_depth=case.get("explicit_depth"))
    expected = case.get("expect", {})
    checks = []
    if "activate" in expected:
        checks.append(check("activate", decision.activate, expected["activate"]))
    if "depth" in expected:
        allowed = list(expected["depth"])
        checks.append(check("depth", decision.depth, allowed, decision.depth in allowed))
    if "mode" in expected:
        allowed = list(expected["mode"])
        checks.append(check("mode", decision.mode, allowed, decision.mode in allowed))
    return decision.to_dict(), checks


def eval_compile(case: dict[str, Any], root: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    caps = discover_capabilities(root, declared=case.get("declared_capabilities"))
    decision = classify_task(case["task"], explicit_depth=case.get("explicit_depth"))
    plan = compile_modules(
        case["task"], root, caps,
        decision=decision,
        budget_tokens=case.get("budget_tokens"),
    )
    selected = {item.path for item in plan.selected}
    checks = []
    for path in case.get("expect_selected", []):
        checks.append(check(f"selected:{path}", path in selected, True))
    for path in case.get("expect_excluded", []):
        checks.append(check(f"excluded:{path}", path not in selected, True))
    if case.get("expect_routing_note_contains"):
        needle = str(case["expect_routing_note_contains"]).lower()
        actual = "\n".join(plan.routing_notes)
        checks.append(check("routing_note_contains", needle in actual.lower(), True))
    return {"decision": decision.to_dict(), "module_plan": plan.to_dict()}, checks


def eval_capability(case: dict[str, Any], root: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    caps = discover_capabilities(root, declared=case.get("declared_capabilities"), active_network_probe=False)
    states = {name: record.state.value for name, record in caps.capabilities.items()}
    checks = [check(f"capability:{name}", states.get(name), expected) for name, expected in case.get("expect_capabilities", {}).items()]
    return {"capabilities": states, "probe_policy": caps.probe_policy}, checks


def eval_claim(case: dict[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    state = new_run_state("claim honesty deterministic eval")
    claim_id = add_claim(state, "evaluation claim", status="implemented")
    evidence_ids = []
    for raw in case.get("evidence", []):
        evidence_ids.append(add_evidence(
            state,
            raw["type"], raw.get("subject", "evaluation evidence"),
            status=raw["status"], source=raw.get("source"),
            metadata={"supports_claim_ids": [claim_id], **dict(raw.get("metadata", {}))},
        ))
    allowed = True
    error = None
    try:
        set_claim_status(state, claim_id, case["target_status"], evidence_ids=evidence_ids)
    except ClaimFirewallError as exc:
        allowed = False
        error = str(exc)
    expected = bool(case["expect_allowed"])
    return {"allowed": allowed, "error": error, "target_status": case["target_status"], "evidence_ids": evidence_ids}, [check("allowed", allowed, expected)]


def eval_report(case: dict[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    state = new_run_state("report deterministic eval")
    add_claim(state, "evaluation claim", status=case.get("claim_status", "not_tested"))
    report = render_report(state)
    needle = str(case.get("expect_contains", ""))
    return {"report": report}, [check("report_contains", needle in report, True)]


def eval_ablation(case: dict[str, Any], root: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    caps = discover_capabilities(root, declared=case.get("declared_capabilities"))
    decision = classify_task(case["task"], explicit_depth=case.get("explicit_depth"))
    kwargs = {"decision": decision, "budget_tokens": case.get("budget_tokens")}
    full = compile_modules(case["task"], root, caps, **kwargs)
    ablate = set(case.get("ablate", []))
    ablated = compile_modules(case["task"], root, caps, ablations=ablate, **kwargs)
    full_paths = {item.path for item in full.selected}
    ablated_paths = {item.path for item in ablated.selected}
    removed = sorted(full_paths - ablated_paths)
    required_guard_missing = any(item.mandatory and item.path in removed for item in full.selected)
    token_reduction = ablated.total_estimated_tokens < full.total_estimated_tokens
    checks = []
    for path in case.get("expect_removed", []):
        checks.append(check(f"removed:{path}", path in removed, True))
    if "expect_token_reduction" in case:
        checks.append(check("token_reduction", token_reduction, bool(case["expect_token_reduction"])))
    if "expect_required_guard_missing" in case:
        checks.append(check("required_guard_missing", required_guard_missing, bool(case["expect_required_guard_missing"])))
    result = {
        "full_tokens": full.total_estimated_tokens,
        "ablated_tokens": ablated.total_estimated_tokens,
        "token_delta": ablated.total_estimated_tokens - full.total_estimated_tokens,
        "removed": removed,
        "required_guard_missing": required_guard_missing,
        "full_plan": full.to_dict(),
        "ablated_plan": ablated.to_dict(),
    }
    return result, checks



def eval_prompt(case: dict[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    result = interpret_task(case["task"]).to_dict()
    checks: list[dict[str, Any]] = []
    if case.get("expect_domain"):
        checks.append(check("domain", case["expect_domain"] in result["domains"], True))
    if "expect_verification" in case:
        checks.append(check("verification", bool(result["verification_needs"]), bool(case["expect_verification"])))
    if "max_success_criteria" in case:
        checks.append(check("success_criteria_count", len(result["success_criteria"]) <= int(case["max_success_criteria"]), True))
    if case.get("expect_research_needs_empty"):
        checks.append(check("research_needs_empty", result["research_needs"], []))
    if case.get("expect_constraint_contains"):
        needle = str(case["expect_constraint_contains"]).lower()
        actual = "\n".join(result["constraints"]).lower()
        checks.append(check("constraint_contains", needle in actual, True))
    if "expect_contradiction" in case:
        checks.append(check("contradiction", bool(result["contradictions"]), bool(case["expect_contradiction"])))
    return result, checks


def eval_research(case: dict[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    result = build_research_plan(case["task"]).to_dict()
    checks: list[dict[str, Any]] = []
    if case.get("expect_level"):
        allowed = list(case["expect_level"])
        checks.append(check("level", result["level"], allowed, result["level"] in allowed))
    for strategy in case.get("expect_strategies", []):
        checks.append(check(f"strategy:{strategy}", strategy in result["strategies"], True))
    for source in case.get("expect_source_types", []):
        checks.append(check(f"source:{source}", source in result["expected_source_types"], True))
    if "expect_freshness" in case:
        checks.append(check("freshness", result["freshness_required"], bool(case["expect_freshness"])))
    return result, checks


def eval_team(case: dict[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    result = build_teaming_plan(case["task"]).to_dict()
    checks: list[dict[str, Any]] = []
    if "expect_roles" in case:
        checks.append(check("roles", result["roles"], list(case["expect_roles"])))
    for role in case.get("expect_roles_contains", []):
        checks.append(check(f"role:{role}", role in result["roles"], True))
    if case.get("expect_authorization"):
        checks.append(check("authorization", result["security_scope"]["authorization_context"], case["expect_authorization"]))
    if case.get("expect_safe_boundary"):
        checks.append(check("safe_boundary", result["security_scope"]["safe_test_boundary"], case["expect_safe_boundary"]))
    return result, checks


def eval_research_ablation(case: dict[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    full = build_research_plan(case["task"])
    direct_only = build_research_plan(case["task"], strategy_allowlist={"direct"})
    no_disconfirm = build_research_plan(case["task"], disabled_strategies={"disconfirmation"})
    removed = sorted(set(full.strategies) - set(no_disconfirm.strategies))
    result = {
        "full_strategies": full.strategies,
        "direct_only_strategies": direct_only.strategies,
        "without_disconfirmation_strategies": no_disconfirm.strategies,
        "full_query_classes": len(full.query_classes),
        "direct_only_query_classes": len(direct_only.query_classes),
        "removed_without_disconfirmation": removed,
        "behavioral_quality_measurement": "NOT_MEASURED",
    }
    checks: list[dict[str, Any]] = []
    for strategy in case.get("expect_full_strategies", []):
        checks.append(check(f"full_strategy:{strategy}", strategy in full.strategies, True))
    if case.get("expect_direct_only_fewer_queries"):
        checks.append(check("direct_only_fewer_queries", len(direct_only.query_classes) < len(full.query_classes), True))
    if case.get("expect_without_disconfirmation_removed"):
        checks.append(check("disconfirmation_removed", "disconfirmation" in removed, True))
    return result, checks


def evaluate(case: dict[str, Any], root: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    operation = case.get("operation")
    if operation == "classify":
        return eval_classify(case)
    if operation == "compile":
        return eval_compile(case, root)
    if operation == "capability":
        return eval_capability(case, root)
    if operation == "claim":
        return eval_claim(case)
    if operation == "report":
        return eval_report(case)
    if operation == "ablation":
        return eval_ablation(case, root)
    if operation == "prompt":
        return eval_prompt(case)
    if operation == "research":
        return eval_research(case)
    if operation == "team":
        return eval_team(case)
    if operation == "research_ablation":
        return eval_research_ablation(case)
    raise ValueError(f"unsupported local eval operation: {operation}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("suite", type=Path)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args()
    root = args.root.resolve()
    suite_path = args.suite.resolve()
    suite = json.loads(suite_path.read_text(encoding="utf-8"))
    cases = suite.get("cases")
    if not isinstance(cases, list):
        raise SystemExit("local eval suite needs a cases array")

    results = []
    for index, case in enumerate(cases):
        if not isinstance(case, dict) or not case.get("id"):
            raise SystemExit(f"case #{index} needs an id")
        try:
            candidate, checks = evaluate(case, root)
            passed = all(bool(item.get("passed")) for item in checks)
            error = None
        except Exception as exc:
            candidate, checks, passed = {}, [], False
            error = f"{exc.__class__.__name__}: {exc}"
        row = {
            "case_id": case["id"],
            "run_index": 0,
            "runner_protocol_ok": error is None,
            "candidate_result": candidate,
            "deterministic_checks": checks,
            "scored_passed": passed,
            "score_source": "local_deterministic",
        }
        if error:
            row["protocol_error"] = error
        results.append(row)
        print(f"{case['id']}: {'PASS' if passed else 'FAIL'}")

    passed_count = sum(bool(row["scored_passed"]) for row in results)
    summary = {
        "runs": len(results),
        "scored_runs": len(results),
        "unscored_runs": 0,
        "protocol_failures": sum(not row["runner_protocol_ok"] for row in results),
        "pass_rate": passed_count / len(results) if results else None,
        "proof_type": "deterministic_local_runtime",
    }

    # Activation/depth quality is meaningful only for classification cases with
    # explicit expected labels. These are deterministic router metrics, not proof
    # that a host model's own semantic Skill auto-discovery behaves identically.
    confusion = {"tp": 0, "tn": 0, "fp": 0, "fn": 0}
    activation_total = 0
    depth_total = 0
    depth_correct = 0
    for case, row in zip(cases, results):
        if case.get("operation") != "classify" or not row.get("runner_protocol_ok"):
            continue
        expected = case.get("expect", {})
        candidate = row.get("candidate_result", {})
        if isinstance(expected.get("activate"), bool):
            actual = bool(candidate.get("activate"))
            wanted = expected["activate"]
            activation_total += 1
            if wanted and actual:
                confusion["tp"] += 1
            elif not wanted and not actual:
                confusion["tn"] += 1
            elif not wanted and actual:
                confusion["fp"] += 1
            else:
                confusion["fn"] += 1
        if isinstance(expected.get("depth"), list) and expected["depth"]:
            depth_total += 1
            if candidate.get("depth") in expected["depth"]:
                depth_correct += 1
    if activation_total:
        summary["activation_confusion"] = confusion
        summary["activation_accuracy"] = (confusion["tp"] + confusion["tn"]) / activation_total
    if depth_total:
        summary["depth_accuracy"] = depth_correct / depth_total
    if any(case.get("operation") == "research_ablation" for case in cases):
        summary["behavioral_quality_measurement"] = "NOT_MEASURED"
    try:
        suite_display = suite_path.relative_to(root).as_posix()
    except ValueError:
        suite_display = suite_path.name
    output = {
        "schema_version": 2,
        "created_at": utc_now(),
        "suite": suite_display,
        "runner": ["scripts/run_local_evals.py"],
        "summary": summary,
        "results": results,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0 if summary["protocol_failures"] == 0 and summary["pass_rate"] == 1.0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
