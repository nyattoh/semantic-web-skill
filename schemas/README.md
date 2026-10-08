# Schemas — design only

The proposed files are `rule.schema.json`, `profile.schema.json`, `test-result.schema.json`, and `claim-evidence.schema.json`. No JSON schemas are supplied because their contracts and validation tests have not been implemented.

Use [specification section 4](../docs/product-spec.ja.md) for fields and states; section 10 describes claim evidence. First choose the schema dialect and versioning approach. Define required fields, enumerations, source/date constraints, conditional requirements, evidence references, and invalid cases. Test rejection as well as acceptance. An empty schema accepting arbitrary input is not a valid implementation of this design.
