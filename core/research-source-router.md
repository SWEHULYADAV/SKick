# Research Source Router


## Executable-runtime ownership
`runtime/research.py` provides the machine-readable initial source hierarchy and source classes when the full runtime is available. Use this module for domain nuance, dynamic source selection, and host-specific research execution after planning. A selected source class is a plan, not evidence that the source was opened.
## Purpose
Route each claim to the highest-value source family instead of searching every source mechanically. Source availability depends on the runtime; never imply access to a database, feed, subscription, or API that is not actually available.

## Routing rule
Use:

`question -> claim type -> authoritative source family -> current/version check -> corroboration -> contradiction pass`

Search only source families that can materially change the answer. For current facts, prefer structured/current data tools when available and confirm timestamps, units, exchanges, jurisdictions, study status, or effective dates.

## General web and software
- General web search: discovery, current events, vendor docs, standards, public records, and cross-checks.
- GitHub and other source forges: source code, tests, releases, tags, issues, pull requests, discussions, commits, security advisories, manifests, and CI. For software behavior, source and tests outrank tutorials.
- Registries and package indexes: version history, dependency metadata, release cadence, provenance, deprecation, and runtime constraints.
- Archives: historical docs, removed behavior, old tags, old standards, and superseded guidance. Label historical evidence explicitly.

## Academic and research literature
For evidence synthesis or experimental claims, also load `empirical-research-methodology.md`.
Use the source closest to the claim:
- arXiv: preprints and technical discovery. Verify peer-reviewed publication when publication status matters.
- PubMed: biomedical literature index. Follow through to the paper, journal, retraction/correction status, methods, and date.
- medRxiv and bioRxiv: preprints. Treat as non-peer-reviewed unless a later publication is verified.
- CERN Open Data and CERN publications: particle physics datasets, reproducibility artifacts, and experiment documentation.
- Patents: WIPO PATENTSCOPE, EPO/Espacenet, USPTO, and jurisdictional registers. Google Patents may help discovery, but legal status and family data should be verified against official registers.
- Crossref/OpenAlex/Semantic Scholar: discovery, DOI/metadata linkage, citation graph exploration, and literature mapping. Follow important claims to the publisher/paper and check corrections, retractions, and publication status.
- Retraction/correction signals: Crossmark, publisher correction/retraction notices, PubMed status, and Retraction Watch-style discovery where available. A citation count is not a validity score.

## Clinical, drug, and biomedical data
Load `biomedical-and-health-research.md` for mechanism/evidence-level/benefit-risk interpretation.
- ClinicalTrials.gov: trial registration, status, protocol fields, and posted results. Registration is not proof of efficacy.
- DailyMed: current US drug labeling and label history. Distinguish label claims from independent clinical evidence.
- WHO health sources: global health statistics, guidance, surveillance, and classifications.
- WHO ICD: classification codes and revisions; resolve the exact ICD release/version.
- ChEMBL: bioactivity and compound-target data; verify assay context and release.
- PubChem: compound, assay, substance, and identifier data; separate depositor records from curated interpretations.
- DrugBank: drug/target/interactions reference when the runtime/user has lawful access. Respect licensing and do not assume unrestricted redistribution.
- Open Targets: target-disease evidence integration; inspect evidence type and data release.
- NPI Registry: US provider identifiers and registry fields. Do not treat registry presence as a quality or credential endorsement.
- NIH RePORTER / NIH research grants: grants, projects, investigators, organizations, and funding history.
- FDA, EMA, CDC, NICE, MHRA, and other relevant regulators/public-health bodies: approvals, safety communications, recalls, guidance, labels, and public-health recommendations. Match jurisdiction and effective date.
- FAERS/EudraVigilance-style spontaneous safety reports: signal-generation evidence only; reports do not establish incidence or causation without stronger analysis.

For high-stakes medical claims, triangulate guidelines/regulators, peer-reviewed evidence, trial data, labeling, and safety updates. Preprints, observational associations, and mechanism data do not by themselves establish clinical effectiveness.

## Securities, companies, and markets
Load `financial-and-economic-research.md` for point-in-time/accounting/market-mechanism discipline and `structured-data-quality.md` for quantitative datasets.
For prices and market state, prefer a runtime's current market/quote source when available, then exchange or issuer sources. Always carry timestamp, currency, venue, and whether values are delayed, real-time, adjusted, or indicative.

Source families:
- Stock prices and market movers: exchange/market data feeds, issuer data, and reputable structured market sources.
- Crypto: exchange-specific markets plus protocol/on-chain primary data when relevant. Name the venue because prices vary.
- Forex: institutional/central-bank reference rates for reference values; market feeds for tradable quotes. State base/quote pair and timestamp.
- Commodities: exchange/futures data, benchmark administrators, government statistics, and spot references as appropriate.
- ETFs and mutual funds: issuer prospectus/fact sheets, SEC filings, portfolio reports, NAV/history, and exchange data.
- Earnings and company stats: issuer investor relations, exchange notices, SEC filings, and earnings materials.
- Balance sheets, income statements, cash flow, and dividends: audited/official filings first; structured aggregators are convenience layers, not primary evidence.
- SEC filings: EDGAR filings and exhibits. Resolve filing form, accession/date, reporting period, amendments, and inline XBRL where useful.
- Insider transactions: SEC Forms 3, 4, and 5 and issuer filings. Distinguish grants, exercises, gifts, planned sales, and open-market trades.
- US market/regulatory context: FINRA, CFTC, CME/ICE/Nasdaq/NYSE and other relevant exchanges or benchmark administrators for rules, market notices, futures/options, short-interest, or contract specifications.
- Treasury/FiscalData and central-bank sources: official rates, yields, auctions, balances, reference rates, and monetary-policy data where those facts are the claim.

Do not infer investment merit from a single price move, insider transaction, prediction market, or social signal.

## Prediction markets
- Polymarket and Kalshi can provide market-implied probabilities and event-contract sentiment.
- Treat prices as market beliefs under specific contract rules, liquidity, fees, participant constraints, and resolution criteria, not objective truth.
- Read the exact contract/resolution language before using a probability as evidence.
- Compare with polling, primary event data, forecasts, or other independent evidence when the conclusion matters.

## Macroeconomic and public finance data
- BLS: US labor, CPI/PPI, productivity, employment, wages, and related series. Track revisions and seasonal adjustment.
- FRED: convenient aggregation of economic series. When provenance matters, follow the series back to its originating agency.
- USAspending.gov: US federal awards and spending data. Reconcile award, obligation, outlay, and fiscal-year semantics.
- World Bank: development indicators and country metadata; inspect indicator definitions and revision dates.
- IMF: WEO, IFS, fiscal, balance-of-payments, and related datasets. Match vintage and methodology.
- German labor: Bundesagentur fuer Arbeit, Destatis, BMAS, and other official German statistical/labor sources. Match definition, seasonality, and geographic scope.
- US BEA and Census: national accounts, GDP, trade, income, population, business, housing, and demographic data when they own the series.
- Eurostat, ECB, OECD, ONS, Bank of England, Bundesbank, and other national statistical/central-bank sources: prefer the originating institution for definitions and revision history.

## UK legal and parliamentary research
Load `legal-policy-and-patent-research.md` for authority/effective-date/procedural discipline.
- UK case law: prefer The National Archives Find Case Law and court/judiciary sources; use BAILII or commentary for discovery and context when appropriate.
- UK legislation: legislation.gov.uk and official amendment/commencement material. Verify the version in force on the relevant date.
- UK Parliament: parliament.uk, bills, committee reports, Hansard, written questions, publications, and voting records.

For legal questions, jurisdiction, court level, effective date, amendments, procedural posture, and whether a source is authoritative are load-bearing facts.

## Transport and tracking
For structured feeds, timestamps, joins, or revisions also load `structured-data-quality.md`.
- UK rail: Network Rail open data, National Rail data/services, ORR statistics, operator notices, and timetable/disruption feeds as available.
- Ship tracking: AIS and port/coast-guard/registry sources where available; commercial AIS services may be useful but can be delayed or access-restricted. Never imply live location if the runtime only has stale/public snapshots.


## Software security and supply-chain sources
When the research question touches vulnerabilities, dependency risk, malicious packages, or exploitability, prefer:
- project security advisories and patched source/tests;
- GitHub Security Advisories / OSV for package-to-version mapping;
- NVD/CVE records for identifier/status context, not as a substitute for vendor analysis;
- CISA KEV for known-exploited status where applicable;
- package registry provenance, release signatures/attestations, lockfiles, SBOMs, and maintainer ownership/history.

Separate `vulnerable version`, `reachable code path`, `exploitable configuration`, and `observed exploitation`; they are not interchangeable.

## Standards, policy, and official records
For standards/protocols/policy questions, route to the body that owns the rule: IETF RFCs, W3C/WHATWG, ISO/IEC where lawfully accessible, language/runtime proposals, regulator rulebooks, government gazettes, standards bodies, or official consultations. Distinguish normative text from drafts, proposals, explanatory notes, and commentary.

## Source conflict rules
When two sources disagree:
1. Compare timestamp, version, reporting period, release vintage, jurisdiction, venue, and definitions.
2. Prefer the source that directly owns the fact (regulator, filing, exchange, trial registry, official dataset, source code/test).
3. Preserve material disagreement in the evidence graph.
4. Do not average incompatible definitions to manufacture agreement.

## Access and licensing rule
A source being named here means it is a preferred research destination, not that every runtime can query it directly. Respect authentication, subscriptions, robots rules, data licenses, rate limits, API terms, and redistribution restrictions.


## Environment, climate, energy, and geospatial
Route to the organization that owns the observation/model/record: NOAA, NASA, USGS, EPA, EIA, Copernicus/ECMWF, IPCC assessments, national meteorological/geological/environmental agencies, grid/system operators, energy regulators, and official satellite/geospatial datasets as appropriate. Track spatial resolution, coordinate reference system, observation/model vintage, forecast lead time, uncertainty, station/sensor changes, and revision/reanalysis status.

## US, EU, and international legal/regulatory sources
For US federal law/policy use Congress/GovInfo, Federal Register/eCFR, official agency rulemaking/guidance, and court sources such as Supreme Court/federal judiciary repositories as appropriate. For EU law use EUR-Lex, CURIA, Commission/Parliament/Council and regulator sources. For treaties/international rules use the responsible treaty organization/depository. Always resolve jurisdiction, authority, effective date, amendments, and whether material is binding, draft, guidance, or commentary.

## Trade, energy, and global public data
When relevant use originating public sources such as UN/UN Comtrade, WTO, IEA or national energy/statistical agencies, customs/trade authorities, and central banks. Match definitions, reporting lag, revisions, currency/unit, geography, and coverage before comparison.
