---
name: responsive-verification
description: "Draft guidance for responsive and real-device verification; use for viewport boundaries, zoom, orientation, and browser differences. Behavior and installation remain unvalidated."
---

# responsive-verification — draft

Status: design-stage guidance. No executable checks or machine-readable rules are implemented for this module.

## When and inputs

Target audience, current support requirements, breakpoints, and available devices/browsers.

## Work and references

Select a dated target matrix, then test ranges and boundaries alongside states. When layout changes can affect sequence, read [device testing](references/device-testing.md) for the visual, DOM, and keyboard-order check. Label emulation, browser engines, and physical devices accurately.

Read the relevant [specification section 8](../../docs/product-spec.ja.md). Use the [rule-authoring contract](../../docs/rule-authoring.md); the [rule library](../../rules/README.md) is still planned. Do not treat a missing check as passed.

## Output

An evidence-linked environment matrix, observed defects, and outstanding physical-device checks. Follow [handover guidance](../../docs/handover.md).

## Stop or qualify

Ask for missing inputs only when they change a consequential decision. If the source, environment, implementation, or authorization needed for a conclusion is absent, mark the limitation and stop dependent actions. Do not certify conformance, legal compliance, or release readiness from these draft instructions.
