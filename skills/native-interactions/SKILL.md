---
name: native-interactions
description: "Draft guidance for native HTML and JavaScript interaction design; use for navigation, disclosure, dialogs, and forms. Behavior and installation remain unvalidated."
---

# native-interactions — draft

Status: design-stage guidance. No executable checks or machine-readable rules are implemented for this module.

## When and inputs

Interaction requirements, markup and script, state transitions, and intended navigation behavior.

## Work and references

Determine disclosure versus modal behavior first. Review state synchronization, keyboard operation, focus reachability, focus return, and viewport changes.

Read [navigation](references/navigation.md) when needed, then the relevant [specification sections 6–7](../../docs/product-spec.ja.md). Use the [rule-authoring contract](../../docs/rule-authoring.md); the [rule library](../../rules/README.md) is still planned. Do not treat a missing check as passed.

## Output

State and interaction findings, reproduction steps, actual evidence, and unavailable tests. Follow [handover guidance](../../docs/handover.md).

## Stop or qualify

Ask for missing inputs only when they change a consequential decision. If the source, environment, implementation, or authorization needed for a conclusion is absent, mark the limitation and stop dependent actions. Do not certify conformance, legal compliance, or release readiness from these draft instructions.
