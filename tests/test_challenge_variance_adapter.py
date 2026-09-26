from __future__ import annotations

import unittest
from dataclasses import replace
from decimal import Decimal
from pathlib import Path

from scripts.challenge_variance_adapter import challenge_variance
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
    Reconciliation,
    VarianceExplanation,
)


ROOT = Path(__file__).resolve().parents[1]
CHALLENGE_SKILL = ROOT / "skills" / "challenge-variance-explanation" / "SKILL.md"


def confirmed_explanation() -> VarianceExplanation:
    return VarianceExplanation(
        baseline=Baseline(
            actual=Decimal("120"),
            reference=Decimal("100"),
            reference_name="Budget",
        ),
        materiality=Materiality(
            absolute_threshold=Decimal("10"),
            decision_relevance="Pressiona a margem operacional.",
            decision_relevant=True,
        ),
        breakdown=("OPEX",),
        drivers=(
            Driver(
                name="Volume de atividade",
                impact=Decimal("8"),
                evidence=("Relatório operacional",),
                status=DriverStatus.CONFIRMED,
            ),
            Driver(
                name="Serviços contratados",
                impact=Decimal("12"),
                evidence=("Razão analítica",),
                status=DriverStatus.CONFIRMED,
            ),
        ),
        evidence=("DRE gerencial",),
        impact=("O OPEX ficou 20 acima do Budget e pressionou a margem operacional.",),
        action=Action(
            description="Validar o reajuste e atualizar o Forecast.",
            owner="FP&A",
            timing="Próximo fechamento",
        ),
        recurrence=Recurrence.RECURRING,
        confidence=Confidence.HIGH,
        status=ExplanationStatus.CONFIRMED,
        primary_driver_name="Serviços contratados",
    )


class ChallengeVarianceAdapterTests(unittest.TestCase):
    def test_skill_classifies_nature_without_turning_it_into_fragility(self):
        content = CHALLENGE_SKILL.read_text(encoding="utf-8")

        self.assertIn("não são fragilidades por si só", content)
        self.assertIn("Preservar o status e a confiança", content)

    def test_confirmed_explanation_has_no_false_fragilities_and_preserves_action(self):
        explanation = confirmed_explanation()

        result = challenge_variance(explanation)

        self.assertIs(result.source, explanation)
        self.assertEqual(result.quantitative_test, Reconciliation.RECONCILED)
        self.assertEqual(result.fragilities, ())
        self.assertEqual(result.pending_confirmation, ())
        self.assertEqual(result.status, ExplanationStatus.CONFIRMED)
        self.assertEqual(result.confidence, Confidence.HIGH)
        self.assertIn("confirmada", result.revised_reading.lower())
        self.assertIn(explanation.action.description, result.revised_reading)

    def test_incomplete_explanation_surfaces_missing_evidence_and_validation(self):
        explanation = VarianceExplanation(
            baseline=Baseline(
                actual=Decimal("130"),
                reference=Decimal("110"),
                reference_name="Forecast",
            ),
            materiality=Materiality(
                percentage_threshold=Decimal("5"),
                decision_relevance="Pode alterar o outlook.",
                decision_relevant=True,
            ),
            breakdown=("Frete", "Eficiência operacional"),
            drivers=(
                Driver(
                    name="Frete urgente",
                    impact=Decimal("12"),
                    evidence=("Relatório de expedições",),
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
            evidence=("DRE e relatório de frete",),
            impact=("O efeito total ainda não pode ser atribuído ao Forecast.",),
            action=Action(
                description="Obter horas padrão e reais por linha.",
                timing="Antes do forecast mensal",
            ),
            recurrence=Recurrence.UNKNOWN,
            confidence=Confidence.MEDIUM,
            status=ExplanationStatus.INSUFFICIENT_EVIDENCE,
            primary_driver_name="Frete urgente",
        )

        result = challenge_variance(explanation)

        self.assertEqual(result.quantitative_test, Reconciliation.INCOMPLETE)
        self.assertIn("incompleta", " ".join(result.fragilities).lower())
        self.assertIn("Eficiência da linha", " ".join(result.fragilities))
        self.assertIn("Eficiência da linha", " ".join(result.pending_confirmation))
        self.assertIn("Horas padrão e reais por linha", " ".join(result.pending_confirmation))
        self.assertIn("Horas padrão e reais por linha", result.revised_reading)
        self.assertIn("preliminar", result.revised_reading.lower())
        self.assertEqual(result.status, ExplanationStatus.INSUFFICIENT_EVIDENCE)
        self.assertEqual(result.confidence, Confidence.MEDIUM)

    def test_competing_hypothesis_and_unreconciled_drivers_are_challenged(self):
        explanation = VarianceExplanation(
            baseline=Baseline(
                actual=Decimal("120"),
                reference=Decimal("100"),
                reference_name="Budget",
            ),
            materiality=Materiality(
                decision_relevance="Exige explicação gerencial.",
                decision_relevant=True,
            ),
            breakdown=("Margem",),
            drivers=(
                Driver(
                    name="Custo de material",
                    impact=Decimal("18"),
                    evidence=("Purchase price variance",),
                    status=DriverStatus.CONFIRMED,
                ),
                Driver(
                    name="Mix de produto",
                    impact=Decimal("5"),
                    evidence=("Sinal preliminar de mix",),
                    status=DriverStatus.HYPOTHESIS,
                ),
            ),
            evidence=("DRE e análise preliminar de mix",),
            impact=("A margem ficou abaixo do Budget.",),
            action=Action(description="Reconciliar preço, volume e mix."),
            recurrence=Recurrence.UNKNOWN,
            confidence=Confidence.MEDIUM,
            status=ExplanationStatus.HYPOTHESIS,
            primary_driver_name="Custo de material",
        )

        result = challenge_variance(explanation)

        self.assertEqual(result.quantitative_test, Reconciliation.UNRECONCILED)
        fragilities = " ".join(result.fragilities)
        self.assertIn("não reconciliam", fragilities.lower())
        self.assertIn("Mix de produto", fragilities)
        self.assertIn("hipótese", fragilities.lower())
        self.assertIn("Mix de produto", " ".join(result.pending_confirmation))
        self.assertIn("hipotética", result.revised_reading.lower())
        self.assertEqual(result.status, ExplanationStatus.HYPOTHESIS)
        self.assertEqual(result.confidence, Confidence.MEDIUM)

    def test_record_keeps_canonical_result_and_challenge_fields_separate(self):
        result = challenge_variance(confirmed_explanation())

        record = result.to_record()

        self.assertEqual(record["original"]["baseline"]["reference_name"], "Budget")
        self.assertEqual(record["original"]["reconciliation"], "reconciled")
        self.assertEqual(record["quantitative_test"], "reconciled")
        self.assertIn("fragilities", record)
        self.assertIn("pending_confirmation", record)
        self.assertEqual(record["confidence"], "high")

    def test_confirmed_accounting_one_off_is_classified_without_false_fragility(self):
        explanation = VarianceExplanation(
            baseline=Baseline(
                actual=Decimal("120"),
                reference=Decimal("100"),
                reference_name="Budget",
            ),
            materiality=Materiality(
                decision_relevance="Exige explicação de fechamento.",
                decision_relevant=True,
            ),
            breakdown=("Reclassificação",),
            drivers=(
                Driver(
                    name="Reclassificação contábil",
                    impact=Decimal("20"),
                    evidence=("Memória de lançamento",),
                    status=DriverStatus.CONFIRMED,
                    kind=DriverKind.ACCOUNTING,
                ),
            ),
            evidence=("Razão e suporte do lançamento",),
            impact=("A linha da DRE mudou, sem evidência de efeito operacional.",),
            action=Action(description="Confirmar a apresentação e o período do lançamento."),
            recurrence=Recurrence.ONE_OFF,
            recurrence_detail="Reclassificação exclusiva deste fechamento, sem repetição prevista.",
            confidence=Confidence.HIGH,
            status=ExplanationStatus.CONFIRMED,
        )

        result = challenge_variance(explanation)

        self.assertEqual(result.classification.accounting_effects, ("Reclassificação contábil",))
        self.assertEqual(result.classification.operational_drivers, ())
        self.assertEqual(result.classification.recurrence, Recurrence.ONE_OFF)
        self.assertEqual(
            result.classification.recurrence_detail,
            "Reclassificação exclusiva deste fechamento, sem repetição prevista.",
        )
        self.assertEqual(result.fragilities, ())
        self.assertEqual(result.pending_confirmation, ())
        self.assertIn("confirmada", result.revised_reading.lower())

    def test_timing_is_classified_and_preserves_the_reversal_detail(self):
        explanation = replace(
            confirmed_explanation(),
            recurrence=Recurrence.TIMING,
            recurrence_detail="Reverte no fechamento seguinte após a apropriação da nota.",
        )

        result = challenge_variance(explanation)

        self.assertEqual(result.classification.recurrence, Recurrence.TIMING)
        self.assertEqual(
            result.classification.recurrence_detail,
            "Reverte no fechamento seguinte após a apropriação da nota.",
        )
        self.assertEqual(result.fragilities, ())
        self.assertIn("confirmada", result.revised_reading.lower())


if __name__ == "__main__":
    unittest.main()
