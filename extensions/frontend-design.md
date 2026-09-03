# Frontend Design Extension

## Purpose
Use when research or implementation includes a web interface and the user wants a distinctive, production-quality visual result rather than a generic template.

For a new product or major redesign, load `core/project-planning-and-structure.md` first so design follows researched product context and user flows.

## Surface class and references first
Identify whether the surface is product/workspace, marketing/portfolio, editorial/content, commerce, docs/developer or data/operations. Load `docs/DESIGN_REFERENCE_PLAYBOOK.md` for consequential creative work. Use 3-7 references to extract principles, not a single site to imitate. Record what must not be copied.

Keep durable product truth separate from the visual system. Use `PRODUCT.md` (or project equivalent) for audience/jobs/content constraints and `DESIGN.md` for thesis/tokens/grid/type/motion/states.

## Design direction first
Before styling, pick one coherent visual direction from the product/brand context. Define:
- typography hierarchy;
- spacing/grid logic;
- color roles and contrast;
- surface/material treatment;
- illustration/icon language;
- motion behavior;
- responsive behavior.

Do not default to fashionable purple gradients, glass cards, random blobs, or excessive rounded containers merely because they are common in generated UIs.

## HTML/CSS-first expressive implementation
Use semantic HTML, modern CSS Grid/Flexbox, custom properties, `clamp()`, container queries, logical properties, native interactive elements and progressive enhancement before introducing a framework. JavaScript should own behavior/state that actually needs it. A portfolio can be visually ambitious and still be mostly HTML/CSS.

For portfolio/marketing work, prefer one signature move and strong real-content composition over a pile of effects.

## Vanilla-first implementation
For the preferred Python web profile, design directly in semantic HTML, modern CSS, and browser-native JavaScript first. Do not translate a design into React/Next/Vue/Svelte automatically. Use native layout, forms, dialogs, CSS variables, Grid/Flexbox, responsive queries, ES modules and DOM APIs where they provide a maintainable solution. Add a frontend framework only when the researched interaction/state/routing/ecosystem requirements materially justify it.

## Interaction and motion stack selection
Load `core/design-and-motion-orchestration.md` before adding a substantial animation or 3D dependency. Choose the smallest capable layer rather than beginning with a library. Keep local UI feedback, scroll choreography, physics and 3D rendering under explicit ownership boundaries.

For React, prefer current Motion guidance for state/layout/gesture animation when it fits; use GSAP for complex cross-layer timelines or scrubbed/pinned narratives; use Three.js/R3F only when spatial visualization is product-relevant. Verify current official imports/APIs instead of copying historical snippets.

## Motion as part of the design system
Define a small interaction grammar alongside typography/color/spacing: feedback, continuity, hierarchy, entrance/exit, narrative and reduced-motion behavior. Do not animate every component because a library is installed. Motion should clarify state or support the product's character.

## 3D and cinematic restraint
Treat WebGL/WebGPU/3D as a product capability with an asset/performance budget. Prefer semantic HTML and functional content outside the canvas, lazy-load heavy scenes, and maintain useful fallbacks. Avoid generic rotating objects, glowing particle fields or cinematic scroll simply as an AI-generated visual signature.

## Production constraints
- preserve semantic HTML and accessible names;
- support keyboard/focus states;
- check contrast and reduced-motion behavior;
- make layouts responsive by design, not by shrinking desktop;
- use design tokens/CSS variables for repeated values;
- keep motion purposeful and performance-aware;
- avoid unnecessary dependencies when CSS/HTML can do the job cleanly.

## Refine existing UI
When editing an existing product, infer its current design system first. Improve within the existing language unless the user asked for a redesign. Avoid replacing a mature component system with bespoke one-off styling.

## Verification
Use `core/webapp-validation.md` plus `extensions/visual-design-qa.md` to inspect rendered output, anti-slop risk, responsive composition, interaction states, console/network errors, accessibility, and screenshots when browser tooling is available.

## Provenance
This extension is an original vendor-neutral implementation informed in part by the MIT-licensed `vipulgupta2048/codex-skills` frontend-design patterns. See `UPSTREAMS.md`.
