# Formal, Property, Fuzz, and Differential Verification

## Purpose
Find correctness failures that example-based tests miss, especially in parsers, protocols, state machines, security boundaries, financial logic, concurrency, serialization, and complex transformations.

## Start with invariants
Write the property that must remain true independently of implementation details. Examples:
- authorization never grants more privilege than policy permits;
- decode(encode(x)) preserves x within specified normalization;
- balance/conservation totals reconcile;
- retrying an idempotent operation does not duplicate effects;
- state transitions cannot skip required authorization/validation states;
- a parser never crashes or reads beyond valid bounds on arbitrary input.

## Verification techniques
Choose by problem:
- property-based testing;
- fuzzing with mutation/generation corpora;
- differential testing against another implementation/version;
- metamorphic testing when exact expected outputs are hard to enumerate;
- state-machine/model-based testing;
- static analysis/type/refinement checks;
- symbolic execution/model checking/formal proof when the risk justifies the tooling.

Do not use formal-sounding tooling when a simple deterministic test proves the property better.

## Oracle independence
Expected results/properties must not be computed by the same buggy algorithm under test. Use skick, independent implementations/calculations, conserved quantities, or metamorphic relations.

## Counterexamples
On failure:
`capture seed/input -> reproduce -> minimize -> identify violated invariant -> trace mechanism -> fix -> preserve regression case/property`.

## Concurrency
For race/deadlock/order problems, vary scheduling/concurrency/load, use repeated stress, deterministic schedulers or model/state exploration when available, and preserve the exact interleaving/trace that exposes the bug.

## Resource limits
Fuzz/model exploration can be unbounded. Apply `resource-budgeting.md`, timeouts, corpus limits, crash deduplication, and stop conditions.
