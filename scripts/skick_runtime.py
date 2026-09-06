#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime import __version__ as runtime_version
from runtime.capabilities import discover_capabilities, load_declared_capabilities
from runtime.claims import ClaimFirewallError, add_claim, set_claim_status
from runtime.depth import classify_task
from runtime.modules import compile_modules
from runtime.orchestrator import build_execution_plan
from runtime.prompt_intelligence import interpret_task
from runtime.research import build_research_plan
from runtime.research_ledger import ResearchLedgerError, add_research_finding
from runtime.teaming import build_teaming_plan
from runtime.report import render_report
from runtime.state import add_evidence, new_run_state, validate_state
from scripts.detect_runtime import detect


def _read_state(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    errors = validate_state(data)
    if errors:
        raise SystemExit("invalid runtime state: " + "; ".join(errors))
    return data


def _write_state(path: Path, state: dict) -> None:
    errors = validate_state(state)
    if errors:
        raise SystemExit("refusing to write invalid runtime state: " + "; ".join(errors))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _declared(path: Path | None):
    return load_declared_capabilities(path) if path else None


def cmd_status(args: argparse.Namespace) -> int:
    project = args.project.resolve()
    candidates = detect(project)
    snapshot = discover_capabilities(
        project,
        declared=_declared(args.capabilities_file),
        active_network_probe=args.probe_network,
        runtime_candidates=candidates,
    )
    package_version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    payload = {
        "skick_package_version": package_version,
        "runtime_version": runtime_version,
        "project": str(project),
        "runtime_candidates": candidates,
        "capabilities": snapshot.to_dict()["capabilities"],
        "probe_policy": snapshot.probe_policy,
        "guarantee_level": "full_runtime_local" if snapshot.capabilities["code_execution"].state.value == "available" else "partial_runtime",
    }
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(f"SKick package: {package_version}")
        print(f"Executable runtime: {runtime_version}")
        print(f"Project: {project}")
        print("Runtime candidates: " + (", ".join(candidates) if candidates else "unknown"))
        for name, record in sorted(snapshot.capabilities.items()):
            provider = f" via {record.provider}" if record.provider else ""
            print(f"{name:24} {record.state.value}{provider}")
    return 0


def cmd_compile(args: argparse.Namespace) -> int:
    project = args.project.resolve()
    candidates = detect(project)
    snapshot = discover_capabilities(
        project,
        declared=_declared(args.capabilities_file),
        active_network_probe=args.probe_network,
        runtime_candidates=candidates,
    )
    payload = build_execution_plan(
        args.task,
        ROOT,
        snapshot,
        explicit_depth=args.depth,
        budget_tokens=args.budget,
    )
    print(json.dumps(payload, indent=2))
    return 0



def cmd_enhance(args: argparse.Namespace) -> int:
    interpretation = interpret_task(args.task, mode=args.mode)
    payload = interpretation.to_dict()
    if args.mode in {"visible", "strict_spec"}:
        payload["rendered_spec"] = interpretation.render_spec()
    print(json.dumps(payload, indent=2))
    return 0


def cmd_research_plan(args: argparse.Namespace) -> int:
    print(json.dumps(build_research_plan(args.task).to_dict(), indent=2))
    return 0


def cmd_team_plan(args: argparse.Namespace) -> int:
    print(json.dumps(build_teaming_plan(args.task).to_dict(), indent=2))
    return 0


def cmd_new_state(args: argparse.Namespace) -> int:
    state = new_run_state(args.task, host=args.host, model=args.model, mode=args.mode, depth=args.depth)
    _write_state(args.output, state)
    print(str(args.output))
    return 0


def cmd_add_evidence(args: argparse.Namespace) -> int:
    state = _read_state(args.state)
    evidence_id = add_evidence(
        state,
        args.type,
        args.subject,
        status=args.status,
        source=args.source,
        command=args.command,
        version=args.version,
        sha256=args.sha256,
        notes=args.notes,
        metadata={key: value for key, value in {
            "lineage_root": args.lineage_root,
            "authority": args.authority,
            "freshness": args.freshness,
            "supports_claim_ids": list(args.supports_claim or []),
        }.items() if value not in (None, [])},
    )
    _write_state(args.state, state)
    print(evidence_id)
    return 0


def cmd_add_finding(args: argparse.Namespace) -> int:
    state = _read_state(args.state)
    try:
        finding_id = add_research_finding(
            state,
            args.question,
            args.claim,
            kind=args.kind,
            evidence_ids=list(args.evidence or []),
            source_class=args.source_class,
            freshness=args.freshness,
            confidence=args.confidence,
            contradictions=list(args.contradiction or []),
        )
    except ResearchLedgerError as exc:
        print(f"research ledger: {exc}", file=sys.stderr)
        return 2
    _write_state(args.state, state)
    print(finding_id)
    return 0


def cmd_set_claim(args: argparse.Namespace) -> int:
    state = _read_state(args.state)
    evidence_ids = list(args.evidence or [])
    try:
        if args.claim_id:
            set_claim_status(state, args.claim_id, args.status, evidence_ids=evidence_ids if args.evidence is not None else None)
            claim_id = args.claim_id
        else:
            if not args.text:
                raise SystemExit("--text is required when --claim-id is omitted")
            claim_id = add_claim(state, args.text, status=args.status, evidence_ids=evidence_ids, claim_type=args.claim_type)
    except ClaimFirewallError as exc:
        print(f"claim firewall: {exc}", file=sys.stderr)
        return 2
    _write_state(args.state, state)
    print(claim_id)
    return 0


def cmd_report(args: argparse.Namespace) -> int:
    state = _read_state(args.state)
    print(render_report(state), end="")
    return 0


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description="Optional executable SKick runtime")
    sub = ap.add_subparsers(dest="command", required=True)

    status = sub.add_parser("status", help="report observable runtime/capability facts")
    status.add_argument("--project", type=Path, default=Path.cwd())
    status.add_argument("--capabilities-file", type=Path)
    status.add_argument("--probe-network", action="store_true")
    status.add_argument("--json", action="store_true")
    status.set_defaults(func=cmd_status)

    compile_cmd = sub.add_parser("compile", help="classify a task and compile a module plan")
    compile_cmd.add_argument("--project", type=Path, default=Path.cwd())
    compile_cmd.add_argument("--task", required=True)
    compile_cmd.add_argument("--depth", choices=["quick", "standard", "deep", "exhaustive"])
    compile_cmd.add_argument("--budget", type=int)
    compile_cmd.add_argument("--capabilities-file", type=Path)
    compile_cmd.add_argument("--probe-network", action="store_true")
    compile_cmd.set_defaults(func=cmd_compile)


    enhance = sub.add_parser("enhance", help="structure and improve task framing without changing user intent")
    enhance.add_argument("--task", required=True)
    enhance.add_argument("--mode", choices=["silent", "visible", "execution", "strict_spec"], default="silent")
    enhance.set_defaults(func=cmd_enhance)

    research_plan = sub.add_parser("research-plan", help="build a question/source/query/budget research plan")
    research_plan.add_argument("--task", required=True)
    research_plan.set_defaults(func=cmd_research_plan)

    team_plan = sub.add_parser("team-plan", help="select adversarial/defensive review roles and safe scope")
    team_plan.add_argument("--task", required=True)
    team_plan.set_defaults(func=cmd_team_plan)

    new_state = sub.add_parser("new-state")
    new_state.add_argument("--task", required=True)
    new_state.add_argument("--output", type=Path, required=True)
    new_state.add_argument("--host")
    new_state.add_argument("--model")
    new_state.add_argument("--mode")
    new_state.add_argument("--depth")
    new_state.set_defaults(func=cmd_new_state)

    evidence = sub.add_parser("add-evidence")
    evidence.add_argument("--state", type=Path, required=True)
    evidence.add_argument("--type", required=True)
    evidence.add_argument("--subject", required=True)
    evidence.add_argument("--status", required=True)
    evidence.add_argument("--source")
    evidence.add_argument("--command")
    evidence.add_argument("--version")
    evidence.add_argument("--sha256")
    evidence.add_argument("--notes")
    evidence.add_argument("--lineage-root")
    evidence.add_argument("--authority", choices=["primary", "authoritative_secondary", "independent", "community", "unverified"])
    evidence.add_argument("--freshness", choices=["current", "fresh", "live", "historical", "unknown"])
    evidence.add_argument("--supports-claim", action="append", help="claim id this evidence directly supports; repeatable")
    evidence.set_defaults(func=cmd_add_evidence)

    finding = sub.add_parser("add-finding", help="record a typed research finding linked to evidence")
    finding.add_argument("--state", type=Path, required=True)
    finding.add_argument("--question", required=True)
    finding.add_argument("--claim", required=True)
    finding.add_argument("--kind", choices=["fact", "inference", "hypothesis", "opinion", "unknown"], required=True)
    finding.add_argument("--evidence", action="append")
    finding.add_argument("--source-class")
    finding.add_argument("--freshness")
    finding.add_argument("--confidence", choices=["high", "medium", "low", "unresolved"])
    finding.add_argument("--contradiction", action="append")
    finding.set_defaults(func=cmd_add_finding)

    claim = sub.add_parser("set-claim")
    claim.add_argument("--state", type=Path, required=True)
    claim.add_argument("--claim-id")
    claim.add_argument("--text")
    claim.add_argument("--status", required=True)
    claim.add_argument("--claim-type", choices=["general", "code_change", "current_fact", "platform_compatibility", "security"])
    claim.add_argument("--evidence", action="append")
    claim.set_defaults(func=cmd_set_claim)

    report = sub.add_parser("report")
    report.add_argument("--state", type=Path, required=True)
    report.set_defaults(func=cmd_report)
    return ap


def main() -> int:
    args = build_parser().parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
