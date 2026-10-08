---
name: search-content
description: "Draft guidance for search and content review; use for discoverability, structured data, provider policies, and evidence consistency. Behavior and installation remain unvalidated."
---

# search-content — draft

Status: design-stage guidance. No executable checks or machine-readable rules are implemented for this module.

## When and inputs

Page purpose, content, intended search providers, crawl controls, and permitted review scope.

## Work and references

Check current primary provider sources for time-sensitive requirements. Keep search inclusion, AI citation, user-initiated access, and training controls distinct.

Read [provider checks](references/provider-checks.md) when needed, then the relevant [specification section 9](../../docs/product-spec.ja.md). Use the [rule-authoring contract](../../docs/rule-authoring.md); the [rule library](../../rules/README.md) is still planned. Do not treat a missing check as passed.

## Output

Dated provider-specific findings without invented rankings, citations, metrics, or mandatory unsupported markup. Follow [handover guidance](../../docs/handover.md).

## Stop or qualify

Ask for missing inputs only when they change a consequential decision. If the source, environment, implementation, or authorization needed for a conclusion is absent, mark the limitation and stop dependent actions. Do not certify conformance, legal compliance, or release readiness from these draft instructions.
