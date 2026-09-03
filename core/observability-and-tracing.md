# Observability and Tracing

## Purpose
Make long and multi-tool investigations debuggable without dumping private reasoning or huge raw logs into context.

## Trace model
A substantial run may expose a trace containing spans/events for:
- framing/version/source routing;
- search/read operations;
- repository/file/code inspection;
- subagent delegation/handoff;
- tool calls and retries;
- browser/reproduction/test runs;
- edits/build/package operations;
- checkpoints/compaction;
- approvals/rollback;
- final validation.

Use `schemas/trace.schema.json` for a portable local representation when persistent files are appropriate.

## Minimum observability fields
Where the runtime exposes them, record:
`trace_id, span_id, parent_span_id, task_id, operation, start/end, status, tool/provider, source/artifact handles, retry_count, error_class, token/input/output usage, cache usage, latency, external cost, and verification outcome`.

Do not fabricate counters a provider/runtime does not expose. Label estimates separately.

## Events vs spans
Use a span for an operation with duration and nested work. Use an event for a meaningful point such as state transition, checkpoint, approval, budget threshold, retry decision, or exception.

## Privacy
Do not log raw credentials, cookies, authorization headers, private keys, sensitive secrets, or unnecessary personal data. Prefer hashes/handles/redacted fields for sensitive artifacts.

## Context efficiency
Trace storage is out-of-band evidence. Active context should retain only anomalies, current budget, important failure events, and handles required for the next decision.

## Runtime mapping
If the host supports OpenTelemetry or native agent tracing, map to it. If not, a compact JSONL trace is sufficient. Observability is optional for simple tasks but should be enabled for difficult/repeated failures when available.

## Trajectory diagnostics
When evaluating the engineering harness itself, retain a compact action trajectory or trace handle sufficient to classify failures by interpretation, retrieval/context, tool routing, action, recovery, verification and stop reason. Aggregate metrics alone can hide the mechanism of a regression; use `evaluation-harness-integration.md` for benchmark/eval analysis.
