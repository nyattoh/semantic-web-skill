# Contributing to the starter

This is a design-stage project. No tested installation or support commitment is established by this repository. Contributions are accepted under the MIT License (code, data) and CC BY 4.0 (prose); see `LICENSE` and `LICENSE-DOCS.txt`.

Read the [specification](docs/product-spec.ja.md), [architecture](docs/architecture.md), and [rule authoring guide](docs/rule-authoring.md). English and Japanese explanations are welcome; keep translated scope and validation status aligned.

Propose narrowly scoped changes with a problem statement, source, applicability, and expected observable behavior. For rules, include positive, negative, and boundary fixtures, false-positive risks, and the human-review boundary. Test changes to actual behavior; wording or heading matches are not behavior tests.

For browser defects, record versions, viewport, input method, real-device versus emulation, reproduction steps, and observed behavior. Redact credentials, private user data, and customer content before sharing evidence. Do not publish third-party materials without appropriate rights.

List the commands actually run and their outcomes. Report missing environments and unexecuted checks explicitly. An empty suite or a schema that accepts every object is not an implementation.

There are no required test commands yet. Add reproducible commands with the first implemented test slice, then document and verify them before adding CI. Use the [handover checklist](docs/handover.md) for review.
