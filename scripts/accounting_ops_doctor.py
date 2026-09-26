#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import sys


PRODUCT_ROOT = Path(__file__).resolve().parents[1]
if str(PRODUCT_ROOT) not in sys.path:
    sys.path.insert(0, str(PRODUCT_ROOT))

from scripts.accounting_ops_product_contract import (
    ACCOUNTING_OPS_PRODUCT_CONTRACT,
    DEFAULT_PRODUCT_CONTRACT,
    FindingCategory,
    ProductContractReport,
    check_broken_references,
    check_product_contract,
    check_surface_drift,
    extract_doc_references,
    normalize_markdown_target,
)


# Aliases de compatibilidade para callers que importavam a superfície antiga.
# A política continua definida exclusivamente no Product Contract.
REQUIRED_PATHS = list(DEFAULT_PRODUCT_CONTRACT.required_paths)
REFERENCE_DOCS = list(DEFAULT_PRODUCT_CONTRACT.canonical_reference_documents)
GLOBAL_SURFACE_DRIFT_TERMS = [
    rule.term
    for rule in DEFAULT_PRODUCT_CONTRACT.drift_rules
    if not rule.allowed_prefixes
]
LAYERED_SURFACE_DRIFT_TERMS = {
    rule.term: list(rule.allowed_prefixes)
    for rule in DEFAULT_PRODUCT_CONTRACT.drift_rules
    if rule.allowed_prefixes
}
DoctorResult = ProductContractReport


def default_root() -> Path:
    return Path(__file__).resolve().parents[1]


def check_accounting_ops(root: Path | None = None) -> DoctorResult:
    return check_product_contract(root, contract=ACCOUNTING_OPS_PRODUCT_CONTRACT)


def render_result(result: DoctorResult) -> str:
    lines = [
        "# accounting-ops doctor",
        "",
        f"Root: {result.root}",
        f"Checked: {len(result.checked)}",
        f"Missing: {len(result.missing)}",
        f"Broken references: {len(result.broken_references)}",
        f"Surface drift: {len(result.surface_drift)}",
        f"Promotion findings: {len(result.findings_for(FindingCategory.PROMOTION))}",
        f"Promotion records: {len(result.promotion_records)}",
        "",
    ]

    if result.ok:
        lines.append("Status: OK")
        return "\n".join(lines)

    lines.append("Status: FAIL")
    lines.append("")

    labels = {
        FindingCategory.STRUCTURE: "Missing required paths",
        FindingCategory.REFERENCE: "Broken references",
        FindingCategory.SURFACE_DRIFT: "Surface drift",
        FindingCategory.PROMOTION: "Promotion findings",
    }
    for category in FindingCategory:
        findings = result.findings_for(category)
        if not findings:
            continue
        lines.append(labels.get(category, f"Findings: {category.value}"))
        lines.extend(
            f"- {finding.target} [{finding.severity.value}]: {finding.message}"
            for finding in findings
        )
        lines.append("")

    if lines[-1] == "":
        lines.pop()

    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check required accounting-ops files and references.")
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="Path to the accounting-ops root. Defaults to the parent of this script directory.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    result = check_accounting_ops(args.root)
    print(render_result(result))
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
