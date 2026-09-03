# Motion and Interaction Design Extension

## Purpose
Create purposeful micro-interactions, transitions, gesture feedback and scroll-linked motion without turning the interface into a demo reel.

Load with `core/design-and-motion-orchestration.md` when motion materially contributes to feedback, continuity, hierarchy or storytelling.

## Interaction-first process
For each animated behavior define:
1. user action or system event;
2. state before and after;
3. information the motion communicates;
4. interruption/reversal behavior;
5. reduced-motion equivalent;
6. mobile/touch/keyboard equivalent;
7. performance cost and cleanup path.

If the motion cannot answer what it communicates, simplify or remove it.

## Pattern selection
### Local UI state
Use CSS for small isolated transitions. Use Motion for component-state, gestures, shared layout, presence/exit and variants when React owns the state.

### Timeline choreography
Use GSAP when several independent targets/layers need precise sequence control, labels, scrub/pin behavior or DOM/SVG/canvas/3D coordination.

### Continuous physical interaction
Use a physics-oriented layer only when spring/inertia behavior itself matters to direct manipulation. Avoid adding a second physics library for decorative bounce.

### Designer-authored animation
Use Rive for interactive state-machine assets and Lottie for exported vector animation when those production pipelines already exist. Keep accessible static/semantic fallbacks.

## Scroll narrative rules
- Scroll position may control presentation, but essential information must remain reachable and understandable.
- Do not create long pinned sections solely to make the page feel cinematic.
- Keep scroll progress reversible and deterministic.
- Avoid scroll-jacking; preserve native navigation expectations unless the product explicitly requires otherwise.
- Test fast scrolling, back navigation, resize/orientation changes, reduced motion and deep links.
- Prefer one timeline owner for a narrative section.

## Layout/shared-element motion
Use shared-element or layout transitions when they preserve object identity across states. Do not animate every layout change by default; large surfaces and long-distance transforms can be distracting or expensive.

## Gesture rules
- Press/tap feedback should confirm the action without delaying it.
- Hover is enhancement, not the only interaction path.
- Drag/swipe needs constraints, cancel behavior and accessible alternatives.
- Use velocity/inertia only where it maps to the object model.
- Avoid accidental gesture conflicts with page scrolling and browser navigation.

## Reduced motion
When the user requests reduced motion:
- replace large translation/scale/parallax with opacity or immediate state change;
- disable decorative auto-play and large background motion;
- preserve educational continuity where possible;
- avoid flashing/strobing and excessive vestibular motion.

For Motion, prefer current official reduced-motion APIs. For GSAP, prefer `gsap.matchMedia()` or equivalent current APIs rather than deprecated historical helpers.

## Bundle and runtime discipline
- Keep CSS/native transitions when sufficient.
- For Motion, use current import paths and consider feature/lazy loading when bundle cost matters.
- For GSAP, register only required plugins and clean contexts/timelines on lifecycle changes.
- Do not combine locomotive/smooth-scroll libraries with browser-native scrolling merely because a template does; justify the behavior and test accessibility/performance.

## QA prompts
Ask:
- Is anything moving without communicating or delighting proportionally to its cost?
- Does motion mask latency or clarify progress, or merely add delay?
- Can the user interrupt/reverse it safely?
- Are multiple libraries fighting over the same transform/scroll state?
- Does it still work at 200% zoom, on touch, with reduced motion, and under slow CPU/network?
- Are entrance animations hiding content from tests/assistive tech?
