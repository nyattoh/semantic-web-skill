# Architecture — design baseline

The [product specification](product-spec.ja.md), sections 3–4 and 11–12, defines the architecture. This file describes intended responsibilities; the rule engine is not implemented.

The `semantic-web` entrypoint determines generation versus review, inputs, scope, and relevant modules. It should load only needed specialists. The eight specialists own HTML meaning, CSS foundations, native interactions, accessibility, responsive verification, search content, regional applicability, and reporting.

Once implemented, `rules/` owns normative requirements and stable IDs. Skill entrypoints route work; references explain decisions; profiles select rule IDs and allowed settings. Avoid duplicated thresholds and conflicting versions. Accessibility owns the target-size rule; CSS and responsive checks will reference the same ID.

Schemas are planned validation contracts, examples are teaching artifacts, fixtures are test inputs, and evaluations measure behavior on held-out tasks. None is interchangeable with a completed audit.

## Packaging boundary

This starter uses repository-relative links. No claim is made that an agent installer can follow references outside a skill folder. Keep the repository together for review. If distribution requires self-contained skills, implement a generator from the single source of truth, record provenance, and validate its output instead of maintaining independent rule copies.

`docs/reference/` summarizes the superseded points of a historical source prompt that is not published. That prompt is not runtime instruction and is superseded where the specification says so.
