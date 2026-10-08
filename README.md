# semantic-web-skill

A documentation-first starter for a modular web-quality skill collection.

**Status: pre-implementation draft, not a validated or released skill package.** Snapshot: 2026-10-08 UTC. The preserved Japanese specification is dated 2026-10-09 in Japan. Hosted at <https://github.com/nyattoh/semantic-web-skill>.

[日本語](README.ja.md) · [Product specification](docs/product-spec.ja.md) · [Current status](docs/starter-status.md) · [Architecture](docs/architecture.md)

## What is here

- The complete Japanese product specification, preserved byte-for-byte.
- An entry skill and eight specialist SKILL.md drafts with focused reference guides.
- Repository structure, contribution guidance, handover criteria, and a manual GitHub setup guide.
- Design notes for rules, profiles, schemas, examples, and tests. These are plans, not executable implementations.
- A summary of the points superseded from an earlier, unpublished source prompt.

## Start here

1. Read the [product specification](docs/product-spec.ja.md) and [open decisions](docs/starter-status.md).
2. Inspect [skills/semantic-web/SKILL.md](skills/semantic-web/SKILL.md) and only the relevant specialist drafts.
3. Develop one traceable vertical slice: a sourced rule, representative fixtures, a real check, and an honest result.
4. Record actual compatibility and test evidence before offering an installation method or release.

Example development request:

> Read this repository as an unvalidated starter. Implement one semantic HTML rule with positive, negative, and boundary fixtures. Identify the applicable specification section, preserve the existing scope, and report the checks actually run.

Keep the whole repository together while reviewing it. Cross-folder references have not been validated in any agent installer; copying only an individual skill folder may break them. There is no supported installation command yet. See [compatibility](docs/compatibility.md).

## Planned scope

Semantic HTML, CSS foundations, native interactions, accessibility, responsive and real-device verification, search content, regional applicability, and evidence reporting. No automatic audit engine, test runner, CI, or regional rule pack is implemented. No search ranking, AI citation, accessibility conformance, or legal compliance is guaranteed.

[File map](docs/file-map.md) · [Rule authoring](docs/rule-authoring.md) · [Support policy](docs/support-policy.md) · [Handover](docs/handover.md) · [Contributing](CONTRIBUTING.md)

## Publishing and licensing

[Manual GitHub setup (Japanese)](docs/github-setup.ja.md) is a reviewed command guide, not an executed setup. Review the account, destination, staged files, public visibility, and commit identity yourself before publishing.

Code, schemas, rule data and tests are under the [MIT License](LICENSE). Prose documentation is under [CC BY 4.0](LICENSE-DOCS.txt). The exact scope is at the top of [LICENSE-DOCS.txt](LICENSE-DOCS.txt).
