#!/usr/bin/env python3
"""Adapter de challenge para o contrato canônico de Variance.

Este módulo não diagnostica uma variação a partir de dados brutos. Ele recebe
uma ``VarianceExplanation`` já construída e transforma sua decisão em uma
saída de challenge, preservando status, confiança, evidência e ação.
"""

from __future__ import annotations

from dataclasses import dataclass

from scripts.variance_explanation_contract import (
    Confidence,
    DriverKind,
    DriverStatus,
    ExplanationStatus,
    Recurrence,
    Reconciliation,
    VarianceExplanation,
)


_READING_PREFIXES = {
    ExplanationStatus.CONFIRMED: "Leitura confirmada",
    ExplanationStatus.HYPOTHESIS: "Leitura hipotética",
    ExplanationStatus.INSUFFICIENT_EVIDENCE: "Leitura preliminar com evidência insuficiente",
}


def _unique(items: list[str]) -> tuple[str, ...]:
    return tuple(dict.fromkeys(items))


@dataclass(frozen=True)
class ChallengeClassification:
    """Classificação que o challenge acrescenta sem reclassificar o domínio."""

    accounting_effects: tuple[str, ...]
    operational_drivers: tuple[str, ...]
    hypothesis_drivers: tuple[str, ...]
    recurrence: Recurrence
    recurrence_detail: str | None

    def to_record(self) -> dict[str, object]:
        return {
            "accounting_effects": list(self.accounting_effects),
            "operational_drivers": list(self.operational_drivers),
            "hypothesis_drivers": list(self.hypothesis_drivers),
            "recurrence": self.recurrence.value,
            "recurrence_detail": self.recurrence_detail,
        }


@dataclass(frozen=True)
class ChallengeResult:
    """Resultado do challenge sem alterar a decisão canônica de origem."""

    source: VarianceExplanation
    fragilities: tuple[str, ...]
    quantitative_test: Reconciliation
    revised_reading: str
    pending_confirmation: tuple[str, ...]
    status: ExplanationStatus
    confidence: Confidence
    classification: ChallengeClassification

    def to_record(self) -> dict[str, object]:
        """Retorna o registro canônico junto da camada específica do challenge."""

        return {
            "original": self.source.to_record(),
            "fragilities": list(self.fragilities),
            "quantitative_test": self.quantitative_test.value,
            "revised_reading": self.revised_reading,
            "pending_confirmation": list(self.pending_confirmation),
            "status": self.status.value,
            "confidence": self.confidence.value,
            "classification": self.classification.to_record(),
        }


def challenge_variance(explanation: VarianceExplanation) -> ChallengeResult:
    """Desafia uma explicação canônica sem reimplementar sua lógica de cálculo."""

    if not isinstance(explanation, VarianceExplanation):
        raise TypeError("challenge_variance precisa receber uma VarianceExplanation.")

    fragilities: list[str] = []
    pending_confirmation: list[str] = []
    accounting_effects: list[str] = []
    operational_drivers: list[str] = []
    hypothesis_drivers: list[str] = []
    quantitative_test = explanation.reconciliation
    variance_record = explanation.to_record()["baseline"]
    variance_text = variance_record["variance"]

    if quantitative_test is Reconciliation.INCOMPLETE:
        fragilities.append("A reconciliação está incompleta; há driver sem impacto conhecido.")
        pending_confirmation.append(
            f"Reconciliar os impactos conhecidos com a Variance total de {variance_text}."
        )
    elif quantitative_test is Reconciliation.UNRECONCILED:
        fragilities.append("Os impactos dos drivers não reconciliam com a Variance total.")
        pending_confirmation.append(
            f"Reconciliar os impactos dos drivers com a Variance total de {variance_text}."
        )

    for driver in explanation.drivers:
        if driver.kind is DriverKind.ACCOUNTING:
            accounting_effects.append(driver.name)
        elif driver.kind is DriverKind.OPERATIONAL:
            operational_drivers.append(driver.name)
        if driver.status is DriverStatus.HYPOTHESIS:
            hypothesis_drivers.append(driver.name)
            fragilities.append(f"Driver '{driver.name}' é hipótese, não fato confirmado.")
            pending_confirmation.append(f"Confirmar ou refutar o driver hipotético '{driver.name}'.")
        elif driver.status is DriverStatus.MISSING_EVIDENCE:
            fragilities.append(f"Driver '{driver.name}' permanece sem evidência suficiente.")
            pending_confirmation.extend(
                f"Obter '{gap}' para confirmar o driver '{driver.name}'."
                for gap in driver.evidence_gap
            )

    if explanation.status is not ExplanationStatus.CONFIRMED and not explanation.evidence:
        fragilities.append("A explicação não possui evidência suficiente para sustentar a leitura.")
        pending_confirmation.append("Obter evidência antes de transformar a explicação em narrativa oficial.")

    unique_fragilities = _unique(fragilities)
    unique_pending = _unique(pending_confirmation)
    reading_parts = [
        f"{_READING_PREFIXES[explanation.status]}: {' '.join(explanation.impact)}",
        f"Próximo passo: {explanation.action.description}",
    ]
    if unique_pending:
        reading_parts.append(f"Confirmações pendentes: {' '.join(unique_pending)}")
    revised_reading = " ".join(reading_parts)

    return ChallengeResult(
        source=explanation,
        fragilities=unique_fragilities,
        quantitative_test=quantitative_test,
        revised_reading=revised_reading,
        pending_confirmation=unique_pending,
        status=explanation.status,
        confidence=explanation.confidence,
        classification=ChallengeClassification(
            accounting_effects=_unique(accounting_effects),
            operational_drivers=_unique(operational_drivers),
            hypothesis_drivers=_unique(hypothesis_drivers),
            recurrence=explanation.recurrence,
            recurrence_detail=explanation.recurrence_detail,
        ),
    )


__all__ = ["ChallengeClassification", "ChallengeResult", "challenge_variance"]
