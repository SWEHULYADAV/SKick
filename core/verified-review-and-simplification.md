# Verified Review and Simplification

## Purpose
Separate defect finding from finding verification and from post-correctness simplification, so review does not become a pile of unverified suspicions or cosmetic changes that hide functional regressions.

## Review pipeline

`DIFF/SPEC -> INDEPENDENT ANGLES -> DEDUPE -> VERIFY FINDINGS -> GAP SWEEP -> FIX -> RETEST -> SIMPLIFY -> RETEST`

## Independent angles
Choose only the angles the change warrants. Common angles are:
- intent/spec and acceptance criteria;
- correctness/edge cases/state transitions;
- security/trust/permissions;
- regression/compatibility/data migration;
- performance/reliability/concurrency;
- architecture/ownership/API boundaries;
- tests/observability/operability.

When subagents or specialist reviewers exist, isolate angles enough to reduce anchoring and duplicate evidence. More reviewers are not automatically better.

## Finding verification
Normalize each material finding to:
- location/scope;
- claim and failure mechanism;
- evidence/reproduction;
- impact and preconditions;
- confidence state: **CONFIRMED**, **PLAUSIBLE**, or **REFUTED**;
- proposed smallest fix/test.

A scanner/model/reviewer assertion is not confirmed merely because multiple agents repeat it. Trace duplicated origins and run the smallest falsifiable check when practical.

Only confirmed findings should normally block completion. Plausible high-impact findings require targeted follow-up or an explicit residual-risk note. Refuted findings are closed and should not keep resurfacing without new evidence.

## Gap sweep
After resolving findings, scan once for classes that the initial angles could systematically miss: missing call sites, version-specific paths, failure cleanup, rollback, authorization boundaries, and test blind spots. Do not restart a full review without new information.

## Simplification pass
Run simplification only from a green/correct state. Inspect changed code for:
- reuse of existing abstractions instead of duplicates;
- unnecessary layers, flags, helpers, branches, or configuration;
- simpler data/control flow with the same behavior;
- accidental complexity introduced during debugging;
- obvious efficiency wins that do not trade away clarity or safety.

Do not combine cleanup with unrelated broad refactors. Preserve the verified behavior and acceptance criteria, then rerun targeted and relevant broader checks after simplification.

## Output contract
Report confirmed defects separately from plausible risks and optional cleanup. Do not inflate severity or present stylistic preference as correctness evidence.
