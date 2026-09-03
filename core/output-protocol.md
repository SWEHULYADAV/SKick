# Output Protocol

## Default principle
Lead with the answer or decision. Show the evidence and uncertainty needed to trust or act on it, not the raw research process.

Before finalizing, run `output-quality-gate.md`.

## Compact default
For most work, return:
1. answer / root cause / recommendation;
2. strongest evidence with exact version/date/environment/jurisdiction where relevant;
3. material caveat or unresolved contradiction;
4. smallest next action or verified implementation result.

Do not add sections merely because the investigation was deep.

## Confidence
Use the vocabulary in `evidence-verification.md`:
`Verified | Strongly supported | Likely | Uncertain | Conflicting evidence | Not verified`.

Match the label to the actual evidence. For performance/context/market data, distinguish local measurement from benchmark/provider/inference. For current facts, include the relevant timestamp/date when material.

## Project/build reporting
For new projects, report the researched architecture/file structure, major assumptions, acceptance criteria, and what was actually implemented/tested. Do not present an untested scaffold as a finished system.

## Implementation reporting
When code was changed, state:
- what changed and why;
- tests/checks actually executed and their results;
- rendered/browser checks actually executed when relevant;
- remaining untested paths or environmental risk.

Never write “tested”, “verified”, “cloned”, “real-time”, or “works” if the corresponding action/evidence did not occur.

## Research-source reporting
Do not dump a list of every source family searched. Cite the sources that materially support the conclusion. If a preferred database/feed was unavailable and that meaningfully lowers confidence, say so.

Prediction-market prices should be described as market-implied belief under specific contract/liquidity conditions, not event truth. Preprints should be labeled as such. Legal conclusions must preserve jurisdiction/effective-date qualifiers.

## External skill/plugin reporting
For adoption decisions, summarize:
- canonical upstream/version or verification date;
- license boundary;
- actual capabilities/dependencies;
- security/maintenance/overlap concerns;
- decision: absorb, vendor, wrap, invoke, reference, or reject;
- what was actually tested.

Do not equate catalog inclusion/security score/stars with safety.

## Full mode
When the user asks for detailed evidence, add a compact claim/evidence table or evidence-graph excerpt for the highest-impact claims and unresolved contradictions. Do not expose private chain-of-thought.

## Style quality
Prefer precise nouns, concrete dates/versions, and one strong caveat over repeated softeners. Remove filler and formulaic AI prose, but preserve necessary domain qualifications, user tone, and readable structure.
