# Research Evidence Lifecycle

## Purpose
Make deep research auditable, uncertainty-aware and useful for downstream decisions by tracking what is known, what is inferred, what remains unexplored and what evidence would change the conclusion.

Use for Deep/Exhaustive research, architecture/security investigations, literature work, codebase archaeology, external-Skill evaluation, and any decision where source quality matters.

## Research-mode router
Classify the dominant evidence mode before searching:
- current web/product/runtime research;
- repository/code/history research;
- academic/systematic literature research;
- empirical/benchmark/experiment research;
- security/threat-intelligence/incident research;
- market/legal/financial/structured-data research;
- mixed-mode synthesis.

Each mode has different primary sources and verification standards. Do not use one generic source ladder for all of them.

## Knowledge frontier
Maintain a compact working map for long investigations:

```text
EXPLORED: area -> strongest evidence / confidence
PARTIAL: area -> known / unknown / blocker
UNEXPLORED: area -> why it may matter
KEY FINDINGS: claim -> impact / confidence
CONTRADICTIONS: claim -> competing evidence
OPEN QUESTIONS: question -> evidence needed
SIDE CLUES: clue -> hypothesis / status
```

Use the frontier to choose the next search. Do not repeatedly reread already-settled material unless new evidence invalidates it.

## Opened-source rule
A search snippet, catalog card, AI summary or citation list is discovery metadata, not read evidence. Do not claim that a source says something material unless the relevant source/unit was actually opened/read or a structured authoritative API returned the fact directly.

Follow promising discovery leads to the canonical source whenever practical.

## Claim ledger
For each load-bearing conclusion capture:

```text
Claim:
Scope/version/date:
Primary evidence:
Independent support:
Counterevidence / limitations:
Source lineage:
Confidence:
Inference vs direct observation:
What would flip or materially weaken this conclusion:
```

Do not expose private chain-of-thought; expose concise evidence, uncertainty and decision-relevant gaps.

## Independence over count
Ten articles repeating one press release are one evidence lineage, not ten confirmations. Weight sources by authority, directness, independence, recency/version fit and method quality.

Do not use a fixed source-count quota as a substitute for saturation. Stop when additional search mostly adds duplicated or low-value evidence and the material contradiction/frontier is resolved enough for the decision.

## Citation and provenance chasing
When a source makes a load-bearing claim:
- follow its cited origin/backward reference when accessible;
- inspect later corrections, successor specs, releases or forward references when recency matters;
- preserve the source/version/date boundary;
- note when an asserted origin cannot be verified.

Use bounded citation chasing: follow branches that can change the conclusion, not every reference in a bibliography.

## Counterevidence and flip conditions
Before finalizing a consequential conclusion, search for credible dissent, failed replications, regressions, exceptions, bypasses, alternative mechanisms, negative results and version-specific contradictions.

Explicitly ask: **what finding would make us choose differently?** If no plausible flip condition can be named, the analysis may be overconfident or the decision may already be dominated by a hard constraint.

## Code/repository research
For unfamiliar codebases, separate context building from verdicts:
1. structure and ownership;
2. data/state/control flow;
3. dependencies and integration seams;
4. invariants/assumptions/guarantees;
5. history and change hotspots;
6. target-specific investigation;
7. synthesis and remaining blind spots.

Prefer Serena semantic symbols/references when available, then file/line/test/history evidence. Naming resemblance is not proof of call flow.

## Academic/systematic research
When the task warrants a literature-style review:
- define inclusion/exclusion and date/version boundaries;
- search multiple relevant indexes/source families;
- distinguish peer-reviewed, preprint, benchmark, dataset, review and commentary;
- compare methods/populations/datasets/metrics before aggregating conclusions;
- organize synthesis by mechanism/theme/claim, not by a list of papers;
- identify consensus, dispute, quality limitations and specific research gaps.

Use PRISMA-style bookkeeping only when systematic coverage is actually requested/valuable; do not ritualize it for ordinary research.

## Evidence-to-SKill learning
When external research causes a durable SKick/Skill change, record:
- origin/canonical source;
- date/version inspected;
- mechanism adopted;
- what was deliberately not copied;
- license/provenance boundary;
- eval or failure mode that should protect the new rule.

A researched idea becomes a durable Skill rule only after it survives overlap/security/portability checks and has a plausible validation path.
