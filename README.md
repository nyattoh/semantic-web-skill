# semantic-web-skill

[日本語（プロジェクトのメインガイド）](README.ja.md)

**From design comps to semantic HTML. From briefs to semantically informed design comps.**

An open project to help spread meaningful, semantic HTML source code. It aims to connect visual design and document meaning, so developers can consider content, interaction, accessibility, and intended markets whether they are translating a design into code or creating a design from a brief.

[Quickstart](docs/quickstart.en.md) · [Static comparison](examples/semantic-comparison/README.md) · [日本語版](README.ja.md) · [Product specification](docs/product-spec.ja.md) · [Current status](docs/starter-status.md) · [Contributing](CONTRIBUTING.md)

> **This repository is currently a starter containing design documents and draft skills.** It is not a completed audit tool, validated agent-skill distribution, or regional rule pack. See [current status](docs/starter-status.md) for limitations.

## Intended workflows

### 1. Design comp to HTML

Use a design comp, content, technical constraints, and intended markets to choose appropriate HTML elements and content structure. Then implement the page and record checks actually run, along with unresolved questions. The goal is to produce meaningful source code, not only a visual match.

### 2. Brief to design comp

When no comp exists, clarify the purpose, audience, content, brand, interactions, and intended markets. Shape the design with semantic structure in mind: content groups, headings, interaction targets and states, and responsive changes. This should give the later HTML implementation a sound starting point.

### 3. Review an existing site

Inspect its code, rendered pages, and interactions. Report improvement opportunities with sources and actual verification results. A review request does not authorise code changes or publication by itself.

These three paths reflect the accepted [design decision, ADR 0003](docs/adr/0003-design-comp-centered-workflows.md). The entry skill now describes all three paths as draft guidance. The product specification remains preserved; its amendment is recorded in [current status](docs/starter-status.md). Input formats (such as images or Figma), agent-specific execution, and runtime behaviour remain undecided or unvalidated.

## Carry every request into implementation

For a build, the entry skill turns each explicit requirement and prohibition into one coverage row: the requested wording/value, target region or state, implementation, observable check, and result state. This prevents details such as a motion direction, a fixed arrow, a specific link, or a mobile layout from disappearing inside a general design summary. The ledger is not a quality score; a requirement remains unresolved until its check passes or is honestly marked `untested`, `blocked`, or `needs_review`.

The supplied Sass pattern compiles to ordinary CSS like this:

```css
.textlink_border_type3 {
  position: relative;
  display: inline-block;
}

.textlink_border_type3::after {
  position: absolute;
  bottom: -3px;
  left: 0;
  width: 100%;
  height: 2px;
  content: "";
  background: #222;
  transform: scale(0, 1);
  transform-origin: left top;
  transition: transform 0.3s ease;
}

.textlink_border_type3:hover::after,
.textlink_border_type3:focus-visible::after {
  transform: scale(1, 1);
}
```

When a link also has an arrow, apply the underline to a text-only label or shorten its width so the arrow stays outside it. Check the actual gap and arrow position. Sample the intermediate transform on hover and focus; a final screenshot alone does not prove the transition ran. Under reduced-motion settings, shorten or remove the transition without resetting the collapsed base transform.

Use formulae only for measurable constraints. WCAG's contrast ratio is `(L1 + 0.05) / (L2 + 0.05)`, where `L1` and `L2` are the lighter and darker relative luminances; the applicable target still comes from the requested evaluation scope ([W3C guidance](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)). Fluid sizing can use `clamp(min, preferred, max)` when the design defines bounds; CSS defines it as the preferred value limited by those bounds ([CSS Values and Units](https://www.w3.org/TR/css-values-4/#comp-func)). These calculations do not turn semantic choices, copy quality, or overall design into a numeric score.

## Using this repository today

For now, use the repository as a set of design documents. Start with the [quickstart and copyable prompt](docs/quickstart.en.md), choose a route, and try the [static source comparison](examples/semantic-comparison/README.md). There is no installer or automatic execution.

1. Read [current status and open decisions](docs/starter-status.md).
2. Read the [entry skill](skills/semantic-web/SKILL.md) and only the specialist drafts relevant to your task.
3. If useful, provide the complete repository as context to a coding agent and ask it to use the drafts as guidance. Keep the repository together: cross-folder references may break if you copy a single file or skill.
4. Review the result yourself. Ask the agent to distinguish checks it actually ran from checks it did not run.

Example trial prompt:

> This repository is an unvalidated starter. Read the entry skill and relevant references, and treat them as drafts. If a design comp is supplied, map its meaning to an HTML/CSS plan or implementation. If there is only a brief, create a semantically informed comp first when the available environment supports it, showing content groups, headings, controls, states, and responsive behaviour. Otherwise, provide a design specification with those details. Report checks actually run, their results, and unresolved points separately. Do not describe reading the skills as verified quality assurance.

This trial is not a supported installation method and does not guarantee compatibility with any agent. Record only installation steps and support that have been tested in [compatibility](docs/compatibility.md).

## Regions and languages

The project aims to support as many regions as practical. Regional advertising, legal, and content requirements should be maintained as rule packs that state their market, product, medium, dates, authoritative sources, and human-review boundaries. No regional pack has been validated yet. The project does not guarantee coverage of unresearched markets or legal compliance. Contributions based on primary sources in local languages are welcome.

## Join in

The project aims to grow through real use, bug reports, and improvements to its rules, examples, and translations. Reaching 1,000 or more GitHub stars is one goal; sustained use, reuse, and contributions matter too.

- Read the [contributing guide](CONTRIBUTING.md) and include the problem, evidence, and applicability of a proposal.
- Rule proposals should include sources, applicability, positive, negative, and boundary cases, and false-positive risks.
- Keep limitations and validation status aligned when translating documentation.
- Do not publish third-party designs, text, or customer data without checking the relevant rights.

## What exists today

The repository contains draft entry and specialist skills, a specification, reference guides, design notes, bilingual quickstarts, three static HTML comparison fixtures, focused documentation/fixture assertions, and one draft forward-evaluation case. The case has not yet been run. The existing checks do not validate skill behaviour or web quality.

Executable audit rules, JSON schemas, a product runtime test runner, CI, an installer, validated runtime demo examples, and validated regional packs are not implemented. Agent, browser, and real-device support has not been validated. No accessibility conformance, search ranking, AI-search citations, or legal compliance is guaranteed.

## Licence

Code, data, and tests are under the [MIT Licence](LICENSE). Prose documentation is under [CC BY 4.0](LICENSE-DOCS.txt). Check both licences and the [licensing note](LICENSE-DOCS.txt) for their exact scope.
