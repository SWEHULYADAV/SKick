# Long-Horizon Research

## Principle
Do not optimize around arbitrary durations. Continue while new work materially resolves uncertainty, contradictions, version confidence, edge cases, security understanding, or implementation decisions. Stop at evidence saturation.

## Execution controls
For materially long or branched work, also load:
- `execution-ledger.md` for task DAG/state;
- `resource-budgeting.md` for token/time/tool/cost limits;
- `observability-and-tracing.md` when debugging the agent/workflow itself matters;
- `multi-agent-orchestration.md` when delegation is available.

## Goal and stop contract
Before extended autonomous work, define a compact completion contract:
- required deliverable/decision;
- load-bearing claims that need a confidence level;
- version/date/environment boundaries;
- required tests/reproductions/records, if any;
- acceptable residual uncertainty;
- explicit blockers that should stop implementation rather than invite guessing.

Use the contract as a judgeable finish line. Do not continue merely because more sources exist. If the runtime supports an independent reviewer, use a cold review near the end for high-impact work; resolve its objections with evidence rather than majority vote.

## Adaptive escalation
Start with the least expensive path capable of producing confidence:

`official docs + project evidence -> source/tests -> issues/PR/history -> deeper archives/alternatives/papers/production evidence`.

Escalate automatically when:
- documentation contradicts source/tests;
- versions disagree;
- maintainers disagree;
- a bug resists reproduction;
- security impact is unclear;
- implementation differs from documented behavior;
- strong community evidence contradicts official claims;
- consequences include security, data loss, authentication/authorization, payments, critical production migration, irreversible changes, or major dependency/architecture replacement.

## Parallel research
When the runtime supports parallel agents/tool calls and branches are independent, split bounded paths such as:
- official docs/skick;
- repository/source/tests;
- issues/PR/history;
- security/production evidence;
- alternatives/benchmarks.

Do not duplicate the same research across branches. Merge results using the evidence hierarchy.

## Subagent handoff
Use minimal bounded instructions:

```text
Goal:
Scope/version:
Sources to prioritize:
Return only:
- conclusion
- strongest evidence
- contradictions
- exact versions
- references
```

Do not give every subagent the entire research manual.

## Compact research state
Maintain only:
`G=goal, V=version/environment, T=terms, C=verified claims, U=unresolved questions, X=contradictions, N=next highest-value action`.

For larger work, short claim IDs reduce repeated context.

When a task DAG is active, the ledger is authoritative for branch status while the checkpoint summarizes only the current frontier and important evidence.

## Source compression
After reading a large source, retain:
`SOURCE / WHAT IT PROVES / VERSION / LIMITATION / FOLLOW-UP`.
Discard irrelevant prose, duplicated searches, and disproved hypotheses while preserving unresolved contradictions.

## Context compaction checkpoint
Periodically compress to:
- objective;
- current conclusion;
- verified facts;
- remaining uncertainties;
- versions/environment;
- relevant project files/symbols;
- important sources;
- next action.

## Saturation
Stop when core claims are supported, versions are known, important contradictions are resolved/documented, relevant edge cases are covered, negative searches no longer change the conclusion, and new query mutations are duplicative.

## Durable checkpoint / resume
For long work, use `research-checkpoint.md`. Persist compact state at meaningful phase boundaries and before context compaction/handoff/restart risk. Prefer host-native persistent state; otherwise use `.skick/checkpoint.md` when file writes are appropriate. Never imply persistence the runtime does not provide.

The checkpoint must preserve verified claim IDs, open questions, contradictions, strongest sources, relevant project anchors, completed validation, and one next highest-value action. Resume from that action after freshness/project-state checks rather than restarting broad research.

## Evidence graph during long work
For complex investigations, maintain `evidence-graph.md` so claims remain linked to source, version/environment, code/patch, test/reproduction, and contradictions across compaction boundaries.

## Frontier before saturation
Before declaring saturation, run `research-frontier.md`. If it reveals a material unanswered question, add it to the evidence graph/checkpoint and reopen the highest-information research branch. If two meaningful frontier scans yield no material insight, stop.

## Large-output context control
When long research generates large browser traces, logs, source dumps, datasets, or tool output, load `context-management.md`. Prefer indexed/file-backed storage where the runtime provides it; retain exact critical evidence plus compact source handles in the active checkpoint. Do not install an external context engine merely to satisfy this method.

## Durable orchestration references
For many independent tasks, use `harness-and-runtime-intelligence.md`: deterministic isolated workspaces, bounded concurrency, one authoritative ledger, retries/reconciliation and proof-of-work artifacts are preferable to one giant shared mutable agent session. Keep task objectives/invariants explicit while avoiding brittle over-scripted reasoning state machines.
