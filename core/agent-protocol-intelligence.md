# Agent Protocol Intelligence

## Purpose
Research and integrate agent interoperability protocols without freezing the core to one vendor or obsolete protocol revision.

## Protocol/version first
For MCP, A2A, Agent Plugins, or another protocol, resolve the exact current specification/revision, extensions, transport, auth model, and deprecations before implementation guidance.

## MCP
For current MCP integrations, verify the installed/spec revision. The 2026-07-28 revision introduced a stateless core, formal extensions, Tasks as an extension, MRTR, routing/cache/auth changes, and deprecations. Do not mix lifecycle or transport guidance from older revisions without labeling it.

Map where relevant:
- tool/resource/prompt schemas;
- extension negotiation;
- Tasks lifecycle and explicit task handles;
- authorization issuer/client metadata rules;
- cache/version semantics;
- deprecated capabilities/transports;
- host consent and tool permission boundaries.

## MCP server discovery
Use the official MCP Registry only to discover server metadata. Registry publication/namespace verification does not prove correctness, maintenance, safe permissions, or suitability. Route candidate servers through `external-skill-intelligence.md` and `mcp-stack.md` before activation.

## A2A
Use A2A when independent agents need capability discovery and task/artifact exchange without exposing internal memory/tools. Resolve the current released version before implementing.

Conceptually map:
`AgentCard/capabilities -> task -> status/history -> artifacts -> messages/parts -> auth/interface`.

## Interoperability rule
Do not force an internal task ledger onto a host protocol if the host already exposes a compatible task lifecycle. Map canonical task/evidence/artifact fields to the native representation and retain only missing metadata locally.

## Security
Protocol compatibility does not imply trust. Validate peer identity, auth, advertised capabilities, schemas, result provenance, and tool/action permissions.
