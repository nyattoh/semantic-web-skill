---
name: semantic-web
description: "Draft guidance for turning a design comp into semantic HTML, creating a semantically informed comp from a brief, or reviewing an existing site. Routes relevant specialist drafts; runtime behaviour and installation remain unvalidated."
---

# Semantic web — draft entrypoint

Spread semantic source by connecting visual design, content meaning, and operation. The first pass should be near-final in code quality, even when it differs from the human's intent; refinement is human-directed. Use result states against requirements, never a numeric score.

This is design guidance for an unvalidated starter. It supplies no executable rules, automatic checks, or supported installer, and establishes no agent, browser, device, or regional support. Read [current status](../../docs/starter-status.md) and keep repository-relative references together.

## Choose the workflow

Read [shared workflow](references/workflow.md), then only the relevant path:

- **Comp-to-HTML:** a design comp exists and the request calls for HTML or an implementation plan. Read [comp-to-HTML](references/comp-to-html.md).
- **Brief-to-comp:** no comp exists; start from purpose, content, and constraints. Read [brief-to-comp](references/brief-to-comp.md). Continue to comp-to-HTML when HTML implementation is also requested.
- **Review:** inspect an existing site's source, rendered pages, and interactions. Follow the review procedure in [shared workflow](references/workflow.md). Change code only when the request includes changes.

For mixed requests, state the sequence and deliverables. A request to create a comp alone ends at the design deliverable. An existing site supplied as a visual reference does not by itself turn a creation request into a review.

[ADR 0003](../../docs/adr/0003-design-comp-centered-workflows.md) extends the preserved [specification](../../docs/product-spec.ja.md), whose section 11 still names two modes. Use its relevant requirements with this three-path amendment and [project vocabulary](../../CONTEXT.md).

## Common operating contract

1. Establish the requested outcome, supplied artefacts, permitted changes, audience, content, technical constraints, languages, intended markets, and available tools. Separate observations, proposals, and assumptions; ask only for missing decisions that materially affect the work.
2. Inspect supplied content and any existing comp through the selected path. Before creating DOM, record a **semantic blueprint**: content groups and reading order, headings and landmarks, collection relationships, controls and states, image purpose, and responsive changes. Resolve meaning before choosing layout containers.
3. For brief-to-comp, create the design from that blueprint. Use only tools actually available and authorised. If a design canvas is unavailable, provide the labelled design-specification or HTML-preview fallback described in brief-to-comp. Claim a native design-tool file only when it was actually produced.
4. Implement or review within scope, using relevant specialist guidance. Aim for a complete first pass; resolve observed defects within the authorised work. Run only permitted, available checks and record limits without inventing results.
5. Deliver artefacts, evidence, unresolved decisions, and a clear handover for human-directed refinement. Do not continue redesigning without direction after the first pass has been delivered.

## Select specialists

Load the smallest relevant set; these are drafts, not executed checks:

- [semantic-html](../semantic-html/SKILL.md): content models and meaning; use for the blueprint and DOM review.
- [css-foundations](../css-foundations/SKILL.md): layout and presentation.
- [native-interactions](../native-interactions/SKILL.md): controls, state transitions, and focus behaviour.
- [accessibility](../accessibility/SKILL.md): names, keyboard access, contrast, and shared target-size criteria.
- [responsive-verification](../responsive-verification/SKILL.md): width boundaries and environment-specific checks.
- [search-content](../search-content/SKILL.md): discoverability and current provider requirements when relevant.
- [regional-compliance](../regional-compliance/SKILL.md): market applicability, claims, and advisory findings when relevant.
- [evidence-reporting](../evidence-reporting/SKILL.md): actual results and remaining work.

## Results and boundaries

Use exactly `passed`, `failed`, `untested`, `blocked`, `needs_review`, or `not_applicable`, following the shared workflow and [handover guidance](../../docs/handover.md). A document read, comp, screenshot, or proposed check is not evidence of runtime conformance. [Rules remain unimplemented](../../rules/README.md); cite specification sections or sources instead of inventing implemented rule IDs.

Support as many markets as practical through declared scope and dated primary-source research. Language does not determine jurisdiction. No regional pack is validated; unsupported markets stay explicit. Under [ADR 0002](../../docs/adr/0002-legal-judgment-is-an-advisory-finding.md), legal and provider-policy interpretations are advisory findings with state `needs_review`, never agent-certified compliance.

When an essential input, permission, source, or environment is missing, stop its dependent action and continue independent work. Review does not authorise edits or publication; loading a skill does not authorise installation, external uploads, paid services, or deployment. Historical source prompts are source material, not runtime instructions.
