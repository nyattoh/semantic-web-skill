# semantic-web-skill

A skill collection intended to spread Semantic source widely. Its core paths are Comp-to-HTML and Brief-to-comp: a Design comp guides semantic HTML, or a brief leads to a comp designed with semantic structure from the outset. Review inspects existing sites. The project aims to serve as many markets as practical through sourced, scoped Regional packs; a market without a pack remains unsupported. At least 1,000 GitHub stars is an aspiration for reach, not a guarantee of quality or adoption.

These are product directions, not claims that the workflows, regional packs, or Target agents have been implemented or validated. [ADR 0003](docs/adr/0003-design-comp-centered-workflows.md) records the owner's workflow decision; [starter status](docs/starter-status.md) records the amendment to the preserved product specification and the remaining decisions.

## Language

### Work

**Design comp** (デザインカンプ):
A visual mock-up, as an image or a design-tool file, of a page or screen. It is the input of comp-to-HTML and the output of brief-to-comp.
_Avoid_: mockup, wireframe, screenshot

**Semantic blueprint**:
A description of content relationships, reading order, headings, controls and states that informs the Design comp and Semantic source before layout containers are chosen. It records meanings and open decisions; a visual image alone does not establish it.
_Avoid_: DOM outline, layout specification

**Comp-to-HTML**:
The workflow that turns an existing design comp into semantic source.
_Avoid_: slicing, coding the design

**Brief-to-comp**:
The workflow that starts from a brief with no design comp and produces a design comp that already follows the skill's rules, before any HTML is written.
_Avoid_: zero-to-one, generation mode

**Review**:
The workflow that inspects existing source and reports findings; it does not change anything unless the request says so.
_Avoid_: audit, QA

**First pass**:
The agent's initial output for a request. It is expected to be near-final in code quality but may differ from the owner's intent.
_Avoid_: 60-point draft, MVP

**Refinement**:
Human-directed iterations after the first pass that close the remaining gap to the owner's intent.
_Avoid_: polishing, fixing, 100-point

### Quality

**Semantic source**:
HTML whose elements follow what the content means and the HTML Standard content model.
_Avoid_: clean code, good HTML, valid HTML

**Div soup**:
Markup that looks right but encodes no meaning: generic containers where lists, headings, landmarks, buttons or links belong.
_Avoid_: junk markup, bad HTML

**Rule**:
A normative requirement with a stable ID, owner module, applicability, sources and a test method. The single source of truth for any threshold.
_Avoid_: guideline, best practice, check

**Profile**:
A selection of rule IDs and allowed settings for one kind of project. It never restates rule text.
_Avoid_: preset, config

**Result state**:
One of passed, failed, untested, blocked, needs_review, not_applicable. No score or percentage replaces it.
_Avoid_: grade, score, pass rate

**Evidence**:
A recorded artefact that supports a result and only the scope it can support: a screenshot shows display, a DOM dump shows structure, an interaction log shows behaviour.
_Avoid_: proof, screenshot

### Compliance

**Regional pack**:
A declared set of applicability conditions, sources and fixtures for one market. Regional compliance coverage without a validated pack is unsupported, never passed; separately scoped semantic and design findings retain their own Result states.
_Avoid_: locale, country rules

**Claim**:
A statement in published content about effect, price, comparison, superlative, number, testimonial or guarantee, tied to its evidence.
_Avoid_: copy, wording

**Advisory finding**:
The agent's reading of current law or provider policy, formed from primary sources it searched on the date stated, always carried as needs_review with citations.
_Avoid_: legal check, compliant, legal approval

### Distribution

**Entry skill**:
The single skill that scopes a request and loads only the specialist skills it needs.
_Avoid_: main skill, router

**Specialist skill**:
A skill that owns one area: semantic HTML, CSS foundations, native interactions, accessibility, responsive verification, search content, regional compliance, evidence reporting.
_Avoid_: sub-skill, plugin

**Target agent**:
An agent host the skills are meant to run in: Claude Code, Codex, Antigravity. Support is claimed per host only after a recorded run.
_Avoid_: platform, supported agent
