# Coverage, Lateral Search and Lateral Thinking

## Purpose
Find important clues, mechanisms and better ideas that narrow keyword matching misses, without turning research into unbounded browsing.

For non-trivial research, lateral work is a core pass rather than an optional afterthought.

## Three complementary directions
Use the minimum combination that closes the evidence gap:

- **Vertical coverage** — read the relevant source deeply enough to understand definitions, surrounding context, exceptions, footnotes, tests, comments, examples, configuration and cross-references.
- **Lateral search** — leave the current source and investigate alternate names, origins, independent sources, adjacent ecosystems, implementations, failures and historical context.
- **Lateral thinking** — use newly found clues to generate alternative mechanisms, analogies, design possibilities and falsifiable questions that were not obvious from the user's initial wording.

A polished page, README, paper, issue, forum post or vendor blog is evidence to inspect, not authority merely because it looks authoritative.

## Terminology lattice
Build a compact evolving lattice around the user's wording:

`user term <-> canonical term <-> old name <-> new/trendy name <-> acronym/full form <-> implementation symbol <-> behavior/symptom <-> competitor term <-> adjacent-domain analogue <-> translated/localized term`

Search laterally when any of these are plausible:
- a feature was renamed/rebranded or superseded;
- a trendy term wraps an older mechanism;
- maintainers use internal terminology different from users;
- competitors implement the same concept under another name;
- an error describes the symptom but not the mechanism;
- a paper uses academic terminology while production systems use engineering terminology;
- the important source is in another language, jurisdiction or ecosystem.

## Lateral query moves
Choose moves with plausible information gain:

1. **Name drift** — renamed, deprecated, legacy, formerly, successor, replacement, alias.
2. **Mechanism-first** — search what the system does, not what the feature is called.
3. **Symptom-first** — observable failure, timing, error text, output shape, state transition.
4. **Implementation-first** — symbols, config keys, protocol fields, filenames, test names.
5. **Neighbour ecosystem** — analogous feature in another framework/language/vendor.
6. **Historical** — old docs, tags, archived terminology, rejected proposals, migrations.
7. **Negative** — unsupported, limitation, failure, regression, won't-fix, edge case.
8. **Source-authenticity** — owner, maintainer, publisher, canonical upstream, mirror/fork lineage.
9. **Trace-to-origin** — quote, statistic, benchmark, chart, claim, code snippet or media back to the earliest reliable source.
10. **Cross-language** — translated technical/legal/scientific terms when regional evidence may differ.
11. **Operational evidence** — issue threads, postmortems, changelogs, migration notes, production examples, support forums.
12. **Test/example inversion** — infer hidden expectations from fixtures, examples and failure tests, then verify them against source/docs.

## Lateral-thinking loop
After a meaningful clue, ask internally:
- What else could explain this observation?
- What assumption did this source make that the user/project may not share?
- Is the same mechanism solved differently in an adjacent ecosystem?
- What failed/rejected approach reveals a hidden constraint?
- What small detail changes the architecture, security, compatibility or operational conclusion?
- What useful design idea follows from this evidence even if it was not the original query?

Turn answers into **testable research branches**, not unsupported conclusions. Ideas are candidates; facts require evidence.

## Serendipity / side-clue ledger
For Deep/Exhaustive work, keep a tiny side-clue ledger outside the main narrative when possible:

```text
CLUE | WHY IT MAY MATTER | NEXT CHECK | STATUS
```

Capture only material clues: surprising defaults, undocumented flags, maintainer rationale, odd tests, migration caveats, competing implementations, security boundaries, performance trade-offs, or reusable design ideas. Promote a clue into the main conclusion only after verification or clearly label it as a hypothesis/opportunity.

## Full relevant reading pass
After targeted discovery identifies a high-value source, read the **full relevant unit**, not only the matching snippet:
- complete function/class/module when behavior depends on surrounding control flow;
- complete relevant test file/fixture when tests define intended behavior;
- complete issue/PR discussion when maintainer rationale matters;
- complete relevant paper sections including methods/limitations/appendices when load-bearing;
- complete legal provision plus definitions/amendments/controlling authority when applicable;
- complete filing section/footnotes when accounting context matters;
- documentation navigation neighborhood and linked limitation/migration pages.

Do not equate "full relevant unit" with "read everything." Expand the boundary when new evidence reveals a dependency, contradiction, hidden assumption or meaningful adjacent clue.

## Small-clue sweep
Before closing a Deep/Exhaustive branch, inspect likely clue-bearing surfaces:
- defaults and fallback branches;
- comments/TODO/FIXME/deprecation notes;
- fixtures and odd edge-case tests;
- examples using undocumented arguments;
- changelog footnotes and migration notes;
- issue/forum discussions around the exact mechanism;
- error strings and warning text;
- feature flags/environment gates;
- benchmark setup and excluded cases;
- paper appendices/supplementary material;
- filing footnotes/reconciliations;
- chart axes/legends/notes;
- license/readme differences between root/subdirectories.

## Exploration budget and stopping
Lateral thinking is not permission for infinite research. Prioritize branches by expected information gain and consequence. Stop or park a branch when:
- repeated sources add no new material mechanism/constraint;
- the branch cannot change the decision or confidence meaningfully;
- evidence saturation is reached;
- the explicit budget/finish condition is met.

Run a bounded final frontier scan for Deep/Exhaustive work to catch one last plausible adjacent mechanism or negative case.

## Independence check
Multiple pages repeating the same upstream claim are one evidence family, not independent corroboration. Link downstream copies to the originating source using `evidence-lineage.md`.

## Context efficiency
Use search/indexing to locate candidate units, then read important units completely. Store bulk text outside active context when possible and retain source handles plus exact load-bearing excerpts.
