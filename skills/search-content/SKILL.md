---
name: search-content
description: "Draft guidance for search and content review; use for discoverability, structured data, provider policies, and evidence consistency. Behavior and installation remain unvalidated."
---

# search-content — draft

Status: design-stage guidance. No executable checks or machine-readable rules are implemented for this module.

## When and inputs

Page purpose, visible content, language/locale, intended search providers, crawl controls, existing head metadata, confirmed public page and image URLs (if any), and permitted review scope.

## Work and references

Check current primary provider sources for time-sensitive requirements. Keep search inclusion, AI citation, user-initiated access, and training controls distinct.

Read [provider checks](references/provider-checks.md) when needed, then the relevant [specification section 9](../../docs/product-spec.ja.md). Use the [rule-authoring contract](../../docs/rule-authoring.md); the [rule library](../../rules/README.md) is still planned. Do not treat a missing check as passed.

For page descriptions, Open Graph, X cards, favicons, home-screen icons or JSON-LD, read [page metadata](references/page-metadata.md). For icons, first research the requested OS/browser and display-context specifications from current primary sources; record target versions, source URLs and retrieval dates before selecting formats and sizes. Match values to visible content, verify the delivered head and JSON, and report unknown public URLs as `needs_review`; do not ship fabricated URL placeholders. Treat browser favicons, Apple home-screen icons, manifest icons and Safari pinned-tab icons as separate display contexts. Icon and manifest files alone do not prove installability or offline support. Structured data supplements semantic HTML and does not guarantee search or sharing outcomes.

## Output

Dated provider-specific findings without invented rankings, citations, metrics, or mandatory unsupported markup. Follow [handover guidance](../../docs/handover.md).

For metadata work, include the content/source mapping, title/description and OG/X checklist, parsed JSON-LD result, emitted and browser-parsed head findings, image checks, and canonical/public-URL status. Distinguish checks performed, failures, checks not run and `needs_review`; local parsing is not evidence of a platform preview or rich-result display.

## Stop or qualify

Ask for missing inputs only when they change a consequential decision. If the source, environment, implementation, or authorization needed for a conclusion is absent, mark the limitation and stop dependent actions. Do not certify conformance, legal compliance, or release readiness from these draft instructions.
