from __future__ import annotations

import unittest
from decimal import Decimal
from pathlib import Path

from scripts.variance_explanation_contract import (
    Action,
    Baseline,
    Confidence,
    Driver,
    DriverStatus,
    ExplanationStatus,
    Materiality,
    Recurrence,
    Reconciliation,
    VarianceExplanation,
)


ROOT = Path(__file__).resolve().parents[1]
CANONICAL_MODULE = ROOT / "skills" / "explain-variance" / "SKILL.md"


class VarianceExplanationContractTests(unittest.TestCase):
    def test_actual_vs_budget_exposes_the_canonical_fields_and_reconciles(self):
        explanation = VarianceExplanation(
            baseline=Baseline(
                actual=Decimal("120"),
                reference=Decimal("100"),
                reference_name="Budget",
                unit="R$",
            ),
            materiality=Materiality(
                absolute_threshold=Decimal("10"),
                percentage_threshold=Decimal("5"),
                decision_relevance="Pressiona a margem operacional.",
                decision_relevant=True,
            ),
            breakdown=("OPEX",),
            drivers=(
                Driver(
                    name="Volume de atividade",
                    impact=Decimal("8"),
                    evidence=("Relatório operacional mensal",),
                    status=DriverStatus.CONFIRMED,
                ),
                Driver(
                    name="Serviços contratados",
                    impact=Decimal("12"),
                    evidence=("Razão analítica e contrato",),
                    status=DriverStatus.CONFIRMED,
                ),
            ),
            evidence=("DRE gerencial de junho",),
            impact=("O OPEX ficou 20 acima do Budget e pressionou a margem operacional.",),
            action=Action(
                description="Validar o reajuste dos serviços e atualizar o Forecast.",
                owner="FP&A",
                timing="Próximo fechamento",
            ),
            recurrence=Recurrence.RECURRING,
            confidence=Confidence.HIGH,
            status=ExplanationStatus.CONFIRMED,
            primary_driver_name="Serviços contratados",
        )

        record = explanation.to_record()

        self.assertEqual(explanation.baseline.variance, Decimal("20"))
        self.assertEqual(explanation.baseline.variance_percent, Decimal("20.00"))
        self.assertTrue(explanation.is_material)
        self.assertEqual(explanation.reconciliation, Reconciliation.RECONCILED)
        self.assertFalse(explanation.requires_validation)
        self.assertEqual(record["baseline"]["reference_name"], "Budget")
        self.assertEqual(record["baseline"]["unit"], "R$")
        self.assertEqual(record["baseline"]["variance"], "20.00")
        self.assertEqual(record["reconciliation"], "reconciled")
        self.assertEqual(record["status"], "confirmed")
        self.assertEqual(record["primary_driver_name"], "Serviços contratados")
        self.assertEqual(
            [driver["name"] for driver in record["drivers"]],
            ["Volume de atividade", "Serviços contratados"],
        )
        self.assertEqual(
            [driver["impact"] for driver in record["drivers"]],
            ["8.00", "12.00"],
        )
        self.assertEqual(
            record["action"],
            {
                "description": "Validar o reajuste dos serviços e atualizar o Forecast.",
                "owner": "FP&A",
                "timing": "Próximo fechamento",
            },
        )

    def test_actual_vs_forecast_preserves_hypothesis_and_incomplete_reconciliation(self):
        explanation = VarianceExplanation(
            baseline=Baseline(
                actual=Decimal("130"),
                reference=Decimal("110"),
                reference_name="Forecast",
                unit="R$",
            ),
            materiality=Materiality(
                percentage_threshold=Decimal("5"),
                decision_relevance="Pode alterar o outlook do trimestre.",
                decision_relevant=True,
            ),
            breakdown=("Frete", "Eficiência operacional"),
            drivers=(
                Driver(
                    name="Frete urgente",
                    impact=Decimal("12"),
                    evidence=("Relatório de expedições urgentes",),
                    status=DriverStatus.CONFIRMED,
                ),
                Driver(
                    name="Eficiência da linha",
                    impact=None,
                    evidence=(),
                    status=DriverStatus.MISSING_EVIDENCE,
                    evidence_gap=("Horas padrão e reais por linha",),
                ),
            ),
            evidence=("DRE gerencial e relatório de frete",),
            impact=("O efeito total ainda não pode ser atribuído ao Forecast.",),
            action=Action(
                description="Obter horas padrão e reais por linha antes de revisar o Forecast.",
                owner=None,
                timing="Antes do forecast mensal",
            ),
            recurrence=Recurrence.UNKNOWN,
            confidence=Confidence.MEDIUM,
            status=ExplanationStatus.INSUFFICIENT_EVIDENCE,
            primary_driver_name="Frete urgente",
        )

        record = explanation.to_record()

        self.assertEqual(explanation.baseline.reference_name, "Forecast")
        self.assertEqual(explanation.reconciliation, Reconciliation.INCOMPLETE)
        self.assertTrue(explanation.requires_validation)
        self.assertEqual(record["drivers"][1]["status"], "missing_evidence")
        self.assertIsNone(record["drivers"][1]["impact"])
        self.assertEqual(
            record["drivers"][1]["evidence_gap"],
            ["Horas padrão e reais por linha"],
        )
        self.assertEqual(record["status"], "insufficient_evidence")

    def test_confirmed_driver_requires_evidence(self):
        with self.assertRaises(ValueError):
            Driver(
                name="Custo sem suporte",
                impact=Decimal("10"),
                evidence=(),
                status=DriverStatus.CONFIRMED,
            )

    def test_confirmed_explanation_cannot_hide_an_unconfirmed_driver(self):
        with self.assertRaises(ValueError):
            VarianceExplanation(
                baseline=Baseline(
                    actual=Decimal("120"),
                    reference=Decimal("100"),
                    reference_name="Budget",
                ),
                materiality=Materiality(
                    decision_relevance="Impacto decisório.",
                    decision_relevant=True,
                ),
                breakdown=("Margem",),
                drivers=(
                    Driver(
                        name="Driver provável",
                        impact=Decimal("20"),
                        evidence=("Sinal preliminar",),
                        status=DriverStatus.HYPOTHESIS,
                    ),
                ),
                evidence=("DRE gerencial",),
                impact=("A margem foi afetada.",),
                action=Action(description="Validar o driver."),
                recurrence=Recurrence.UNKNOWN,
                confidence=Confidence.LOW,
                status=ExplanationStatus.CONFIRMED,
            )

    def test_decision_relevance_requires_an_explicit_boolean(self):
        with self.assertRaises(ValueError):
            Materiality(decision_relevance="Sem relevância para a decisão.")

        materiality = Materiality(
            decision_relevance="Sem relevância para a decisão.",
            decision_relevant=False,
        )

        self.assertFalse(
            materiality.evaluate(
                Baseline(actual=Decimal("120"), reference=Decimal("100"), reference_name="Budget")
            )
        )

    def test_hypothesis_requires_a_basis_and_missing_evidence_names_the_gap(self):
        with self.assertRaises(ValueError):
            Driver(
                name="Hipótese sem base",
                impact=Decimal("20"),
                evidence=(),
                status=DriverStatus.HYPOTHESIS,
            )

        with self.assertRaises(ValueError):
            Driver(
                name="Lacuna não nomeada",
                impact=None,
                evidence=("DRE preliminar",),
                status=DriverStatus.MISSING_EVIDENCE,
            )

    def test_multiple_drivers_require_a_canonical_primary_driver(self):
        with self.assertRaises(ValueError):
            VarianceExplanation(
                baseline=Baseline(
                    actual=Decimal("120"), reference=Decimal("100"), reference_name="Budget"
                ),
                materiality=Materiality(absolute_threshold=Decimal("10")),
                breakdown=("OPEX",),
                drivers=(
                    Driver(
                        name="Volume",
                        impact=Decimal("8"),
                        evidence=("Relatório operacional",),
                        status=DriverStatus.CONFIRMED,
                    ),
                    Driver(
                        name="Preço",
                        impact=Decimal("12"),
                        evidence=("Relatório comercial",),
                        status=DriverStatus.CONFIRMED,
                    ),
                ),
                evidence=("DRE gerencial",),
                impact=("O OPEX ficou acima do Budget.",),
                action=Action(description="Monitorar drivers."),
                recurrence=Recurrence.RECURRING,
                confidence=Confidence.HIGH,
                status=ExplanationStatus.CONFIRMED,
            )

    def test_timing_and_one_off_require_a_recurrence_detail(self):
        common = {
            "baseline": Baseline(
                actual=Decimal("120"), reference=Decimal("100"), reference_name="Budget"
            ),
            "materiality": Materiality(absolute_threshold=Decimal("10")),
            "breakdown": ("OPEX",),
            "drivers": (
                Driver(
                    name="Serviços contratados",
                    impact=Decimal("20"),
                    evidence=("Razão analítica",),
                    status=DriverStatus.CONFIRMED,
                ),
            ),
            "evidence": ("DRE gerencial",),
            "impact": ("O OPEX ficou acima do Budget.",),
            "action": Action(description="Monitorar a reversão."),
            "confidence": Confidence.HIGH,
            "status": ExplanationStatus.CONFIRMED,
        }
        for recurrence in (Recurrence.TIMING, Recurrence.ONE_OFF):
            with self.subTest(recurrence=recurrence):
                with self.assertRaises(ValueError):
                    VarianceExplanation(recurrence=recurrence, **common)

        explanation = VarianceExplanation(
            recurrence=Recurrence.TIMING,
            recurrence_detail="Reverte no fechamento de julho após a apropriação da nota.",
            **common,
        )
        self.assertEqual(
            explanation.to_record()["recurrence_detail"],
            "Reverte no fechamento de julho após a apropriação da nota.",
        )

    def test_non_finite_numbers_and_confirmed_low_confidence_are_rejected(self):
        for value in ("NaN", "Infinity", "-Infinity"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    Baseline(actual=value, reference=Decimal("100"), reference_name="Budget")

        with self.assertRaises(ValueError):
            VarianceExplanation(
                baseline=Baseline(
                    actual=Decimal("120"), reference=Decimal("100"), reference_name="Budget"
                ),
                materiality=Materiality(absolute_threshold=Decimal("10")),
                breakdown=("OPEX",),
                drivers=(
                    Driver(
                        name="Serviços contratados",
                        impact=Decimal("20"),
                        evidence=("Razão analítica",),
                        status=DriverStatus.CONFIRMED,
                    ),
                ),
                evidence=("DRE gerencial",),
                impact=("O OPEX ficou acima do Budget.",),
                action=Action(description="Monitorar o próximo fechamento."),
                recurrence=Recurrence.RECURRING,
                confidence=Confidence.LOW,
                status=ExplanationStatus.CONFIRMED,
            )

    def test_canonical_agent_module_publishes_the_interface_and_reference_scenarios(self):
        content = CANONICAL_MODULE.read_text(encoding="utf-8")

        for heading in (
            "## Interface",
            "## Sequência",
            "## Contrato de saída",
            "## Invariantes",
            "## Cenários de referência",
            "## Guardrails",
        ):
            self.assertIn(heading, content)

        for field in (
            "Baseline",
            "Materialidade",
            "Quebra",
            "Driver",
            "Evidência",
            "Impacto",
            "Ação",
            "Recorrência",
            "Confiança",
        ):
            self.assertIn(field, content)

        self.assertIn("Actual vs. Budget", content)
        self.assertIn("Actual vs. Forecast", content)


if __name__ == "__main__":
    unittest.main()
