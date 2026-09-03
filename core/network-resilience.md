# Network and Source Resilience

## Purpose
Keep long research reliable when websites, APIs, repositories, or data providers fail intermittently or impose limits.

## Retry policy
Classify failure before retrying:
- `429/rate-limit` -> respect `Retry-After`/provider policy and reduce request rate;
- transient `5xx`, reset, timeout -> bounded retry with backoff/jitter when safe;
- deterministic `4xx`, auth, invalid query -> fix request or stop, do not blind-retry;
- partial pagination -> persist cursor/page and completed results;
- source outage -> route to another authoritative source family if available and record the gap.

## Idempotency
Only retry mutating operations when the action is known idempotent or protected by an idempotency key/state check. Read operations are usually safer but still respect provider limits.

## Partial progress
Checkpoint retrieved pages/records and source identifiers. A failure on page 90 must not force re-fetching pages 1-89 when persistence exists.

## Integrity
Detect truncated responses, duplicate pages, unstable ordering, schema changes, and HTML error pages returned with success status before treating content as data.

## Freshness/cache
Use provider cache metadata/ETags/last-modified when available. Revalidate current facts whose source could have changed since the cached artifact.
