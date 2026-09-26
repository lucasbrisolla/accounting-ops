#!/usr/bin/env python3
"""Política executável de estrutura, referências e promoção do accounting-ops.

O módulo concentra a política que o doctor precisa avaliar. O caller recebe um
relatório tipado e pode decidir como renderizá-lo sem reimplementar caminhos,
referências ou regras de surface drift.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
import re


CONTRACT_VERSION = "1.0"


class FindingCategory(str, Enum):
    STRUCTURE = "structure"
    REFERENCE = "reference"
    SURFACE_DRIFT = "surface_drift"
    PROMOTION = "promotion"


class FindingSeverity(str, Enum):
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


class ProductLayer(str, Enum):
    USER = "user"
    SYSTEM = "system"
    INGESTION = "ingestion"


class PromotionDestination(str, Enum):
    CONCEPT = "concept"
    HEURISTIC = "heuristic"
    CHECKLIST = "checklist"
    WORKFLOW = "workflow"
    PLAYBOOK = "playbook"
    SKILL = "skill"
    TEMPLATE = "template"
    NONE = "none"


@dataclass(frozen=True)
class LayerPolicy:
    """Mapa de responsabilidade dos caminhos de uma camada do produto."""

    name: ProductLayer
    prefixes: tuple[str, ...]
    description: str


@dataclass(frozen=True)
class SurfaceDriftRule:
    """Termo que não pode escapar de seus caminhos situados permitidos."""

    term: str
    allowed_prefixes: tuple[str, ...] = ()
    severity: FindingSeverity = FindingSeverity.ERROR


@dataclass(frozen=True)
class PromotionCriterion:
    """Campo ou decisão que uma futura promoção deverá registrar."""

    key: str
    description: str
    required: bool = True


@dataclass(frozen=True)
class PromotionPolicy:
    """Critérios comuns para fontes de livros e contexto empresarial."""

    destinations: tuple[PromotionDestination, ...]
    criteria: tuple[PromotionCriterion, ...]
    situated_source_prefixes: tuple[str, ...]
    system_destination: ProductLayer = ProductLayer.SYSTEM
    generalization_required: bool = True
    next_test_required: bool = True
    source_kind_prefixes: tuple[tuple[str, str], ...] = (
        ("book", "books/"),
        ("company_context", "context/companies/"),
    )
    record_prefixes: tuple[str, ...] = ("books/", "context/companies/")
    record_directory: str = "promotions"
    record_suffix: str = ".md"

    @property
    def required_fields(self) -> tuple[str, ...]:
        return tuple(criterion.key for criterion in self.criteria if criterion.required)


@dataclass(frozen=True)
class ContractFinding:
    """Resultado observável de uma regra do Product Contract."""

    category: FindingCategory
    target: str
    message: str
    severity: FindingSeverity

    def __post_init__(self) -> None:
        object.__setattr__(self, "category", _as_enum(self.category, FindingCategory, "category"))
        object.__setattr__(self, "severity", _as_enum(self.severity, FindingSeverity, "severity"))
        for field_name in ("target", "message"):
            value = getattr(self, field_name)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{field_name} precisa ser um texto não vazio.")
            object.__setattr__(self, field_name, value.strip())

    def to_record(self) -> dict[str, str]:
        return {
            "category": self.category.value,
            "target": self.target,
            "message": self.message,
            "severity": self.severity.value,
        }


@dataclass(frozen=True)
class ProductContractReport:
    """Relatório imutável produzido pela avaliação da política."""

    root: Path
    contract_version: str
    checked: tuple[str, ...]
    findings: tuple[ContractFinding, ...]
    promotion_records: tuple[str, ...] = ()

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def missing(self) -> list[str]:
        return self._targets_for(FindingCategory.STRUCTURE)

    @property
    def broken_references(self) -> list[str]:
        return self._targets_for(FindingCategory.REFERENCE)

    @property
    def surface_drift(self) -> list[str]:
        return self._targets_for(FindingCategory.SURFACE_DRIFT)

    def findings_for(self, category: FindingCategory) -> tuple[ContractFinding, ...]:
        category = _as_enum(category, FindingCategory, "category")
        return tuple(finding for finding in self.findings if finding.category == category)

    def to_record(self) -> dict[str, object]:
        return {
            "root": str(self.root),
            "contract_version": self.contract_version,
            "checked": list(self.checked),
            "promotion_records": list(self.promotion_records),
            "status": "ok" if self.ok else "fail",
            "findings": [finding.to_record() for finding in self.findings],
        }

    def _targets_for(self, category: FindingCategory) -> list[str]:
        return [finding.target for finding in self.findings_for(category)]


@dataclass(frozen=True)
class ProductContract:
    """Política versionada que governa a saúde estrutural do produto."""

    version: str
    layers: tuple[LayerPolicy, ...]
    required_paths: tuple[str, ...]
    canonical_reference_documents: tuple[str, ...]
    reference_prefixes: tuple[str, ...]
    drift_rules: tuple[SurfaceDriftRule, ...]
    ignored_prefixes: tuple[str, ...]
    promotion: PromotionPolicy

    def check(self, root: Path | str) -> ProductContractReport:
        return check_product_contract(root, contract=self)


def _as_enum(value: object, enum_type: type[Enum], field_name: str) -> Enum:
    if isinstance(value, enum_type):
        return value
    try:
        return enum_type(value)
    except ValueError as error:
        allowed = ", ".join(member.value for member in enum_type)
        raise ValueError(f"{field_name} precisa ser um de: {allowed}.") from error


def _relative_path(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)


def _starts_with_prefix(relative_path: str, prefix: str) -> bool:
    normalized = prefix.rstrip("/")
    return relative_path == normalized or relative_path.startswith(f"{normalized}/")


def _is_ignored(relative_path: str, prefixes: tuple[str, ...]) -> bool:
    return any(_starts_with_prefix(relative_path, prefix) for prefix in prefixes)


BACKTICK_PATH_PATTERN = re.compile(
    r"`(?P<path>(?:_method-wiki|tracks|templates|skills|books|context|archive|stateless)/[^`\n]+?\.md)`"
)
MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]+\]\((?P<path>[^)]+)\)")
DEFAULT_REFERENCE_PREFIXES = (
    "_method-wiki/",
    "tracks/",
    "templates/",
    "skills/",
    "books/",
    "context/",
    "archive/",
    "stateless/",
)
VAULT_ACCOUNTING_OPS_ANCHOR = (
    "accounting-ops/"
)


def normalize_markdown_target(
    reference: str,
    accepted_prefixes: tuple[str, ...] = DEFAULT_REFERENCE_PREFIXES,
) -> str | None:
    target = reference.strip()
    if not target:
        return None
    target = target.split("#", 1)[0].split("?", 1)[0].strip()
    if not target or target.startswith(("http://", "https://", "mailto:")):
        return None
    if target.startswith("</") and target.endswith(">"):
        target = target[2:-1]
    elif target.startswith("<") and target.endswith(">"):
        target = target[1:-1]

    if target.startswith(VAULT_ACCOUNTING_OPS_ANCHOR):
        target = target.removeprefix(VAULT_ACCOUNTING_OPS_ANCHOR)

    if target.startswith(accepted_prefixes):
        return target
    return None


def extract_doc_references(
    content: str,
    accepted_prefixes: tuple[str, ...] = DEFAULT_REFERENCE_PREFIXES,
) -> list[str]:
    references: list[str] = []
    for match in BACKTICK_PATH_PATTERN.finditer(content):
        references.append(match.group("path"))
    for match in MARKDOWN_LINK_PATTERN.finditer(content):
        normalized = normalize_markdown_target(match.group("path"), accepted_prefixes)
        if normalized is not None:
            references.append(normalized)
    return sorted(set(references))


def _structure_findings(root: Path, contract: ProductContract) -> list[ContractFinding]:
    findings: list[ContractFinding] = []
    for relative_path in contract.required_paths:
        if (root / relative_path).exists():
            continue
        findings.append(
            ContractFinding(
                category=FindingCategory.STRUCTURE,
                target=relative_path,
                message=f"Caminho obrigatório ausente: {relative_path}",
                severity=FindingSeverity.ERROR,
            )
        )
    return findings


def _reference_findings(root: Path, contract: ProductContract) -> list[ContractFinding]:
    findings: list[ContractFinding] = []
    for document in contract.canonical_reference_documents:
        document_path = root / document
        if not document_path.exists():
            continue
        content = document_path.read_text(encoding="utf-8")
        for reference in extract_doc_references(content, contract.reference_prefixes):
            if (root / reference).exists():
                continue
            target = f"{document} -> {reference}"
            findings.append(
                ContractFinding(
                    category=FindingCategory.REFERENCE,
                    target=target,
                    message=f"Referência interna quebrada: {target}",
                    severity=FindingSeverity.ERROR,
                )
            )
    return findings


def _surface_drift_findings(root: Path, contract: ProductContract) -> list[ContractFinding]:
    findings: list[ContractFinding] = []
    for path in root.rglob("*.md"):
        relative_path = _relative_path(root, path)
        if _is_ignored(relative_path, contract.ignored_prefixes):
            continue
        content = path.read_text(encoding="utf-8")
        for rule in contract.drift_rules:
            if rule.term not in content:
                continue
            if any(
                _starts_with_prefix(relative_path, prefix)
                for prefix in rule.allowed_prefixes
            ):
                continue
            findings.append(
                ContractFinding(
                    category=FindingCategory.SURFACE_DRIFT,
                    target=f"{relative_path} -> {rule.term}",
                    message=(
                        f"Termo situado fora de uma superfície permitida: {relative_path} -> {rule.term}"
                    ),
                    severity=rule.severity,
                )
            )
    return findings


def _promotion_findings(root: Path, contract: ProductContract) -> list[ContractFinding]:
    from scripts.promotion_pipeline import (
        PromotionRecordError,
        iter_promotion_record_paths,
        load_promotion_record,
    )

    findings: list[ContractFinding] = []
    for path in iter_promotion_record_paths(root, contract.promotion):
        relative_path = _relative_path(root, path)
        try:
            decision = load_promotion_record(path, policy=contract.promotion)
            errors = decision.validate_against_policy(
                contract.promotion,
                record_path=relative_path,
                expected_version=contract.version,
            )
            if not (root / decision.origin).is_file():
                errors = errors + (
                    f"origin não existe na raiz do produto: {decision.origin}.",
                )
            if errors:
                raise PromotionRecordError(" ".join(errors))
        except PromotionRecordError as error:
            findings.append(
                ContractFinding(
                    category=FindingCategory.PROMOTION,
                    target=relative_path,
                    message=f"Registro de promoção incoerente: {error}",
                    severity=FindingSeverity.ERROR,
                )
            )
    return findings


def check_product_contract(
    root: Path | str | None = None,
    *,
    contract: ProductContract | None = None,
) -> ProductContractReport:
    active_contract = contract or ACCOUNTING_OPS_PRODUCT_CONTRACT
    product_root = (Path(root) if root is not None else Path(__file__).resolve().parents[1]).resolve()
    from scripts.promotion_pipeline import iter_promotion_record_paths

    promotion_records = tuple(
        _relative_path(product_root, path)
        for path in iter_promotion_record_paths(product_root, active_contract.promotion)
    )
    findings = (
        _structure_findings(product_root, active_contract)
        + _reference_findings(product_root, active_contract)
        + _surface_drift_findings(product_root, active_contract)
        + _promotion_findings(product_root, active_contract)
    )
    ordered_findings = tuple(
        sorted(
            findings,
            key=lambda finding: (
                finding.category.value,
                finding.target,
                finding.message,
            ),
        )
    )
    return ProductContractReport(
        root=product_root,
        contract_version=active_contract.version,
        checked=tuple(active_contract.required_paths),
        findings=ordered_findings,
        promotion_records=promotion_records,
    )


def check_broken_references(
    root: Path | str,
    *,
    contract: ProductContract | None = None,
) -> list[str]:
    active_contract = contract or ACCOUNTING_OPS_PRODUCT_CONTRACT
    product_root = Path(root).resolve()
    return [
        finding.target
        for finding in _reference_findings(product_root, active_contract)
    ]


def check_surface_drift(
    root: Path | str,
    *,
    contract: ProductContract | None = None,
) -> list[str]:
    active_contract = contract or ACCOUNTING_OPS_PRODUCT_CONTRACT
    product_root = Path(root).resolve()
    return [
        finding.target
        for finding in _surface_drift_findings(product_root, active_contract)
    ]


_REQUIRED_PATHS = (
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "DATA_CONTRACT.md",
    "PRODUCT_INDEX.md",
    "HEALTH_CHECK.md",
    "domain.md",
    "_method-wiki/README.md",
    "_method-wiki/index.md",
    "_method-wiki/guide.md",
    "_method-wiki/patterns/variance-analysis.md",
    "tracks/accounting/README.md",
    "tracks/accounting/modes/accounting-closing-and-quality.md",
    "tracks/accounting/modes/accounting-technical-application.md",
    "tracks/fpa/README.md",
    "tracks/fpa/modes/fpa-learning.md",
    "tracks/fpa/modes/variance-analysis.md",
    "templates/flash-report.md",
    "CONTEXT.md",
    "skills/financial-investigation/SKILL.md",
    "skills/explain-variance/SKILL.md",
    "skills/diagnose-industrial-costs/SKILL.md",
    "scripts/variance_explanation_contract.py",
    "scripts/challenge_variance_adapter.py",
    "scripts/variance_output_adapters.py",
    "scripts/accounting_ops_product_contract.py",
    "scripts/promotion_pipeline.py",
    "skills/cpc-impact-translation/SKILL.md",
    "skills/challenge-variance-explanation/SKILL.md",
    "skills/number-to-management-story/SKILL.md",
    "skills/prepare-journal-entry-support/SKILL.md",
    "skills/context-gap-audit/SKILL.md",
    "stateless/README.md",
    "stateless/operating-manuals/general-analysis-manual.md",
    "stateless/core-lenses/accounting-ops-core-lens.md",
    "stateless/analytical-lenses/presentation-critique.md",
    "stateless/analytical-lenses/variance-analysis.md",
    "stateless/analytical-lenses/forecast-review.md",
    "stateless/analytical-lenses/executive-storyline.md",
    "stateless/output-modes/executive-summary-mode.md",
    "stateless/prompt-templates/analyze-material-base.md",
    "stateless/adaptation/README.md",
)

_CANONICAL_REFERENCE_DOCUMENTS = (
    "CLAUDE.md",
    "PRODUCT_INDEX.md",
    "README.md",
    "stateless/README.md",
    "stateless/operating-manuals/general-analysis-manual.md",
    "stateless/core-lenses/accounting-ops-core-lens.md",
    "stateless/analytical-lenses/presentation-critique.md",
    "stateless/analytical-lenses/variance-analysis.md",
    "stateless/analytical-lenses/forecast-review.md",
    "stateless/analytical-lenses/executive-storyline.md",
    "stateless/output-modes/executive-summary-mode.md",
    "stateless/prompt-templates/analyze-material-base.md",
    "stateless/adaptation/README.md",
)

ACCOUNTING_OPS_PRODUCT_CONTRACT = ProductContract(
    version=CONTRACT_VERSION,
    layers=(
        LayerPolicy(
            name=ProductLayer.USER,
            prefixes=("context/",),
            description="Contexto pessoal, empresas específicas e casos situados.",
        ),
        LayerPolicy(
            name=ProductLayer.SYSTEM,
            prefixes=(
                "AGENTS.md",
                "CLAUDE.md",
                "README.md",
                "PRODUCT_INDEX.md",
                "DATA_CONTRACT.md",
                "HEALTH_CHECK.md",
                "domain.md",
                "_method-wiki/",
                "books/",
                "skills/",
                "tracks/",
                "templates/",
                "stateless/",
            ),
            description="Método, operação, roteamento e formatos reutilizáveis.",
        ),
        LayerPolicy(
            name=ProductLayer.INGESTION,
            prefixes=("books/", "context/companies/"),
            description="Fontes, evidências e decisões de promoção rastreáveis.",
        ),
    ),
    required_paths=_REQUIRED_PATHS,
    canonical_reference_documents=_CANONICAL_REFERENCE_DOCUMENTS,
    reference_prefixes=DEFAULT_REFERENCE_PREFIXES,
    drift_rules=(
        SurfaceDriftRule(term="entrevista"),
        SurfaceDriftRule(
            term="Acme",
            allowed_prefixes=("context/companies/", "stateless/company-packs/"),
        ),
        SurfaceDriftRule(
            term="Comparável",
            allowed_prefixes=("context/companies/", "stateless/company-packs/"),
        ),
    ),
    ignored_prefixes=("archive/",),
    promotion=PromotionPolicy(
        destinations=tuple(PromotionDestination),
        criteria=(
            PromotionCriterion("promotion_contract_version", "Versão do contrato do registro."),
            PromotionCriterion("origin", "Fonte e caminho de origem do candidato."),
            PromotionCriterion("source_kind", "Tipo de origem: livro ou contexto empresarial."),
            PromotionCriterion("candidate", "Ideia ou conteúdo candidato à promoção."),
            PromotionCriterion(
                "probable_destination",
                "Destino mais provável na taxonomia do produto.",
            ),
            PromotionCriterion("confidence", "Confiança da decisão editorial."),
            PromotionCriterion("evidence", "Evidência que sustenta a decisão."),
            PromotionCriterion("justification", "Justificativa do destino ou da não promoção."),
            PromotionCriterion("next_test", "Próximo teste de generalização ou de utilidade."),
            PromotionCriterion(
                "no_test_justification",
                "Justificativa explícita quando não houver próximo teste.",
            ),
            PromotionCriterion(
                "not_promoted_content",
                "Conteúdo mantido fora da camada promovida.",
            ),
            PromotionCriterion("editorial_status", "Status atual da decisão editorial."),
            PromotionCriterion(
                "generalization_statement",
                "Declaração de generalização para promoção de contexto empresarial.",
            ),
        ),
        situated_source_prefixes=("context/companies/",),
    ),
)

DEFAULT_PRODUCT_CONTRACT = ACCOUNTING_OPS_PRODUCT_CONTRACT
