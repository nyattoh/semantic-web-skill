# Quickstart: use the drafts as repository context

[日本語](quickstart.ja.md) · [Current status](starter-status.md) · [Static comparison](../examples/semantic-comparison/README.md)

This is a human trial with nine skill drafts and three routes, not a supported installation procedure. Keep the whole repository available to your agent as local context; preserve its relative paths. Point to `skills/semantic-web/SKILL.md` from the repository root. Copying only that file loses its references. No particular host's discovery, invocation or runtime behaviour has been validated.

## 1. Choose the outcome and supply the inputs

Choose one route; combine routes only when your requested output needs both:

- **comp-to-html:** supply a comp or accessible export, the actual copy/assets, known destinations/actions and constraints. Request either an implementation or a plan. An image alone cannot establish source-code quality, DOM order, link targets or form behaviour.
- **brief-to-comp:** supply purpose, audience, content, brand and interactions; request a comp alone or a comp plus HTML. If an authorised design canvas is unavailable, accept a labelled design specification (or a local HTML preview when within scope). A fallback is not a native design-tool file.
- **review:** supply the existing source/revision and pages or URL, observations and review scope. Ask for findings; edits require a request that includes corrections. Source-only access leaves rendered and interaction checks outstanding.

State the permitted changes, delivery location, technical constraints, available tools, languages and intended markets where relevant. Reuse supplied facts; ask only for gaps that affect meaning, required operation or scope. Unknown form endpoints stay open: do not invent a backend, validation response or successful submission.

## 2. Read the smallest useful set

Start with the [entry skill](../skills/semantic-web/SKILL.md) and [shared workflow](../skills/semantic-web/references/workflow.md). Read [comp-to-HTML](../skills/semantic-web/references/comp-to-html.md) for that route, or [brief-to-comp](../skills/semantic-web/references/brief-to-comp.md) for its route. Review uses the shared workflow's review procedure. You do not need every repository document for every task.

Use [semantic-html](../skills/semantic-html/SKILL.md) for the semantic blueprint and markup decisions; follow its content-model/pattern references for the regions at issue. Add [native-interactions](../skills/native-interactions/SKILL.md) for controls/forms, [CSS](../skills/css-foundations/SKILL.md) for layout, [accessibility](../skills/accessibility/SKILL.md) for its applicable checks, and [responsive verification](../skills/responsive-verification/SKILL.md) for width/input changes. Read search or regional drafts only when relevant. Use [evidence reporting](../skills/evidence-reporting/SKILL.md) and [handover](handover.md) when delivering actual results. These are instructions to consult, not checks that run when read.

## 3. Copy and adapt this prompt

Fill in the first three lines, keep the repository as context, and attach only inputs you may share with that environment. No upload, paid service or installation is implied.

```text
Route: <comp-to-html | brief-to-comp | review>
Inputs and outcome: <comp/brief/source, copy, destinations/actions, constraints, markets if relevant; plan/comp/HTML/findings>
Permitted changes and delivery: <files, output location; review-only unless corrections are requested>
Use this whole repository as local context; start at skills/semantic-web/SKILL.md. Treat its nine skills as drafts. Read the shared workflow, chosen route and smallest relevant specialist/reference set.
First deliver a semantic blueprint: content facts/sources, groups and reading order, headings, element choices/reasons, links versus actions, labels/states, responsive intent and open facts. Then produce the requested markup, comp/labelled fallback, or review findings within scope. Unknown destinations or form endpoints remain open; do not invent services.
Run the permitted checks available in this environment. Report requirement, target/revision, method/environment/time, expected/observed result and evidence location, using passed, failed, untested, blocked, needs_review or not_applicable. Reading instructions or viewing a screenshot is not verification. Return artefact paths and remaining decisions for human-directed refinement; do not claim host support, accessibility or legal conformance from these drafts.
```

## 4. Inspect the deliverables and evidence

Expect **semantic blueprint → markup/design or findings → actual checks/evidence**. For brief-to-comp, the blueprint precedes the design; continue to HTML only if requested. The [static comparison](../examples/semantic-comparison/README.md) shows content facts → element → interaction → check. Matching appearance does not prove code quality; compare actual markup, then perform the applicable runtime checks separately.

Keep the basis separate: `standard` identifies the source and its normative force, `convention` is project policy, `judgment` is a content interpretation. A convention mismatch is not automatically an HTML conformance failure.

Use one state per scoped requirement/check:

| State | Meaning |
|---|---|
| `passed` | An actual check ran and its recorded evidence meets the stated requirement. |
| `failed` | An actual observation did not meet the requirement; record reproduction and impact. |
| `untested` | The check was not performed; state the remaining work. |
| `blocked` | Required input, permission, source or environment is missing; name the dependency. |
| `needs_review` | Interpretation or a human decision remains; name the reviewer and question. |
| `not_applicable` | The condition does not apply; explain why. Missing evidence is not this state. |

For example: target `fixed.html`, requirement “Clear note is a non-submit button”, method “Python HTMLParser fixture assertion”, expected/observed `button type="button"`, state `passed`, evidence the local test output, plus the run timestamp and Python/OS versions. That passes only the static assertion. Keyboard activation and focus remain `untested` until actually exercised. An unknown enquiry endpoint is `blocked`, not a simulated success. Legal/provider-policy interpretations remain advisory `needs_review`.

Hand back paths, evidence and unresolved decisions so the human can direct refinement. A complete report can still contain unverified product behaviour; do not describe it as release-ready.

## 5. Try the local static examples

Read [bad, fixed and boundary examples](../examples/semantic-comparison/README.md), inspect their source, and optionally open their HTML files locally. No build, dependency download or installer is needed. This opening procedure does not assert browser compatibility. To reproduce the narrow documentation/fixture checks, use the command and tested environment in [tests](../tests/README.md).

These checks are not a generic HTML auditor, WCAG assessment or agent validation. Runtime demonstrations, engine/installer, host behaviour, conformance, assistive technology, real devices and regional packs remain unvalidated. Consult [current status](starter-status.md) for the precise boundary.
