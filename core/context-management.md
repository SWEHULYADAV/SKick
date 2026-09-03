# Context Management

## Purpose
Preserve reasoning quality during long sessions by keeping large raw outputs out of the active prompt when the runtime provides safer indexed, file-backed, or persistent storage.

## Principle
`keep handles + evidence + exact critical excerpts; move bulk data out of active context`

Context compression must not weaken verification.

## Large-output routing
When tool output is large or repetitive:
1. Store or index the raw artifact using the strongest runtime-supported mechanism.
2. Keep a source handle/path/query plus a compact summary in active context.
3. Search/extract only the relevant ranges for the next decision.
4. Preserve exact code, commands, error text, numeric results, legal wording, or other load-bearing excerpts byte-for-byte when precision matters.
5. Re-open the raw source before a final high-impact claim if the compact summary could have lost nuance.

If the runtime has no indexed/out-of-band storage, use targeted reads and explicit compact checkpoints instead of pretending the data was persisted.

## Compaction and resume
Before compaction/restart risk, persist:
- goal;
- current version/environment;
- verified claim IDs;
- unresolved questions and contradictions;
- source/code/test anchors;
- edits already made;
- tests run and exact status;
- one next highest-value action.

On resume, verify repository HEAD, lockfiles, external freshness, and referenced artifacts before trusting the checkpoint.

## Privacy and secrets
Before persisting tool inputs/outputs outside active context:
- redact credentials, tokens, cookies, private keys, authorization headers, and unnecessary personal data;
- respect user/workspace boundaries;
- do not send private material to external compression/indexing services without explicit authorization;
- document telemetry or external storage when an optional integration uses it.

## Compression quality
Label quantitative savings claims as one of:
- **Measured locally**: observed in the current runtime/task.
- **Benchmarked**: from a documented reproducible benchmark.
- **Provider-reported**: from provider telemetry/counters.
- **Inferred**: estimated from size/token heuristics.

Never turn a third-party benchmark into a guaranteed saving for the current user.

## Tool/schema context
Large installed tool surfaces can consume context even when their schemas are irrelevant. When the host supports it, use `deferred-capability-loading.md`: keep a compact capability index, load only shortlisted Skill bodies/tool schemas, and invalidate cached schema choices when provider/version/capability snapshots change.

## Optional integrations
External context engines, proxies, MCP servers, and hooks can be wrapped when installed and trusted, but the canonical method must work without them. Re-verify current runtime support, feature flags, storage paths, telemetry, and license before installation guidance.
