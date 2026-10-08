---
name: accessibility
description: "Draft guidance for accessibility review; use for names, roles, states, keyboard, focus, contrast, zoom, and reflow. Behavior and installation remain unvalidated."
---

# accessibility — draft

Status: design-stage guidance. No executable checks or machine-readable rules are implemented for this module.

## When and inputs

Target interface, chosen evaluation scope, input methods, and available assistive technology.

## Work and references

Separate the evaluation target, project-specific criteria, and exceptions. Coordinate shared target-size rules through the future accessibility-owned rule rather than duplicating thresholds.

Read [manual checks](references/manual-checks.md) when needed, then the relevant [specification section 7](../../docs/product-spec.ja.md). Use the [rule-authoring contract](../../docs/rule-authoring.md); the [rule library](../../rules/README.md) is still planned. Do not treat a missing check as passed.

## Output

Scoped findings with automated versus manual evidence, plus untested or human-review items. Follow [handover guidance](../../docs/handover.md).

## Stop or qualify

Ask for missing inputs only when they change a consequential decision. If the source, environment, implementation, or authorization needed for a conclusion is absent, mark the limitation and stop dependent actions. Do not certify conformance, legal compliance, or release readiness from these draft instructions.
