from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "accounting_ops_doctor.py"


def load_module():
    spec = importlib.util.spec_from_file_location("accounting_ops_doctor", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def touch(root: Path, relative_path: str, content: str = "") -> None:
    path = root / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def touch_required_paths(root: Path, module) -> None:
    for relative_path in module.REQUIRED_PATHS:
        touch(root, relative_path)


class AccountingOpsDoctorTests(unittest.TestCase):
    def test_reports_ok_when_required_structure_and_docs_exist(self):
        module = load_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            touch_required_paths(root, module)
            touch(root, "CLAUDE.md", "`tracks/fpa/modes/fpa-learning.md`")
            touch(root, "PRODUCT_INDEX.md", "`tracks/accounting/modes/accounting-closing-and-quality.md`")
            touch(root, "README.md", "`templates/flash-report.md`")
            touch(root, "INDEX.md", "`skills/number-to-management-story.md`")

            result = module.check_accounting_ops(root)

            self.assertTrue(result.ok)
            self.assertEqual(result.missing, [])
            self.assertEqual(result.broken_references, [])
            self.assertEqual(result.surface_drift, [])

    def test_reports_missing_required_files(self):
        module = load_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            touch(root, "README.md")

            result = module.check_accounting_ops(root)

            self.assertFalse(result.ok)
            self.assertIn("AGENTS.md", result.missing)
            self.assertIn("CLAUDE.md", result.missing)
            self.assertIn("HEALTH_CHECK.md", result.missing)
            self.assertIn("tracks/accounting/modes/accounting-closing-and-quality.md", result.missing)
            self.assertIn("skills/prepare-journal-entry-support.md", result.missing)

    def test_reports_broken_internal_references(self):
        module = load_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            touch_required_paths(root, module)
            touch(root, "CLAUDE.md", "`tracks/fpa/modes/ghost-mode.md`")
            touch(root, "PRODUCT_INDEX.md", "[ghost](tracks/accounting/modes/ghost-mode.md)")
            touch(root, "README.md", "`templates/flash-report.md`")
            touch(root, "INDEX.md", "`skills/number-to-management-story.md`")

            result = module.check_accounting_ops(root)

            self.assertFalse(result.ok)
            self.assertIn("CLAUDE.md -> tracks/fpa/modes/ghost-mode.md", result.broken_references)
            self.assertIn("PRODUCT_INDEX.md -> tracks/accounting/modes/ghost-mode.md", result.broken_references)

    def test_reports_surface_drift_outside_archive(self):
        module = load_module()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            touch_required_paths(root, module)
            touch(root, "CLAUDE.md", "entrevista")
            touch(root, "PRODUCT_INDEX.md", "")
            touch(root, "README.md", "")
            touch(root, "INDEX.md", "")
            touch(root, "context/nota.md", "Belgo")
            touch(root, "archive/interview/legacy.md", "Belgo")

            result = module.check_accounting_ops(root)

            self.assertFalse(result.ok)
            self.assertIn("CLAUDE.md -> entrevista", result.surface_drift)
            self.assertIn("context/nota.md -> Belgo", result.surface_drift)
            self.assertNotIn("archive/interview/legacy.md -> Belgo", result.surface_drift)


if __name__ == "__main__":
    unittest.main()
