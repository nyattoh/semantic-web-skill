# Comp-to-HTML — draft guidance

Use when a design comp is supplied and the request calls for semantic HTML or an implementation plan. Read the [shared workflow](workflow.md) for intake, blueprint, checks, result states, and handover. This path is operational guidance, not a validated conversion tool or a promise of design-format support.

## 1. Inspect the supplied comp

Identify the supplied artefact and version, pages/views, viewport dimensions, assets, typography, content, and any state or responsive annotations. Open only formats supported by tools actually available and authorised. If a design-tool file is inaccessible, request an export or inspect supplied images; record the resulting limits. A link or filename alone is not evidence that its design was inspected.

Inventory the visible content groups and controls. Separate observed details from inferences: a static comp can show a button but cannot establish its action, keyboard operation, menu modality, validation behaviour, or narrow-screen layout. Use supplied interaction notes; list consequential gaps for the human. Minor spacing or breakpoint choices may be provisional assumptions.

Extract reusable design values only where supported by the artefact: colours, spacing relationships, type hierarchy, and asset roles. Label approximations from an image. Use the supplied content/assets or clearly identified placeholders; do not invent testimonial facts, destinations, claim evidence, or unavailable fonts.

## 2. Map meaning before writing DOM

Produce the semantic blueprint before HTML. Connect each comp region to its content purpose, reading order, element candidates and rationale, controls/states, and responsive behaviour. Mark unresolved meaning separately from visual detail.

- Distinguish page headings and content hierarchy from decorative text styling.
- Treat repeated cards according to their relationship; choose list, description list, article, or table by content, not their rectangular appearance.
- Distinguish links from actions and ordinary navigation disclosures from modal interfaces. Specify labels, states, and focus behaviour before scripting.
- Identify decorative, informative, and functional images; plan alternatives appropriate to their role.
- Identify footer navigation and rights information using specification section 5, without inventing a rights holder.

When the comp conflicts with semantics or accessibility, identify the region, requirement/source, and minimum proposed departure. Resolve objective defects within the authorised implementation while preserving the intended visual hierarchy. If a consequential choice needs the human, pause that part and proceed with independent regions; do not silently change the product's meaning or leave a known defect unreported.

## 3. Implement the first pass

For an implementation request, follow the existing stack and conventions. Build semantic source from the blueprint, then use CSS to express layout and presentation, and native controls plus scoped JavaScript for requested behaviour. Preserve meaningful DOM order and existing unrelated edits. Do not add a framework solely for this skill.

Complete requested responsive layouts and interaction states, including relevant open/closed, focus, loading, empty, success, and error states. Do not invent a backend or describe a simulated form as connected. If only an implementation plan was requested, deliver the blueprint, proposed component/element mapping, design values, state plan, and verification plan without changing source.

Aim for near-final code quality in the first pass. Missing browser/device access limits verification; it does not justify knowingly incomplete markup, inaccessible controls, or decorative substitutes for meaningful elements.

## 4. Compare and verify

Use the shared checks on the resulting code and rendered page with available, permitted tools. Compare like viewports/states and record the actual rendering environment, including font/asset differences. Inspect visual hierarchy, spacing, text wrapping, target areas, and intentional departures; test semantics, keyboard operation, and focus separately from visual similarity.

Explore content-driven width boundaries and state transitions instead of declaring responsiveness from one matching image. Keep unavailable physical-device and assistive-technology checks explicit. Repair observed implementation defects within scope and preserve evidence of failed and subsequent checks.

## 5. Return for refinement

Deliver code or plan locations, the inspected comp/version, blueprint, assumptions, departures, six-state results, and evidence. Show the human which regions/states need direction and distinguish preference questions from unresolved defects or blocked checks. First-pass quality is an aim, not a numeric score or a substitute for evidence. Human feedback starts refinement; it does not retroactively turn untested checks into passes.
