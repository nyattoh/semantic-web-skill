---
name: semantic-web
description: "Guide comp-to-HTML, brief-to-comp, and existing-site review. Routes only relevant specialist drafts. Runtime behaviour and installation are unvalidated."
---

# Semantic web — draft entrypoint

Use to connect design, content meaning, and operation in comp-to-HTML, brief-to-comp, or review. Implement explicit requests in the first pass; human refinement is for remaining preferences, not known omissions. See [current status](../../docs/starter-status.md); this starter is guidance, not a validator or verified host integration.

## Route

- **Comp-to-HTML:** a comp exists and HTML or an implementation plan is requested. Read [comp-to-HTML](references/comp-to-html.md).
- **Brief-to-comp:** no comp exists. Read [brief-to-comp](references/brief-to-comp.md); continue to comp-to-HTML only if HTML is also requested.
- **Review:** inspect the supplied source/rendering and report findings. Follow [shared workflow](references/workflow.md); do not edit unless requested.

For mixed requests, state the order and deliverables. A visual reference does not itself make a creation request a review. A comp-only task ends at the design deliverable.

## Build and verify

Before design or DOM work, preserve every explicit requirement and prohibition in the [coverage ledger](references/workflow.md), including literal values and no-go constraints. Create the semantic blueprint before layout; use [semantic-html](../semantic-html/SKILL.md) for its content and element decisions.

Implement each ledger row within scope. Base copy on the stated audience, primary task, and supplied facts. Do not publish internal `unknown` placeholders, invent destinations, or add irrelevant links. Choose image alternatives from image purpose; `alt` and visible captions serve different purposes.

For requested interaction or motion, record trigger, visible effect, property/direction, and reduced-motion state. Use [CSS foundations](../css-foundations/SKILL.md) and [native interactions](../native-interactions/SKILL.md) when relevant. Test actual pointer/keyboard states and an intermediate transition value. Verify the requested widths; measure collisions and arrow clearance where they matter.

Use the smallest relevant specialist set:

- [semantic-html](../semantic-html/SKILL.md) for content models and DOM meaning.
- [css-foundations](../css-foundations/SKILL.md), [native-interactions](../native-interactions/SKILL.md), [accessibility](../accessibility/SKILL.md), and [responsive-verification](../responsive-verification/SKILL.md) for relevant presentation and operation.
- [search-content](../search-content/SKILL.md), [regional-compliance](../regional-compliance/SKILL.md), and [evidence-reporting](../evidence-reporting/SKILL.md) only when those areas apply.

Reconcile every ledger row against its expected evidence. A document or screenshot does not prove runtime behaviour. Use the [shared workflow](references/workflow.md) result states. Leave unavailable checks `untested` or `blocked`; do not claim verification while a requested row remains unresolved.

## Boundaries

Rules and regional packs remain unimplemented or unvalidated; cite sources rather than inventing rule IDs. Language does not determine jurisdiction. Legal and provider-policy interpretations remain advisory `needs_review` findings under [ADR 0002](../../docs/adr/0002-legal-judgment-is-an-advisory-finding.md). Stop only the dependent work when an essential input, permission, source, or environment is missing. Loading a skill does not authorise edits, installation, external uploads, paid services, or publication.
