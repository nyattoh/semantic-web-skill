---
name: evidence-reporting
description: "Draft guidance for evidence-based handover; use when recording actual checks, results, limitations, exceptions, and unresolved decisions. Behavior and installation remain unvalidated."
---

# evidence-reporting — draft

Status: design-stage guidance. No executable checks or machine-readable rules are implemented for this module.

## When and inputs

Target/revision, selected rules, real execution records, environment details, and review decisions.

## Work and references

Record only checks actually performed. Preserve failures and uncertainty, separate reporting completion from product readiness, and constrain conclusions to what evidence proves.

Read [report format](references/report-format.md) when needed, then the relevant [specification sections 4 and 11–12](../../docs/product-spec.ja.md). Use the [rule-authoring contract](../../docs/rule-authoring.md); the [rule library](../../rules/README.md) is still planned. Do not treat a missing check as passed.

## Output

A scoped report using the six result states and explicit remaining actions. Follow [handover guidance](../../docs/handover.md).

## Stop or qualify

Ask for missing inputs only when they change a consequential decision. If the source, environment, implementation, or authorization needed for a conclusion is absent, mark the limitation and stop dependent actions. Do not certify conformance, legal compliance, or release readiness from these draft instructions.
