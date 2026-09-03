# Mechanism-First Dual-Lens Reasoning

## Principle
Surface labels are often incomplete. Understand the mechanism that produces the observed behavior before choosing an intervention.

Use the general chain:

`observation -> mechanism -> enabling conditions -> causal/functional pathway -> intervention/control -> expected consequence -> verification -> residual risk`

This is a reasoning discipline, not permission to perform unsafe real-world actions.

## Why it matters across domains
- **Software bugs**: symptom -> state/control-flow mechanism -> trigger -> fix -> regression test.
- **Security**: attacker objective -> prerequisite -> primitive/weakness -> attack path -> observable -> prevention/detection/containment -> safe validation.
- **Health/biomedicine**: symptom/association -> pathogen/biological mechanism -> evidence level -> intervention mechanism -> benefit/risk evidence -> clinical/regulatory context.
- **Finance/economics**: price/metric movement -> accounting/market/macro mechanism -> timing/venue/incentive -> competing explanations -> observable confirmation.
- **Reliability/performance**: slowdown/outage -> resource/queue/cache/network/concurrency mechanism -> saturation point -> mitigation -> load/recovery validation.
- **Architecture**: requirement/failure mode -> coupling/trust/data-flow mechanism -> design intervention -> trade-off -> testable property.

## Dual-lens rule
When a system must defend, cure, mitigate, or prevent something, model the opposing/mechanistic process deeply enough to discover effective choke points.

Do not stop at named categories such as "SQL injection", "bacterial infection", "liquidity issue", or "race condition". Ask what concrete primitive or causal pathway makes it possible.

## Competing mechanisms
Maintain more than one plausible explanation until discriminating evidence exists. For each candidate specify:
- prediction if true;
- prediction if false;
- evidence that distinguishes it;
- confounders/alternative benign explanations;
- conditions under which it applies.

Prefer one observation that separates several mechanisms over many observations that merely fit the leading story.

## Intervention discipline
Map each proposed action to the mechanism it is supposed to change. If the mechanism is uncertain, prefer reversible diagnostics/prototypes before high-impact intervention.

## Verification
A mechanism claim is strongest when independent evidence connects:
`cause/pathway <-> observable <-> intervention <-> changed outcome`.

Do not upgrade correlation, plausibility, simulation, in-vitro evidence, market narrative, or exploitability theory into causal certainty without appropriate evidence for the domain.
