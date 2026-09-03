# Structured Data Quality and Normalization

## Purpose
Prevent correct-looking calculations from being wrong because units, vintages, joins, definitions, or point-in-time semantics differ.

## Dataset contract
Before analysis, resolve where material:
- owner/source and license/access terms;
- schema/field definitions;
- update/revision cadence and vintage;
- units, currency, timezone, geography, frequency;
- nominal/real, seasonally adjusted/raw, adjusted/unadjusted;
- keys/entity identifiers and join cardinality;
- missing/null/sentinel conventions;
- duplicate records and revision records;
- known breaks/methodology changes.

## Quality dimensions
Assess fitness for the current decision rather than a universal "quality" score. Useful dimensions include accuracy, completeness, consistency, timeliness, provenance, relevance, accessibility, and semantic clarity.

## Validation checks
Use as relevant:
`row counts, uniqueness, referential integrity, ranges, units, nulls, duplicates, impossible combinations, date ordering, outliers, reconciliation totals, cross-source spot checks, revision differences`.

## Time-series hazards
Check:
- revised vs first-release values;
- survivorship bias;
- look-ahead leakage;
- corporate-action adjustments;
- timezone/session boundaries;
- interpolation/backfill;
- frequency conversion;
- calendar/fiscal-period mismatch.

## Joins
Before merging datasets, define the expected relationship (`1:1`, `1:m`, `m:1`, `m:m`) and detect accidental row multiplication.

## Transformations
Record transformations that materially affect conclusions, including filtering, exclusions, imputation, winsorization, currency conversion, inflation adjustment, rebasing, and derived metrics.

Use provenance/quality metadata when available rather than stripping it during analysis.
