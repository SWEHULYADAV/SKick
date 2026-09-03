# Token and Context Efficiency

## Principle
Optimize for `minimum active context + maximum relevant evidence`. Efficiency removes duplication; it never permits weaker evidence or skipped verification.

Load `context-management.md` when raw tool output, long documents, browser traces, or long sessions threaten the context window.

## Progressive disclosure
Keep `SKILL.md` small. Load only modules required by the current task branch. Do not repeatedly reload or restate modules already understood unless the task materially changes.

## Compact task state
Use:
`G=goal, V=version/date/environment, T=terminology, C=verified claims, U=unresolved, X=contradictions, N=next highest-value action`.

Use short claim IDs for large investigations.

## Query batching and funnel
Batch query families:
`broad discovery -> canonical terminology -> authoritative source -> highest-value reads -> linked evidence -> verification`.
Do not deeply read many pages before knowing which matter.

## Targeted reading
For long docs, use navigation/TOC/find/headings/API index and then read relevant sections plus a lightweight coverage scan.

For repositories, start from symbol/error/API/config/test/commit and expand definition -> references -> dependencies -> tests -> history.

For structured sources, fetch only the relevant series/filing/trial/record/date range rather than importing an entire dataset into the prompt.

## Keep raw output out of active context
When the runtime provides indexed/file-backed storage, retain large raw outputs there and keep in active context only:
- source handle/location;
- what it proves;
- version/date/environment;
- exact critical excerpts/values needed for the claim;
- limitation/follow-up.

Never compress away error text, code spans, numeric values, legal language, contract resolution criteria, or other evidence whose exact form is load-bearing.

## Deduplication
When many sources repeat a fact, keep the strongest representative source. Community/catalog repetition matters only when prevalence itself is relevant.

## Research memory
Reuse verified versions, terminology, repository URLs, series/filing identifiers, sources, and conclusions within the current task unless conflicting or fresher evidence appears.

## No raw research dump by default
Do not show every query, page, failed search, hypothesis, repeated source, or copied documentation. Default output: answer, strongest evidence, caveat, action, sources.

## Research depth != response length
Deep research can produce a compact answer. Output density:
- COMPACT default;
- STANDARD structured summary;
- FULL detailed evidence trail when requested.

## Claims about efficiency
Label context/performance savings as `Measured locally`, `Benchmarked`, `Provider-reported`, or `Inferred`. Do not convert vendor claims or a small benchmark into a universal measured result.

## Never sacrifice evidence
Do not skip version/date verification, contradictions, relevant tests, or primary evidence merely to save tokens.

## Checkpoint instead of transcript retention
For long work, use `research-checkpoint.md` rather than retaining the full transcript. Keep the evidence graph sparse and store only verified claims, unresolved questions/contradictions, strongest evidence, project anchors, completed actions, and the next highest-value action.
