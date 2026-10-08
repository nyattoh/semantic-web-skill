# The skills serve comp-to-HTML and brief-to-comp, with Review as a third path

Status: accepted (2026-10-09). Extends product spec section 11, which names only new generation and existing review.

The purpose is to spread Semantic source and reduce Div soup. The owner's main use is converting a Design comp into HTML, and, when no comp exists, producing a comp that already follows the rules before HTML is written. Rules therefore apply at the comp stage as well as the code stage (for example, content grouping and target sizes are decided in the comp).

The expectation is explicit: the First pass need not match the owner's intent, but its code should already be near-final in quality; Refinement is human-directed. Quality is reported through Result states against Rules, never as a numeric score, because the spec forbids invented scores.

Consequence: the spec's mode list and the entry skill's workflow must be amended to add these two workflows; the spec file itself stays preserved and the amendment is recorded in `docs/starter-status.md`.
