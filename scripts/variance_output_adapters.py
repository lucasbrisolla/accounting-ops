#!/usr/bin/env python3
"""Adapters de apresentação para a decisão canônica de Variance.

As funções públicas deste módulo recebem apenas uma ``VarianceExplanation``.
Elas ajustam formato, audiência e canal, mas não recalculam baseline,
reconciliação, drivers, impacto ou confiança.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from decimal import Decimal
from enum import Enum
from types import MappingProxyType

from scripts.variance_explanation_contract import (
    Confidence,
    DriverKind,
    DriverStatus,
    ExplanationStatus,
    Recurrence,
    Reconciliation,
    VarianceExplanation,
)


_STATUS_LABELS = {
    ExplanationStatus.CONFIRMED: "confirmada",
    ExplanationStatus.HYPOTHESIS: "hipótese",
    ExplanationStatus.INSUFFICIENT_EVIDENCE: "insuficiente",
}
_RECONCILIATION_LABELS = {
    Reconciliation.RECONCILED: "reconciliada",
    Reconciliation.UNRECONCILED: "não reconciliada",
    Reconciliation.INCOMPLETE: "incompleta",
}


class PresentationDensity(str, Enum):
    CONCISE = "concise"
    STANDARD = "standard"
    DETAILED = "detailed"


_CHANNEL_DENSITY = {
    "slide": PresentationDensity.CONCISE,
    "reunião": PresentationDensity.CONCISE,
    "meeting": PresentationDensity.CONCISE,
    "e-mail": PresentationDensity.STANDARD,
    "email": PresentationDensity.STANDARD,
    "report": PresentationDensity.DETAILED,
    "one-pager": PresentationDensity.DETAILED,
}
_AUDIENCE_DENSITY = {
    "conselho": PresentationDensity.CONCISE,
    "diretoria": PresentationDensity.CONCISE,
    "gestão": PresentationDensity.STANDARD,
    "equipe técnica": PresentationDensity.DETAILED,
}


def _non_empty_text(value: str, field_name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} precisa ser um texto não vazio.")
    return value.strip()


def _format_decimal(value: Decimal) -> str:
    return format(value.quantize(Decimal("0.01")), "f")


def _format_percentage(value: object) -> str:
    return _format_decimal(abs(Decimal(str(value))))


def _freeze(value: object) -> object:
    if isinstance(value, Mapping):
        return MappingProxyType({key: _freeze(item) for key, item in value.items()})
    if isinstance(value, (list, tuple)):
        return tuple(_freeze(item) for item in value)
    return value


def _to_record_value(value: object) -> object:
    if isinstance(value, Mapping):
        return {key: _to_record_value(item) for key, item in value.items()}
    if isinstance(value, tuple):
        return [_to_record_value(item) for item in value]
    return value


def _copy_mapping(value: object, field_name: str) -> Mapping[str, object]:
    if not isinstance(value, dict):
        raise TypeError(f"O registro canônico precisa conter {field_name} como objeto.")
    frozen = _freeze(value)
    if not isinstance(frozen, Mapping):
        raise TypeError(f"O registro canônico precisa conter {field_name} como objeto.")
    return frozen


def _copy_driver_records(record: dict[str, object]) -> tuple[Mapping[str, object], ...]:
    drivers = record["drivers"]
    if not isinstance(drivers, list):
        raise TypeError("O registro canônico precisa conter drivers como lista.")
    return tuple(_copy_mapping(driver, "drivers") for driver in drivers)


def _direction(explanation: VarianceExplanation) -> str:
    variance = explanation.baseline.variance
    if variance > 0:
        return "acima"
    if variance < 0:
        return "abaixo"
    return "em linha"


def _principal_driver(explanation: VarianceExplanation) -> str:
    return explanation.primary_driver_name


def _format_amount(value: Decimal, unit: object) -> str:
    unit_text = _non_empty_text(unit, "unit") if isinstance(unit, str) else "unidades"
    amount = _format_decimal(abs(value))
    if unit_text in {"R$", "US$", "$", "€", "£"}:
        return f"{unit_text} {amount}"
    return f"{amount} {unit_text}"


def _build_headline(
    explanation: VarianceExplanation,
    baseline_record: dict[str, object],
    principal_driver: str,
) -> str:
    reference_name = baseline_record["reference_name"]
    variance = explanation.baseline.variance
    if variance == 0:
        comparison = f"Actual ficou em linha com {reference_name}"
    else:
        amount = _format_amount(variance, baseline_record["unit"])
        percent = baseline_record["variance_percent"]
        percent_clause = ""
        if percent is not None:
            percent_clause = f" ({_format_percentage(percent)}%)"
        comparison = (
            f"Actual ficou {amount} {_direction(explanation)} de {reference_name}"
            f"{percent_clause}"
        )

    if explanation.status is ExplanationStatus.CONFIRMED:
        return f"{comparison}, principalmente por {principal_driver}."
    if explanation.status is ExplanationStatus.HYPOTHESIS:
        return (
            f"{comparison}; a leitura permanece hipotética. "
            f"Driver principal declarado: {principal_driver}."
        )
    return (
        f"{comparison}; a causa permanece com evidência insuficiente. "
        f"Driver principal declarado: {principal_driver}."
    )


def _build_caveat(explanation: VarianceExplanation) -> str:
    notes: list[str] = []
    accounting_drivers = [
        driver.name
        for driver in explanation.drivers
        if driver.kind is DriverKind.ACCOUNTING
    ]
    if accounting_drivers:
        names = ", ".join(accounting_drivers)
        notes.append(
            f"Efeito contábil identificado em {names}; natureza contábil preservada separadamente."
        )

    if explanation.reconciliation is not Reconciliation.RECONCILED:
        reconciliation = _RECONCILIATION_LABELS[explanation.reconciliation]
        notes.append(
            f"A reconciliação está {reconciliation}; a composição da Variance ainda não está fechada."
        )

    unconfirmed_drivers = [
        driver.name
        for driver in explanation.drivers
        if driver.status is not DriverStatus.CONFIRMED
    ]
    if unconfirmed_drivers:
        names = ", ".join(unconfirmed_drivers)
        status = _STATUS_LABELS[explanation.status]
        notes.append(f"A leitura é {status}; falta confirmar evidência para {names}.")
        evidence_gaps = [
            f"{driver.name}: {', '.join(driver.evidence_gap)}"
            for driver in explanation.drivers
            if driver.evidence_gap
        ]
        if evidence_gaps:
            notes.append(f"Lacunas de evidência: {'; '.join(evidence_gaps)}.")
    elif explanation.status is not ExplanationStatus.CONFIRMED:
        status = _STATUS_LABELS[explanation.status]
        notes.append(f"A leitura é {status}; não deve ser apresentada como causa confirmada.")

    if explanation.recurrence is Recurrence.TIMING:
        notes.append(
            f"O efeito está classificado como timing: {explanation.recurrence_detail}"
        )
    elif explanation.recurrence is Recurrence.ONE_OFF:
        notes.append(
            f"O efeito está classificado como one-off: {explanation.recurrence_detail}"
        )

    if not notes:
        return "Leitura confirmada, reconciliada e sem ressalva adicional no contrato canônico."
    return " ".join(notes)


def _resolve_density(
    density: PresentationDensity | str | None,
    *,
    audience: str,
    channel: str,
) -> PresentationDensity:
    if density is not None:
        try:
            return density if isinstance(density, PresentationDensity) else PresentationDensity(density)
        except ValueError as error:
            allowed = ", ".join(item.value for item in PresentationDensity)
            raise ValueError(f"density precisa ser uma de: {allowed}.") from error
    return _CHANNEL_DENSITY.get(
        channel.casefold(),
        _AUDIENCE_DENSITY.get(audience.casefold(), PresentationDensity.STANDARD),
    )


def _build_message(
    *,
    headline: str,
    caveat: str,
    impact: tuple[str, ...],
    action: Mapping[str, object],
    density: PresentationDensity,
) -> str:
    if density is PresentationDensity.CONCISE:
        return headline

    parts = [headline, f"Implicação: {' '.join(impact)}"]
    if density is PresentationDensity.DETAILED:
        parts.insert(1, f"Ressalva: {caveat}")
        monitoring = f"Monitoramento: {action['description']}"
        if action["owner"]:
            monitoring += f" Owner: {action['owner']}."
        if action["timing"]:
            monitoring += f" Timing: {action['timing']}."
        parts.append(monitoring)
    return " ".join(parts)


@dataclass(frozen=True)
class OnePagerResult:
    """Saída estruturada do adapter de one-pager."""

    source: VarianceExplanation
    audience: str
    channel: str
    density: PresentationDensity
    question: str
    summary: str
    numbers: Mapping[str, object]
    materiality: Mapping[str, object]
    breakdown: tuple[str, ...]
    drivers: tuple[Mapping[str, object], ...]
    evidence: tuple[str, ...]
    caveat: str
    recurrence: Recurrence
    recurrence_detail: str | None
    impact: tuple[str, ...]
    next_step: Mapping[str, object]
    confidence: Confidence
    status: ExplanationStatus
    reconciliation: Reconciliation
    requires_validation: bool

    def to_record(self) -> dict[str, object]:
        """Retorna o formato do one-pager sem perder a decisão original."""

        original = self.source.to_record()
        return {
            "format": "one_pager",
            "audience": self.audience,
            "channel": self.channel,
            "density": self.density.value,
            "original": original,
            "question": self.question,
            "summary": self.summary,
            "numbers": _to_record_value(self.numbers),
            "materiality": _to_record_value(self.materiality),
            "breakdown": list(self.breakdown),
            "drivers": [_to_record_value(driver) for driver in self.drivers],
            "evidence": list(self.evidence),
            "caveat": self.caveat,
            "recurrence": self.recurrence.value,
            "recurrence_detail": self.recurrence_detail,
            "impact": list(self.impact),
            "next_step": _to_record_value(self.next_step),
            "confidence": self.confidence.value,
            "status": self.status.value,
            "reconciliation": self.reconciliation.value,
            "requires_validation": self.requires_validation,
        }


@dataclass(frozen=True)
class ManagementStoryResult:
    """Saída estruturada do adapter de narrativa executiva."""

    source: VarianceExplanation
    audience: str
    channel: str
    density: PresentationDensity
    headline: str
    message: str
    principal_driver: str
    drivers: tuple[Mapping[str, object], ...]
    caveat: str
    managerial_implication: tuple[str, ...]
    monitoring: Mapping[str, object]
    breakdown: tuple[str, ...]
    materiality: Mapping[str, object]
    evidence: tuple[str, ...]
    recurrence: Recurrence
    recurrence_detail: str | None
    confidence: Confidence
    status: ExplanationStatus
    reconciliation: Reconciliation
    requires_validation: bool

    def to_record(self) -> dict[str, object]:
        """Retorna a narrativa junto da decisão canônica que a sustenta."""

        original = self.source.to_record()
        impact = list(self.managerial_implication)
        return {
            "format": "management_story",
            "audience": self.audience,
            "channel": self.channel,
            "density": self.density.value,
            "original": original,
            "headline": self.headline,
            "message": self.message,
            "principal_driver": self.principal_driver,
            "drivers": [_to_record_value(driver) for driver in self.drivers],
            "caveat": self.caveat,
            "managerial_implication": impact,
            "impact": impact,
            "monitoring": _to_record_value(self.monitoring),
            "breakdown": list(self.breakdown),
            "materiality": _to_record_value(self.materiality),
            "evidence": list(self.evidence),
            "recurrence": self.recurrence.value,
            "recurrence_detail": self.recurrence_detail,
            "confidence": self.confidence.value,
            "status": self.status.value,
            "reconciliation": self.reconciliation.value,
            "requires_validation": self.requires_validation,
        }


def build_one_pager(
    explanation: VarianceExplanation,
    *,
    audience: str = "gestão",
    channel: str = "one-pager",
    density: PresentationDensity | str | None = None,
) -> OnePagerResult:
    """Adapta uma decisão canônica para leitura de one-pager."""

    if not isinstance(explanation, VarianceExplanation):
        raise TypeError("build_one_pager precisa receber uma VarianceExplanation.")
    audience = _non_empty_text(audience, "audience")
    channel = _non_empty_text(channel, "channel")

    record = explanation.to_record()
    baseline = _copy_mapping(record["baseline"], "baseline")
    materiality = _copy_mapping(record["materiality"], "materiality")
    action = _copy_mapping(record["action"], "action")
    principal_driver = _principal_driver(explanation)
    resolved_density = _resolve_density(density, audience=audience, channel=channel)
    caveat = _build_caveat(explanation)
    headline = _build_headline(explanation, baseline, principal_driver)

    return OnePagerResult(
        source=explanation,
        audience=audience,
        channel=channel,
        density=resolved_density,
        question=(
            f"Qual variação estamos explicando? Actual vs. {baseline['reference_name']} "
            f"em {', '.join(explanation.breakdown)}."
        ),
        summary=_build_message(
            headline=headline,
            caveat=caveat,
            impact=explanation.impact,
            action=action,
            density=resolved_density,
        ),
        numbers=baseline,
        materiality=materiality,
        breakdown=explanation.breakdown,
        drivers=_copy_driver_records(record),
        evidence=explanation.evidence,
        caveat=caveat,
        recurrence=explanation.recurrence,
        recurrence_detail=explanation.recurrence_detail,
        impact=explanation.impact,
        next_step=action,
        confidence=explanation.confidence,
        status=explanation.status,
        reconciliation=explanation.reconciliation,
        requires_validation=explanation.requires_validation,
    )


def build_management_story(
    explanation: VarianceExplanation,
    *,
    audience: str = "diretoria",
    channel: str = "report",
    density: PresentationDensity | str | None = None,
) -> ManagementStoryResult:
    """Adapta uma decisão canônica para narrativa executiva curta."""

    if not isinstance(explanation, VarianceExplanation):
        raise TypeError("build_management_story precisa receber uma VarianceExplanation.")
    audience = _non_empty_text(audience, "audience")
    channel = _non_empty_text(channel, "channel")

    record = explanation.to_record()
    baseline = _copy_mapping(record["baseline"], "baseline")
    materiality = _copy_mapping(record["materiality"], "materiality")
    action = _copy_mapping(record["action"], "action")
    principal_driver = _principal_driver(explanation)
    resolved_density = _resolve_density(density, audience=audience, channel=channel)
    caveat = _build_caveat(explanation)
    headline = _build_headline(explanation, baseline, principal_driver)

    return ManagementStoryResult(
        source=explanation,
        audience=audience,
        channel=channel,
        density=resolved_density,
        headline=headline,
        message=_build_message(
            headline=headline,
            caveat=caveat,
            impact=explanation.impact,
            action=action,
            density=resolved_density,
        ),
        principal_driver=principal_driver,
        drivers=_copy_driver_records(record),
        caveat=caveat,
        managerial_implication=explanation.impact,
        monitoring=action,
        breakdown=explanation.breakdown,
        materiality=materiality,
        evidence=explanation.evidence,
        recurrence=explanation.recurrence,
        recurrence_detail=explanation.recurrence_detail,
        confidence=explanation.confidence,
        status=explanation.status,
        reconciliation=explanation.reconciliation,
        requires_validation=explanation.requires_validation,
    )


__all__ = [
    "ManagementStoryResult",
    "OnePagerResult",
    "PresentationDensity",
    "build_management_story",
    "build_one_pager",
]
