# Content Models — draft guidance

Resolve element placement against the current [HTML Standard](https://html.spec.whatwg.org/multipage/) and the actual parent and child context. A parser or conformance checker can establish some structural constraints; it cannot establish whether the element matches the content's meaning. This guide is a reading aid, not a tested implementation or an independent normative source. If wording here and the Standard differ, the Standard wins; re-read it before encoding anything as a rule. The Standard is a living document. On 2026-10-09, the grouping-content, sections, headings, text-level-semantics (`a`), tables, main, image alternative, label association, `details`/`summary`, `button` content model and Auto `type` behaviour, and DOM content-category claims were checked. Recheck them before encoding rules.

Tag every decision with a basis (see [SKILL.md](../SKILL.md)): **standard** (the HTML Standard is the source; record its force separately), **convention** (this project's policy), or **judgment** (a reading of the content). Do not report conventions or judgments as standards violations.

## A. HTML Standard constraints and guidance

This table includes conformance constraints, authoring recommendations, and semantic descriptions. A statement's presence in the HTML Standard does not by itself make it normative: preserve whether the source says `must`, `should`, `encouraged`, or gives a descriptive note. Report only failure to meet an actual requirement as an HTML conformance failure. Summaries are paraphrases; quoted fragments are from the cited page. Follow the links for full models, contexts, and exceptions.

| Topic | Force or meaning | What the Standard says | Source |
|---|---|---|---|
| `div` | Meaning and recommendation | It has no special meaning; the Standard describes it as an element of last resort and encourages it for styling-only wrappers. This is guidance, not a conformance test. | [grouping-content](https://html.spec.whatwg.org/multipage/grouping-content.html) |
| `p` | Content-model requirement and recommendation | Its content model is phrasing content. The Standard says it "should not be used when a more specific element is more appropriate"; that sentence is guidance. | [grouping-content](https://html.spec.whatwg.org/multipage/grouping-content.html) |
| `ul` / `ol` | Content-model requirement and meaning | Children are `li` and script-supporting elements only. `ol` represents intentionally ordered items; `ul` represents items where order is not important. | [grouping-content](https://html.spec.whatwg.org/multipage/grouping-content.html) |
| `dl` | Content-model requirement and meaning | Groups of one or more `dt` then one or more `dd`; each group may be wrapped in one `div`. Its meaning is name/value groups, not generic two-column layout. | [grouping-content](https://html.spec.whatwg.org/multipage/grouping-content.html) |
| `blockquote` | Requirement | Attribution, if any, "must be placed outside the blockquote element" (for example in a `figcaption` of an enclosing `figure`). | [grouping-content](https://html.spec.whatwg.org/multipage/grouping-content.html) |
| `figure` / `figcaption` | Content-model requirement and meaning | `figcaption` is the caption of the rest of the figure's content, as first or last child. | [grouping-content](https://html.spec.whatwg.org/multipage/grouping-content.html) |
| `section` | Meaning and authoring guidance | It represents a thematic grouping, typically with a heading; the Standard says it is not a generic container and is appropriate when its contents would be listed in an outline. Treat this as guidance, not an automatic violation. | [sections](https://html.spec.whatwg.org/multipage/sections.html) |
| `article` | Meaning | A complete or self-contained composition that is, in principle, independently distributable or reusable. Nested articles are related to the outer one. | [sections](https://html.spec.whatwg.org/multipage/sections.html) |
| `nav` | Meaning and authoring guidance | It represents major navigation blocks. "Not all groups of links on a page need to be in a nav element"; a `footer` alone is often enough for a short link list. | [sections](https://html.spec.whatwg.org/multipage/sections.html) |
| `aside` | Meaning and authoring guidance | It represents content only indirectly related to its surroundings; it is not for mere parentheticals. | [sections](https://html.spec.whatwg.org/multipage/sections.html) |
| `header` / `footer` | Meaning and context constraints | Neither is sectioning content and neither starts a new section. Check allowed descendants and ancestors in the Standard for exact context rules. | [sections](https://html.spec.whatwg.org/multipage/sections.html) |
| `main` | Requirement | A document must not have more than one visible `main`; ancestor constraints also apply. | [grouping-content](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) |
| Headings | Requirement and recommendation | Successive heading levels must not jump by more than one. A document with headings should have a level-1 heading; one without it is conforming but not encouraged. Multiple `h1` elements are permitted. | [sections: headings and outlines](https://html.spec.whatwg.org/multipage/sections.html#headings-and-outlines) |
| `a` | Content-model requirement | With `href`, it is a link. Its transparent content model forbids interactive-content descendants, nested `a` elements, and descendants with `tabindex`. Without `href`, it is a placeholder. | [text-level-semantics](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-a-element) |
| `button` | Content-model requirement and default behaviour | Its content model is phrasing content, with no interactive-content descendants or descendants with `tabindex`. Missing `type` is Auto; it acts as a submit button only under the Standard's conditions, including the absence of `command` and `commandfor` and not being the first child of `select`. | [form-elements](https://html.spec.whatwg.org/multipage/form-elements.html#the-button-element) |
| `img` | Requirement and role-dependent text alternative | An `alt` attribute is required except in cases the Standard lists. Its value depends on the image's role and content. | [images](https://html.spec.whatwg.org/multipage/images.html) |
| Tables | Requirement and recommendation | Tables must not be used as layout aids. `caption` titles a table; the Standard says it should be omitted when the table is the only content of a `figure`, in favour of `figcaption`. Header cells are `th`, associated using `scope` or `headers` as appropriate. | [tables](https://html.spec.whatwg.org/multipage/tables.html) |
| `label` | Mechanism | The `label` element represents a caption and can associate with a control by `for` or by wrapping the control. This describes the HTML mechanism, not an accessibility criterion for every control. | [forms: label](https://html.spec.whatwg.org/multipage/forms.html#the-label-element) |
| `details` / `summary` | Content-model requirement and meaning | `summary` is the first child of `details`; its content is phrasing content, optionally mixed with heading content. | [interactive-elements](https://html.spec.whatwg.org/multipage/interactive-elements.html) |
| Content categories | Content-model requirement | Authors "must not use HTML elements anywhere except where they are explicitly allowed, as defined for each element"; each element's content model, expressed partly through categories (flow, phrasing, interactive, heading, sectioning), decides what is allowed. The per-element "contexts" entries are non-normative. Check the element's own content model before judging nesting. | [dom: content categories](https://html.spec.whatwg.org/multipage/dom.html#kinds-of-content) |

Both the `button` and content-category rows were checked on 2026-10-09 against the linked pages; the `button` page was read only up to its first 100,000 characters, so confirm exceptions in the full text before turning a row into a rule.

## B. Project conventions (not conformance requirements)

These come from the project's purpose of reducing Div soup ([ADR 0003](../../../docs/adr/0003-design-comp-centered-workflows.md)) and [specification section 5](../../../docs/product-spec.ja.md). They may be applied by default and recorded as `convention`; a deviation needs a stated reason, and a violation is never a standards failure.

- One `h1` representing the page, set before other headings.
- A page-level `main`; `header`/`footer` used for the page frame when one exists.
- Repeated peer items go in `ul`/`ol` rather than sibling `div`s.
- Do not wrap every container in `section`; do not make every card an `article`.
- Navigation link sets use a list inside `nav`.
- Footer: a rights-holder-confirmed copyright line plus navigation to main pages. This is a project production standard, not a legal duty.
- No historical rigid wrappers or element swaps kept for tradition in the shared baseline (for example a mandatory section under `main`).

## B2. Accessibility guidance (not HTML conformance)

Label and instruction needs come from accessibility guidance, not from the HTML Standard's content models; failing them is not an HTML conformance failure. Tag them with the accessibility source and hand the check to [accessibility](../../accessibility/SKILL.md).

- Provide labels or instructions when user input is required ([WCAG 3.3.2, Labels or Instructions](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html)). Prefer visible labels that are programmatically associated with the control; `label` with `for` or wrapping is the HTML mechanism for the association (row `label` above).
- Placeholder text is not a substitute for a label, and grouping related choices with `fieldset` and `legend` is a pattern to apply where a group needs a shared label. Both are WAI guidance: see [WAI form-label guidance](https://www.w3.org/WAI/tutorials/forms/labels/) and [WAI grouping controls](https://www.w3.org/WAI/tutorials/forms/grouping/).

## C. Judgment (content reading)

Whether a group is "ordered", whether a quote is a quotation, whether an image is informative or decorative, whether data is tabular, and whether a link set is "major navigation" are readings of the content. Record the evidence and the rejected alternative; mark `needs_review` when the evidence is only visual.

## What automation can and cannot establish

A conformance checker (for example the W3C Nu HTML Checker) could in principle establish some content-model and attribute constraints. It cannot establish authoring recommendations, project conventions, or content judgment. No checker is wired into this repository; until one is run and its output recorded as Evidence, structural conformance is `untested`. Implement owned rules and real fixtures before claiming automated support; see [rule authoring](../../../docs/rule-authoring.md).
