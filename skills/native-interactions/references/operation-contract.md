# Operation contract — draft guidance

Use this reference when creating or reviewing links, actions, native data-entry controls, or forms with changing states. It is a decision aid, not a validator. Report what was inspected and keep runtime and assistive-technology checks `untested` until performed.

## Choose from the user's intent

Resolve the operation from the supplied content, brief, owner direction, or existing behaviour before selecting an element:

| Intent | Native element | Basis |
|---|---|---|
| Navigate to a known URL or in-page target | An `a href` link | HTML Standard: an `a` with `href` is a hyperlink. |
| Perform an action or submit/reset a form | A button with `type` explicitly set to `button`, `submit`, or `reset` | Button behaviour is defined by the HTML Standard. An explicit `button type` is a project convention because the Standard's missing-value behaviour depends on context. |
| Enter or choose a value | A suitable native form control with a label programmatically associated with it; provide visible text and instructions where needed | WCAG 2.2 SC 3.3.2 requires labels or instructions when content requires user input. WAI recommends an associated label; a visible label is the default design recommendation, not a blanket criterion requirement. |
| Operation or destination is unknown | Keep it open in the blueprint. Ask only for the essential decision if the missing information changes the element, target, or requested behaviour; continue independent work. | Do not invent destinations, actions, field meaning, or endpoints. |

A visual style does not determine an element: a button-shaped destination remains a link; a link-looking in-page action remains a button. Do not use a clickable generic element, `href="#"` as a placeholder, or an `a` without `href` as an action. A layout-only `div` remains appropriate when no meaningful HTML element fits the content.

```html
<!-- Avoid: this action is disguised as a link; the placeholder destination can navigate to the page top. -->
<a href="#" onclick="showPlans()">View plans</a>

<!-- A known destination is a link, even if CSS makes it look like a button. -->
<a class="button" href="/plans">View plans</a>

<!-- A local disclosure is an action; expose its state with the native control. -->
<button type="button" aria-expanded="false" aria-controls="site-navigation">
  Open navigation
</button>
<nav id="site-navigation" hidden>
  <a href="/products">Products</a>
</nav>

<label for="email">Email address</label>
<input id="email" name="email" type="email" autocomplete="email">
```

`aria-expanded` and `aria-controls` are an implementation choice for this disclosure example, not a blanket requirement for every button. Define how state changes and focus behaves from the actual interaction design.

## Asynchronous form state contract

For a form that updates without a full page navigation, record the expected visible message, programmatic relationship/notification, focus outcome, entered-value retention, and retry path for each state. Use the supplied endpoint and validation rules only; if they are absent, mark them open rather than simulating a real submission.

| State | User-visible outcome | Programmatic update | Focus and recovery |
|---|---|---|---|
| Idle | Labels, instructions, required fields, and submit action are available. | Associate labels and instructions with their controls. | Normal keyboard order reaches fields and submit action. |
| Submitting | Clearly show that the request is in progress and prevent accidental duplicate submission when needed. | If the status changes without moving focus or navigating, expose that status to assistive technology using an appropriate mechanism. Do not add ARIA without checking whether the update already causes a context change or is otherwise announced. | Keep focus predictable; preserve entered values while pending. |
| Success | Confirm the requested action completed. | Make an in-place success status available programmatically when it is not otherwise announced. | If replacing or moving focus, place it at a useful heading/confirmation; otherwise leave focus where it remains useful. State whether another submission is possible. |
| Field error | Identify each affected field, explain the problem, and give a correction when known. | Connect the error to its field; provide an error summary when useful. | Consider moving focus to the first invalid field or a useful error summary. Preserve other entered values and allow correction/retry. |
| Server error | Explain that submission did not complete without blaming the user or discarding input. | If shown in place without a context change, expose the status programmatically. | Preserve values; describe whether retry is possible and whether support/another path is available. |

These are planning and review prompts, not requirements to use ARIA roles or move focus in every implementation. WAI's form guidance describes techniques for feedback; WCAG's status-message criterion concerns relevant updates that do not receive focus. Choose the behaviour that fits the real interaction, then verify it with the available browser and assistive technology. Do not claim conformance from this table.

## Sources and force

Checked 2026-10-09; links are primary sources. The WHATWG HTML Standard is normative for its defined element semantics and algorithms. WCAG 2.2 success criteria are normative requirements when claiming WCAG conformance; WAI Understanding documents and techniques are informative guidance, not additional requirements. Project policy to set `button type` explicitly is a convention.

- WHATWG, [the `a` element](https://html.spec.whatwg.org/multipage/text-level-semantics.html) (Living Standard last updated 2026-10-07; retrieved 2026-10-09).
- WHATWG, [the `button` element](https://html.spec.whatwg.org/multipage/form-elements.html) (Living Standard last updated 2026-10-07; retrieved 2026-10-09).
- WHATWG, [forms](https://html.spec.whatwg.org/multipage/forms.html) (Living Standard last updated 2026-10-07; retrieved 2026-10-09).
- W3C WAI, [Form Notifications](https://www.w3.org/WAI/tutorials/forms/notifications/) (updated 2022-06-03; retrieved 2026-10-09): advice on visible feedback, field errors, and announcing dynamic updates.
- W3C WAI, [Labelling Controls](https://www.w3.org/WAI/tutorials/forms/labels/) (updated 2024-05-13; retrieved 2026-10-09): recommended programmatic label association and cases where a label can be visually hidden.
- W3C WAI, [WCAG 2.2 SC 3.3.2: Labels or Instructions](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html) (retrieved 2026-10-09).
- W3C WAI, [WCAG 2.2 SC 4.1.3: Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) (retrieved 2026-10-09). This Understanding page is informative; the success criterion itself is in the [WCAG 2.2 Recommendation](https://www.w3.org/TR/WCAG22/#status-messages).

This reference and its static examples are not a conformance result and do not establish browser, screen-reader, or runtime support.
