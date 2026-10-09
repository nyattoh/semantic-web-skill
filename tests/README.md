# Tests — scoped static documentation and fixture checks

The starter now includes local documentation checks and narrow assertions for the [semantic comparison fixtures](../examples/semantic-comparison/README.md). Packaging integrity checks and these assertions do not establish product-quality, agent behaviour or web conformance. No general audit engine or validated runtime evaluation suite is implemented.

## Reproduce the quickstart/static fixture checks

From the repository root, with Python available:

```powershell
python -m unittest discover -s tests/documentation -p "test_quickstart_examples.py" -v
```

Tested environment: Windows, PowerShell, Python 3.14.2 (2026-10-09); the test uses the Python standard library and needs no dependency installation, service, API key or network. It exits non-zero on an assertion failure or missing required file. See [test source](documentation/test_quickstart_examples.py). The implementation run passed all 13 tests; its RED/GREEN records are local, Git-ignored files under `worklog/20261009-differentiation/`, not bundled evidence. Run the command to obtain output for your checkout.

The checks cover:

- README entry links, both guides' copyable three-route prompts, six-state explanations, relative document links and declared evidence limits.
- Actual fixture tags/attributes and selected direct-child relationships via `HTMLParser`: the known anchor destination, non-submit action, peer list versus generic bad blocks, visible label/control association and the local dialog form context.
- Boundary exceptions: independent headed regions keep a layout `div`; the unknown endpoint preview is disabled and has no form or invented action URL.
- Authored fixtures have no `src` dependencies, form action or named network handlers. This is a limited fixture contract, not a general security proof.

`HTMLParser` does not implement browser DOM construction, execute JavaScript or validate full HTML content models. The assertions encode this example's supplied facts; they cannot infer content meaning for arbitrary pages. This is **not a generic HTML auditor**, WCAG validator, agent validation or skill runtime test runner. Bad cases remain intentionally wrong even when the suite passes, because the suite confirms the contrast and boundaries.

The separately owned `test_interaction_guidance.py` checks interaction/responsive documentation. Its presence does not mean interactions were executed; its independent run results belong to that worker's evidence. Keep test paths and records distinct.

**NOT_RUN by the quickstart checks:** browser rendering and visual comparison, pointer/keyboard/focus operation, JavaScript execution, responsive widths, accessibility tree/assistive technology, HTML conformance checking, physical devices, host installation/invocation, regional validation and backend submission. An unknown endpoint blocks connected form work rather than passing a simulation.

## Future behavioural tests

Implement meaningful invariants tied to sourced rules, with positive, negative, boundary and non-applicable inputs. Record actual environment, steps and output; text matching cannot substitute for behaviour checks. [Specification sections 12–13](../docs/product-spec.ja.md) define the intended approach. Never infer full accessibility, legal compliance or physical-device behaviour from one automated tool.

One draft [semantic first-pass smoke case](evaluations/semantic-first-pass-smoke.md) records previously missed visual, content and interaction requirements. It is an evaluation prompt and rubric, not an executable test or a validated host result. No run has been recorded.
