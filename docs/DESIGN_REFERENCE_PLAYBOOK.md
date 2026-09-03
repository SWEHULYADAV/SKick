# Design Reference and Portfolio Playbook

Use this guide for websites, landing pages, portfolios, editorial experiences, product marketing, creative tools, and substantial UI redesigns. It turns visual inspiration into an auditable design direction without copying another site's brand or layout.

## 1. Classify the surface before choosing aesthetics

Choose the primary surface class:
- **product/workspace** — task completion, density, clarity, speed and state coverage dominate;
- **marketing/portfolio** — storytelling, identity, typography and a memorable signature move may use a larger expressive budget;
- **editorial/content** — rhythm, reading width, typographic hierarchy and media sequencing dominate;
- **commerce** — trust, comparison, imagery, conversion and checkout clarity dominate;
- **docs/developer** — navigation, search, code readability, information scent and versioning dominate;
- **data/operations** — scanability, comparison, status hierarchy and error prevention dominate.

Do not apply portfolio theatrics to a task-heavy admin console or dashboard without evidence that the trade-off helps users.

## 2. Build a reference set, not a clone target

Collect **3-7 references** with different strengths. Useful discovery sources include:
- SiteInspire — curated portfolio, typography, grid and unusual-layout references;
- Land-book — large curated library of landing/portfolio sections and page compositions;
- Awwwards and CSS Design Awards — art direction, interaction and experimental execution;
- Mobbin/Pageflows — product interaction and flow references where available;
- official product/design-system examples for the actual framework or component system.

Inspiration galleries are **art-direction evidence only**. They do not prove accessibility, usability, performance, semantic quality, or conversion. Validate those separately.

Maintain `DESIGN_REFERENCES.md` for consequential design work:

```text
Reference:
Surface / context:
What is worth learning:
What must NOT be copied:
Applicability to our product:
Accessibility/performance risk:
Decision: use principle | reject | prototype
```

Extract principles such as grid, type scale, density, rhythm, contrast, motion grammar and content sequencing. Never copy logos, proprietary assets, exact layouts, text, illustrations or distinctive brand expression.

## 3. Separate product truth from visual direction

Keep durable product facts in `PRODUCT.md` (or the project's equivalent): audience, jobs, constraints, content truth, flows, domain terms, business rules. Keep visual/interaction decisions in `DESIGN.md`: thesis, grid, type, tokens, components, motion, responsive behavior, states and intentional deviations.

This separation makes redesigns easier without accidentally rewriting product requirements.

## 4. HTML/CSS-first expressive toolkit

For host-neutral web work, first ask how far semantic HTML and modern CSS can go before adding a framework or animation runtime:
- semantic landmarks and native controls;
- CSS Grid/Flexbox;
- custom properties/tokens;
- fluid `clamp()` typography/spacing;
- container queries and logical properties;
- `aspect-ratio`, `object-fit`, modern color functions when supported;
- `details`, `dialog`, popover and other native primitives where appropriate;
- CSS transitions/keyframes and View Transitions when support/fallback is acceptable;
- progressive enhancement for JavaScript behavior.

Use JavaScript when it owns real state/behavior, not merely because an inspiration site looks sophisticated. A striking portfolio can still be small, semantic, fast and mostly HTML/CSS.

## 5. One signature move

For expressive marketing/portfolio work, prefer **one memorable idea** executed consistently rather than many unrelated effects. Examples of principles (not templates):
- editorial/newspaper grid;
- oversized typographic rhythm;
- one spatial navigation metaphor;
- one scroll-driven narrative;
- a restrained generative/3D hero;
- a distinctive case-study transition.

The signature move must preserve reading, keyboard use, reduced-motion behavior, mobile usability and performance.

## 6. Content before decoration

Use real or structurally realistic content early. Portfolio quality comes from the relationship between content, hierarchy and pacing—not placeholder gradients. Case studies should make outcome, role, constraints and evidence easy to scan.

## 7. Two-pass rendered QA

Avoid infinite polish loops. After the implementation is functionally complete:

**Pass 1 — batch inspection**
- desktop and narrow/mobile;
- main flow and selected edge states;
- hierarchy, type wrapping, overflow, broken assets;
- keyboard/focus and accessible names;
- console/network issues;
- obvious motion/performance problems.

Fix all material issues in one batch.

**Pass 2 — confirmation**
- re-run the affected states/viewports;
- confirm no regressions;
- stop when acceptance criteria are satisfied.

Escalate to traces, visual diff, real devices or user testing only when the risk/claim requires it.

## 8. Evidence boundary

A screenshot can show composition but not prove semantics. Lighthouse or a lab trace is not field performance. A design award is not usability evidence. A code review is not rendered proof. Keep source inference, rendered observation, measured performance and user/field evidence separate.

## References used to shape this playbook

- https://www.siteinspire.com/
- https://land-book.com/
- https://www.awwwards.com/
- https://www.cssdesignawards.com/
- https://github.com/pbakaus/impeccable
- https://github.com/vercel-labs/web-interface-guidelines
- https://github.com/google-labs-code/stitch-skills

These are reference/discovery sources, not dependencies. Re-check licenses and current behavior before copying any upstream material; SKick adopts principles, not proprietary design assets.
