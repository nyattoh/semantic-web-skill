# Content Patterns — draft guidance

Patterns for deciding structure from content meaning. Each gives the question to ask, the candidates, and a skeleton. Skeletons are illustrations of a decision, not fixtures: none has been run through a conformance checker, and none is a rule. Nesting claims are checked against [content models](content-models.md). Basis tags identify the source, not its normative force: a Standard recommendation is not a conformance failure. Use the **standard** / **convention** / **judgment** tags from [SKILL.md](../SKILL.md).

Visual card styling never justifies `article` or `section` by itself. At the comp stage, decide these patterns in the comp (what is grouped, which text is a heading, which label is visible) so the HTML stage only transcribes them. Keep historical rigid wrappers and element substitutions out of the shared baseline.

## Choosing a collection

| Content reads as | Candidate | Basis |
|---|---|---|
| Items whose order matters (steps, ranking, sequence) | `ol` | standard (meaning) + judgment (is order intended?) |
| Peer items, order not important | `ul` | standard + judgment |
| Names/terms paired with descriptions or values | `dl` | standard + judgment |
| Independent self-contained items with their own heading | list of `article`, only if each is independently distributable | judgment |
| One-off blocks with no peer relationship | no list; headings and paragraphs | judgment |

Evidence to cite: the copy itself (numbering words such as "Step 1", dates, rankings), not the visual rhythm. If the comp is an image and the copy shows no order, record `inferred` and prefer `ul`.

## Headings and landmarks

Ask: what is this region's purpose, and does the document outline need to list it?

- Give each region that the outline should list a heading; the heading level reflects hierarchy, never font size.
- A thematic group that belongs in the document outline can use `section`; a visible heading is a useful signal, not a conformance test. This is authoring guidance. A purely visual wrapper or decorative band → `div`.
- `nav` only for major navigation. A short link list inside `footer` needs no `nav` (standard note); the project convention is to use `nav` for the main footer navigation.
- `aside` for tangential content, not for any side-by-side column.
- Comp stage: mark the heading text for every listed region; a region without visible heading text needs either one added or a stated reason for `div`.

```html
<main>
  <h1>…page heading…</h1>
  <section aria-labelledby="plans-h"><h2 id="plans-h">…</h2>…</section>
</main>
```

`aria-labelledby` on `section` is optional naming; whether it is needed is an accessibility decision, not a content-model requirement.

## FAQ

Ask: is it a set of question/answer pairs, a set of disclosures, or a set of short articles?

- **Plain Q&A, always visible** → `dl` with `dt` question and `dd` answer (each pair optionally wrapped in a `div`). Standard allows it; fitting is judgment. A `dd` may hold several paragraphs or a list.
- **Collapsible** → one `details` per item, `summary` as the question (phrasing, optionally with heading content). Open/close behaviour, keyboard and grouping belong to [native-interactions](../../native-interactions/SKILL.md).
- **Long, linkable answers** → a heading per question with paragraphs below; list wrapper only if peers.
- Do not fix every FAQ to one pattern. Record the chosen one and why.
- FAQ structured data and search eligibility → [search-content](../../search-content/SKILL.md), dated provider checks; do not assume markup alone earns anything.

```html
<dl>
  <div><dt>…question…</dt><dd><p>…answer…</p></dd></div>
</dl>
```

## Testimonials

Ask: are these quotations of a named or described person, and is each independent of the others?

- Default candidate (convention): `ul` > `li` per testimonial.
- Inside the item: `figure` > `blockquote` (the quoted words only) + `figcaption` (person, role, source). Standard requires attribution outside `blockquote`; `figure`/`figcaption` is one place to put it.
- Use `blockquote` only when the text is a quotation. A paraphrase or summary is a `p`.
- Photos of the person: informative or decorative? Decide per [images](#images-and-figures).
- Whether a testimonial may be published, and what it must be tied to, is a Claim question → [regional-compliance](../../regional-compliance/SKILL.md); carry it as `needs_review` and do not decide it here.

```html
<ul>
  <li>
    <figure>
      <blockquote><p>…quote…</p></blockquote>
      <figcaption>…name, role…</figcaption>
    </figure>
  </li>
</ul>
```

## Card grids

Peer cards → `ul` > `li`; the card's title is a heading at the next outline level. Make the title (or an explicit "read more" with a distinct name) the link; a full-card hit area can be done in CSS without wrapping the whole card in `a`. If a card is wrapped in `a`, the Standard forbids interactive content inside it, and the link's name becomes the whole card text (judgment: usually too long). Use `article` per card only if each card is an independently reusable item such as a post.

## Navigation and links vs buttons

Decision, from behaviour (evidence: the destination or the action, not the look):

| It does | Use | Basis |
|---|---|---|
| Goes to another URL or in-page target | `a href` | standard (meaning) |
| Performs an action on this page or submits | `button`; set `type` to match the intended action | standard (element meaning); convention (explicit `type`) |
| Changes a value | form control | standard (HTML control); accessibility criteria require suitable labels/instructions |
| Looks like a button but navigates | `a href`, styled as needed | judgment |
| Looks like a link but acts | `button` styled as needed | judgment |

Avoid `div`/`span` with click handlers, `a` without `href` acting as a button, and `href="#"` stand-ins (convention). Never nest interactive elements (standard for `a` and `button`). Primary navigation: `nav` > `ul` > `li` > `a`; mark the current page with the mechanism chosen by [native-interactions](../../native-interactions/SKILL.md) / [accessibility](../../accessibility/SKILL.md), not by colour alone.

Comp stage: label each clickable item as link or button and give its destination or action; a comp with only styled rectangles leaves this `open`.

## Images and figures

Ask: what is the image's role?

- **Informative** → `alt` conveys the information the image carries in context.
- **Functional** (inside a link or button) → `alt` describes the action or destination.
- **Decorative** → `alt=""`; do not write "decoration" in it. See the WAI [decorative images](https://www.w3.org/WAI/tutorials/images/decorative/) guidance.
- **Complex** (chart, diagram) → short `alt` plus a long description reachable nearby; chart data as a table if it is tabular.
- `figure`/`figcaption` only when the item is self-contained and referred to as a unit and needs a caption. Not on every image.
- Never invent `alt` text from the pixels alone when the role depends on the surrounding copy; mark it `needs_review` until a person confirms. Exact alt rules: [images](https://html.spec.whatwg.org/multipage/images.html) (not re-read in this pass).

## Tables

Ask: are the cells related by rows and columns of data, or is it a visual grid?

- Tabular data (pricing comparison with row and column headers, schedules) → `table`; `th` header cells with `scope` (or `headers` for irregular tables); `caption` for the title. The Standard says tables must not be layout aids.
- Visual grid of peer items → list or CSS layout, not a table.
- Comparison cards that are really a feature matrix → `needs_review`; ask the owner whether rows/columns carry meaning.
- Narrow-width reading of tables is a CSS/responsive matter → [css-foundations](../../css-foundations/SKILL.md), [responsive-verification](../../responsive-verification/SKILL.md).

## Forms

Ask: what data is requested, and how does each field get its name, constraints, errors and a fix hint?

- Accessibility criterion, not an HTML conformance rule: provide labels or instructions when user input is required; prefer visible, programmatically associated labels. Placeholder text is not a replacement for a label. At comp stage, show the label/instructions or mark them unresolved. See the [WAI form-label guidance](https://www.w3.org/WAI/tutorials/forms/labels/) and [WCAG 3.3.2](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html).
- Choose the input `type`, `autocomplete` and constraint attributes from the data, not from the look.
- Related radio/checkbox sets → `fieldset` + `legend` when the group needs a shared label; treat this as an accessibility pattern, not a blanket HTML conformance rule ([WAI grouping controls](https://www.w3.org/WAI/tutorials/forms/grouping/)).
- Submit with `button type="submit"` (or `input type="submit"`); set `type` explicitly for other actions as a project convention, since the HTML Standard's missing-value behaviour is context-dependent.
- Error text, how it is tied to the field, and the fix are an accessibility/interaction concern; record them in the blueprint as `interaction` and hand over to [accessibility](../../accessibility/SKILL.md) and [native-interactions](../../native-interactions/SKILL.md).
- Never invent field names, endpoints or validation rules the brief does not give; mark them `open`.

## Residual generic elements

`div` is correct for a wrapper that exists for layout or grouping with no meaning; `span` for an unlabeled text run that needs a hook. Record a one-phrase reason in the blueprint. A page where a generic element stands in for a list, heading, landmark, button or link is Div soup; report it with the element that should replace it, the content evidence, and the basis.

## What this guide cannot establish

Reading these patterns does not show that any markup is conformant, accessible, or what the owner wants. Report structural conformance as `untested` until a real check is run and recorded; report visual-only inferences as `needs_review`. This guide is not a tested implementation or an independent normative rule source; implement owned rules and real fixtures before claiming automated support.
