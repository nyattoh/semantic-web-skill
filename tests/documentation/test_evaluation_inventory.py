"""Static inventory checks only; these do not validate evaluation outcomes."""

from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit


EVALUATIONS = Path(__file__).resolve().parents[1] / "evaluations"
INVENTORY = EVALUATIONS / "README.md"


class EvaluationInventoryTests(unittest.TestCase):
    def test_local_inventory_links_exist(self):
        text = INVENTORY.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            path = (EVALUATIONS / unquote(url.path)).resolve()
            with self.subTest(target=target):
                self.assertTrue(path.is_file(), f"Missing inventory target: {target}")

    def test_every_evaluation_file_is_registered(self):
        text = INVENTORY.read_text(encoding="utf-8")
        registered = set()
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            url = urlsplit(target)
            if not url.scheme and not url.netloc and url.path:
                registered.add((EVALUATIONS / unquote(url.path)).resolve())
        files = {path.resolve() for path in EVALUATIONS.rglob("*") if path.is_file()}
        unregistered = files - registered - {INVENTORY.resolve()}
        self.assertEqual(
            sorted(path.relative_to(EVALUATIONS).as_posix() for path in unregistered),
            [],
            "Register each evaluation file with a local link in evaluations/README.md",
        )


if __name__ == "__main__":
    unittest.main()
