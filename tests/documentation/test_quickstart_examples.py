"""Narrow quickstart/documentation and static-fixture contracts, not an HTML auditor.

HTMLParser reads only these authored fixtures; it does not build a browser DOM,
execute JavaScript, validate HTML content models, or assess WCAG conformance.
"""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
EXAMPLES = ROOT / "examples/semantic-comparison"
QUICKSTARTS = (ROOT / "docs/quickstart.ja.md", ROOT / "docs/quickstart.en.md")
STATES = ("passed", "failed", "untested", "blocked", "needs_review", "not_applicable")


class Element:
    def __init__(self, tag, attrs=()):
        self.tag = tag
        self.attrs = dict(attrs)
        self.children = []
        self.text = ""

    def walk(self):
        yield self
        for child in self.children:
            yield from child.walk()


class FixtureParser(HTMLParser):
    VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}

    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.root = Element("document")
        self.stack = [self.root]
        self.feed(source)
        self.close()

    def handle_starttag(self, tag, attrs):
        node = Element(tag, attrs)
        self.stack[-1].children.append(node)
        if tag not in self.VOID:
            self.stack.append(node)

    def handle_endtag(self, tag):
        if len(self.stack) > 1 and self.stack[-1].tag == tag:
            self.stack.pop()

    def handle_data(self, data):
        self.stack[-1].text += data

    def by_id(self, name):
        return next(node for node in self.root.walk() if node.attrs.get("id") == name)


def fixture(name):
    return FixtureParser((EXAMPLES / name).read_text(encoding="utf-8"))


class QuickstartDocumentationTests(unittest.TestCase):
    def test_readmes_link_quickstarts_near_intro(self):
        for name, guide in (("README.md", "quickstart.en.md"), ("README.ja.md", "quickstart.ja.md")):
            self.assertIn("docs/" + guide, (ROOT / name).read_text(encoding="utf-8")[:2000])

    def test_copyable_prompt_selects_path_blueprint_and_scoped_evidence(self):
        for path in QUICKSTARTS:
            text = path.read_text(encoding="utf-8")
            prompts = re.findall(r"```text\n(.*?)```", text, re.S)
            self.assertEqual(len(prompts), 1, path)
            prompt = prompts[0]
            for required in ("comp-to-html", "brief-to-comp", "review", "skills/semantic-web/SKILL.md", "semantic blueprint", *STATES):
                self.assertIn(required, prompt, path)
            self.assertIn("../skills/semantic-web/references/workflow.md", text)
            self.assertIn("../skills/semantic-web/references/comp-to-html.md", text)
            self.assertIn("../skills/semantic-web/references/brief-to-comp.md", text)
            self.assertIn("../examples/semantic-comparison/README.md", text)

    def test_each_state_has_a_distinct_explanation_in_each_guide(self):
        for path in QUICKSTARTS:
            text = path.read_text(encoding="utf-8")
            descriptions = []
            for state in STATES:
                row = re.search(r"^\| `" + state + r"` \| ([^\n]+)\|$", text, re.M)
                self.assertIsNotNone(row, f"{path}: {state}")
                descriptions.append(row.group(1).strip())
            self.assertEqual(len(set(descriptions)), len(STATES))

    def test_relative_document_links_resolve(self):
        paths = [*QUICKSTARTS, EXAMPLES / "README.md", ROOT / "examples/README.md", ROOT / "tests/README.md", ROOT / "docs/starter-status.md"]
        for path in paths:
            text = path.read_text(encoding="utf-8")
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
                if target.startswith(("http://", "https://", "#")):
                    continue
                resolved = (path.parent / target.split("#", 1)[0]).resolve()
                self.assertNotIn("worklog", resolved.relative_to(ROOT).parts, "Published docs must not depend on ignored local evidence")
                self.assertTrue(resolved.exists(), f"{path}: {target}")

    def test_examples_explain_content_evidence_and_primary_sources(self):
        text = (EXAMPLES / "README.md").read_text(encoding="utf-8")
        for required in ("Content facts", "Element", "Interaction", "Check", "judgment", "convention", "unknown endpoint", "independent", "appearance", "not a conformance", "2026-10-09", "bad.html", "fixed.html", "boundary.html"):
            self.assertIn(required, text)
        for url in ("https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-a-element", "https://html.spec.whatwg.org/multipage/form-elements.html#the-button-element", "https://html.spec.whatwg.org/multipage/grouping-content.html", "https://www.w3.org/WAI/tutorials/forms/labels/"):
            self.assertIn(url, text)

    def test_test_command_and_limits_are_documented(self):
        text = (ROOT / "tests/README.md").read_text(encoding="utf-8")
        self.assertIn('python -m unittest discover -s tests/documentation -p "test_quickstart_examples.py" -v', text)
        self.assertIn("HTMLParser", text)
        self.assertIn("not a generic HTML auditor", text)
        self.assertIn("NOT_RUN", text)
        status = (ROOT / "docs/starter-status.md").read_text(encoding="utf-8")
        self.assertIn("test_quickstart_examples.py", status)
        self.assertIn("static HTML", status)


class StaticComparisonTests(unittest.TestCase):
    def test_known_navigation_is_real_local_link_in_fixed_not_fake_bad(self):
        corrected = fixture("fixed.html")
        link = corrected.by_id("plans-link")
        self.assertEqual(link.tag, "a")
        self.assertEqual(link.attrs.get("href"), "#plans")
        self.assertEqual(corrected.by_id("plans").tag, "section")
        bad = fixture("bad.html").by_id("plans-link")
        self.assertEqual(bad.tag, "div")
        self.assertNotIn("href", bad.attrs)

    def test_local_action_is_explicit_button_with_no_fake_navigation(self):
        corrected = fixture("fixed.html")
        action = corrected.by_id("clear-note")
        self.assertEqual(action.tag, "button")
        self.assertEqual(action.attrs.get("type"), "button")
        self.assertNotIn("href", action.attrs)
        self.assertEqual(corrected.by_id("local-note").tag, "textarea")
        bad = fixture("bad.html").by_id("clear-note")
        self.assertEqual((bad.tag, bad.attrs.get("href")), ("a", "#"))

    def test_peer_collection_is_list_but_bad_uses_generic_blocks(self):
        for name, tag, children in (("fixed.html", "ul", ["li", "li"]), ("bad.html", "div", ["div", "div"])):
            node = fixture(name).by_id("features")
            self.assertEqual(node.tag, tag)
            self.assertEqual([child.tag for child in node.children], children)

    def test_visible_form_label_is_associated_not_placeholder_only(self):
        corrected = fixture("fixed.html")
        control = corrected.by_id("local-note")
        labels = [n for n in corrected.root.walk() if n.tag == "label" and n.attrs.get("for") == control.attrs["id"]]
        self.assertEqual(len(labels), 1)
        self.assertTrue(labels[0].text.strip())
        form = corrected.by_id("local-editor")
        self.assertEqual(form.tag, "form")
        self.assertEqual(form.attrs.get("method"), "dialog")
        self.assertTrue(any(n.tag == "dialog" and form in n.children for n in corrected.root.walk()))
        self.assertNotIn("action", form.attrs)
        self.assertEqual(fixture("bad.html").by_id("local-note").attrs.get("placeholder"), "Local note")
        self.assertFalse(any(n.tag == "label" for n in fixture("bad.html").root.walk()))

    def test_independent_layout_retains_legitimate_div_in_boundary(self):
        boundary = fixture("boundary.html")
        wrapper = boundary.by_id("independent-layout")
        self.assertEqual(wrapper.tag, "div")
        self.assertEqual([n.tag for n in wrapper.children], ["section", "section"])
        self.assertFalse(any(n.tag in {"ul", "ol", "li"} for n in wrapper.walk()))
        for section in wrapper.children:
            self.assertEqual(section.children[0].tag, "h2")

    def test_unknown_endpoint_cannot_submit_or_claim_service(self):
        boundary = fixture("boundary.html")
        preview = boundary.by_id("enquiry-preview")
        self.assertEqual(preview.tag, "fieldset")
        self.assertIn("disabled", preview.attrs)
        self.assertFalse(any(n.tag == "form" for n in boundary.root.walk()))
        action = boundary.by_id("send-enquiry")
        self.assertEqual((action.tag, action.attrs.get("type")), ("button", "button"))
        self.assertIn("disabled", action.attrs)
        field = boundary.by_id("enquiry")
        self.assertEqual(field.tag, "textarea")
        self.assertTrue(any(n.tag == "label" and n.attrs.get("for") == field.attrs["id"] for n in preview.walk()))
        self.assertIn("blocked", boundary.by_id("endpoint-status").text)

    def test_fixtures_have_no_external_dependencies_or_network_handlers(self):
        for name in ("bad.html", "fixed.html", "boundary.html"):
            source = (EXAMPLES / name).read_text(encoding="utf-8")
            page = FixtureParser(source)
            self.assertEqual(page.by_id("fixture-title").tag, "h1")
            for node in page.root.walk():
                self.assertNotIn("src", node.attrs)
                self.assertNotIn("action", node.attrs)
                if node.tag == "script":
                    self.assertNotIn("fetch(", node.text)
                    self.assertNotIn("XMLHttpRequest", node.text)
            self.assertIn("Static fixture", source)


if __name__ == "__main__":
    unittest.main()
