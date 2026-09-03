# Specialist Skill and Plugin Orchestration

## Purpose
Compose SKick with the best available specialist Skills/plugins/MCPs without duplicating workflows, creating instruction conflicts or turning optional dependencies into requirements.

`capability-and-skill-routing.md` is the primary broker. This file defines how specialist methodologies cooperate after selection.

## Precedence
Use this order:
1. governing system/safety/user constraints;
2. SKick objective, evidence, action and verification contract;
3. explicit project-local instructions and the actual active host;
4. best task-matched installed/native specialist for the current phase;
5. trusted, configured MCP/tool provider for a required capability;
6. SKick-native fallback methodology.

A narrower specialist may own execution for its phase, but it does not override factual verification, version boundaries, permissions/action approvals, evidence provenance or the user's objective.

## Best-skill behavior
For substantial work, do not merely use the first known Skill. Compare plausible installed/native candidates by scope fit, project fit, capability quality, freshness, safety/provenance, testability, overlap and context cost. Keep one primary workflow owner per phase and a documented fallback when material.

If no installed specialist is strong enough and a missing specialist could materially improve the result, use `external-skill-intelligence.md` for current upstream evaluation. Do not silently install it.

## Superpowers
When `obra/superpowers` is installed and relevant, use its engineering workflow Skills for phases such as brainstorming/design clarification, planning/executing plans, TDD, systematic debugging, subagent execution, code review and completion verification.

Do not load both a Superpowers workflow and a duplicate SKick workflow at full detail. Map instead:
- Superpowers brainstorming/planning -> SKick research-backed context, constraints and architecture inputs;
- Superpowers TDD/debugging -> SKick red-capable feedback-loop evidence;
- Superpowers subagent workflows -> SKick task ledger/budget/evidence handoff;
- Superpowers review/finish -> SKick acceptance/evidence/provenance/remaining-risk gate.

If Superpowers is absent, use SKick planning, implementation discipline, feedback loops, orchestration and verification.

## Serena
Serena is a semantic code-intelligence provider, not a competing development methodology. For non-trivial repo/code work, apply the Serena-first gate from `serena-integration.md`; prefer it for symbols, references/call relationships, semantic repository exploration and targeted edits while retaining native git/shell/tests/browser/runtime tools for their jobs.

## Review/security specialists
When installed and task-matched, use dedicated review/security Skills (for example CodeRabbit-style review or security scanning/triage workflows) as narrow or independent passes. Reconcile findings against source, tests, threat model and project constraints; scanner/model agreement is not proof.

## Domain specialists
Use narrower data/analytics, document, infrastructure, cloud, database, incident, frontend/design or testing Skills when they materially improve execution. Pass only the compact task/evidence state required by that phase.

## Host-native specialist workflows
Some runtimes include strong built-in research, planning, review or orchestration workflows. Treat them as candidates in the same broker rather than suppressing them because SKick is present. The active host may own a phase when its capability is better and verifiable; SKick keeps cross-phase control.

## Conflict resolution
If two Skills disagree:
1. identify whether the conflict is factual, methodological or host-specific;
2. prefer current primary/project evidence for facts;
3. prefer the narrower specialist only within its declared scope;
4. preserve SKick safety/provenance/version/acceptance requirements;
5. run the smallest falsifiable test when practical;
6. record unresolved material conflict instead of silently merging incompatible instructions.

## Expanded specialist registry
Use `integrations/README.md` for optional providers and `integrations/catalog.json` for structured discovery. High-value categories include AI/ML, security, code review, frontend/browser, cloud/database, research and eval/harness specialists. Their phase ownership never overrides SKick evidence, safety, action or provenance gates.
