# Rule authoring — design contract

No rule data or validator is implemented yet. Use [specification section 4](product-spec.ja.md) as the authoritative field contract and sections 12–15 for evidence and release requirements.

For each proposed rule, establish a stable ID, owning module, severity, requirement type, applicability, and an observable requirement. Record primary sources and their sections, effective dates when known, last checked date, review due date, test method, expected evidence, exceptions, and human-review boundary. Unknown dates remain unknown.

Distinguish a standard from project policy, a recommendation, law, regulatory guidance, self-regulation, and provider policy. A project's preference must not be reported as a standards violation. Keep severity distinct from mandatory applicability.

Provide realistic passing, failing, boundary, and non-applicable cases. Explain likely false positives and what automation cannot establish. A change to the meaning of a rule requires versioning and migration notes; never recycle an obsolete ID for a different requirement.

Results use `passed`, `failed`, `untested`, `blocked`, `needs_review`, or `not_applicable`. Explain non-applicability. Missing evidence is not a pass or a reason to evade a check. An exception decision does not erase a failure.

Do not add unconstrained JSON merely to populate the schema folders. First define and test required fields, conditional rules, and rejected invalid cases.
