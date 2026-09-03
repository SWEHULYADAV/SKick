# Evidence Graph

## Purpose
For complex investigations, maintain traceability as a graph rather than a flat source list. Connect conclusions to the exact version, implementation, test, contradiction, and project context that support or weaken them.

## Graph model
Use compact typed nodes:

```text
C# = claim
S# = source/document/advisory/paper
V# = version/tag/branch/environment
K# = code symbol/file/commit/patch
T# = test/reproduction/benchmark
X# = contradiction/counter-evidence
L# = lineage/derivation relation
Q# = open question
A# = action/decision
```

Use explicit edges such as:

```text
S1 --supports--> C1
S2 --contradicts--> C1
C1 --applies_to--> V2
K3 --implements--> C1
T4 --verifies--> C1
X1 --challenges--> C1
S2 --derived_from--> S1
S3 --independent_replication_of--> S1
C1 --depends_on--> C2
Q2 --blocks--> A1
```

## Minimum node metadata
Retain only information needed to audit the conclusion:

```text
ID:
TYPE:
SUMMARY:
VERSION/ENV:
LOCATION: <URL, file/symbol, commit, test, or citation handle>
STATUS: verified | strong | likely | uncertain | conflicting | stale
```

## Construction rules
- Create graph nodes only for material claims and evidence; do not graph every trivial fact.
- Reuse existing nodes instead of duplicating equivalent evidence.
- Attach version/environment nodes whenever a claim is version-sensitive.
- Link documentation claims to source/tests when implementation evidence exists.
- Link fixes to patch commits and regression tests when available.
- Preserve contradiction nodes until resolved; never delete disagreement merely because one source is preferred.
- Mark superseded or stale nodes rather than silently overwriting history when it matters.

## Traceability gate
Before treating a complex conclusion as Verified or Strongly supported, be able to answer:
- Which source(s) support it?
- Which version/environment does it apply to?
- What source code or implementation path realizes it, if relevant?
- What test/reproduction validates it, if relevant?
- What credible contradiction exists?
- What project-specific evidence changes its applicability?

If an important edge is missing, lower confidence or research that gap.

## Independence and lineage
Load `evidence-lineage.md` when multiple sources may share one origin, dataset, press release, benchmark, or syndicated report. Raw citation count must not inflate confidence.

## Storage
For long-horizon work, prefer a durable compact graph at `.skick/evidence-graph.md` or host-native persistent state. If persistence is unavailable, keep the graph in compressed internal task state and expose only the user-relevant trace in the final answer.

Do not auto-commit research-state files unless asked.

## Final-answer use
Do not dump the full graph by default. Use it to produce concise claim-to-evidence traceability. In FULL mode, include a compact evidence table or graph excerpt for the highest-impact claims and unresolved contradictions.
