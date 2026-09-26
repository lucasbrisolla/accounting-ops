from __future__ import annotations

import unittest
from dataclasses import replace
from decimal import Decimal
from pathlib import Path

from scripts.variance_explanation_contract import (
    Action,
    Baseline,
    Confidence,
    Driver,
    DriverKind,
    DriverStatus,
    ExplanationStatus,
    Materiality,
    Recurrence,
    VarianceExplanation,
)
from scripts.variance_output_adapters import (
    PresentationDensity,
    build_management_story,
    build_one_pager,
)


ROOT = Path(__file__).resolve().parents[1]


def explanation_for_domain(
    domain: str,
    *,
    reference_name: str = "Budget",
    kind: DriverKind = DriverKind.OPERATIONAL,
) -> VarianceExplanation:
    return VarianceExplanation(
        baseline=Baseline(
            actual=Decimal("120"),
            reference=Decimal("100"),
            reference_name=reference_name,
            unit="R$",
        ),
        materiality=Materiality(
            absolute_threshold=Decimal("10"),
            decision_relevance=f"A variação de {domain} altera a decisão gerencial.",
            decision_relevant=True,
        ),
        breakdown=(domain,),
        drivers=(
            Driver(
                name=f"Driver de {domain}",
                impact=Decimal("20"),
                evidence=(f"Evidência de {domain}",),
                status=DriverStatus.CONFIRMED,
                kind=kind,
            ),
        ),
        evidence=(f"Relatório de {domain}",),
        impact=(f"A variação de {domain} pressiona a leitura gerencial.",),
        action=Action(
            description=f"Monitorar a variação de {domain} no próximo fechamento.",
            owner="FP&A",
            timing="Próximo fechamento",
        ),
        recurrence=Recurrence.RECURRING,
        confidence=Confidence.HIGH,
        status=ExplanationStatus.CONFIRMED,
    )


def incomplete_accounting_explanation() -> VarianceExplanation:
    return VarianceExplanation(
        baseline=Baseline(
            actual=Decimal("120"),
            reference=Decimal("100"),
            reference_name="Forecast",
            unit="R$",
        ),
        materiality=Materiality(
            percentage_threshold=Decimal("5"),
            decision_relevance="Pode alterar o outlook do trimestre.",
            decision_relevant=True,
        ),
        breakdown=("Reclassificação", "Custo comercial"),
        drivers=(
            Driver(
                name="Reclassificação contábil",
                impact=Decimal("12"),
                evidence=("Memória de lançamento",),
                status=DriverStatus.CONFIRMED,
                kind=DriverKind.ACCOUNTING,
            ),
            Driver(
                name="Custo comercial ainda sem suporte",
                impact=None,
                evidence=(),
                status=DriverStatus.MISSING_EVIDENCE,
                kind=DriverKind.COMMERCIAL,
                evidence_gap=("Suporte comercial do lançamento",),
            ),
        ),
        evidence=("DRE preliminar e razão analítica",),
        impact=("Ainda não é possível separar o efeito contábil do efeito comercial.",),
        action=Action(
            description="Reconciliar o lançamento e obter o suporte comercial.",
            owner="Controladoria",
            timing="Antes do forecast mensal",
        ),
        recurrence=Recurrence.TIMING,
        recurrence_detail="Reverte quando o lançamento for apropriado ao período correto.",
        confidence=Confidence.LOW,
        status=ExplanationStatus.INSUFFICIENT_EVIDENCE,
        primary_driver_name="Custo comercial ainda sem suporte",
    )


class VarianceOutputAdapterTests(unittest.TestCase):
    def test_one_pager_preserves_the_canonical_decision_fields(self):
        explanation = explanation_for_domain("OPEX")
        canonical = explanation.to_record()

        record = build_one_pager(explanation).to_record()

        self.assertEqual(record["format"], "one_pager")
        self.assertEqual(record["original"], canonical)
        self.assertEqual(record["numbers"], canonical["baseline"])
        self.assertEqual(record["breakdown"], canonical["breakdown"])
        self.assertEqual(record["evidence"], canonical["evidence"])
        self.assertEqual(record["drivers"], canonical["drivers"])
        self.assertEqual(record["recurrence"], canonical["recurrence"])
        self.assertEqual(record["recurrence_detail"], canonical["recurrence_detail"])
        self.assertEqual(record["impact"], canonical["impact"])
        self.assertEqual(record["next_step"], canonical["action"])
        self.assertEqual(record["confidence"], canonical["confidence"])
        self.assertEqual(record["status"], canonical["status"])

    def test_management_story_preserves_driver_impact_and_monitoring(self):
        explanation = explanation_for_domain("Industrial", kind=DriverKind.OPERATIONAL)
        canonical = explanation.to_record()

        record = build_management_story(explanation).to_record()

        self.assertEqual(record["format"], "management_story")
        self.assertEqual(record["original"], canonical)
        self.assertEqual(record["principal_driver"], canonical["primary_driver_name"])
        self.assertEqual(record["drivers"], canonical["drivers"])
        self.assertEqual(record["impact"], canonical["impact"])
        self.assertEqual(record["managerial_implication"], canonical["impact"])
        self.assertEqual(record["monitoring"], canonical["action"])
        self.assertEqual(record["recurrence"], canonical["recurrence"])
        self.assertEqual(record["recurrence_detail"], canonical["recurrence_detail"])
        self.assertEqual(record["confidence"], canonical["confidence"])
        self.assertEqual(record["status"], canonical["status"])

    def test_uncertainty_and_accounting_effect_remain_visible_in_both_formats(self):
        explanation = incomplete_accounting_explanation()

        one_pager = build_one_pager(explanation).to_record()
        story = build_management_story(explanation).to_record()

        self.assertEqual(one_pager["original"], story["original"])
        self.assertEqual(one_pager["confidence"], "low")
        self.assertEqual(one_pager["status"], "insufficient_evidence")
        self.assertEqual(
            one_pager["recurrence_detail"],
            "Reverte quando o lançamento for apropriado ao período correto.",
        )
        self.assertEqual(one_pager["recurrence_detail"], story["recurrence_detail"])
        self.assertEqual(one_pager["drivers"][0]["kind"], "accounting")
        self.assertEqual(one_pager["drivers"][1]["status"], "missing_evidence")
        for caveat in (one_pager["caveat"], story["caveat"]):
            self.assertIn("contábil", caveat.lower())
            self.assertIn("incompleta", caveat.lower())
            self.assertIn("Custo comercial ainda sem suporte", caveat)
        self.assertEqual(story["managerial_implication"], explanation.to_record()["impact"])
        self.assertNotIn("principalmente por", story["headline"].lower())
        self.assertIn("evidência insuficiente", story["headline"].lower())
        self.assertIn("Suporte comercial do lançamento", story["caveat"])

    def test_same_decision_has_no_semantic_drift_across_industrial_commercial_opex_and_forecast(self):
        scenarios = (
            ("Industrial", "Budget", DriverKind.OPERATIONAL),
            ("Comercial", "Budget", DriverKind.COMMERCIAL),
            ("OPEX", "Budget", DriverKind.OPERATIONAL),
            ("Forecast", "Forecast", DriverKind.COMMERCIAL),
        )

        for domain, reference_name, kind in scenarios:
            with self.subTest(domain=domain):
                explanation = explanation_for_domain(
                    domain,
                    reference_name=reference_name,
                    kind=kind,
                )
                one_pager = build_one_pager(
                    explanation,
                    audience="gestão",
                    channel="one-pager",
                ).to_record()
                story = build_management_story(
                    explanation,
                    audience="diretoria",
                    channel="report",
                ).to_record()

                self.assertEqual(one_pager["original"], story["original"])
                self.assertEqual(one_pager["numbers"], story["original"]["baseline"])
                self.assertEqual(one_pager["drivers"], story["drivers"])
                self.assertEqual(one_pager["impact"], story["managerial_implication"])
                self.assertEqual(one_pager["confidence"], story["confidence"])
                self.assertEqual(one_pager["status"], story["status"])
                self.assertEqual(one_pager["recurrence"], story["recurrence"])
                self.assertEqual(one_pager["recurrence_detail"], story["recurrence_detail"])

    def test_outputs_cannot_drift_after_construction(self):
        explanation = explanation_for_domain("OPEX")
        one_pager = build_one_pager(explanation)
        story = build_management_story(explanation)

        with self.assertRaises(TypeError):
            one_pager.numbers["variance"] = "999.00"
        with self.assertRaises(TypeError):
            one_pager.drivers[0]["name"] = "Causa mutada"
        with self.assertRaises(TypeError):
            story.monitoring["description"] = "Ação mutada"

        self.assertEqual(one_pager.to_record()["original"], explanation.to_record())
        self.assertEqual(story.to_record()["original"], explanation.to_record())

    def test_primary_driver_comes_from_the_canonical_decision_not_tuple_position(self):
        explanation = incomplete_accounting_explanation()
        reordered = replace(explanation, drivers=tuple(reversed(explanation.drivers)))

        original_story = build_management_story(explanation)
        reordered_story = build_management_story(reordered)

        self.assertEqual(original_story.principal_driver, "Custo comercial ainda sem suporte")
        self.assertEqual(reordered_story.principal_driver, original_story.principal_driver)
        self.assertEqual(reordered_story.headline, original_story.headline)

    def test_channel_and_density_change_presentation_without_changing_semantics(self):
        explanation = explanation_for_domain("Comercial", kind=DriverKind.COMMERCIAL)

        slide = build_management_story(explanation, channel="slide").to_record()
        report = build_management_story(explanation, channel="report").to_record()
        board = build_management_story(
            explanation,
            audience="diretoria",
            channel="mensagem",
        ).to_record()
        technical = build_management_story(
            explanation,
            audience="equipe técnica",
            channel="mensagem",
        ).to_record()

        self.assertEqual(slide["density"], PresentationDensity.CONCISE.value)
        self.assertEqual(report["density"], PresentationDensity.DETAILED.value)
        self.assertEqual(board["density"], PresentationDensity.CONCISE.value)
        self.assertEqual(technical["density"], PresentationDensity.DETAILED.value)
        self.assertNotEqual(slide["message"], report["message"])
        for field in ("original", "drivers", "impact", "confidence", "status"):
            self.assertEqual(slide[field], report[field])

    def test_headline_includes_the_canonical_unit_and_natural_direction(self):
        story = build_management_story(explanation_for_domain("OPEX")).to_record()

        self.assertIn("R$ 20.00 acima de Budget", story["headline"])
        self.assertNotIn("acima de 20.00 contra", story["headline"])

if __name__ == "__main__":
    unittest.main()
