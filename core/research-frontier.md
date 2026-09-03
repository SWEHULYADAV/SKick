# Research Frontier and Unknown-Unknown Scan

## Purpose
Before finalizing a non-trivial Deep/Exhaustive investigation, deliberately search for relevant questions that were never asked. This is a blind-spot scan, not an invitation to research indefinitely.

## Frontier question
Ask internally:

> What relevant fact, dependency, assumption, failure mode, version boundary, or stakeholder constraint could change the conclusion even though it has not yet appeared in our current questions?

## Scan dimensions
Choose only dimensions relevant to the task:
- hidden version/deployment/environment differences;
- default/fallback behavior;
- undocumented constraints or feature flags;
- compatibility boundaries and transitive dependencies;
- migration/deprecation/removal history;
- negative/rejected design decisions;
- production incidents and scale behavior;
- security/privacy/abuse implications;
- license/governance/supply-chain changes;
- recovery/data-integrity risks;
- alternate implementations exposing missing terminology;
- test gaps or paths not exercised by the current reproduction;
- local wrappers/custom patches that invalidate generic guidance;
- operational constraints such as permissions, CI/CD, containers, serverless, ARM/GPU, network topology, or IAM.

## Information-gain rule
Convert a frontier candidate into a real research branch only if answering it could materially:
- reverse or qualify the conclusion;
- change the recommended implementation;
- reveal a serious edge case or security/reliability risk;
- resolve an unexplained contradiction;
- lower confidence enough that the user should know.

Otherwise record it as a low-priority residual risk and stop.

## Frontier loop
Use:

```text
provisional answer
-> frontier scan
-> material new question?
   YES: add Q# to evidence graph -> choose highest-information search -> verify/challenge -> update checkpoint -> rescan
   NO: evidence saturation -> report
```

Limit the scan by evidence saturation, not by arbitrary source count. Two consecutive frontier expansions that produce no material new insight are a strong stop signal.

## Security/architecture variant
For high-impact security or architecture work, include an assumption attack:
- What if the trusted component is compromised?
- What if credentials leak?
- What if documentation is stale?
- What if a dependency changes ownership?
- What if user-controlled/untrusted text crosses an agent/tool boundary?
- What if the preferred control fails?

Translate any material finding into prevention, detection, containment, recovery, or validation work rather than merely listing scary possibilities.
