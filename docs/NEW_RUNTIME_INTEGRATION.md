# Adding SKick to a New AI Agent or Harness

Use this guide when a new AI coding agent, LLM harness, browser agent, IDE extension, autonomous agent, or internal runtime is not yet named in SKick.

## Goal

Make SKick discoverable without copying the full instructions into every base prompt. Preserve progressive loading:

1. **Discovery** — expose only `name` and `description` from `SKILL.md`.
2. **Activation** — when SKick matches the task or the user explicitly requests it, load the full `SKILL.md`.
3. **Resources** — load referenced `core/`, `docs/`, `scripts/`, and other files only when needed.

## Filesystem implementation

A local harness should ideally scan both a client-specific root and the shared Agent Skills root:

```text
<project>/.<client>/skills/skick/SKILL.md
<project>/.agents/skills/skick/SKILL.md
~/.<client>/skills/skick/SKILL.md
~/.agents/skills/skick/SKILL.md
```

The exact client-specific path is owned by the runtime. `.agents/skills` is a cross-client convention, not a requirement of the core Skill specification.

## Activation implementation

If the model can read files, provide the discovered `SKILL.md` location and instruct it to read that file before executing a matching task. If it cannot read files, expose an `activate_skill(name)` tool that returns SKick's instructions and base directory.

Support explicit invocation through whatever mechanism fits the harness (`/skick`, `@skick`, picker, command palette, API flag), but do not require a special syntax for normal automatic activation.

## Resource access

Relative paths in SKick are relative to the SKick directory. The harness should allow read access to that directory while still applying normal permission/security controls to external files, terminals, networks, credentials, and tools.

## Security requirements

- Treat the downloaded SKick package as untrusted until scanned/reviewed.
- Never auto-execute bundled scripts during discovery.
- Do not grant network/terminal/write permissions just because a Skill asks for them.
- Keep secrets outside the Skill directory.
- Log/diagnose malformed Skills instead of silently executing partial content.

## Compatibility test

A new runtime adapter is not `VERIFIED` until all of the following are demonstrated:

1. `skick` is discovered from the documented path or upload mechanism.
2. A matching low-risk prompt activates SKick.
3. A referenced supporting file can be loaded on demand.
4. Explicit invocation works if the runtime claims such a feature.
5. Removing/disable the Skill makes it unavailable as expected.
6. Update/reload behavior is documented.

## Upstream implementation reference

- https://agentskills.io/client-implementation/adding-skills-support
- https://agentskills.io/specification
