#!/usr/bin/env python3
"""Contrato executável do módulo canônico de explicação de Variance.

O módulo concentra invariantes da decisão analítica. Os callers podem adaptar o
registro retornado para challenge, one-pager, narrativa ou outro formato sem
recalcular a explicação.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from enum import Enum
from typing import Iterable, TypeVar


class DriverStatus(str, Enum):
    CONFIRMED = "confirmed"
    HYPOTHESIS = "hypothesis"
    MISSING_EVIDENCE = "missing_evidence"


class DriverKind(str, Enum):
    OPERATIONAL = "operational"
    ACCOUNTING = "accounting"
    COMMERCIAL = "commercial"
    UNKNOWN = "unknown"


class ExplanationStatus(str, Enum):
    CONFIRMED = "confirmed"
    HYPOTHESIS = "hypothesis"
    INSUFFICIENT_EVIDENCE = "insufficient_evidence"


class Confidence(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class Recurrence(str, Enum):
    RECURRING = "recurring"
    ONE_OFF = "one_off"
    TIMING = "timing"
    UNKNOWN = "unknown"


class Reconciliation(str, Enum):
    RECONCILED = "reconciled"
    UNRECONCILED = "unreconciled"
    INCOMPLETE = "incomplete"


EnumT = TypeVar("EnumT", bound=Enum)


def _as_decimal(value: object, field_name: str) -> Decimal:
    if isinstance(value, bool):
        raise ValueError(f"{field_name} precisa ser numérico.")
    try:
        decimal_value = Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError) as error:
        raise ValueError(f"{field_name} precisa ser um número válido.") from error
    if not decimal_value.is_finite():
        raise ValueError(f"{field_name} precisa ser um número finito.")
    return decimal_value


def _as_enum(value: EnumT | str, enum_type: type[EnumT], field_name: str) -> EnumT:
    if isinstance(value, enum_type):
        return value
    try:
        return enum_type(value)
    except ValueError as error:
        allowed = ", ".join(member.value for member in enum_type)
        raise ValueError(f"{field_name} precisa ser um de: {allowed}.") from error


def _as_texts(values: Iterable[str] | str, field_name: str) -> tuple[str, ...]:
    if isinstance(values, str):
        values = (values,)
    normalized: list[str] = []
    for value in values:
        if not isinstance(value, str):
            raise ValueError(f"{field_name} precisa conter textos.")
        stripped = value.strip()
        if stripped:
            normalized.append(stripped)
    return tuple(normalized)


def _format_decimal(value: Decimal | None) -> str | None:
    if value is None:
        return None
    return format(value.quantize(Decimal("0.01")), "f")


@dataclass(frozen=True)
class Baseline:
    """Comparação que define o tamanho e a direção da Variance."""

    actual: Decimal | int | str
    reference: Decimal | int | str
    reference_name: str
    unit: str = "unidades"

    def __post_init__(self) -> None:
        object.__setattr__(self, "actual", _as_decimal(self.actual, "actual"))
        object.__setattr__(self, "reference", _as_decimal(self.reference, "reference"))
        if not isinstance(self.reference_name, str) or not self.reference_name.strip():
            raise ValueError("reference_name é obrigatório.")
        object.__setattr__(self, "reference_name", self.reference_name.strip())
        if not isinstance(self.unit, str) or not self.unit.strip():
            raise ValueError("unit é obrigatória.")
        object.__setattr__(self, "unit", self.unit.strip())

    @property
    def variance(self) -> Decimal:
        return self.actual - self.reference

    @property
    def variance_percent(self) -> Decimal | None:
        if self.reference == 0:
            return None
        return (self.variance / self.reference * Decimal("100")).quantize(Decimal("0.01"))


@dataclass(frozen=True)
class Materiality:
    """Critérios quantitativos e decisórios para priorizar a investigação."""

    absolute_threshold: Decimal | int | str | None = None
    percentage_threshold: Decimal | int | str | None = None
    decision_relevance: str = ""
    decision_relevant: bool | None = None

    def __post_init__(self) -> None:
        if self.absolute_threshold is not None:
            threshold = _as_decimal(self.absolute_threshold, "absolute_threshold")
            if threshold < 0:
                raise ValueError("absolute_threshold não pode ser negativo.")
            object.__setattr__(self, "absolute_threshold", threshold)
        if self.percentage_threshold is not None:
            threshold = _as_decimal(self.percentage_threshold, "percentage_threshold")
            if threshold < 0:
                raise ValueError("percentage_threshold não pode ser negativo.")
            object.__setattr__(self, "percentage_threshold", threshold)
        if not isinstance(self.decision_relevance, str):
            raise ValueError("decision_relevance precisa ser texto.")
        object.__setattr__(self, "decision_relevance", self.decision_relevance.strip())
        if self.decision_relevant is not None and not isinstance(self.decision_relevant, bool):
            raise ValueError("decision_relevant precisa ser verdadeiro, falso ou ausente.")
        if self.decision_relevant is True and not self.decision_relevance:
            raise ValueError("Relevância decisória positiva precisa de justificativa.")
        if (
            self.absolute_threshold is None
            and self.percentage_threshold is None
            and self.decision_relevant is None
        ):
            raise ValueError("Materialidade precisa de um critério quantitativo ou decisório.")
        if self.decision_relevance and self.decision_relevant is None:
            raise ValueError(
                "decision_relevance precisa declarar decision_relevant como verdadeiro ou falso."
            )

    def evaluate(self, baseline: Baseline) -> bool:
        if self.absolute_threshold is not None and abs(baseline.variance) >= self.absolute_threshold:
            return True
        if (
            self.percentage_threshold is not None
            and baseline.variance_percent is not None
            and abs(baseline.variance_percent) >= self.percentage_threshold
        ):
            return True
        return self.decision_relevant is True


@dataclass(frozen=True)
class Driver:
    """Driver que explica parte conhecida ou hipotética da Variance."""

    name: str
    impact: Decimal | int | str | None
    evidence: Iterable[str] | str
    status: DriverStatus | str
    kind: DriverKind | str = DriverKind.UNKNOWN
    evidence_gap: Iterable[str] | str = ()

    def __post_init__(self) -> None:
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("Driver precisa ter um nome.")
        object.__setattr__(self, "name", self.name.strip())
        if self.impact is not None:
            object.__setattr__(self, "impact", _as_decimal(self.impact, f"impacto de {self.name}"))
        object.__setattr__(self, "evidence", _as_texts(self.evidence, f"evidência de {self.name}"))
        status = _as_enum(self.status, DriverStatus, f"status de {self.name}")
        kind = _as_enum(self.kind, DriverKind, f"tipo de {self.name}")
        object.__setattr__(self, "status", status)
        object.__setattr__(self, "kind", kind)
        evidence_gap = _as_texts(self.evidence_gap, f"lacuna de evidência de {self.name}")
        object.__setattr__(self, "evidence_gap", evidence_gap)
        if status is DriverStatus.CONFIRMED and (self.impact is None or not self.evidence):
            raise ValueError(f"Driver confirmado precisa de impacto e evidência: {self.name}.")
        if status is DriverStatus.CONFIRMED and evidence_gap:
            raise ValueError(f"Driver confirmado não pode manter lacuna de evidência: {self.name}.")
        if status is DriverStatus.HYPOTHESIS and not self.evidence:
            raise ValueError(f"Hipótese precisa declarar a evidência que lhe dá base: {self.name}.")
        if status is DriverStatus.MISSING_EVIDENCE and not evidence_gap:
            raise ValueError(f"Driver sem evidência precisa nomear a lacuna: {self.name}.")


@dataclass(frozen=True)
class Action:
    """Próxima ação, owner e timing da explicação."""

    description: str
    owner: str | None = None
    timing: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.description, str) or not self.description.strip():
            raise ValueError("Ação precisa ter uma descrição.")
        object.__setattr__(self, "description", self.description.strip())
        if self.owner is not None:
            if not isinstance(self.owner, str):
                raise ValueError("Owner precisa ser texto.")
            object.__setattr__(self, "owner", self.owner.strip() or None)
        if self.timing is not None:
            if not isinstance(self.timing, str):
                raise ValueError("Timing precisa ser texto.")
            object.__setattr__(self, "timing", self.timing.strip() or None)


@dataclass(frozen=True)
class VarianceExplanation:
    """Decisão canônica consumida por todos os adapters de Variance."""

    baseline: Baseline
    materiality: Materiality
    breakdown: Iterable[str]
    drivers: Iterable[Driver]
    evidence: Iterable[str] | str
    impact: Iterable[str] | str
    action: Action
    recurrence: Recurrence | str
    confidence: Confidence | str
    status: ExplanationStatus | str
    primary_driver_name: str | None = None
    recurrence_detail: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.baseline, Baseline):
            raise ValueError("baseline precisa ser um Baseline.")
        if not isinstance(self.materiality, Materiality):
            raise ValueError("materiality precisa ser uma Materiality.")
        if not isinstance(self.action, Action):
            raise ValueError("action precisa ser uma Action.")

        breakdown = _as_texts(self.breakdown, "breakdown")
        drivers = tuple(self.drivers)
        evidence = _as_texts(self.evidence, "evidence")
        impact = _as_texts(self.impact, "impact")
        if not breakdown:
            raise ValueError("Variance precisa de pelo menos uma quebra.")
        if not drivers:
            raise ValueError("Variance precisa de pelo menos um driver.")
        if not impact:
            raise ValueError("Variance precisa declarar seu impacto.")
        if not all(isinstance(driver, Driver) for driver in drivers):
            raise ValueError("drivers precisa conter apenas Driver.")

        recurrence = _as_enum(self.recurrence, Recurrence, "recurrence")
        confidence = _as_enum(self.confidence, Confidence, "confidence")
        status = _as_enum(self.status, ExplanationStatus, "status")
        primary_driver_name = self.primary_driver_name
        if primary_driver_name is not None:
            if not isinstance(primary_driver_name, str):
                raise ValueError("primary_driver_name precisa ser texto.")
            primary_driver_name = primary_driver_name.strip() or None
        if primary_driver_name is None:
            if len(drivers) != 1:
                raise ValueError(
                    "Explicações com múltiplos drivers precisam declarar primary_driver_name."
                )
            primary_driver_name = drivers[0].name
        if primary_driver_name not in {driver.name for driver in drivers}:
            raise ValueError("primary_driver_name precisa identificar um driver da explicação.")
        recurrence_detail = self.recurrence_detail
        if recurrence_detail is not None:
            if not isinstance(recurrence_detail, str):
                raise ValueError("recurrence_detail precisa ser texto.")
            recurrence_detail = recurrence_detail.strip() or None
        if recurrence in (Recurrence.TIMING, Recurrence.ONE_OFF) and not recurrence_detail:
            raise ValueError(
                "Timing e one-off precisam explicar a reversão, o encerramento ou a não recorrência."
            )

        object.__setattr__(self, "breakdown", breakdown)
        object.__setattr__(self, "drivers", drivers)
        object.__setattr__(self, "evidence", evidence)
        object.__setattr__(self, "impact", impact)
        object.__setattr__(self, "recurrence", recurrence)
        object.__setattr__(self, "confidence", confidence)
        object.__setattr__(self, "status", status)
        object.__setattr__(self, "primary_driver_name", primary_driver_name)
        object.__setattr__(self, "recurrence_detail", recurrence_detail)

        if status is ExplanationStatus.CONFIRMED:
            if not evidence:
                raise ValueError("Explicação confirmada precisa de evidência.")
            if any(driver.status is not DriverStatus.CONFIRMED for driver in drivers):
                raise ValueError("Explicação confirmada não pode esconder driver não confirmado.")
            if self.reconciliation is not Reconciliation.RECONCILED:
                raise ValueError("Explicação confirmada precisa reconciliar os drivers.")
            if confidence is Confidence.LOW:
                raise ValueError("Explicação confirmada não pode declarar confiança baixa.")

    @property
    def is_material(self) -> bool:
        return self.materiality.evaluate(self.baseline)

    @property
    def reconciliation(self) -> Reconciliation:
        if any(driver.impact is None for driver in self.drivers):
            return Reconciliation.INCOMPLETE
        total = sum((driver.impact for driver in self.drivers), Decimal("0"))
        if total == self.baseline.variance:
            return Reconciliation.RECONCILED
        return Reconciliation.UNRECONCILED

    @property
    def requires_validation(self) -> bool:
        return (
            self.status is not ExplanationStatus.CONFIRMED
            or self.reconciliation is not Reconciliation.RECONCILED
            or any(driver.status is not DriverStatus.CONFIRMED for driver in self.drivers)
        )

    def to_record(self) -> dict[str, object]:
        """Retorna a interface estável que os adapters podem transformar."""

        return {
            "baseline": {
                "actual": _format_decimal(self.baseline.actual),
                "reference": _format_decimal(self.baseline.reference),
                "reference_name": self.baseline.reference_name,
                "unit": self.baseline.unit,
                "variance": _format_decimal(self.baseline.variance),
                "variance_percent": _format_decimal(self.baseline.variance_percent),
            },
            "materiality": {
                "absolute_threshold": _format_decimal(self.materiality.absolute_threshold),
                "percentage_threshold": _format_decimal(self.materiality.percentage_threshold),
                "decision_relevance": self.materiality.decision_relevance,
                "decision_relevant": self.materiality.decision_relevant,
                "is_material": self.is_material,
            },
            "breakdown": list(self.breakdown),
            "drivers": [
                {
                    "name": driver.name,
                    "impact": _format_decimal(driver.impact),
                    "evidence": list(driver.evidence),
                    "evidence_gap": list(driver.evidence_gap),
                    "status": driver.status.value,
                    "kind": driver.kind.value,
                }
                for driver in self.drivers
            ],
            "primary_driver_name": self.primary_driver_name,
            "evidence": list(self.evidence),
            "impact": list(self.impact),
            "action": {
                "description": self.action.description,
                "owner": self.action.owner,
                "timing": self.action.timing,
            },
            "recurrence": self.recurrence.value,
            "recurrence_detail": self.recurrence_detail,
            "confidence": self.confidence.value,
            "status": self.status.value,
            "reconciliation": self.reconciliation.value,
            "requires_validation": self.requires_validation,
        }


__all__ = [
    "Action",
    "Baseline",
    "Confidence",
    "Driver",
    "DriverKind",
    "DriverStatus",
    "ExplanationStatus",
    "Materiality",
    "Recurrence",
    "Reconciliation",
    "VarianceExplanation",
]
