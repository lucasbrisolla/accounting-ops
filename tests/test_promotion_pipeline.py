from __future__ import annotations

import unittest
import tempfile
from pathlib import Path

from scripts.promotion_pipeline import (
    EditorialStatus,
    PromotionConfidence,
    PromotionDecision,
    PromotionRecordError,
    PromotionSourceKind,
    load_promotion_record,
    register_promotion,
)
from scripts.accounting_ops_product_contract import PromotionDestination


class PromotionPipelineTests(unittest.TestCase):
    def test_book_decision_exposes_the_common_editorial_record(self):
        decision = PromotionDecision(
            source_kind=PromotionSourceKind.BOOK,
            origin="books/budgeting/distillations/chapter-2-cost-volume-profit-analysis.md",
            candidate="Conectar contribuição, volume, preço, custo fixo e mix à sensibilidade.",
            probable_destination=PromotionDestination.CONCEPT,
            justification="A ideia melhora uma pergunta recorrente de orçamento e forecast.",
            confidence=PromotionConfidence.HIGH,
            evidence=("Destilação do Cap. 2", "Aplicação no workflow de orçamento"),
            next_test="Aplicar em um caso industrial com cenários base, upside e downside.",
            not_promoted_content=("Exemplos numéricos extensos do capítulo.",),
            editorial_status=EditorialStatus.PROMOTED,
        )

        record = decision.to_record()

        self.assertEqual(record["source_kind"], "book")
        self.assertEqual(record["origin"], decision.origin)
        self.assertEqual(record["probable_destination"], "concept")
        self.assertEqual(record["confidence"], "high")
        self.assertEqual(record["evidence"], list(decision.evidence))
        self.assertEqual(record["not_promoted_content"], list(decision.not_promoted_content))
        self.assertEqual(record["editorial_status"], "promoted")

    def test_company_context_uses_the_same_record_and_requires_generalization(self):
        with self.assertRaisesRegex(PromotionRecordError, "generalização"):
            PromotionDecision(
                source_kind=PromotionSourceKind.COMPANY_CONTEXT,
                origin="context/companies/company-slug/promotion-matrix.md",
                candidate="Abrir margem industrial por mercado final e aplicação.",
                probable_destination=PromotionDestination.HEURISTIC,
                justification="A análise sugere uma pergunta potencialmente recorrente.",
                confidence=PromotionConfidence.MEDIUM,
                evidence=("promotion-matrix.md",),
                next_test="Aplicar em outra companhia industrial.",
                not_promoted_content=("Fatos específicos da Acme.",),
                editorial_status=EditorialStatus.PROMOTED,
            )

        decision = PromotionDecision(
            source_kind=PromotionSourceKind.COMPANY_CONTEXT,
            origin="context/companies/company-slug/promotion-matrix.md",
            candidate="Abrir margem industrial por mercado final e aplicação.",
            probable_destination=PromotionDestination.HEURISTIC,
            justification="A análise sugere uma pergunta potencialmente recorrente.",
            confidence=PromotionConfidence.MEDIUM,
            evidence=("promotion-matrix.md",),
            next_test="Aplicar em outra companhia industrial.",
            not_promoted_content=("Fatos específicos da Acme.",),
            editorial_status=EditorialStatus.PROMOTED,
            generalization_statement=(
                "A regra foi reescrita como pergunta geral, sem depender da Acme."
            ),
        )

        self.assertEqual(decision.to_record()["source_kind"], "company_context")

    def test_completed_decision_requires_next_test_or_explicit_reason_not_to_test(self):
        common = {
            "source_kind": PromotionSourceKind.BOOK,
            "origin": "books/budgeting/distillations/chapter-2.md",
            "candidate": "Conectar drivers de contribuição e volume.",
            "probable_destination": PromotionDestination.NONE,
            "justification": "A cobertura existente já é suficiente.",
            "confidence": PromotionConfidence.MEDIUM,
            "evidence": ("Capítulo 2",),
            "not_promoted_content": ("Exemplos extensos.",),
            "editorial_status": EditorialStatus.NOT_PROMOTED,
        }

        with self.assertRaisesRegex(PromotionRecordError, "next_test"):
            PromotionDecision(**common)

        decision = PromotionDecision(
            **common,
            no_test_justification="Não há lacuna operacional restante que justifique um teste.",
        )

        self.assertTrue(decision.is_complete)
        self.assertEqual(decision.to_record()["next_test"], None)

    def test_register_and_load_keep_the_same_decision_for_a_book_record(self):
        decision = PromotionDecision(
            source_kind=PromotionSourceKind.BOOK,
            origin="books/budgeting/distillations/chapter-2.md",
            candidate="Conectar drivers de contribuição e volume.",
            probable_destination=PromotionDestination.CONCEPT,
            justification="A ideia fecha uma lacuna recorrente de orçamento.",
            confidence=PromotionConfidence.HIGH,
            evidence=("Capítulo 2",),
            next_test="Aplicar em um caso industrial.",
            not_promoted_content=("Exemplos extensos.",),
            editorial_status=EditorialStatus.PROMOTED,
        )

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            origin = root / decision.origin
            origin.parent.mkdir(parents=True, exist_ok=True)
            origin.write_text("fonte", encoding="utf-8")
            written_path = register_promotion(
                decision,
                root,
                "books/budgeting/promotions/2026-08-23-chapter-2.md",
            )

            loaded = load_promotion_record(written_path)

        self.assertEqual(loaded.to_record(), decision.to_record())


if __name__ == "__main__":
    unittest.main()
