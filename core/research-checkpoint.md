# Research Checkpoint and Resume

## Purpose
Preserve enough compact state for long-horizon research to resume after context compaction, tool handoff, or agent/runtime restart without rereading the entire research history.

## When to checkpoint
Create or refresh a checkpoint when any of these apply:
- the investigation is long-running, exhaustive, or likely to span a context boundary;
- a major phase completes (version resolved, root cause narrowed, implementation begins, validation completes);
- active context is being compacted;
- a subagent/runtime handoff is imminent;
- the host indicates restart, interruption, or session persistence risk;
- the user explicitly asks to save progress.

Do not checkpoint after every minor search. Prefer meaningful phase boundaries.

## Durable storage policy
Use the strongest persistence mechanism the runtime provides:
1. host-native persistent task/workspace state;
2. persistent file storage in a user/workspace-controlled area;
3. `.skick/checkpoint.md` in the workspace root when file writes are available and no better scratch location exists;
4. a compact resumable checkpoint in the visible response when durable storage is unavailable.

Never claim restart/session persistence unless the runtime actually provides it. Do not auto-commit checkpoint files to version control unless the user asks.

## Checkpoint schema
Keep the state compact and factual:

```text
CHECKPOINT_VERSION: 2
TASK_ID: <stable local identifier if available>
UPDATED: <timestamp if available>
GOAL: <one sentence>
MODE: QUICK | DEEP | EXHAUSTIVE
ENV: <runtime, OS, project/runtime/library versions that matter>
TERMS: <canonical terminology discovered>
CURRENT_CONCLUSION: <best supported conclusion or none>
VERIFIED_CLAIMS: <claim IDs + one-line statements>
OPEN_QUESTIONS: <ranked unresolved questions>
CONTRADICTIONS: <claim/source conflicts still unresolved>
KEY_SOURCES: <source IDs/URLs/files + what each proves>
PROJECT_ANCHORS: <files/symbols/tests/configs relevant to resume>
EVIDENCE_GRAPH: <path or compact node/edge summary>
COMPLETED_ACTIONS: <important searches/tests/edits already done>
TASK_LEDGER: <path/handle or none>
BUDGET: <remaining material limits or none>
TRACE: <trace handle or none>
NEXT_ACTION: <single highest-information next step>
STOP_REASON: <blank unless saturated/blocked>
```

Exclude duplicated prose, full search logs, copied documentation, dead hypotheses, secrets, credentials, and unnecessary personal data.

## Resume protocol
On resume:
1. load the latest checkpoint before broad searching;
2. verify that referenced project files/source versions still match the checkpoint where practical;
3. restore verified claims, open questions, contradictions, task-ledger/budget/trace handles, and the next action;
4. reload only the core modules required for the resumed phase;
5. continue from `NEXT_ACTION` unless new evidence invalidates it;
6. refresh the checkpoint after material progress.

Do not blindly trust stale checkpoints. If repository HEAD, dependency lockfiles, release state, or current external facts changed, mark affected claims stale and re-verify them.

## Handoff protocol
For another agent/subagent, pass only:
- goal and scope;
- relevant version/environment;
- verified claim IDs;
- unresolved contradiction/question IDs;
- strongest source/code/test anchors;
- next requested action.

The receiving agent should not receive the entire historical transcript unless necessary.
