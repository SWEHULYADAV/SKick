# Visual Design QA and Anti-Slop Gate

## Purpose
Turn "avoid generic AI UI" from an instruction into a rendered-quality review step.

## Use after rendering
Treat inspiration and correctness as separate evidence. A design award/gallery reference can justify an art-direction experiment but cannot establish accessibility, usability or performance.

For substantial creative work, use a bounded two-pass loop: first inspect all material desktop/mobile/states and batch fixes; second confirm affected states and stop when acceptance criteria are met. Do not polish indefinitely without a new defect or requirement.
When a browser/screenshot capability exists, inspect representative desktop and mobile states after the main UI works. Use this rubric as a diagnostic, not a rigid aesthetic law.

## Slop-risk checks
Look for unexplained repetition of common generated-UI defaults:
- every section becoming a rounded card;
- same large radius on unrelated elements;
- purple/blue gradient used without product rationale;
- glassmorphism/backdrop blur everywhere;
- decorative glowing blobs/orbs;
- generic centered hero + three cards + logo wall regardless of product workflow;
- stock icon/emoji language without a coherent system;
- excessive shadow/gradient/noise layers;
- typography with little hierarchy or personality;
- uniform spacing that ignores information density;
- oversized empty hero areas;
- vague marketing copy replacing product information.

A style is not bad merely because it uses one of these devices. Flag overuse, lack of rationale, and sameness.

## Quality rubric
Assess:
- product/brand fit;
- information hierarchy;
- typography and readability;
- spacing/grid rhythm;
- visual distinctiveness;
- interaction clarity and state feedback;
- accessibility/contrast/focus;
- responsive composition;
- purposeful motion and reduced-motion behavior;
- density appropriate to the task;
- performance/layout stability;
- consistency without monotony.

## Motion and interaction QA
Check:
- motion has a clear feedback/continuity/narrative purpose rather than decorative repetition;
- reduced-motion preserves meaning and removes/simplifies large transforms, parallax and autoplay where appropriate;
- hover-only interactions have touch/keyboard equivalents;
- entrance animations do not hide essential content from testing or assistive technology;
- page/scroll animations remain interruptible, reversible and usable under fast scrolling;
- multiple animation libraries are not fighting over the same properties or scroll state;
- lifecycle cleanup removes timelines, listeners, observers and animation loops.

## 3D/spatial QA
For WebGL/WebGPU/3D work additionally check:
- 3D has a product/storytelling purpose;
- scene/camera/UI/timeline ownership is clear;
- useful HTML/fallback content exists when the canvas or assets fail;
- asset transfer, texture memory, draw calls, DPR/post-processing and mobile performance are proportionate;
- controls work with touch and have accessible non-3D paths for critical information;
- resize/orientation/unmount/remount does not leak GPU resources or duplicate render loops.

## Responsive review
Do not treat mobile as shrunken desktop. Check navigation, touch targets, content order, table/form behavior, overflow, safe areas, virtual keyboard effects, and long labels/error states.

## Evidence
Capture screenshots or stable visual artifacts for important regressions when tooling permits. Combine visual judgment with DOM/accessibility/network/console checks from `core/webapp-validation.md`.

## Static preflight
`scripts/visual_qa.py` can flag possible CSS/template overuse patterns, but it is only a preflight. A rendered visual review is required for a strong design conclusion.
