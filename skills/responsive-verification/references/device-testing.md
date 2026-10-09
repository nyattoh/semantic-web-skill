# Device Testing — draft guidance

Record device, OS/browser/engine versions, viewport, DPR, zoom, input, date, and physical versus emulated testing. Explore ranges and breakpoint edges, orientation, dynamic viewport UI, soft keyboard, font differences, and interaction states. Reproduce narrow gaps and overflow before masking them with overflow rules.

## Check order when the layout changes

At each affected width, compare the visual order with the DOM reading sequence and keyboard focus order when focusable items are involved. Check whether each sequence still communicates the intended meaning and supports operation. The orders do not have to match exactly when the content is independent and more than one sequence is meaningful; record why the chosen sequence remains clear. If a visual rearrangement makes a meaningful sequence confusing or changes the expected relationship between content and controls, fix the source order or layout within scope, or record the unresolved design decision. Do not infer the intended order from a static comp alone when its meaning is unknown.

```html
<!-- Meaningful sequence: steps must read in their intended order. -->
<ol class="steps">
  <li>Choose a plan</li>
  <li>Enter your details</li>
  <li>Review and submit</li>
</ol>
```

```css
/* If this makes step 3 appear before step 1 at a narrow width,
   check and correct the mismatch rather than relying on the screenshot. */
.steps { display: flex; flex-direction: column; }
@media (max-width: 40rem) {
  .steps > li:first-child { order: 1; }
}
```

This is a meaning-based check, not a rule that visual and DOM order must always be identical. WCAG 2.2 SC 1.3.2 requires a programmatically determinable meaningful sequence when sequence affects meaning; SC 2.4.3 requires focus order to preserve meaning and operability. WAI's Understanding pages clarify that independent content may have more than one sensible order; those pages are informative, not extra normative requirements. Do not report a failure solely because two independent columns or peer cards have a different visual and DOM order.

Sources checked 2026-10-09:

- W3C WAI, [WCAG 2.2 SC 1.3.2: Meaningful Sequence](https://www.w3.org/WAI/WCAG22/Understanding/meaningful-sequence.html) (retrieved 2026-10-09; informative explanation; criterion in the [WCAG 2.2 Recommendation](https://www.w3.org/TR/WCAG22/#meaningful-sequence)).
- W3C WAI, [WCAG 2.2 SC 2.4.3: Focus Order](https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html) (retrieved 2026-10-09; informative explanation; criterion in the [WCAG 2.2 Recommendation](https://www.w3.org/TR/WCAG22/#focus-order)).

Read [specification section 8](../../../docs/product-spec.ja.md) for the design baseline. These static examples and checks are documentation guidance; they do not establish WCAG conformance, browser or device behaviour, or screen-reader support. This guide is not a tested implementation or an independent normative rule source. Implement owned rules and real fixtures before claiming automated support.
