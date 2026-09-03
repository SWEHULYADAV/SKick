# Implementation Discipline

## Purpose
Reduce common agent coding failures: silent assumptions, overengineering, collateral edits, and unverifiable completion.

## Research before plan before code
For a new project or major redesign, first inspect the domain, platform/runtime, comparable patterns, constraints, and user workflow. Then define architecture/UI/file structure and success criteria. Only then implement. Small low-risk scripts may use a lightweight version of this gate.

## Think before editing
Before a non-trivial change, establish a compact execution contract:
- requested outcome;
- important assumptions;
- constraints and compatibility boundaries;
- success criteria that can be checked;
- smallest likely change surface.

Do not ask the user to resolve information that the repository, tests, docs, or current research can answer. If a material ambiguity truly cannot be resolved, state it concisely and choose the safest reversible path when the task must proceed.

## Simplicity first
Solve the current requirement. Avoid:
- speculative flags or configuration;
- generic frameworks for one concrete use;
- extra abstraction layers without a second real consumer;
- premature performance machinery;
- broad rewrites when a local fix is sufficient.

Complexity is justified only when it removes a demonstrated risk, duplication, coupling, or requirement gap.

## Surgical changes
Every changed line should trace to one of:
- the requested behavior;
- the verified root cause;
- a required regression test;
- necessary compatibility/security handling;
- cleanup made obsolete directly by the change.

Preserve surrounding style and public behavior unless the task explicitly requires otherwise. Avoid drive-by formatting, unrelated renames, dependency churn, or opportunistic refactors.

## Goal-driven execution
Convert vague imperatives into observable completion criteria internally. Examples:
- "fix the bug" -> a reproduction goes red before and green after;
- "add validation" -> invalid cases fail with the specified behavior and valid cases remain green;
- "refactor" -> behavior/tests remain unchanged while the target design property improves.

Loop on evidence until the criteria are met or a real blocker is identified.

## Verification before confidence
Prefer evidence from tests, type/build/lint checks, runtime behavior, or source/spec comparison. Do not call a change complete because it compiles, looks plausible, or matches an architectural pattern.
