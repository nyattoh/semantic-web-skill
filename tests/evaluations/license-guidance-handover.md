# Licence guidance handover

Branch: `devin/20261010-license-guidance` (based on origin/main). Not committed, pushed, or PR'd.

## Sources
`LICENSE` (MIT), `LICENSE-DOCS.txt` (CC BY 4.0 prose), `docs/adr/0001-split-license-mit-code-cc-by-docs.md`.
README.md, README.ja.md, docs/starter-status.md were already correct.

## Before / after
- `LICENSE-NOT-SELECTED.md`: "No project license selected / LICENSE deliberately absent" -> short superseded pointer to LICENSE, LICENSE-DOCS.txt, ADR 0001 (file kept, not deleted).
- `docs/file-map.md` line 3: removed only `LICENSE` from the deliberately-absent list; "JSON schemas/profiles, executable scripts, demos, and CI are deliberately absent" preserved.
- New `tests/documentation/test_license_notice.py` (4 tests): licence labels, recursive scan of README*.md + docs/**/*.md + skills/**/*.md excluding gitignored `docs/reference/web_spec.original.md`, nested-path coverage (docs/adr, docs/concepts, docs/reference, skills/semantic-web), stale-phrase rejection, preserved absence statement.

## Results
- RED: `python -m unittest discover -s tests/documentation -p test_license_notice.py` -> FAILED (failures=1), `test_no_stale_licence_statements`, match in `docs\file-map.md` (`LICENSE, JSON schemas/... deliberately absent`); 3 others passed.
- GREEN focused: same command -> Ran 4 tests, OK.
- GREEN full: `python -m unittest discover -s tests/documentation` -> Ran 24 tests, OK.

## Cycle 2 (parent review finding)
Finding: the test omitted root `LICENSE-NOT-SELECTED.md`, so the user's original stale notice could recur undetected. Fix: added it to `public_markdown()` in `tests/documentation/test_license_notice.py`; no other content edits, file not deleted.
- RED: temporarily restored the HEAD version of `LICENSE-NOT-SELECTED.md` -> focused test FAILED (failures=1): `No project license has been selected` matched in `LICENSE-NOT-SELECTED.md`. Corrected file then restored.
- GREEN focused: Ran 4 tests, OK.
- GREEN full: `python -m unittest discover -s tests/documentation` -> Ran 24 tests, OK.
- External review: Grok 4.7 attempts failed twice before the provider started; no Grok verdict exists. No other provider used.

## Docs cleanup decision
No deletions. `docs/file-map.md` and `docs/concepts/human-entrypoint.ja.md` have no inbound references outside docs/ but are not proven obsolete; kept.

## Limitations
- Stale-phrase regexes are heuristic English-only patterns; Japanese prose is not checked.
- promo/, articles, images, worklogs not inspected.

## Independent review
- Verifier: OpenAI Codex parent; implementer: Claude Sonnet 5.5 medium (different vendors).
- Verdict: pass within the licence-consistency and regression-test scope. Reviewed the exact recorded patches, final test source, authoritative licence headers, hand-over, and RED/GREEN command outcomes.
- The corrected root notice points to the MIT and CC BY 4.0 files and ADR 0001; `docs/file-map.md` no longer says LICENSE is absent. The test now scans the root notice and nested `docs/` and `skills/` Markdown, with a focused assertion for its original stale sentence.
- Grok 4.7 attempts did not start twice; no Grok verdict is claimed. This Codex review used the current work context and did not send another copy to an external provider.
- No `docs/` file was proven obsolete; no deletions were made. The regex coverage is English-only and is not a legal or third-party licence audit.
