# Starter status and next decisions

## Available now

This archive supplies human-readable documentation, nine structurally checkable SKILL.md drafts, and an organised development starting point. Local packaging checks establish file integrity and link/frontmatter structure only; they do not establish agent behaviour, browser support, or web-quality results.

Also available: [JA quickstart](quickstart.ja.md), [UK-English quickstart](quickstart.en.md), [three static HTML comparison fixtures](../examples/semantic-comparison/README.md) with focused assertions in `tests/documentation/test_quickstart_examples.py`, and one [draft semantic first-pass evaluation case](../tests/evaluations/semantic-first-pass-smoke.md). That evaluation case has not been run. [Test instructions](../tests/README.md) distinguish static documentation/fixture checks from runtime checks. These local checks inspect authored tags, attributes and documented contracts; they do not implement an audit engine or validate host behaviour, HTML/WCAG conformance or product quality. Interaction/responsive documentation checks are separately scoped.

## Not implemented or validated

- Machine-readable rules, profiles, and JSON schemas.
- General executable audit checks, product runtime test runner, CI, or install scripts. Scoped static fixture assertions are available as described above.
- Validated runtime examples, rendered semantic comparisons, behaviour results or benchmarks. Static source fixtures do not establish these results.
- Agent installation, discovery, invocation, and isolated skill distribution.
- Real-device coverage or regional compliance packs.
- Releases. (The repository is public; code is MIT, prose is CC BY 4.0.)

## Decided (2026-10-09, owner)

- Licence: MIT for code/data, CC BY 4.0 for prose ([ADR 0001](adr/0001-split-license-mit-code-cc-by-docs.md)).
- Purpose: spread Semantic source widely and reduce Div soup. The core paths are Comp-to-HTML (Design comp to semantic HTML) and Brief-to-comp (brief to a comp designed with semantic structure from the outset), with Review of existing sites as the third path ([ADR 0003](adr/0003-design-comp-centered-workflows.md)). The owner's First pass is expected to be near-final in code quality; Refinement closes gaps with the owner's intent. Results use Rule-based Result states, not an invented quality score.
- Amendment to [product-spec.ja.md](product-spec.ja.md) section 11: its two-mode list (new generation and existing review) is superseded for workflow routing by the three paths above. The specification remains preserved byte-for-byte. The entry skill now describes all three paths as draft guidance; this status record is the amendment, not evidence that the workflow runs.
- Legal and provider-policy judgment: researched by the agent, reported as `needs_review` ([ADR 0002](adr/0002-legal-judgment-is-an-advisory-finding.md)).
- Target agents: Claude Code, Codex, Antigravity. No host is validated; Antigravity's skill loading has not been checked at all.
- Rule, profile, result and claim schemas are JSON (JSON Schema 2020-12 proposed as the default dialect; owner said only "JSON is fine").
- Region ambition: as many markets as practical, supported only through sourced, scoped Regional packs. A market without a pack is unsupported; regional coverage has not been validated.
- Distribution aspiration: at least 1,000 GitHub stars. Stars are not a quality guarantee or evidence of verified outcomes.
- The historical source prompt `web_spec.original.md` is not published (kept locally, git-ignored); `docs/reference/README.md` keeps the list of superseded points.
- Vocabulary: [CONTEXT.md](../CONTEXT.md).

## Still open

Minimum browser/OS and real devices; the first rule slice (a machine-checkable HTML content-model rule is the suggested start); comp input format (image, Figma, or both) and brief input format; host installation, loading and distribution support; who signs off on advertising and legal review; release evaluation tasks.

## Decisions before a first implementation/release

Use specification sections 15–16 and the accepted ADRs to settle the still-open first agent/distribution target, input formats, initial browser/OS matrix, real-device access, first market/product/media scope, legal-review responsibilities, accessibility target and exceptions, and release evaluation set. The licence is decided in ADR 0001. The repository name used in this archive is a working name; availability is not verified.

Start with one small end-to-end slice. Acceptance evidence should connect the original requirement, a sourced rule, a meaningful failing fixture, a passing fixture, a boundary fixture, an actual check, and a result record. Expand only after that path works.

Historical specifications may contain dated provider information. Recheck current primary sources when implementing time-sensitive requirements; preserving a source file is not a fresh factual validation.
