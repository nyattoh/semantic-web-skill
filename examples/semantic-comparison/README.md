# Semantic comparison — static source fixtures

[日本語 quickstart](../../docs/quickstart.ja.md) · [English quickstart](../../docs/quickstart.en.md) · [Tests and limits](../../tests/README.md)

Read the source of [bad.html](bad.html), [fixed.html](fixed.html) and [boundary.html](boundary.html), then optionally open the files locally in a browser. They contain fictional, rights-cleared text written for this example, embedded CSS and no external assets, dependencies or server. They require no build or installation. Opening a file is a manual trial, not evidence of browser support.

The first two fixtures keep related content and broadly similar styling, but no rendered similarity or quality measurement has been made. Source-code quality cannot be inferred from appearance. **Bad is intentionally flawed; fixed corrects only the documented choices and is not a conformance or accessibility result.** Boundary prevents the assumption that every grid needs a list or that every form-looking panel has a known backend. These are source fixtures, not verified end-to-end runtime demos.

## Semantic blueprint: facts before elements

The supplied facts here are the fictional copy and the explicit local interaction brief below. They are not conclusions inferred from a screenshot. In a real visual-only task, unknown targets, grouping and labels remain `needs_review` until confirmed.

| Content facts | Element | Interaction | Check |
|---|---|---|---|
| “View plans” navigates to the known `plans` region of the same document. | Fixed: `a href="#plans"`; bad: clickable `div`. | Native in-page navigation is intended; it is not a clear/reset action. | Static assertion checks actual tag, href and target. Browser keyboard navigation remains `untested`. |
| “Clear note” clears only the temporary local textarea. | Fixed: `button type="button"`; bad: `a href="#"`. | Tiny local handler clears and returns focus in fixed. No storage or network service. | Static assertion checks non-submit type and absence of href. Activation/focus must be tested separately. |
| Local notes and Clear notes are two unordered peer features. | Fixed: `ul > li`; bad: sibling `div` cards. | No card-wide action; text is informational. | Fixture parser checks direct child tags. Whether content is a collection is a documented judgment, not something the parser discovers. |
| The local textarea has a known visible label. | Fixed: `label for="local-note"` and matching `textarea id`; bad: placeholder only. | Fixed uses a local `form method="dialog"` inside an already-open, non-modal `dialog`; no server submission. | Static assertions check label association, form method and enclosing dialog. Labels/focus in assistive technology remain untested. |
| Boundary: Document purpose and Enquiry preview are independent regions. Their adjacency is only layout. | `div` layout wrapper containing two headed `section` regions, no forced list. | No sequential task or peer-item collection is intended. | Static assertion preserves the legitimate `div` and sections. A count of divs is not a semantic-quality test. |
| Boundary: an unknown endpoint and unknown submission contract prevent a connected enquiry. | Disabled `fieldset`, illustrative label/textarea, disabled `button type="button"`; no `form` or invented action URL. | Intentionally inactive preview; no simulated submit, success, error or backend. | Static assertions check disabled controls and absence of form/action; service delivery is `blocked`. Owner must supply requirements. |

Reading order follows the source: heading, navigation, plan features, local editor. The grid CSS is presentational; responsive correctness has not been measured. The boundary's disabled wording and field are explicitly illustrative, not invented production requirements. Once a real submission contract is supplied, use the [native interaction guidance](../../skills/native-interactions/SKILL.md) for states, focus, error handling and retry, then test the actual implementation.

## Basis and current primary sources

Sources checked 2026-10-09. These summaries explain choices, not a full rule implementation:

- **standard, semantic description:** an anchor with `href` represents a link; this known destination uses one. [WHATWG: a](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-a-element).
- **standard, behaviour:** explicit button type selects behaviour; `type="button"` needs the local handler to perform this action. **convention:** this example makes the type explicit. [WHATWG: button](https://html.spec.whatwg.org/multipage/form-elements.html#the-button-element).
- **standard, description/recommendation:** `ul` expresses unordered items; `div` has no special meaning and can provide a styling wrapper. **judgment:** the feature copy forms peers; the boundary panels do not. **convention:** prefer a list for confirmed peer items. Generic blocks are not automatically invalid HTML. [WHATWG: grouping content](https://html.spec.whatwg.org/multipage/grouping-content.html).
- **accessibility guidance:** associate visible label text using a matching `for` and control `id`. [WAI: labelling controls](https://www.w3.org/WAI/tutorials/forms/labels/). **standard, recommendation:** a textarea placeholder should not replace its label; this recommendation is separate from a content-model requirement. [WHATWG: textarea placeholder](https://html.spec.whatwg.org/multipage/form-elements.html#attr-textarea-placeholder).
- **standard, behaviour:** dialog-method forms provide a local dialog submission mechanism rather than server delivery. The fixed action is explicitly non-submit, and the dialog is already open; this is not a modal lifecycle demo. [WHATWG: form submission method](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fs-method).

See the [semantic HTML draft](../../skills/semantic-html/SKILL.md) for how to record basis and normative force. Appearance, structural parsing and source recommendations cannot establish all content meaning or conformance.

## What has and has not been checked

Run the focused command from the repository root with Python available:

```powershell
python -m unittest discover -s tests/documentation -p "test_quickstart_examples.py" -v
```

The test uses Python's `HTMLParser` to inspect only these authored fixtures and asserts the specific tags, attributes and relationships above. Bad keeps the counterexamples while fixed and boundary retain the documented corrections and exceptions. This is not a generic HTML auditor, browser DOM parser, WCAG agent validation, conformance checker or behaviour engine. Passing its assertions says nothing about another site's code or an agent's performance.

The implementation run recorded 13 passing scoped tests on 2026-10-09 (Windows, PowerShell 7.6.6, Python 3.14.2). RED/GREEN output is retained in the author's ignored local `worklog/20261009-differentiation/` records, which are not bundled evidence; use the command above to obtain your own output. The static checks are `passed` only within that recorded scope. **NOT_RUN:** rendered comparison, JavaScript execution, pointer/keyboard/focus checks, responsive widths, accessibility tree/assistive technology, HTML conformance checker, physical devices, agent installation and regional validation. Runtime checks remain `untested`; the endpoint-dependent boundary stays `blocked`. No legal, search-performance or full accessibility claim is made.

For an independent runtime review, open the fixtures locally, record OS/browser/viewport/input/time, inspect source and accessibility tree, exercise the real anchor and local clear action, and confirm the boundary cannot submit. Preserve findings even when the scoped static suite passes. Do not upload private inputs to external validators without authorisation.
