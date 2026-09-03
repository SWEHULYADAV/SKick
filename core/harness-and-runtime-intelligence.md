# Harness and Runtime Intelligence

## Purpose
Choose and shape the execution harness around the task instead of assuming that more agents, tools, persistence, or orchestration always improve results.

## Harness-selection rule
Start with the smallest loop that can satisfy the completion contract:

`single agent + native tools -> specialist capability -> isolated task workspace -> bounded subagents -> durable orchestrator`

Escalate only when evidence shows a need for parallelism, long-lived state, isolation, retries, human approval, independent review, or cross-service coordination.

## Harness properties to inspect
For an external or host harness, resolve:
- task/workspace isolation and lifecycle;
- shell/browser/network/filesystem permissions;
- credential plane versus execution data plane;
- context/history model and compaction behavior;
- tool/capability discovery and deferred loading;
- subagent isolation, depth and concurrency limits;
- task IDs, stable capability/tool IDs and resumability;
- retries, timeouts, cancellation and reconciliation;
- human interrupts/approvals;
- structured outputs and schema validation;
- traces, trajectories, cost/token/time usage;
- proof-of-work artifacts and final verification.

## Minimal-harness discipline
A small append-only trajectory with a few reliable tools is often easier to debug than a rich autonomous framework. Do not add planning agents, memories, graphs, routers or tool servers merely because they exist. Measure the failure mode first.

## Durable-work discipline
For multi-hour or multi-task work, prefer:
- deterministic per-task workspaces;
- bounded concurrency;
- one authoritative task ledger;
- idempotent/reconcilable transitions;
- explicit stop/failure reasons;
- stable task/tool/capability identifiers;
- proof of work such as tests, CI, review evidence or reproducible artifacts.

Keep secrets in the control plane when possible; inject the least credentials into isolated execution environments.

## Objective over brittle state machines
Define the desired outcome, invariants, acceptance checks and boundaries. Use state machines for safety/recovery where they add value, but do not over-script every reasoning step when the agent can navigate the objective with stronger feedback.

## Harness references
Use `integrations/harnesses-and-evals.md` for OpenAI Symphony/Harness Engineering, mini-SWE-agent, Open SWE/Deep Agents, Pydantic AI Harness and related references. External harnesses are optional; SKick's canonical method must work without them.
