# Superpowers Integration

## Status
Optional first-class engineering workflow integration. Canonical upstream: `obra/superpowers` (MIT). It is not vendored into SKick.

## Why it fits
Superpowers supplies composable software-development workflows around brainstorming/design, implementation planning, TDD, systematic debugging, subagent-driven execution, code review, and verification-before-completion. SKick supplies broader current research, evidence/version intelligence, cross-domain reasoning, tool/MCP routing, provenance, safety, and long-horizon control.

## Runtime support
Re-verify current upstream instructions before install. At the 2026-08-21 verification point:
- Claude Code: official Claude plugin marketplace support is documented by upstream.
- Codex App/CLI: official Codex plugin marketplace support is documented by OpenAI/upstream.
- Upstream also documents current support paths for several other coding-agent hosts; use the actual runtime adapter rather than assuming one install format works everywhere.

## Invocation contract
When Superpowers is installed:
1. SKick researches and frames the real engineering problem, versions, constraints, mechanisms, risks, and acceptance criteria.
2. Delegate the relevant engineering-method phase to the matching Superpowers skill when it is narrower and useful.
3. Keep Serena/MCP/native tools as capability providers underneath the workflow.
4. Preserve SKick evidence lineage, action-safety, project constraints, provenance, and final confidence calibration.
5. Do not invoke redundant SKick and Superpowers TDD/debugging/planning manuals simultaneously.

When Superpowers is absent, SKick's native project planning, implementation discipline, feedback loops, multi-agent orchestration, review and completion gates provide the fallback.

## Conflict rule
Superpowers methodology is strong but not project ground truth. If its generic workflow conflicts with the repository's verified constraints, platform specifications, safety requirements, or explicit user intent, adapt the method rather than forcing the project to fit the workflow.
