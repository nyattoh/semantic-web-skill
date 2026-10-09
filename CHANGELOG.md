# Changelog

## Unreleased — remove stale internal docs

- Removed the ChatGPT handover prompt and the obsolete GitHub setup guide. They described an unpushed repository.

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
