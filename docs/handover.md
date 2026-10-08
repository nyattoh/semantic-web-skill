# Handover

Use this checklist when an implementation or review is actually delivered. The starter itself contains no site-quality test results.

- Scope: target, revision, requested work, changes, and excluded work.
- Rule selection: rule IDs/versions, applicability, sources, and relevant dates.
- Environment: tools/versions, OS, browser, device, input, viewport, DPR, zoom, and real-device/emulation distinction.
- Execution: actual commands or manual steps, timestamps, expected and observed behavior, and evidence locations.
- Results: passed, failed, untested, blocked, needs_review, or not_applicable; explain the last state.
- Exceptions: reason, affected scope, reviewer role, expiry, and remaining risk.
- Remaining work: owner/role, required decision or environment, and the next concrete step.

Keep DOM, screenshot, interaction, automated, and manual evidence distinct. A screenshot does not prove keyboard operation, semantic correctness, or legal compliance.

If mandatory applicable checks remain failed, untested, blocked, or needs_review, do not label the product verified, release-ready, or all-passing. The report itself can be complete while product verification remains incomplete. See [specification section 12](product-spec.ja.md).
