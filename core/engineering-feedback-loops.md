# Engineering Feedback Loops

## Purpose
Turn coding, debugging, and review into short falsifiable loops instead of long speculative edits.

## Hard bug loop
For non-trivial bugs and performance regressions:

`reproduce -> tighten -> minimize -> hypothesize -> instrument -> fix -> regression-test -> cleanup`

### 1. Build a red-capable loop first
Before forming an elaborate theory, create the smallest runnable check that exercises the reported path and fails on the actual symptom. Examples:
- focused unit/integration test;
- CLI command with an assertion/diff;
- curl request;
- headless-browser script;
- replayed trace or fixture;
- differential run against a known-good version;
- `git bisect run` harness;
- repeated stress/fuzz loop for intermittent failures.

If a deterministic repro is impossible, improve the reproduction rate and collect enough structured evidence to falsify hypotheses. Do not pretend a flaky signal is deterministic.

### 2. Minimize without changing the bug
Reduce inputs, environment, configuration, and call path while repeatedly confirming the original symptom remains.

### 3. Rank falsifiable hypotheses
Each hypothesis should predict an observable result. Prefer tests that eliminate several hypotheses at once. Record alternative benign explanations such as configuration, stale state, version mismatch, test pollution, or unrelated races.

### 4. Instrument narrowly
Add temporary diagnostics with an obvious marker and remove them before completion unless the user wants permanent observability. Capture state at the transition where hypotheses diverge, not everywhere.

### 5. Fix the cause, then lock it down
Make the smallest correct change, rerun the red loop to green, add/retain a regression test through a durable interface, and run broader relevant checks.

## TDD for new behavior
Use vertical slices:

`one failing behavior test -> minimal implementation -> green -> next behavior`

Rules:
- Test observable behavior through stable/public seams, not private implementation detail.
- Expected values should come from a spec, fixture, known-good literal, standard, or independent calculation, not the same algorithm as the code under test.
- Do not write a large batch of imagined tests before learning from the first slice.
- Do not add speculative future features to make a later test easier.
- Refactor only from a green state.
- Choose seams from the existing interface/spec when clear; ask only if a materially ambiguous seam cannot be inferred.

## Prototype loop
When the uncertainty is about design or feasibility rather than a bug, build the cheapest throwaway that answers one question. State the question before prototyping, define what observation would change the decision, and do not let prototype code silently become production code.

## Code review and simplification
For non-trivial changes, load `verified-review-and-simplification.md`. Review intent/correctness independently from other warranted angles, verify findings as CONFIRMED/PLAUSIBLE/REFUTED, then run simplification only after correctness is green and retest afterward. Do not let a style cleanup hide a missed requirement or turn reviewer suspicion into an unverified defect.

## High-assurance verification
When example tests are insufficient for invariants, parsers, protocols, state machines, security boundaries, concurrency, or complex transformations, load `formal-verification-and-fuzzing.md`.

## Completion gate
A code change is not done until the relevant chain is green:

`success criteria -> targeted check -> broader relevant checks -> diff review -> regression risk -> remaining uncertainty`

Never claim a command/test ran if it did not.
