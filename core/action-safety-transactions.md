# Action Safety, Approval, and Transactions

## Purpose
Make tool actions predictable and recoverable, especially when they can mutate external state.

## Action classes
Classify consequential actions by effect, not by tool name:
- **READ_ONLY** - inspection/search/read operations.
- **REVERSIBLE_LOCAL** - local scratch/workspace edits with a clear restore path.
- **REVERSIBLE_EXTERNAL** - external writes with a reliable undo/compensating action.
- **IRREVERSIBLE_OR_HIGH_IMPACT** - deletion, publication, credential/security changes, production changes, financial/legal/medical operational actions, destructive migrations, or actions whose consequences cannot be confidently reversed.

## Transaction pattern
For non-trivial mutation:

`preconditions -> dry-run/plan -> snapshot/backup when useful -> approval if required -> execute -> verify postconditions -> commit/report OR rollback/compensate`

For consequential or externally influenced actions, also load `action-firewall.md` and bind authorization to the exact proposed target/arguments/effect. A previous approval is not reusable after material scope drift.

## Idempotency
When retries are possible, use an idempotency key or state check so the same task cannot accidentally send/publish/create/pay/delete twice.

## Approval
Respect host/user confirmation policies. Do not split one consequential action into smaller calls to evade an approval boundary.

## Rollback
Before a risky change, identify whether rollback is:
- exact restoration;
- compensating action;
- forward-fix only;
- impossible.

If rollback is impossible and impact is material, surface that before execution.

## Verification
A tool reporting success is not enough. Verify the expected state through an independent read/check when practical.
