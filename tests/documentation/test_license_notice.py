"""Static contract: public Markdown must not claim that no licence is selected."""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[2]
EXCLUDED = {ROOT / "docs/reference/web_spec.original.md"}  # gitignored local copy
STALE = (
    re.compile(r"no project licen[cs]e (has been )?selected", re.I),
    re.compile(r"licen[cs]e[^.\n]{0,40}not selected", re.I),
    re.compile(r"LICENSE\s*,[^.\n]*deliberately absent", re.I),
    re.compile(r"LICENSE file is deliberately absent", re.I),
)


def public_markdown():
    files = [ROOT / "README.md", ROOT / "README.ja.md", ROOT / "LICENSE-NOT-SELECTED.md"]
    for top in ("docs", "skills"):
        files += (ROOT / top).rglob("*.md")
    return sorted(f for f in files if f not in EXCLUDED)


class LicenseNoticeTests(unittest.TestCase):
    def test_authoritative_licence_labels(self):
        self.assertIn("MIT License", (ROOT / "LICENSE").read_text(encoding="utf-8"))
        self.assertIn(
            "Creative Commons Attribution 4.0 International (CC BY 4.0)",
            (ROOT / "LICENSE-DOCS.txt").read_text(encoding="utf-8"),
        )

    def test_nested_paths_are_scanned(self):
        rel = {p.relative_to(ROOT).as_posix() for p in public_markdown()}
        for sub in ("docs/adr/", "docs/concepts/", "docs/reference/", "skills/semantic-web/"):
            self.assertTrue(any(r.startswith(sub) for r in rel), sub)
        self.assertNotIn("docs/reference/web_spec.original.md", rel)

    def test_no_stale_licence_statements(self):
        for path in public_markdown():
            text = path.read_text(encoding="utf-8")
            for pat in STALE:
                self.assertIsNone(pat.search(text), f"{path.relative_to(ROOT)}: {pat.pattern}")

    def test_scripts_demos_ci_absence_is_preserved(self):
        text = (ROOT / "docs/file-map.md").read_text(encoding="utf-8")
        self.assertRegex(text, r"executable scripts, demos, and CI are deliberately absent")


if __name__ == "__main__":
    unittest.main()
