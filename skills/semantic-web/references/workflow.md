# Shared workflow — draft guidance

Apply this procedure to comp-to-HTML, brief-to-comp, and review under [ADR 0003](../../../docs/adr/0003-design-comp-centered-workflows.md). Read the chosen path from the [entry skill](../SKILL.md). These instructions do not execute checks or validate runtime behaviour; the [starter limitations](../../../docs/starter-status.md) still apply.

## Intake and assumptions

Record enough context to act; reuse supplied answers rather than requiring a questionnaire:

- Outcome and scope: design comp, design specification, HTML/CSS plan, implementation, or review; target pages and revision; permitted edits and delivery location.
- Inputs: comp or brief, content and assets, existing source/design system, interactions, and rights or restrictions affecting their use. Record unavailable or inaccessible inputs.
- Audience and content: primary task, intended reading order, language and writing direction, real or placeholder text, brand requirements, and content owner.
- Constraints: existing stack and conventions, required states, responsive expectations, accessibility evaluation target, browser/device requirements, and available tools.
- Markets when relevant: distribution or sales markets, product/service, audience, medium, publication date, and evidence supporting consequential claims. Do not infer these from page language.

Keep an assumption list with the choice, reason, effect, and who can confirm it. Use reversible assumptions for missing minor detail and proceed. Ask before dependent work when an unknown changes content meaning, a required interaction, permission, or the requested deliverable. Distinguish proposed copy and labelled placeholders from supplied facts; do not invent factual claims, supported environments, installed tools, or human approval.

Inspect the actual environment before selecting methods. A browser, design canvas, validator, assistive technology, or physical device mentioned in the specification is a candidate, not an installed capability. Use existing authorised tools; a missing canvas can use the brief-to-comp fallback. Label a missing environment for a required check as `blocked`; a check not attempted as `untested`.

## Request coverage

For a build, copy every explicit user requirement and prohibition into a compact ledger before design or code. Preserve literal copy, URLs, directions, timings, and no-go constraints. Map each row to a target region/state, implementation, and an observable check with its expected result:

| Request | Target/state | Implementation | Check and expected result | Result state |
|---|---|---|---|---|

Include only relevant rows, but do not omit a requested item because it seems cosmetic. For interaction or motion, name the trigger, visible effect, affected property, direction and reduced-motion behavior. If text sits beside an icon, verify the line's measured clearance and whether the icon moves. For copy, name the audience and task; check visible text and destinations against supplied facts. The ledger carries intent into implementation and reconciliation, not a quality score.

## Semantic blueprint before DOM

Write a short outline or mapping alongside the design. Each group should identify:

- Content purpose and source, reading order, heading hierarchy, and candidate landmarks.
- Whether items form an ordered sequence, unordered collection, name/value relationship, independent article, or tabular data, with the reason for the choice.
- Navigation destinations versus actions, visible/accessible names, control type, states, keyboard behaviour, and focus entry/return where relevant.
- Image purpose and planned text alternative, captions or longer descriptions where needed; form labels, instructions, and error relationships.
- Layout and content changes at narrow/wide widths, text expansion, writing direction, and disclosure placement.

For example: feature cards describing peer features -> an unordered collection with item headings; “View plans” navigating to a page -> a link; “Open navigation” toggling a panel -> a button with an explicit closed/open state. Appearance alone does not establish semantics.

Use [semantic-html](../../semantic-html/SKILL.md) and specification section 5 for element choices and content-model constraints. Layout containers may be `div`; replacing every container with `section` does not create semantic source. Choose headings by content hierarchy, not font size. Keep content order meaningful when CSS changes the visual arrangement. Reference shared criteria through their owner rather than copying thresholds here.

For review, build this outline from observed source/content as the comparison basis before proposing a DOM change. Distinguish existing behaviour from the proposed blueprint.

## First pass and review

For creation, complete the selected path and deliver code intended to be near-final in quality: appropriate content models, maintainable styles, complete requested states, meaningful labels, and robust responsive behaviour. The visual interpretation may still need human refinement. “First pass” is not permission to leave known defects as a rough scaffold; unavailable verification remains explicit.

For review:

1. Identify the source revision or URL and pages/states in scope. Inspect the actual source and rendered interface where access permits; keep source-only, rendered-only, and runtime observations separate.
2. Compare content meaning, DOM, visual presentation, and interactions against the blueprint and applicable requirements. Reproduce a finding in the affected state/environment when possible.
3. Record affected location, expected/observed behaviour, impact, evidence, and a focused remedy. A visual preference is a refinement proposal, not a standards violation.
4. Return findings and result states. If corrections were also requested, make scoped edits and recheck the affected behaviour using permitted methods; otherwise leave code unchanged.

## Checks and evidence

Reconcile every ledger row with its artifact and check. Run applicable checks from the request and specialist drafts with tools actually available. For a design-only delivery, check the design specification/comp itself; future DOM and runtime checks remain separate, usually `untested`. Do not silently skip a row or claim keyboard/assistive-technology support from annotations.

- **Structure:** inspect the resulting DOM, headings, landmarks, collections, element placement, nested interactive content, labels, and image alternatives. Use an available validator when permitted; record semantic judgements separately from parser results.
- **Visual and responsive:** inspect actual rendered output against the comp or design specification at agreed widths and key states. Check hierarchy, typography, spacing, assets, overflow, long/translated text, and fonts. Explore breakpoint edges, zoom, orientation, and input changes; record intentional departures. A single image cannot establish responsive behaviour.
- **Interaction:** exercise navigation, disclosures, dialogs, and forms with the applicable keyboard and pointer/touch methods. Check open/close transitions, hidden content's focus reachability, focus return, submission/error states, and state after viewport changes. When a transition is requested, inspect its base and active state and an intermediate computed value; a final screenshot alone does not prove that it ran.
- **Accessibility:** inspect names, roles, states, keyboard order, visible/unobscured focus, contrast, reflow, and actual hit areas against the [accessibility-owned criteria](../../accessibility/SKILL.md). Use assistive technology when available and in scope. Separate automated output from manual tasks.
- **Content and markets:** when applicable, inspect claims, disclosures, translations, and visible/metadata consistency. Use [regional-compliance](../../regional-compliance/SKILL.md) and [search-content](../../search-content/SKILL.md) for dated research. Follow ADR 0002 for advisory findings.

Record target revision, timestamp, method/tool/version, steps, expected and observed behaviour, and evidence location. Browser evidence also needs OS/browser, viewport, DPR, zoom, and input; distinguish physical devices from emulation. DOM evidence supports structure, images support display, interaction records support behaviour, and manual records support only the tasks performed.

Fix observed defects within the authorised creation/correction scope, then rerun only affected permitted checks. Preserve the original failure and the later result. If checks are prohibited, report that limitation; do not substitute a fabricated run.

## Result states

Use one of the six states for each applicable requirement or proposed check, without a quality score or percentage:

- `passed`: the stated check actually ran and its evidence meets the stated requirement in the recorded scope.
- `failed`: an actual observation does not meet the requirement; include reproduction and impact.
- `untested`: the check was not performed; state what remains to be done.
- `blocked`: an essential input, permission, source, or environment prevented the check/action; name the dependency and how to unblock it.
- `needs_review`: interpretation or a human decision remains; identify the reviewer role and question. Agent legal/provider-policy interpretations always use this state with sources and retrieval date.
- `not_applicable`: the condition does not apply; state the applicability reason. Missing evidence or an unsupported market is not an applicability exemption.

Where no implemented rule ID exists, reference the specification section or primary source and label the proposed check; do not invent an executable rule, schema, or automatic result. Keep exceptions separate from observed failures. Regional compliance coverage without a validated regional pack is unsupported; this starter has no validated pack. Separately scoped semantic, design and interaction checks retain their own result states. Research for additional markets can produce a scoped advisory finding, not a claim of validated regional support.

## Delivery and human-directed refinement

Use [handover guidance](../../../docs/handover.md) and [evidence-reporting](../../evidence-reporting/SKILL.md). Deliver:

- Artefact paths/URLs and format, target revision, completed scope, blueprint, assumptions, and intentional design departures.
- Checks actually run, result states, evidence, and unavailable/prohibited checks; sources and dates for advisory findings.
- Unresolved decisions and defects with affected scope, owner/role, dependency, and next action.
- A short refinement agenda for the human: content/order, visual hierarchy, brand interpretation, or behaviour that needs their direction. Point to concrete regions/states so they can respond precisely.

End the first pass by returning control to the human. When they provide refinement, update the affected blueprint/design/code and repeat only the affected checks. Do not start an unrequested redesign loop or replace the result states with a claimed improvement score.

The report may be complete while verification is incomplete. If mandatory applicable checks remain `failed`, `untested`, `blocked`, or `needs_review`, do not label the product verified, release-ready, or all-passing.
