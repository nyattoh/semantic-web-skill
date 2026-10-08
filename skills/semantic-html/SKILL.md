---
name: semantic-html
description: "Draft guidance for choosing HTML elements from content meaning, in comp-to-HTML, brief-to-comp and Review work: headings, landmarks, lists, FAQ, testimonials, forms, figures, tables, links vs buttons, and when a generic div is right. Behaviour and installation remain unvalidated."
---

# semantic-html — draft

Status: design-stage guidance. No executable checks or machine-readable rules are implemented for this module. Everything below is a procedure for the agent to follow and report on, not a tested validator. Purpose and workflows: [ADR 0003](../../docs/adr/0003-design-comp-centered-workflows.md); vocabulary: [CONTEXT.md](../../CONTEXT.md).

## When and inputs

Use when a request involves markup structure in any workflow:

- **Comp-to-HTML**: input is a Design comp (image or design-tool file) plus any copy. Output is Semantic source.
- **Brief-to-comp**: input is a brief. Output is a Design comp plus the semantic blueprint below, so the structure is fixed before HTML exists.
- **Review**: input is existing source. Output is findings; change nothing unless the request says so.

Needed inputs: the content (real text if available), page purpose, the workflow, and whether edits are authorized. A missing input matters only if it changes an element choice; otherwise record an assumption and continue.

## Evidence-first sequence

Decide from evidence of what the content *is*, never from how it looks. Do the steps in order and record each decision in the blueprint.

1. **Collect evidence.** List what you actually have: copy, brief, comp image, design-tool structure, existing DOM. Mark each fact's source (`text`, `brief`, `comp-visual`, `comp-structure`, `owner`, `dom`). Anything you only inferred from pixels is `inferred`.
2. **State the meaning of each region** in one phrase (for example "primary navigation", "ordered steps", "customer quotes", "question/answer pairs", "tabular comparison"). Do this before naming any element.
3. **Page frame.** Choose landmarks (`header`, `nav`, `main`, `footer`, `aside`) and the heading outline from the regions' roles. Heading level follows the content hierarchy, not type size.
4. **Groups.** Decide for each repeated set: ordered (`ol`), unordered (`ul`), name/value (`dl`), or independent items that are not a list. See [content patterns](references/content-patterns.md) for FAQ, testimonials and cards.
5. **Media and data.** Decide each image's role (informative, functional, decorative, complex), whether a `figure` is warranted, and whether data is truly tabular.
6. **Operation.** For every clickable thing decide: navigates (`a href`), acts or submits (`button`), or enters data (form controls with labels). Disclosure and dialog behaviour belongs to [native-interactions](../native-interactions/SKILL.md).
7. **Residual generic elements.** Anything left over may be `div` or `span` *only if* no element above fits. Record why in one phrase; "for styling" is a valid reason, "I did not check" is not.
8. **Check and report.** Compare against [content models](references/content-models.md). Run an actual conformance checker if one is available and authorized; otherwise report `untested`. Never report `passed` from reading the markup.

## Visual-only input

A comp image or a screenshot shows display. It cannot show: heading level, DOM and reading order, link target, whether an element is a link or button, `alt` text, form label association, table header scope, hidden text, or what a repeated card group is. Therefore:

- Treat each such fact as `inferred` and carry it as `needs_review` until the owner, copy, or source confirms it.
- Ask the owner only when the inference changes a consequential choice (for example whether a price grid is a table); otherwise state the assumption in the blueprint.
- Layer names, auto-layout frames and text styles in a design-tool file are authoring artefacts, not semantics. They are evidence of designer intent at best; label them `comp-structure`, not confirmed.
- Never invent copy, `alt` text, link targets or labels to make a region look complete. Mark a gap `open` and name who must supply it.
- Screenshots of the produced HTML do not prove semantics. Use a DOM dump or accessibility tree for structure (see [handover](../../docs/handover.md): keep evidence kinds distinct).

## Semantic blueprint (output contract)

One compact record set, usable at both stages. At the comp stage it is delivered beside the Design comp so layout decisions (what is grouped, which label is visible, which item is a link) already match it; at the HTML stage it is the plan the markup is checked against. This is a working convention for the draft, not a schema; do not present it as a validated format.

```
page: <purpose in one line>        workflow: comp-to-html | brief-to-comp | review
regions:
- id: <short-name>
  meaning: <what the content is>
  evidence: text | brief | comp-visual | comp-structure | owner | dom | inferred
  element: <chosen element(s), e.g. ul > li > figure > blockquote + figcaption>
  basis: standard | convention | judgment      # source; see content-models.md
  # accessibility guidance: basis stays judgment/convention, name the WAI/WCAG source in the finding
  standard-force: requirement | recommendation | description | not_applicable
  heading: <level + text, or "none: reason">
  interaction: <link | button | control | none, with target/label if known>
  alt-considered: <rejected alternative and why, only if non-obvious>
  open: <missing fact and owner, or "-">
  state: passed | failed | untested | blocked | needs_review | not_applicable
```

Rules for the contract:

- `basis: standard` identifies the HTML Standard as the source; it does not by itself say the statement is normative. Record whether it is a requirement, recommendation, or description in `standard-force`. Only failure to meet an actual requirement may be reported as an HTML conformance failure.
- `convention` identifies project policy; `judgment` identifies a reading of content. Neither is reported as an HTML conformance failure.
- Use `passed` or `failed` only when an actual check produced recorded evidence; otherwise use the appropriate remaining result state.
- At the comp stage, add per region the visible things the markup will depend on: visible heading text, form labels and instructions, visible caption or source for figures and quotes, and which items are links vs buttons.
- Result states are the six in [CONTEXT.md](../../CONTEXT.md); there is no score or percentage.
- Keep the blueprint to regions that carry a decision. A uniform paragraph needs no record.

## Work and references

Read [content models](references/content-models.md) for the HTML Standard constraints (with force noted per row), the convention list, and accessibility guidance, and [content patterns](references/content-patterns.md) for FAQ, testimonials, cards, navigation, figures, tables and forms. Then the relevant [specification section 5](../../docs/product-spec.ja.md). Use the [rule-authoring contract](../../docs/rule-authoring.md); the [rule library](../../rules/README.md) is still planned, so no rule ID exists to cite. Do not treat a missing check as passed.

Boundaries with other modules: CSS layout and target sizes → [css-foundations](../css-foundations/SKILL.md) and [accessibility](../accessibility/SKILL.md); open/close and dialog behaviour → [native-interactions](../native-interactions/SKILL.md); structured data and search → [search-content](../search-content/SKILL.md); testimonial or claim substantiation → [regional-compliance](../regional-compliance/SKILL.md). Name the specialist that owns the handover; do not re-decide it here.

## Output

For a first pass (comp-to-HTML or brief-to-comp): the blueprint, then the markup or comp that follows it, then open items. For Review: findings with affected markup, reasoning, `basis` and `standard-force` (accessibility guidance cites its WAI/WCAG source instead), primary-source link, and the evidence still needed. Follow [handover guidance](../../docs/handover.md). The expectation (ADR 0003) is near-final structure on the first pass; Refinement is human-directed.

## Stop or qualify

If the source, environment, implementation, or authorization needed for a conclusion is absent, mark the limitation and stop dependent actions. Do not certify conformance, accessibility, legal compliance, or release readiness from these draft instructions.
