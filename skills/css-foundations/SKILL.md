---
name: css-foundations
description: "Draft guidance for CSS layout, units, cascade, typography, and input-aware presentation; use for CSS design or review. Behavior and installation remain unvalidated."
---

# css-foundations — draft

Status: design-stage guidance. No executable checks or machine-readable rules are implemented for this module.

## When and inputs

Styles, target content, existing conventions, and relevant input/viewport constraints.

## Work and references

Inspect flow, intrinsic sizing, overflow, cascade, typography, and input capabilities. Do not impose the historical prompt’s universal unit or layout restrictions.

Read [layout and units](references/layout-and-units.md) when needed, then the relevant [specification sections 6–7](../../docs/product-spec.ja.md). Use the [rule-authoring contract](../../docs/rule-authoring.md); the [rule library](../../rules/README.md) is still planned. Do not treat a missing check as passed.

## Hover and focus transitions

For hover and keyboard-focus effects, declare `transition` on the base selector and include each visual property that should animate. For a left-to-right underline, a pseudo-element can use `transform: scale(0, 1)` to `scale(1, 1)`, `transform-origin: left top`, and `transition: transform 300ms ease` on the base state. Position it relative to the text, leave measured clearance before adjacent icons, and do not move arrows or icons unless requested. If using `background-size` instead, use compatible computed value types at both ends, such as `0% 1px` to `100% 1px`; a unitless or pixel zero to a percentage may change discretely. Check an intermediate computed value in a browser while the pointer or keyboard focus is active. A final-state screenshot alone does not show that the transition ran. Keep motion brief and provide a visible `:focus-visible` state. In `prefers-reduced-motion`, shorten or remove the transition; do not globally reset `transform`, which can erase the collapsed base state.

## Output

Layout decisions and observed defects, with actual test environments and unresolved checks. Follow [handover guidance](../../docs/handover.md).

## Stop or qualify

Ask for missing inputs only when they change a consequential decision. If the source, environment, implementation, or authorization needed for a conclusion is absent, mark the limitation and stop dependent actions. Do not certify conformance, legal compliance, or release readiness from these draft instructions.
