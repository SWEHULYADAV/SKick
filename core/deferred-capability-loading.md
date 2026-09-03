# Deferred Capability Loading

## Purpose
Keep tool and Skill context small by discovering capabilities through compact metadata first, then loading full instructions or schemas only for the few capabilities that are about to be used.

Use this module when a host exposes many Skills, MCP tools, plugins, commands, or tool schemas.

## Two-stage discovery

### Stage A: capability index
Keep or query a compact index containing only what routing needs:
- stable capability/tool id;
- short description and domain tags;
- provider/server;
- read/write/destructive risk class;
- availability/auth state when known;
- version or capability-snapshot id when material.

Do not preload hundreds of full JSON schemas or long Skill bodies merely because they are installed.

### Stage B: narrow load
After routing, load the full instructions/schema for only the shortlisted capability set, normally the smallest set that can complete the current phase. For ambiguous tool choice, inspect a few top candidates rather than the entire catalog.

`intent -> capability search -> shortlist -> load exact schema/instructions -> call -> verify`

## Routing rules
- Prefer exact task fit over popularity.
- Prefer stable ids over fuzzy names after discovery.
- Keep one primary owner per phase unless independent comparison is justified.
- Load destructive/write schemas only when the task can legitimately require them.
- If a selected tool fails because a needed capability was omitted, expand the shortlist deliberately; do not permanently preload everything.

## Schema and capability freshness
Tie a loaded schema to its provider/server version or capability snapshot when possible. If tool names, descriptions, annotations, or schemas change materially, discard the stale cached decision and re-run routing/security qualification.

## MCP relationship
For MCP, combine this module with `mcp-validation-and-security.md`: deferred loading reduces prompt surface but does not make an unknown server trustworthy. A quarantined/unqualified server remains blocked even if its tool description matches the task perfectly.

## Context accounting
Measure rather than advertise token savings. If the runtime exposes prompt/tool-schema usage, record baseline vs deferred-loading input tokens, latency, cache behavior, and task accuracy. Third-party savings claims are evidence to test, not guarantees for the active host.

## Fallback
If the runtime cannot search capabilities lazily, emulate the pattern with a small local catalog/manifest and targeted reads. If no indexing mechanism exists, keep the installed set minimal and activate only task-matched providers.
