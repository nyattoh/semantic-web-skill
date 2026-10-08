# Brief-to-comp — draft guidance

Use when there is no design comp. Create a design that already accounts for meaning, operation, and intended markets; use it for HTML when implementation is also requested. Read the [shared workflow](workflow.md). Canvas access, native comp formats, and agent execution remain unvalidated in this starter.

## 1. Shape the brief and blueprint

Use supplied purpose, audience, primary task, content, brand, assets, interactions, technical constraints, languages, and intended markets. Identify the required output: comp alone, design specification, or comp plus HTML. Ask only about gaps that materially change the design; record provisional choices for the rest.

Outline the page's content and reading order before drawing or creating DOM. Build the semantic blueprint with heading levels, landmark candidates, collection relationships, image purpose, controls, states, labels, and responsive changes. This lets semantic requirements shape the comp rather than being added after its layout is fixed.

Use real content where available. Label placeholder text and assets, consider long or translated content and writing direction, and do not create factual claims or customer quotations. For public claims, identify evidence and disclosure needs early through the regional specialist. Do not assume the publication market from language or claim researched-market coverage as validated support.

## 2. Choose an honest design deliverable

Inspect the current environment and use an available, authorised design canvas when it can produce the requested artefact. Do not assume Figma or any other service is installed, accessible, or permitted to receive the inputs.

If no suitable canvas is available:

- **Design specification:** deliver a labelled specification with the content outline, visual layout, type/colour/spacing choices, asset roles, control/state annotations, and responsive behaviour. This is the default when no rendered preview can be produced.
- **HTML preview:** where within scope and local rendering tools are available, use the specification and blueprint to create a labelled HTML preview. It demonstrates the proposed design in a browser; it is not a native design-tool comp. Record whether it was actually rendered, the environment, and any simulated interactions.

The specification and blueprint must precede any fallback HTML. Keep the distinction between the intended design, a rendered preview, and the final site implementation. If a native comp file is required but unavailable, mark that deliverable `blocked`, explain what capability/input is missing, and offer the specification as interim work; do not claim the fallback fulfils the native-file requirement.

## 3. Create the semantically informed design

Develop one coherent first pass using the brief, blueprint, and existing design system where supplied. Choose layout and typography to make the content hierarchy legible. Document:

- The relationship between each visual region and its content group, heading, or navigation purpose.
- Wide and narrow layout behaviour, meaningful reading order, content-driven breakpoints, long text, localisation, and writing direction.
- Actual control hit areas using the accessibility-owned criteria; visible labels, focus appearance, contrast, and non-colour cues.
- Required interaction states and transitions, keyboard paths, focus management, and touch operation without hover dependence.
- Image alternatives, captions, form instructions/errors, and any evidence-related disclosures in their intended context.

Provide representative views and state annotations, or describe them explicitly in the specification when drawing is unavailable. Comp dimensions and annotations express design intent; they do not prove DOM structure, accessible names, or runtime behaviour.

## 4. Inspect the design; continue when requested

Inspect the produced artefact against the brief and blueprint. Check content completeness, hierarchy, label clarity, target-area plans, contrast where it can actually be measured, and narrow/long-text arrangements. Record the method, evidence, and result states. If the artefact cannot be opened/rendered, say so rather than claiming a visual inspection.

For **comp-only** work, return the design artefact or labelled fallback and stop at that scope. List later DOM, browser interaction, and assistive-technology checks as outstanding; design intent does not pass them.

For **comp plus HTML**, record the design artefact/specification version and proceed through [comp-to-HTML](comp-to-html.md) using the blueprint. The original request supplies authorisation for that continuation; do not add an automatic approval gate. Pause only decisions that materially need the human. Carry assumptions, states, and disclosures into implementation, then perform the applicable permitted checks.

## 5. Hand over to the human

Deliver artefact locations and exact format: native design-tool comp actually produced, exported image, design specification, or HTML preview. Include the brief interpretation, blueprint, assumptions, actual inspections/checks, six-state results, and remaining work. A design specification is a fallback, not evidence that a visual comp exists.

Invite concrete refinement direction on content/order, layout, brand, and interactions. End the first pass with control returned to the human; apply their feedback in the next iteration and recheck affected design/code. Do not use scores or describe draft guidance as validated runtime quality assurance.
