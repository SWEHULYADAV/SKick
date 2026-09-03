# Source Strategy

## Authority is claim-specific
Use the strongest source for the exact claim, not a universal website ranking. Load `research-source-router.md` to choose among software, academic, biomedical, market, regulatory, legal, government, transport/tracking, CERN, and patent sources.

A source named in the router is a preferred research destination, not a guarantee that the current runtime can query its API/database.

## General authority hierarchy
Use as a trust guide when the domain does not provide a more direct owner.

### Tier 1 - Normative / primary
- standards/specifications/RFCs/proposals;
- official documentation/API references;
- official source code and tests;
- regulators, statutory registers, filings, judgments, official datasets, trial registries, and drug labels for the facts they own;
- release notes/changelogs/migration guides;
- official security advisories.

### Tier 2 - Maintainer/institutional evidence
- maintainer issues/discussions, PRs, commits, design docs, architecture decisions, roadmaps;
- official engineering/research blogs and conference talks;
- institutional methods notes, committee reports, and official explanatory material.

### Tier 3 - Academic / experimental
- peer-reviewed papers and official research publications;
- preprints such as arXiv/medRxiv/bioRxiv when publication status is explicit;
- reproducible benchmark/experimental results.

### Tier 4 - Community / market sentiment
- Stack Overflow, Reddit, Hacker News, forums, mailing lists, technical blogs;
- prediction markets or other sentiment signals when the market belief itself is relevant.
Use for discovery/field experience; verify factual claims against stronger evidence. A market-implied probability is not ground truth.

### Tier 5 - Discovery-only / low authority
SEO/scraped/anonymous/AI-generated/unsourced summaries and catalogs without resolved upstreams. Use only to find leads.

## Lateral source evaluation
For unfamiliar or self-interested sources, do not judge trustworthiness only from the source itself. Leave the source, identify who is behind it, find better coverage, and trace important claims/quotes/media to their original context. See `coverage-and-lateral-search.md`.

## Discovery is not verification
A weak source may reveal terminology, an issue number, candidate skill, workaround, paper, filing, or event. Follow the lead into stronger evidence whenever possible.

For external skills/plugins, catalogs are discovery only. Load `external-skill-intelligence.md` and resolve the real upstream, version, component-level license, actual scripts/capabilities, security posture, and maintenance before adoption.

## Documentation and implementation coverage
Inspect the official documentation/navigation, concepts, API, configuration, examples, troubleshooting, limitations, compatibility, migration, deprecation, release/security material, and relevant cross-references. Do not read unrelated pages for volume.

When docs are ambiguous or contradicted, inspect implementation, defaults, conditionals, flags, environment checks, validation, error/retry/fallback paths, compatibility shims, platform branches, and tests. Treat tests as executable documentation for edge cases and regressions.

## Domain-specific primary records
Match the claim to its owner. Examples:
- software behavior -> matching version of source/tests/releases;
- company financials -> issuer/regulatory filing and reporting period;
- clinical trial state -> registry record plus results/publication where applicable;
- US drug labeling -> current/relevant DailyMed/FDA label source;
- UK law -> legislation/judgment effective on the relevant date;
- macro series -> originating statistical agency and exact series vintage/definition;
- patent status -> official jurisdiction/family records;
- current market price -> timestamped venue/feed, not an undated article.

## History and rejected designs
Use commits, blame, tag diffs, old branches, archived docs, issue/PR discussions, rejected proposals, `won't fix`/`not planned`, amendments, corrections, retractions, or superseded records when history affects the conclusion.

## Papers and experiments
Inspect methodology, dataset, baselines, environment, limitations, reproducibility, code/data, peer-review status, corrections/retractions, and later work. Do not promote a preprint or single experiment into a universal production/clinical fact.

## Production and operational evidence
Use engineering blogs, incident reports, postmortems, RCAs, migrations, regulatory notices, and compatible benchmarks for operational lessons. Distinguish system-specific incidents from general limitations.

## Package/registry and maintenance evidence
When evaluating dependencies, inspect registry metadata, release history, maintainers, runtime requirements, transitive dependencies, license, deprecated/archived status, recent activity, issue/PR responsiveness, security response, governance/ownership changes, and package provenance. Popularity alone is not quality.

## Compatibility and benchmarks
Do not generalize compatibility or benchmarks without matching version, OS, architecture, runtime, configuration, workload/dataset, hardware, units, and time window where material.

## Non-GitHub and non-English ecosystems
Use the project's actual tracker/registry/standards body/court/government source even if it is GitLab, Jira, Bugzilla, vendor portals, national statistics, working groups, mailing lists, or non-English official material. Translate carefully but preserve original definitions.

## Search hygiene
Never use search snippets, titles, AI summaries, stars, download counts, copied excerpts, accepted answers, marketplace badges, or automated security scores as sufficient evidence by themselves.

## Source-value heuristic
Prioritize approximately by:
`relevance x authority x version/date match x specificity x freshness x direct ownership`.
A current matching regression test, filing, trial record, judgment, or statistical release can be more valuable than many generic summaries.
