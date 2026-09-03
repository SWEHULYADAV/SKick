# Durable Execution Ledger

## Purpose
Represent long-horizon work as resumable, machine-readable tasks rather than one prose "next action".

## When to use
Use for extended, multi-branch, multi-agent, failure-prone, or artifact-producing work. Keep simple tasks in normal compact state.

## Task model
Each material unit of work should be representable as:

```text
ID
PARENT
GOAL
STATUS: pending | ready | running | blocked | completed | failed | cancelled
DEPENDENCIES
ATTEMPT
INPUT_ANCHORS
OUTPUT_ARTIFACTS
EVIDENCE_IDS
BUDGET_ALLOCATED / BUDGET_USED
CREATED / UPDATED
RESUME_CURSOR
BLOCKER / ERROR
IDEMPOTENCY_KEY
```

Use `schemas/task-state.schema.json` for persistent JSON when file state is available.

## DAG rules
- dependencies must be explicit for branches that cannot safely run yet;
- independent branches may run in parallel;
- do not duplicate a completed task merely because context compacted;
- retries increment `ATTEMPT` and preserve the previous failure/evidence;
- terminal tasks are immutable except for annotations/corrections;
- a replacement task should link to the superseded task rather than rewriting history.

## Artifact rule
Outputs belong to tasks, not to chat turns. Record stable file/object handles, hashes when practical, and whether an artifact is intermediate or deliverable.

## Resume
On restart/compaction:
1. load ledger and latest checkpoint;
2. validate project/source freshness that could invalidate completed work;
3. recompute which tasks are `ready`;
4. resume the highest-information ready task within remaining budget;
5. preserve failed attempts and their evidence.

## Interoperability
When a host exposes task primitives (for example a runtime task API, MCP Tasks, or A2A Task), map the ledger fields to the host rather than inventing a second lifecycle. The canonical method remains host-neutral.
