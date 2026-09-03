# Evidence Lineage and Independence

## Purpose
Distinguish many URLs from many independent evidence origins.

## Lineage edges
Extend the evidence graph with relationships such as:

```text
S2 --quotes--> S1
S3 --syndicated_from--> S1
S4 --derived_from--> S1
S5 --mirrors--> S1
S6 --same_dataset_as--> S1
S7 --independent_replication_of--> S1
```

## Independence rule
Ten articles that repeat one wire report, press release, benchmark, registry record, or vendor claim are not ten independent confirmations.

For important claims, identify:
- earliest/canonical source;
- primary data/record owner;
- transformations/aggregators;
- genuinely independent measurement/replication;
- conflicts introduced by different definitions, dates, or samples.

## Claim counting
Confidence should depend on source quality and independence, not raw citation count.

## Provenance
Use `schemas/evidence-lock.schema.json` for durable source records when reproducibility matters. Preserve URL/identifier, access date, version/commit/vintage, content hash when available, license/access constraints, and linked claim IDs.

## Corrections
When an upstream source changes, is corrected, retracted, amended, or superseded, mark dependent claims stale and traverse affected lineage edges before reusing them.
