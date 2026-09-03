# UI System and Render Intelligence

## Purpose
Treat UI work as a product system that must survive real rendering, interaction, accessibility, responsive states and performance constraints, not as a collection of attractive source-code snippets.

Use with `design-and-motion-orchestration.md`, `webapp-validation.md`, and `extensions/visual-design-qa.md`.

## Surface fingerprint
Before changing a UI, establish:
- product/user job and primary flows;
- platform: web, native mobile, desktop, embedded, XR, design-tool source;
- framework/runtime and installed version;
- existing component library/design system;
- tokens: color, typography, spacing, radii, elevation, motion, breakpoints;
- content density and localization/RTL needs;
- accessibility baseline;
- target devices/input modes;
- current screenshots/rendered states when available.

Prefer the project's design system over inventing new primitives.


## Surface-class and reference router
Classify the UI before assigning an expressive budget:
- product/workspace -> clarity, state coverage, speed and error prevention first;
- marketing/portfolio -> stronger identity/storytelling allowed, but keep navigation/content legible;
- editorial/content -> reading rhythm, hierarchy and media sequencing first;
- commerce -> trust, comparison and conversion clarity first;
- docs/developer -> information scent, search, code readability and version clarity first;
- data/operations -> scanability, comparison and status hierarchy first.

For consequential visual direction, build a 3-7 reference set and write `DESIGN_REFERENCES.md` with: reference, transferable principle, what must not be copied, applicability, accessibility/performance risk, and decision. Use curated galleries such as SiteInspire, Land-book, Awwwards or CSS Design Awards for **art direction only**; use product-pattern galleries such as Mobbin/Pageflows only as interaction references. Neither category proves usability, accessibility, semantics or performance. Load `docs/DESIGN_REFERENCE_PLAYBOOK.md` for the full method.

Separate durable product truth (`PRODUCT.md` or project equivalent) from visual/interaction direction (`DESIGN.md`). A redesign should not silently rewrite product requirements.

## Design contract
For substantial UI work maintain a compact, implementation-neutral contract analogous to a `DESIGN.md`:

```text
Product direction / visual thesis:
Layout and composition rules:
Component primitives and reuse rules:
Design tokens / semantic variables:
Typography hierarchy:
Interaction and motion grammar:
Responsive breakpoints/adaptation:
Accessibility requirements:
State matrix:
Performance budget / heavy assets:
Known intentional deviations:
```

This artifact can be derived from source/design-tool state and can guide code-to-design or design-to-code work. Keep vendor-specific IDs in adapters/references, not in the canonical method.

## State matrix
A UI is not verified from one happy-path screenshot. Select relevant states from:
- default / hover / focus / active / disabled;
- loading / skeleton / empty / partial / error / retry / offline;
- authenticated / unauthenticated / permission denied;
- short / long / missing / localized / RTL content;
- narrow phone / tablet / desktop / wide display;
- keyboard-only / touch / pointer;
- normal motion / reduced motion;
- light / dark / high-contrast when supported;
- slow network / failed asset / JavaScript failure where resilience matters.

Do not test every Cartesian combination; choose combinations that exercise materially different behavior.

## Tool routing
Choose the smallest capable verification surface:
- semantic/static inspection for trivial markup/style questions;
- browser CLI for token-efficient short coding-agent checks;
- browser MCP for persistent/exploratory flows and structured accessibility snapshots;
- DevTools/trace/memory tooling for performance, network, heap or runtime diagnosis;
- design-tool integration for authoritative design/component/token state;
- screenshots/visual diff for rendered hierarchy and regression evidence.

When a tool exposes optional capability groups, enable only what the phase needs. Deferred loading applies to browser/design schemas too.

## Design-system invariant
Before hard-coding a color, spacing value, typography size, icon, interaction primitive or component, check whether the project/design system already owns it. Prefer semantic tokens and existing components. If a new primitive is justified, define its contract and reuse path rather than sprinkling one-off values.

## Rendered evidence boundary
Separate:
- **source inference**: likely outcome based on code/styles;
- **rendered observation**: actual browser/device/design-tool state;
- **measured performance**: trace/lab/field metric from a real artifact;
- **user/field evidence**: production telemetry/RUM or user testing.

Never report a Core Web Vital, accessibility pass, visual parity, or device behavior as measured when no corresponding tool/artifact was actually used. When only source inspection exists, label the conclusion as inferred.

## Functional and visual QA order
1. Verify the primary user task works.
2. Verify semantics, keyboard/focus and accessible names/states.
3. Verify responsive composition and selected state matrix.
4. Inspect console/network/runtime failures.
5. Run visual hierarchy/design-system consistency review.
6. Run targeted performance/trace checks when the change can affect them.
7. Re-test after cleanup/simplification.

A beautiful broken flow is a failure; a functional but inaccessible or unusable flow is also a failure.

## HTML/CSS-first expressive implementation
For host-neutral web work, first test whether semantic HTML plus modern CSS can own the experience: Grid/Flexbox, custom properties, `clamp()`, container queries, logical properties, native controls/dialog/popover/details, CSS transitions/keyframes and progressive enhancement. Add JavaScript for real state/behavior; add a framework or animation runtime only when its ownership boundary is justified.

For expressive marketing/portfolio work, prefer one coherent **signature move** over many unrelated effects. Strong typography, disciplined grid, real content and deliberate whitespace often create more identity than dependency-heavy animation. Preserve reduced motion, keyboard access, mobile composition and performance.

## Performance discipline
Use `MEASURE -> IDENTIFY -> CHANGE -> VERIFY -> GUARD`.

Distinguish field telemetry from lab traces and static suspicion. Optimize from evidence when performance is consequential. For Android/native surfaces use platform traces/profilers; for web use browser/DevTools/field tooling; for heavy 3D/motion account for GPU/CPU/network/memory separately.

## Framework specialists
After detecting the stack, route narrow work to official/current specialists when they add version-specific value (for example Android adaptive UI/Perfetto, Angular modern signals/SSR/accessibility, React/Next performance, Playwright testing). SKick retains design intent, evidence and final rendered-verification gates.
