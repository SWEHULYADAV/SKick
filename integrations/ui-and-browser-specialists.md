# UI, Design and Browser Specialists

## Policy
Use one primary owner per UI concern and preserve project design-system rules. UI tools are evidence/implementation providers; SKick retains product intent, accessibility, performance and rendered-verification gates.

## Playwright CLI and MCP
Playwright provides both token-efficient CLI/Skills for coding agents and MCP for persistent structured browser automation. Prefer:
- CLI/Skills for short, scripted coding-agent checks where lower schema/context overhead matters;
- MCP for exploratory/persistent flows using accessibility snapshots;
- only the MCP capability groups needed for the task.

Treat stored browser profiles/cookies as sensitive. Prefer isolated contexts for tests unless authenticated state is intentionally required.

## Chrome DevTools MCP
Use for browser-native performance/network/runtime/memory diagnosis when available. It is especially useful when the conclusion depends on traces/heap/DevTools evidence rather than static source suspicion. Pin/version and qualify the MCP like any external executable capability.

## Figma/design-tool Skills
Use authoritative design-tool state for tokens, variables, components and design-to-code/code-to-design parity when the project actually uses the tool. Keep a project-neutral design contract (`ui-system-and-render-intelligence.md`) so core methodology is not tied to Figma IDs.

## Google Stitch
Use as an optional design/code generation and design-system extraction surface when available. A derived `DESIGN.md`-style contract can bridge design and implementation, but generated code/design remains subject to normal quality and accessibility review.

## Framework UI specialists
Examples include Angular official Skills, Android adaptive/Compose skills and Vercel React/Next performance Skills. Route only after stack/version detection; framework specialists do not override the project's component system or product direction.

## Accessibility and visual QA
Prefer semantic browser snapshots plus actual rendered screenshots/device states. For accessibility, combine automated checks with keyboard/focus/semantic-state verification; automated WCAG scanners are not full conformance proof.
