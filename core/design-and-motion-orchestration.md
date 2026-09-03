# Design, Motion and 3D Orchestration

## Purpose
Choose the smallest visual/interaction stack that can deliver the product experience while preserving accessibility, performance, maintainability and brand specificity.

Load this module for substantial frontend, interaction, motion, 3D, WebGL/WebGPU, creative-coding, product-demo, landing-page, portfolio, scrollytelling or design-system work.

## Reference-informed direction
Before choosing a visual stack, classify the surface and, when visual direction is consequential, use `docs/DESIGN_REFERENCE_PLAYBOOK.md`. Extract principles from multiple references rather than cloning one site. Keep `PRODUCT.md`-style product truth separate from `DESIGN.md`-style visual decisions. For portfolio/marketing surfaces allow a larger expressive budget; for task-heavy product surfaces require stronger utility evidence.

## Research before visual implementation
Before choosing a library, establish:
- product/job-to-be-done and target users;
- brand/design language and existing component system;
- information hierarchy and critical user flows;
- interaction/input modes: keyboard, pointer, touch, wheel, scroll, assistive technology;
- target browsers/devices and performance budget;
- reduced-motion and accessibility requirements;
- asset pipeline and deployment constraints;
- whether motion/3D communicates useful state or is purely decorative.

Do not choose a technology merely because an example looks impressive.

## Capability ladder
Prefer the lowest layer that fully solves the interaction:

1. **Semantic HTML + CSS / native platform APIs** — simple hover/focus/press, opacity/transform transitions, view transitions, scroll snapping, basic keyframes.
2. **Motion** — React state-driven animation, gestures, layout/shared-element transitions, exit/enter states, reusable variants and lightweight scroll-linked UI.
3. **GSAP** — complex timelines, fine-grained sequencing, pinned/scrubbed scrollytelling, SVG/DOM/canvas/WebGL choreography and cross-layer imperative timelines.
4. **React Spring / physics layer** — interaction where continuous spring dynamics are central rather than decorative.
5. **Rive / Lottie** — designer-authored vector/state-machine animation or exported motion assets where that pipeline is already justified.
6. **Three.js / React Three Fiber** — custom 3D scenes, product visualization, interactive spatial UI and WebGL/WebGPU experiences.
7. **Babylon.js / PlayCanvas / A-Frame / XR engines** — game-like physics, editor-first real-time 3D, VR/AR/XR or engine-level requirements.

Do not load several overlapping animation libraries for the same ownership boundary without a clear reason.

## Ownership boundaries
For multi-library experiences assign one owner per concern:
- application state;
- UI/component animation;
- scroll/timeline orchestration;
- 3D render loop;
- physics simulation;
- asset loading/cache;
- navigation/page transition;
- accessibility fallback.

Example: React owns product state, R3F owns scene rendering, GSAP owns one scroll choreography timeline, Motion owns local button/modal/layout feedback. Avoid making both GSAP and Motion continuously write the same property.

## Motion grammar
Design a small motion language before implementing individual effects:
- **feedback**: press, hover, focus, drag, validation, loading;
- **continuity**: shared layout/state transitions that preserve spatial understanding;
- **hierarchy**: important state changes get stronger motion than secondary decoration;
- **entrance/exit**: content should appear/disappear with predictable causality;
- **narrative**: scroll-linked motion should reveal or explain, not merely delay content;
- **physics**: use springs/inertia when they improve perceived direct manipulation;
- **restraint**: repeated animation should not compete with reading or task completion.

Avoid hard-coded universal durations/spring values. Tune to distance, size, interaction frequency and product feel, then validate in context.

## Accessibility contract
- Respect `prefers-reduced-motion` and equivalent framework controls.
- Preserve essential state changes when movement is reduced; prefer opacity/color/static state changes instead of removing meaning.
- Disable or simplify large parallax, auto-playing decorative video and large transform motion for reduced-motion users.
- Do not rely on hover alone for important functionality.
- Keep keyboard focus, semantic controls and screen-reader state independent from animation completion.
- Ensure drag/swipe interactions have non-drag alternatives when needed.
- Keep custom cursors optional and never replace the only clear interaction affordance.

## Performance contract
- Prefer transform/opacity or platform-accelerated properties for frequent animation.
- Avoid continuous layout-thrashing reads/writes; batch measurements and updates.
- Load animation/3D dependencies only when the feature justifies them; lazy-load optional interaction bundles and heavy scenes where practical.
- Keep a single intentional render loop for each canvas/scene and avoid duplicate per-frame schedulers.
- For 3D, budget polygons/draw calls/lights/post-processing/texture memory, use compressed assets, lazy loading, LOD/culling where justified, and provide a low-cost fallback.
- Validate lab behavior and, when available, field performance. Current Core Web Vitals are LCP, INP and CLS; re-check official definitions because these metrics evolve.

## 3D/Web integration architecture
Prefer a layered architecture:

```text
Product/App State
├── UI Layer
│   ├── semantic controls/content
│   └── local motion/feedback
├── Timeline/Interaction Layer
│   └── scroll/sequence orchestration
└── 3D Layer
    ├── scene/camera/lights
    ├── assets/materials
    └── render/physics loop
```

Use explicit bridges between layers instead of global mutable state. Keep expensive scene state outside high-frequency UI rerenders. Cleanup listeners, timelines, animation contexts, RAF loops, GPU resources and scene assets when routes/components unmount.

## Responsive and device adaptation
Do not simply shrink a desktop cinematic layout. Recompose for mobile/touch:
- reduce or remove expensive/pinned sequences when they obstruct navigation;
- use alternate camera compositions and content order;
- account for viewport chrome and dynamic viewport units;
- limit hover-only behavior;
- adapt motion distance and 3D detail to device capability;
- validate orientation changes and resize/reflow cleanup.

## Portfolio / editorial restraint
A premium portfolio does not require a heavy framework. Prefer semantic content, type/grid discipline, fluid CSS, real case-study structure and one signature interaction. Treat award galleries as inspiration, not correctness evidence. If an effect cannot survive mobile, keyboard use, reduced motion or the performance budget, simplify it.

## Validation
After implementation validate:
1. user flow without animation/3D;
2. normal interaction flow;
3. reduced-motion flow;
4. keyboard/touch alternatives;
5. mobile/desktop composition;
6. console/network errors and cleanup leaks;
7. layout stability and interaction responsiveness;
8. GPU/CPU/network cost for heavy experiences;
9. screenshot/visual hierarchy against the product-specific design direction;
10. fallback when heavy assets or JavaScript fail.

Use `core/webapp-validation.md`, `extensions/visual-design-qa.md`, and the appropriate browser/performance specialist.

## Version discipline
Animation and 3D APIs move quickly. Treat external skill examples as discovery/reference material and re-check current official library docs before implementation. Prefer current package names/import paths and current accessibility/performance APIs over historical examples.

## Product UI system gate
For substantial interface work, load `ui-system-and-render-intelligence.md` before selecting animation/3D libraries. Preserve existing tokens/components and validate a representative state matrix. Distinguish source inference from rendered observation and real performance/accessibility measurement.
