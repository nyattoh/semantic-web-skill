# Starter status and next decisions

## Available now

This archive supplies human-readable documentation, nine structurally checkable SKILL.md drafts, and an organized development starting point. Local packaging checks establish file integrity and link/frontmatter structure only; they do not establish agent behavior, browser support, or web-quality results.

## Not implemented or validated

- Machine-readable rules, profiles, and JSON schemas.
- Executable audit checks, fixture assertions, test runner, CI, or install scripts.
- Working examples, screenshots, comparison results, or benchmarks.
- Agent installation, discovery, invocation, and isolated skill distribution.
- Real-device coverage or regional compliance packs.
- Releases. (The repository is public; code is MIT, prose is CC BY 4.0.)

## Decided (2026-10-09, owner)

- License: MIT for code/data, CC BY 4.0 for prose ([ADR 0001](adr/0001-split-license-mit-code-cc-by-docs.md)).
- Purpose and workflows: comp-to-HTML, brief-to-comp, review ([ADR 0003](adr/0003-design-comp-centered-workflows.md)). The product specification and entry skill still describe only generation and review and need this amendment.
- Legal and provider-policy judgment: researched by the agent, reported as `needs_review` ([ADR 0002](adr/0002-legal-judgment-is-an-advisory-finding.md)).
- Target agents: Claude Code, Codex, Antigravity. No host is validated; Antigravity's skill loading has not been checked at all.
- Rule, profile, result and claim schemas are JSON (JSON Schema 2020-12 proposed as the default dialect; owner said only "JSON is fine").
- Region ambition: as many markets as practical, each only as a declared pack.
- The historical source prompt `web_spec.original.md` is not published (kept locally, git-ignored); `docs/reference/README.md` keeps the list of superseded points.
- Vocabulary: [CONTEXT.md](../CONTEXT.md).

## Still open

Minimum browser/OS and real devices, the first rule slice (a machine-checkable HTML content-model rule is the suggested start), the comp input format (image, Figma, or both), who signs off on advertising and legal review, release evaluation tasks.

## Decisions before a first implementation/release

Use specification sections 15–16 to decide the license, first agent/distribution target, initial browser/OS matrix, real-device access, first market/product/media scope, legal-review responsibilities, accessibility target and exceptions, and release evaluation set. The repository name used in this archive is a working name; availability is not verified.

Start with one small end-to-end slice. Acceptance evidence should connect the original requirement, a sourced rule, a meaningful failing fixture, a passing fixture, a boundary fixture, an actual check, and a result record. Expand only after that path works.

Historical specifications may contain dated provider information. Recheck current primary sources when implementing time-sensitive requirements; preserving a source file is not a fresh factual validation.
