# SKick Runtime and Guarantee Levels

SKick is portable because executable enforcement is optional. The same package can operate with different guarantee levels depending on the host.

## FULL RUNTIME

The host exposes a filesystem plus Python/code execution sufficient to run SKick runtime helpers. Observable guarantees can include capability probes, deterministic depth selection, module compilation, instruction-budget accounting, structured run state, evidence/claim validation, doctor/status, installer state and local evaluations.

A FULL RUNTIME label still does not imply browser/network/secrets/subagents are available. Each capability has its own observed state.

## PARTIAL RUNTIME

Some executable helpers work but one or more required surfaces are absent or restricted. Examples include read-only filesystem access, code execution without network, or an installer that can copy files but cannot verify host discovery.

The runtime must downgrade unavailable proof. A copied package can remain `discovered=false`; a changed patch can remain `not_tested` when test execution is unavailable.

## DECLARATIVE MODE

The host can load `SKILL.md` and referenced material but cannot execute SKick's Python runtime. Progressive loading, evidence discipline and claim-honesty rules are instructions to the host model rather than deterministic enforcement.

The Skill must remain internally understandable in this mode. Runtime scripts are optional enhancements, not mandatory references that make the declarative package unusable.

## PROMPT FALLBACK

No native Skill mechanism is verified. SKick can be supplied as session/project instructions through the host's supported prompt or rules surface. Persistent discovery and explicit Skill invocation are not claimed unless the host provides them.

## Feature guarantees

| Feature | FULL RUNTIME | PARTIAL RUNTIME | DECLARATIVE MODE | PROMPT FALLBACK |
|---|---|---|---|---|
| Capability probe | Observed local probes + conservative unknowns | Available probes only | Host-reported/instructed | None unless supplied by host |
| Depth selection | Deterministic model available | Deterministic when runtime runs | Instructed | Instructed |
| Module compiler | Executable selection + cost estimate | Executable if filesystem/runtime available | Semantic/manual progressive loading | Manual/context attachment |
| Instruction budget | Measured/estimated by runtime | Partial estimate | Instructed | Optional |
| Evidence ledger | Structured runtime artifact | Partial structured artifact | Model-maintained concept | Optional |
| Claim firewall | Mechanically validated reporter | Enforced where state/report runtime runs | Instructed | Instructed |
| Install proof states | Copied/installed/discovered/invokable/live-tested separated | Only observable states | Host/UI dependent | Not applicable |
| Evaluation | Deterministic local harness + optional providers | Available local checks | External harness required | External harness required |
| Platform proof | Still requires real host evidence | Still requires real host evidence | Docs/host observation only | Docs/host observation only |

## Proof vocabulary

SKick never upgrades one proof layer into another automatically:

- `STATIC VALIDATION` — files/config/schema/package are structurally valid.
- `RUNTIME TEST` — deterministic code/tool executed successfully.
- `BEHAVIORAL EVALUATION` — an AI agent completed evaluated tasks.
- `DOC VERIFIED` — first-party documentation supports a compatibility claim.
- `LIVE PLATFORM TEST` — real platform install/discovery/invocation was observed and recorded.

## Capability state vocabulary

Use `available`, `unavailable`, `unknown`, `restricted`, `permission_required`, or `host_dependent`. Unknown is a first-class state and must not be filled with an optimistic guess.
