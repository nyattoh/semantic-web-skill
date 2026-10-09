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

For hover and keyboard-focus effects, declare `transition` on the base selector and include each visual property that should animate. Use compatible computed value types at both ends so the browser can interpolate them. For example, `background-size: 0% 1px` to `100% 1px` is interpolable; a unitless or pixel zero to a percentage may change discretely. If the effect changes `background-position`, include it in the transition as well.

Check an intermediate computed value in a browser while the pointer or keyboard focus is active. A final-state screenshot alone does not show that the transition ran. Keep motion brief, provide a visible `:focus-visible` state, and respect `prefers-reduced-motion`.

## Output

Layout decisions and observed defects, with actual test environments and unresolved checks. Follow [handover guidance](../../docs/handover.md).

## Stop or qualify

Ask for missing inputs only when they change a consequential decision. If the source, environment, implementation, or authorization needed for a conclusion is absent, mark the limitation and stop dependent actions. Do not certify conformance, legal compliance, or release readiness from these draft instructions.
