# Changelog

## Unreleased — guidance and onboarding, 2026-10-09 JST

- Added Japanese and UK-English quickstarts and three static semantic comparison fixtures.
- Added narrowly scoped documentation/fixture tests; these do not validate agent behaviour, HTML/WCAG conformance or regional support.
- Clarified operation intent, asynchronous form states and meaningful responsive reading/focus order checks.
- Added a dated seven-repository comparison and a sourced differentiation/adoption proposal.
- Defined Semantic blueprint and clarified that unsupported regional compliance coverage does not replace separately scoped semantic/design result states.
- Kept desktop/SaaS implementation out of this branch; the separate concept branch contains only a proposal document.

## Unreleased — documentation starter, 2026-10-08 UTC

- Preserved the Japanese product specification without changes.
- Added English/Japanese entry documents and nine draft skill entrypoints.
- Added architecture, reference guides, development folder notes, and a manual GitHub setup guide.
- Isolated the historical source prompt with migration warnings.
- Corrected "specification sections N" wording and rule folder titles; added `.gitattributes` (LF) so the preserved specification stays byte-stable under `core.autocrlf`.
- Selected licenses (MIT code/data, CC BY 4.0 prose), added CONTEXT.md and ADRs 0001-0003.
- Unpublished the historical source prompt (`web_spec.original.md`): git-ignored, kept locally; references and licensing scope updated.
- Created the public GitHub repository and connected `origin` (nothing pushed yet).

No executable rules, schemas, demos, automated audits, tested installer, or CI are released. The archive is not a tagged software version.
