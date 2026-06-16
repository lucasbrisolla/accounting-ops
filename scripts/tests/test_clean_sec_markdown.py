from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from clean_sec_markdown import clean_markdown


class CleanSecMarkdownTests(unittest.TestCase):
    def test_rejoins_broken_heading_and_paragraph(self) -> None:
        raw = (
            "### U.S. investors may\n"
            "have difficulty enforcing civil liabilities against ArcelorMittal and its directors.\n"
            "ArcelorMittal\n"
            "is incorporated under the laws of Luxembourg.\n"
        )

        cleaned = clean_markdown(raw)

        self.assertIn(
            "### U.S. investors may have difficulty enforcing civil liabilities against ArcelorMittal and its directors.",
            cleaned,
        )
        self.assertIn(
            "ArcelorMittal is incorporated under the laws of Luxembourg.",
            cleaned,
        )

    def test_preserves_markdown_tables(self) -> None:
        raw = (
            "| Col A | Col B |\n"
            "|-------|-------|\n"
            "| one   | two   |\n"
            "\n"
            "Trailing\n"
            "paragraph.\n"
        )

        cleaned = clean_markdown(raw)

        self.assertIn("| Col A | Col B |", cleaned)
        self.assertIn("| one   | two   |", cleaned)
        self.assertIn("Trailing paragraph.", cleaned)


if __name__ == "__main__":
    unittest.main()
