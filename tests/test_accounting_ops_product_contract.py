from __future__ import annotations

import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

from scripts.accounting_ops_product_contract import (
    ACCOUNTING_OPS_PRODUCT_CONTRACT,
    ContractFinding,
    FindingCategory,
    FindingSeverity,
    ProductLayer,
    PromotionDestination,
    check_product_contract,
)
from scripts.promotion_pipeline import (
    EditorialStatus,
    PromotionConfidence,
    PromotionDecision,
    PromotionSourceKind,
    register_promotion,
)


def touch(root: Path, relative_path: str, content: str = "") -> None:
    path = root / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def touch_required_paths(root: Path) -> None:
    for relative_path in ACCOUNTING_OPS_PRODUCT_CONTRACT.required_paths:
        touch(root, relative_path)


def touch_reference_docs(root: Path, *, content: str = "") -> None:
    for relative_path in ACCOUNTING_OPS_PRODUCT_CONTRACT.canonical_reference_documents:
        touch(root, relative_path, content)


class AccountingOpsProductContractTests(unittest.TestCase):
    def test_missing_path_is_returned_as_a_typed_structure_finding(self):
        with tempfile.TemporaryDirectory() as tmp:
            report = check_product_contract(Path(tmp))

            finding = next(
                finding for finding in report.findings if finding.target == "CLAUDE.md"
            )

            self.assertIsInstance(finding, ContractFinding)
            self.assertEqual(finding.category, FindingCategory.STRUCTURE)
            self.assertEqual(finding.severity, FindingSeverity.ERROR)
            self.assertIn("ausente", finding.message)
            self.assertIn("CLAUDE.md", report.missing)

    def test_broken_reference_is_returned_as_a_typed_reference_finding(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            touch_required_paths(root)
            touch_reference_docs(root)
            touch(root, "CLAUDE.md", "`tracks/fpa/modes/ghost-mode.md`")

            report = check_product_contract(root)

            finding = next(
                finding
                for finding in report.findings
                if finding.category == FindingCategory.REFERENCE
            )

            self.assertEqual(finding.target, "CLAUDE.md -> tracks/fpa/modes/ghost-mode.md")
            self.assertEqual(finding.severity, FindingSeverity.ERROR)
            self.assertIn(finding.target, report.broken_references)

    def test_situated_company_terms_are_allowed_but_generic_surface_drift_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            touch_required_paths(root)
            touch_reference_docs(root)
            touch(root, "context/companies/company-slug/enterprise-context.md", "Acme")
            touch(root, "stateless/company-packs/company-lens.md", "Acme")
            touch(root, "archive/interview/legacy.md", "Acme")

            allowed_report = check_product_contract(root)

            self.assertTrue(allowed_report.ok)
            self.assertEqual(allowed_report.surface_drift, [])

            touch(root, "_method-wiki/concepts/generic-method.md", "Acme")
            drift_report = check_product_contract(root)

            finding = next(
                finding
                for finding in drift_report.findings
                if finding.category == FindingCategory.SURFACE_DRIFT
            )

            self.assertEqual(finding.target, "_method-wiki/concepts/generic-method.md -> Acme")
            self.assertEqual(finding.severity, FindingSeverity.ERROR)
            self.assertIn(finding.target, drift_report.surface_drift)

    def test_findings_are_serializable_without_reconstructing_policy(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            touch_required_paths(root)
            touch_reference_docs(root)
            touch(root, "CLAUDE.md", "`tracks/fpa/modes/ghost-mode.md` entrevista")
            touch(root, "_method-wiki/concepts/generic-method.md", "Acme")

            report = check_product_contract(root)
            records = [finding.to_record() for finding in report.findings]

            self.assertGreaterEqual(len(records), 3)
            for record in records:
                self.assertEqual(
                    set(record),
                    {"category", "target", "message", "severity"},
                )
                self.assertTrue(record["category"])
                self.assertTrue(record["target"])
                self.assertTrue(record["message"])
                self.assertTrue(record["severity"])

            report_record = report.to_record()
            self.assertEqual(report_record["contract_version"], "1.0")
            self.assertEqual(len(report_record["findings"]), len(report.findings))

    def test_policy_centralizes_layers_and_promotion_criteria(self):
        contract = ACCOUNTING_OPS_PRODUCT_CONTRACT

        self.assertEqual(contract.version, "1.0")
        self.assertIn(ProductLayer.SYSTEM, tuple(layer.name for layer in contract.layers))
        self.assertIn(ProductLayer.INGESTION, tuple(layer.name for layer in contract.layers))
        self.assertIn(PromotionDestination.WORKFLOW, contract.promotion.destinations)
        self.assertIn("evidence", contract.promotion.required_fields)
        self.assertIn("next_test", contract.promotion.required_fields)
        self.assertIn("context/companies/", contract.promotion.situated_source_prefixes)
        self.assertTrue(contract.promotion.generalization_required)

    def test_new_structural_rule_is_added_to_policy_without_changing_cli_adapter(self):
        from scripts.accounting_ops_doctor import render_result

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            touch_required_paths(root)
            touch_reference_docs(root)
            extended_contract = replace(
                ACCOUNTING_OPS_PRODUCT_CONTRACT,
                required_paths=ACCOUNTING_OPS_PRODUCT_CONTRACT.required_paths
                + ("docs/policy/new-rule.md",),
            )

            report = extended_contract.check(root)
            rendered = render_result(report)

            self.assertIn("docs/policy/new-rule.md", report.missing)
            self.assertIn("docs/policy/new-rule.md", rendered)

    def test_product_contract_accepts_book_and_company_promotion_records(self):
        book_decision = PromotionDecision(
            source_kind=PromotionSourceKind.BOOK,
            origin="books/budgeting/distillations/chapter-2.md",
            candidate="Conectar contribuição, volume e mix à sensibilidade.",
            probable_destination=PromotionDestination.CONCEPT,
            justification="A ideia melhora uma pergunta recorrente de orçamento.",
            confidence=PromotionConfidence.HIGH,
            evidence=("Destilação do Capítulo 2",),
            next_test="Aplicar em um caso industrial.",
            not_promoted_content=("Exemplos extensos.",),
            editorial_status=EditorialStatus.PROMOTED,
        )
        company_decision = PromotionDecision(
            source_kind=PromotionSourceKind.COMPANY_CONTEXT,
            origin="context/companies/company-slug/promotion-matrix.md",
            candidate="Abrir margem por mercado final e aplicação.",
            probable_destination=PromotionDestination.HEURISTIC,
            justification="A pergunta pode ser útil em outras empresas industriais.",
            confidence=PromotionConfidence.MEDIUM,
            evidence=("Matriz de candidatos da Acme",),
            next_test="Aplicar em outra companhia industrial.",
            not_promoted_content=("Fatos específicos da Acme.",),
            editorial_status=EditorialStatus.PROMOTED,
            generalization_statement="A regra foi reescrita para uso comparável.",
        )

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            touch_required_paths(root)
            touch_reference_docs(root)
            touch(root, book_decision.origin)
            touch(root, company_decision.origin)
            register_promotion(
                book_decision,
                root,
                "books/budgeting/promotions/2026-08-23-book.md",
            )
            register_promotion(
                company_decision,
                root,
                "context/companies/company-slug/promotions/2026-08-23-company.md",
            )

            report = check_product_contract(root)

        self.assertTrue(report.ok)
        self.assertEqual(
            report.promotion_records,
            (
                "books/budgeting/promotions/2026-08-23-book.md",
                "context/companies/company-slug/promotions/2026-08-23-company.md",
            ),
        )
        self.assertEqual(report.findings_for(FindingCategory.PROMOTION), ())

    def test_product_contract_reports_an_incoherent_promotion_record(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            touch_required_paths(root)
            touch_reference_docs(root)
            touch(
                root,
                "books/budgeting/promotions/broken.md",
                "---\nsource_kind: \"book\"\n---\n",
            )

            report = check_product_contract(root)
            from scripts.accounting_ops_doctor import render_result

            rendered = render_result(report)

            findings = report.findings_for(FindingCategory.PROMOTION)

        self.assertFalse(report.ok)
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0].target, "books/budgeting/promotions/broken.md")
        self.assertEqual(findings[0].severity, FindingSeverity.ERROR)
        self.assertIn("Campos ausentes", findings[0].message)
        self.assertIn("Promotion findings", rendered)
        self.assertIn("books/budgeting/promotions/broken.md", rendered)

    def test_product_contract_keeps_company_records_in_the_situated_layer(self):
        decision = PromotionDecision(
            source_kind=PromotionSourceKind.COMPANY_CONTEXT,
            origin="context/companies/company-slug/promotion-matrix.md",
            candidate="Abrir margem por mercado final e aplicação.",
            probable_destination=PromotionDestination.HEURISTIC,
            justification="A pergunta pode ser útil em outras empresas.",
            confidence=PromotionConfidence.MEDIUM,
            evidence=("Matriz de candidatos da Acme",),
            next_test="Aplicar em outra companhia industrial.",
            not_promoted_content=("Fatos específicos da Acme.",),
            editorial_status=EditorialStatus.PROMOTED,
            generalization_statement="A pergunta foi reescrita como regra geral.",
        )

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            touch_required_paths(root)
            touch_reference_docs(root)
            touch(root, decision.origin)
            touch(
                root,
                "books/budgeting/promotions/company-in-wrong-layer.md",
                decision.to_markdown(),
            )

            report = check_product_contract(root)

        findings = report.findings_for(FindingCategory.PROMOTION)
        self.assertFalse(report.ok)
        self.assertEqual(len(findings), 1)
        self.assertIn("camada context/companies/", findings[0].message)

    def test_product_contract_reports_missing_promotion_origin(self):
        decision = PromotionDecision(
            source_kind=PromotionSourceKind.BOOK,
            origin="books/budgeting/distillations/missing.md",
            candidate="Conectar drivers de contribuição e volume.",
            probable_destination=PromotionDestination.CONCEPT,
            justification="A ideia parece reutilizável.",
            confidence=PromotionConfidence.MEDIUM,
            evidence=("Capítulo de orçamento",),
            next_test="Aplicar em um caso industrial.",
            not_promoted_content=("Exemplos extensos.",),
            editorial_status=EditorialStatus.PROMOTED,
        )

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            touch_required_paths(root)
            touch_reference_docs(root)
            touch(
                root,
                "books/budgeting/promotions/missing-origin.md",
                decision.to_markdown(),
            )

            report = check_product_contract(root)

        findings = report.findings_for(FindingCategory.PROMOTION)
        self.assertFalse(report.ok)
        self.assertEqual(len(findings), 1)
        self.assertIn("origin não existe", findings[0].message)


if __name__ == "__main__":
    unittest.main()
