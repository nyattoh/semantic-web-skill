---
name: regional-compliance
description: "Draft guidance for identifying regional advertising review needs; use when public claims depend on market, product, medium, and date. Behavior and installation remain unvalidated."
---

# regional-compliance — draft

Status: design-stage guidance. No executable checks or machine-readable rules are implemented for this module.

## When and inputs

Market, advertiser, product/service category, audience, medium, publication date, and claim evidence.

## Work and references

Determine applicability before selecting sources. Track claims and supporting evidence; unresolved scope or interpretation remains needs_review, never assumed compliance.

Read [applicability](references/applicability.md) when needed, then the relevant [specification section 10](../../docs/product-spec.ja.md). Use the [rule-authoring contract](../../docs/rule-authoring.md); the [rule library](../../rules/README.md) is still planned. Do not treat a missing check as passed.

## Output

Applicability questions, unsupported-market notices, claim/evidence gaps, and qualified-review needs. Follow [handover guidance](../../docs/handover.md).

## Stop or qualify

Ask for missing inputs only when they change a consequential decision. If the source, environment, implementation, or authorization needed for a conclusion is absent, mark the limitation and stop dependent actions. Do not certify conformance, legal compliance, or release readiness from these draft instructions.
