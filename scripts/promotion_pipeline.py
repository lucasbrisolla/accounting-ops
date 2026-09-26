#!/usr/bin/env python3
"""Registro comum de decisões de promoção editorial.

O módulo transforma candidatos de livros e de contexto empresarial em um
registro único, validável e persistível. A política de destinos continua no
Product Contract; este módulo concentra a decisão e seus invariantes.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import json
from pathlib import Path
from typing import Iterable

from scripts.accounting_ops_product_contract import (
    ACCOUNTING_OPS_PRODUCT_CONTRACT,
    ProductContract,
    PromotionDestination,
    PromotionPolicy,
)


PROMOTION_CONTRACT_VERSION = ACCOUNTING_OPS_PRODUCT_CONTRACT.version


class PromotionSourceKind(str, Enum):
    BOOK = "book"
    COMPANY_CONTEXT = "company_context"


class PromotionConfidence(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class EditorialStatus(str, Enum):
    CANDIDATE = "candidate"
    IN_REVIEW = "in_review"
    PROMOTED = "promoted"
    NOT_PROMOTED = "not_promoted"
    DISCARDED = "discarded"


_COMPLETE_STATUSES = frozenset(
    {
        EditorialStatus.PROMOTED,
        EditorialStatus.NOT_PROMOTED,
        EditorialStatus.DISCARDED,
    }
)


class PromotionRecordError(ValueError):
    """Erro de formato ou coerência em um registro persistido."""


@dataclass(frozen=True)
class PromotionDecision:
    """Decisão editorial comum para livros e contexto empresarial."""

    source_kind: PromotionSourceKind
    origin: str
    candidate: str
    probable_destination: PromotionDestination
    justification: str
    confidence: PromotionConfidence
    evidence: tuple[str, ...]
    not_promoted_content: tuple[str, ...]
    editorial_status: EditorialStatus
    next_test: str | None = None
    no_test_justification: str | None = None
    generalization_statement: str | None = None
    contract_version: str = PROMOTION_CONTRACT_VERSION

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "source_kind",
            _as_enum(self.source_kind, PromotionSourceKind, "source_kind"),
        )
        object.__setattr__(
            self,
            "probable_destination",
            _as_enum(
                self.probable_destination,
                PromotionDestination,
                "probable_destination",
            ),
        )
        object.__setattr__(
            self,
            "confidence",
            _as_enum(self.confidence, PromotionConfidence, "confidence"),
        )
        object.__setattr__(
            self,
            "editorial_status",
            _as_enum(self.editorial_status, EditorialStatus, "editorial_status"),
        )
        for field_name in ("origin", "candidate", "justification", "contract_version"):
            object.__setattr__(self, field_name, _required_text(getattr(self, field_name), field_name))
        object.__setattr__(self, "evidence", _required_texts(self.evidence, "evidence"))
        object.__setattr__(
            self,
            "not_promoted_content",
            _required_texts(self.not_promoted_content, "not_promoted_content"),
        )
        object.__setattr__(self, "next_test", _optional_text(self.next_test, "next_test"))
        object.__setattr__(
            self,
            "no_test_justification",
            _optional_text(self.no_test_justification, "no_test_justification"),
        )
        object.__setattr__(
            self,
            "generalization_statement",
            _optional_text(self.generalization_statement, "generalization_statement"),
        )

        if self.editorial_status in _COMPLETE_STATUSES and not (
            self.next_test or self.no_test_justification
        ):
            raise PromotionRecordError(
                "Uma decisão editorial concluída precisa de next_test ou "
                "no_test_justification."
            )
        if (
            self.editorial_status == EditorialStatus.PROMOTED
            and self.probable_destination == PromotionDestination.NONE
        ):
            raise PromotionRecordError(
                "Uma decisão promovida precisa de um destino provável diferente de none."
            )
        if (
            self.source_kind == PromotionSourceKind.COMPANY_CONTEXT
            and self.editorial_status == EditorialStatus.PROMOTED
            and not self.generalization_statement
        ):
            raise PromotionRecordError(
                "Uma promoção de contexto empresarial precisa declarar a generalização."
            )
        if (
            self.editorial_status in {EditorialStatus.NOT_PROMOTED, EditorialStatus.DISCARDED}
            and self.probable_destination != PromotionDestination.NONE
        ):
            raise PromotionRecordError(
                "Uma decisão não promovida ou descartada precisa usar o destino none."
            )

    @property
    def is_complete(self) -> bool:
        return self.editorial_status in _COMPLETE_STATUSES

    def to_record(self) -> dict[str, object]:
        return {
            "promotion_contract_version": self.contract_version,
            "source_kind": self.source_kind.value,
            "origin": self.origin,
            "candidate": self.candidate,
            "probable_destination": self.probable_destination.value,
            "justification": self.justification,
            "confidence": self.confidence.value,
            "evidence": list(self.evidence),
            "next_test": self.next_test,
            "no_test_justification": self.no_test_justification,
            "not_promoted_content": list(self.not_promoted_content),
            "editorial_status": self.editorial_status.value,
            "generalization_statement": self.generalization_statement,
        }

    @classmethod
    def from_record(
        cls,
        record: dict[str, object],
        *,
        required_fields: Iterable[str] | None = None,
    ) -> "PromotionDecision":
        if not isinstance(record, dict):
            raise PromotionRecordError("O registro de promoção precisa ser um objeto.")
        default_fields = (
            "promotion_contract_version",
            "source_kind",
            "origin",
            "candidate",
            "probable_destination",
            "justification",
            "confidence",
            "evidence",
            "next_test",
            "no_test_justification",
            "not_promoted_content",
            "editorial_status",
            "generalization_statement",
        )
        fields = tuple(required_fields or default_fields)
        missing = [field for field in fields if field not in record]
        if missing:
            raise PromotionRecordError(
                "Campos ausentes no registro de promoção: " + ", ".join(missing)
            )
        return cls(
            source_kind=record["source_kind"],
            origin=record["origin"],
            candidate=record["candidate"],
            probable_destination=record["probable_destination"],
            justification=record["justification"],
            confidence=record["confidence"],
            evidence=record["evidence"],
            next_test=record["next_test"],
            not_promoted_content=record["not_promoted_content"],
            editorial_status=record["editorial_status"],
            no_test_justification=record["no_test_justification"],
            generalization_statement=record["generalization_statement"],
            contract_version=record["promotion_contract_version"],
        )

    def validate_against_policy(
        self,
        policy: PromotionPolicy,
        *,
        record_path: str | None = None,
        expected_version: str | None = None,
    ) -> tuple[str, ...]:
        errors: list[str] = []
        if expected_version is not None and self.contract_version != expected_version:
            errors.append(
                f"promotion_contract_version precisa ser {expected_version}."
            )
        if self.probable_destination not in policy.destinations:
            errors.append(
                "probable_destination não pertence à taxonomia do Product Contract."
            )

        source_prefixes = dict(policy.source_kind_prefixes)
        expected_source_prefix = source_prefixes.get(self.source_kind.value)
        if expected_source_prefix is None:
            errors.append("source_kind não está habilitado pela política de promoção.")
        elif not self.origin.startswith(expected_source_prefix):
            errors.append(
                f"origin precisa começar por {expected_source_prefix} para {self.source_kind.value}."
            )

        if record_path is not None:
            if not record_path.endswith(policy.record_suffix):
                errors.append(
                    f"O registro precisa usar o sufixo {policy.record_suffix}."
                )
            if policy.record_directory not in Path(record_path).parts:
                errors.append(
                    f"O registro precisa estar em uma pasta {policy.record_directory}."
                )
            if not any(
                _path_starts_with(record_path, prefix)
                for prefix in policy.record_prefixes
            ):
                errors.append("O registro está fora das camadas de promoção permitidas.")
            if expected_source_prefix and not _path_starts_with(
                record_path, expected_source_prefix
            ):
                errors.append(
                    f"O registro precisa permanecer na camada {expected_source_prefix}."
                )

        return tuple(errors)

    def to_markdown(self, title: str | None = None) -> str:
        record = self.to_record()
        heading = title or "Decisão de promoção"
        lines = ["---"]
        lines.extend(
            f"{key}: {json.dumps(value, ensure_ascii=False)}"
            for key, value in record.items()
        )
        lines.extend(
            [
                "---",
                "",
                f"# {heading}",
                "",
                "## Decisão",
                "",
                f"- Origem: `{self.origin}`",
                f"- Tipo de origem: `{self.source_kind.value}`",
                f"- Candidato: {self.candidate}",
                f"- Destino provável: `{self.probable_destination.value}`",
                f"- Confiança: `{self.confidence.value}`",
                f"- Status editorial: `{self.editorial_status.value}`",
                "",
                "## Justificativa",
                "",
                self.justification,
                "",
                "## Evidência",
                "",
            ]
        )
        lines.extend(f"- {item}" for item in self.evidence)
        lines.extend(["", "## Próximo teste", ""])
        if self.next_test:
            lines.append(self.next_test)
        else:
            lines.append(self.no_test_justification or "Nenhum teste registrado.")
        lines.extend(["", "## Conteúdo não promovido", ""])
        lines.extend(f"- {item}" for item in self.not_promoted_content)
        if self.generalization_statement:
            lines.extend(["", "## Generalização", "", self.generalization_statement])
        return "\n".join(lines) + "\n"


def _as_enum(value: object, enum_type: type[Enum], field_name: str) -> Enum:
    if isinstance(value, enum_type):
        return value
    try:
        return enum_type(value)
    except ValueError as error:
        allowed = ", ".join(member.value for member in enum_type)
        raise PromotionRecordError(f"{field_name} precisa ser um de: {allowed}.") from error


def _required_text(value: object, field_name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise PromotionRecordError(f"{field_name} é obrigatório.")
    return value.strip()


def _optional_text(value: object, field_name: str) -> str | None:
    if value is None:
        return None
    return _required_text(value, field_name)


def _required_texts(values: Iterable[str], field_name: str) -> tuple[str, ...]:
    if isinstance(values, str):
        raise PromotionRecordError(f"{field_name} precisa ser uma lista de textos.")
    normalized = tuple(_required_text(value, field_name) for value in values)
    if not normalized:
        raise PromotionRecordError(f"{field_name} precisa conter ao menos um item.")
    return normalized


def _path_starts_with(relative_path: str, prefix: str) -> bool:
    normalized = prefix.rstrip("/")
    return relative_path == normalized or relative_path.startswith(f"{normalized}/")


def _read_frontmatter(path: Path) -> dict[str, object]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise PromotionRecordError("O registro precisa começar com frontmatter.")
    try:
        end = lines.index("---", 1)
    except ValueError as error:
        raise PromotionRecordError("O frontmatter do registro não foi encerrado.") from error

    payload: dict[str, object] = {}
    for line_number, line in enumerate(lines[1:end], start=2):
        if not line.strip():
            continue
        key, separator, raw_value = line.partition(":")
        if not separator or not key.strip():
            raise PromotionRecordError(
                f"Linha {line_number} do frontmatter precisa conter chave e valor."
            )
        try:
            payload[key.strip()] = json.loads(raw_value.strip())
        except json.JSONDecodeError as error:
            raise PromotionRecordError(
                f"Valor inválido para {key.strip()} na linha {line_number}."
            ) from error
    return payload


def load_promotion_record(
    path: Path | str,
    *,
    policy: PromotionPolicy | None = None,
) -> PromotionDecision:
    record_path = Path(path)
    try:
        payload = _read_frontmatter(record_path)
        active_policy = policy or ACCOUNTING_OPS_PRODUCT_CONTRACT.promotion
        return PromotionDecision.from_record(
            payload,
            required_fields=active_policy.required_fields,
        )
    except PromotionRecordError:
        raise
    except OSError as error:
        raise PromotionRecordError(f"Não foi possível ler o registro {record_path}.") from error


def register_promotion(
    decision: PromotionDecision,
    root: Path | str,
    relative_path: str,
    *,
    contract: ProductContract | None = None,
) -> Path:
    active_contract = contract or ACCOUNTING_OPS_PRODUCT_CONTRACT
    product_root = Path(root).resolve()
    target = (product_root / relative_path).resolve()
    try:
        normalized_path = target.relative_to(product_root).as_posix()
    except ValueError as error:
        raise PromotionRecordError("O caminho do registro precisa ficar dentro da raiz.") from error

    errors = decision.validate_against_policy(
        active_contract.promotion,
        record_path=normalized_path,
        expected_version=active_contract.version,
    )
    if not (product_root / decision.origin).is_file():
        errors = errors + (
            f"origin não existe na raiz do produto: {decision.origin}.",
        )
    if errors:
        raise PromotionRecordError(" ".join(errors))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(decision.to_markdown(), encoding="utf-8")
    return target


def iter_promotion_record_paths(
    root: Path | str,
    policy: PromotionPolicy,
) -> tuple[Path, ...]:
    product_root = Path(root).resolve()
    records: list[Path] = []
    for path in product_root.rglob(f"*{policy.record_suffix}"):
        if not path.is_file():
            continue
        relative_path = path.relative_to(product_root).as_posix()
        if policy.record_directory not in path.relative_to(product_root).parts:
            continue
        if not any(
            _path_starts_with(relative_path, prefix)
            for prefix in policy.record_prefixes
        ):
            continue
        records.append(path)
    return tuple(sorted(records))
