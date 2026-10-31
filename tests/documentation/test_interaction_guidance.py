"""Static documentation contracts only; these tests do not assess web conformance."""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[2]


class InteractionGuidanceTests(unittest.TestCase):
    def test_native_interactions_routes_to_focused_contract(self):
        text = (ROOT / "skills/native-interactions/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("references/operation-contract.md", text)

    def test_operation_contract_covers_intent_boundary_and_all_form_states(self):
        path = ROOT / "skills/native-interactions/references/operation-contract.md"
        text = path.read_text(encoding="utf-8").lower()
        for phrase in (
            "known destination",
            "`a href`",
            "action",
            "`button type`",
            "enter or choose a value",
            "label",
            "unknown",
            "essential",
            "idle",
            "submitting",
            "success",
            "field error",
            "server error",
            "focus",
            "retry",
            "retention",
            "do not invent",
            "untested",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_operation_contract_contains_concrete_bad_and_corrected_controls(self):
        path = ROOT / "skills/native-interactions/references/operation-contract.md"
        text = path.read_text(encoding="utf-8")
        for snippet in ('href="#"', '<a class="button" href="/plans">', '<button type="button"', '<label for="email">'):
            with self.subTest(snippet=snippet):
                self.assertIn(snippet, text)

    def test_placeholder_link_explanation_describes_the_real_failure(self):
        path = ROOT / "skills/native-interactions/references/operation-contract.md"
        text = path.read_text(encoding="utf-8").lower()
        self.assertNotIn("keyboard and browser link behaviour are missing", text)
        self.assertIn("placeholder destination can navigate to the page top", text)

    def test_operation_contract_cites_current_primary_guidance_with_dates(self):
        path = ROOT / "skills/native-interactions/references/operation-contract.md"
        text = path.read_text(encoding="utf-8")
        for url in (
            "https://html.spec.whatwg.org/multipage/text-level-semantics.html",
            "https://html.spec.whatwg.org/multipage/form-elements.html",
            "https://www.w3.org/WAI/tutorials/forms/notifications/",
            "https://www.w3.org/WAI/tutorials/forms/labels/",
            "https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html",
        ):
            with self.subTest(url=url):
                self.assertIn(url, text)
        self.assertRegex(text.lower(), r"retrieved 2026-10-09")
        self.assertIn("not a conformance result", text.lower())

    def test_responsive_entry_routes_and_reference_compares_order_only_when_meaningful(self):
        entry = (ROOT / "skills/responsive-verification/SKILL.md").read_text(encoding="utf-8")
        path = ROOT / "skills/responsive-verification/references/device-testing.md"
        reference = path.read_text(encoding="utf-8").lower()
        self.assertIn("references/device-testing.md", entry)
        for phrase in ("visual order", "dom order", "keyboard focus order", "meaningful", "independent", "layout changes"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, reference)
        self.assertIn("https://www.w3.org/wai/wcag22/understanding/focus-order.html", reference)
        self.assertIn("order: 1", reference)
        self.assertIn("steps", reference)

    def test_documentation_links_resolve_and_limitations_are_explicit(self):
        paths = (
            ROOT / "skills/native-interactions/SKILL.md",
            ROOT / "skills/native-interactions/references/operation-contract.md",
            ROOT / "skills/responsive-verification/SKILL.md",
            ROOT / "skills/responsive-verification/references/device-testing.md",
        )
        for source in paths:
            text = source.read_text(encoding="utf-8")
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
                if target.startswith(("http://", "https://", "#")):
                    continue
                self.assertTrue((source.parent / target.split("#", 1)[0]).resolve().exists(), f"{source}: {target}")
        responsive = (paths[3]).read_text(encoding="utf-8").lower()
        self.assertIn("static examples", responsive)
        self.assertIn("do not establish", responsive)

    def test_motion_policy_is_asked_and_defaults_to_prefers_reduced_motion(self):
        default = re.compile(r"if unanswered[^.]*\bfollow(?:s|ing)? `prefers-reduced-motion`")
        for path in ("skills/semantic-web/SKILL.md", "skills/semantic-web/references/workflow.md"):
            text = (ROOT / path).read_text(encoding="utf-8").lower()
            for phrase in ("always on", "prefers-reduced-motion", "on-site toggle", "collapsed base state", "unsuppressed only when the user", "reduced-motion policy"):
                with self.subTest(path=path, phrase=phrase):
                    self.assertIn(phrase, text)
            with self.subTest(path=path, check="default"):
                self.assertRegex(text, default)
        readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
        self.assertIn("on-site toggle", readme)
        self.assertRegex(readme, default)
        readme_ja = (ROOT / "README.ja.md").read_text(encoding="utf-8")
        self.assertIn("サイト内切替", readme_ja)
        self.assertIn("未指定なら `prefers-reduced-motion` に従う", readme_ja)
        smoke = (ROOT / "tests/evaluations/semantic-first-pass-smoke.md").read_text(encoding="utf-8").lower()
        for phrase in (
            "animation policy is not specified",
            "asks whether animation is always on",
            "with no answer it records the default of following `prefers-reduced-motion`",
            "collapsed base state is preserved",
            "without the full-duration transition",
            "only a variant prompt that chooses always on",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, smoke)

    def test_old_animation_enabled_default_does_not_return(self):
        stale = ("animation enabled", "suppression is off", "suppression off", "does not apply a `prefers-reduced-motion` override", "抑制しない（アニメーション有効）", "アニメーション有効")
        for path in (
            "README.md",
            "README.ja.md",
            "skills/semantic-web/SKILL.md",
            "skills/semantic-web/references/workflow.md",
            "tests/evaluations/semantic-first-pass-smoke.md",
        ):
            text = (ROOT / path).read_text(encoding="utf-8").lower()
            for phrase in stale:
                with self.subTest(path=path, phrase=phrase):
                    self.assertNotIn(phrase, text)


if __name__ == "__main__":
    unittest.main()
