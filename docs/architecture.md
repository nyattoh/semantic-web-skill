# Architecture — design baseline

The preserved [product specification](product-spec.ja.md), sections 3–4 and 11–12, defines the architecture baseline. [ADR 0003](adr/0003-design-comp-centered-workflows.md) is the accepted workflow extension, recorded as an amendment in [starter status](starter-status.md). This file describes intended responsibilities; the workflows and rule engine are not implemented or validated.

The `semantic-web` Entry skill is intended to route three paths: Comp-to-HTML turns a Design comp into Semantic source; Brief-to-comp creates a comp with semantic structure planned before HTML is written; Review inspects an existing site and reports findings, with changes only when requested. It determines inputs, scope, and relevant modules, and should load only needed Specialist skills. Comp-stage decisions, such as content grouping and target sizes, must use the same Rules that govern code-stage work. The eight specialists own HTML meaning, CSS foundations, native interactions, accessibility, responsive verification, search content, regional applicability, and reporting. Input formats for comps and briefs and Target agent loading/distribution support remain undecided or unverified.

Once implemented, `rules/` owns normative requirements and stable IDs. Skill entrypoints route work; references explain decisions; profiles select rule IDs and allowed settings. Avoid duplicated thresholds and conflicting versions. Accessibility owns the target-size rule; CSS and responsive checks will reference the same ID.

Schemas are planned validation contracts, examples are teaching artefacts, fixtures are test inputs, and evaluations measure behaviour on held-out tasks. None is interchangeable with a completed audit.

Regional packs are planned to extend coverage to as many markets as practical. Each pack needs declared applicability, sources and fixtures; a market without a validated pack remains unsupported. GitHub stars express a distribution aspiration, not a quality measure.

## Packaging boundary

This starter uses repository-relative links. No claim is made that an agent installer can follow references outside a skill folder. Keep the repository together for review. If distribution requires self-contained skills, implement a generator from the single source of truth, record provenance, and validate its output instead of maintaining independent rule copies.

`docs/reference/` summarizes the superseded points of a historical source prompt that is not published. That prompt is not runtime instruction and is superseded where the specification says so.
