# Harnesses and Evaluation Backends

## OpenAI Harness Engineering / Symphony
Absorb the repository-as-system-of-record, agent-legibility, mechanical invariant and recurring quality-maintenance principles from OpenAI's Harness Engineering work. For durable task orchestration, Symphony's per-task isolated workspaces, bounded concurrency, reconciliation, repo-owned workflow contract and proof-of-work model are strong references.

Do not make the experimental Symphony daemon a core dependency. Use its spec/design patterns when the host needs durable autonomous task orchestration.

## mini-SWE-agent
Use as the reference for harness minimalism: a compact linear trajectory and a small reliable action surface can be easier to debug and benchmark than a large framework. Escalate only after identifying a concrete missing capability.

## Open SWE / Deep Agents
Use as references for isolated per-task sandboxes, curated tools, durable state, context-isolated subagents, read-only reviewer separation and keeping credentials/control-plane state out of the execution sandbox when possible.

## Pydantic AI / Harness
Use as references for typed tool/result contracts, modular/deferred capabilities, durable execution, exact subagent budgets, human approval interrupts and stable capability/tool IDs. Approval is not a substitute for authorization.

## Inspect AI / Inspect Evals
Use as an optional external evaluation backend for model/agent behavior. Pin harness, eval package, task/dataset, scorer and environment versions. Inspect task validity and trajectories before interpreting scores.

## Harbor / Terminal-Bench
Use as an optional isolated coding-agent benchmark backend. Verify the environment/oracle first, pin benchmark revision/container/harness and keep cost/token/time/trajectory records. Benchmark fixes can change scores; do not compare across incompatible revisions.

## Compound Engineering and other workflow plugins
May serve as optional phase owners when installed and narrower than SKick. Do not run a second full control plane beside Superpowers/SKick; select one workflow owner and retain SKick evidence/safety/provenance gates.
