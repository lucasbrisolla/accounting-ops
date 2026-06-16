#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


REQUIRED_PATHS = [
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
    "tracks/accounting/README.md",
    "tracks/accounting/modes/accounting-closing-and-quality.md",
    "tracks/accounting/modes/accounting-technical-application.md",
    "tracks/fpa/README.md",
    "tracks/fpa/modes/fpa-learning.md",
    "tracks/fpa/modes/variance-analysis.md",
    "templates/flash-report.md",
    "templates/variance-analysis-one-pager.md",
    "skills/cpc-impact-translation.md",
    "skills/challenge-variance-explanation.md",
    "skills/number-to-management-story.md",
    "skills/prepare-journal-entry-support.md",
]

REFERENCE_DOCS = [
    "CLAUDE.md",
    "PRODUCT_INDEX.md",
    "README.md",
    "INDEX.md",
]

BANNED_SURFACE_TERMS = [
    "interview-technical-prep",
    "lucas-fpa-bridge",
    "interview-drill",
    "Belgo",
    "entrevista",
]

BACKTICK_PATH_PATTERN = re.compile(
    r"`(?P<path>(?:_method-wiki|tracks|templates|skills|books|context|examples|archive)/[^`\n]+?\.md)`"
)
MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]+\]\((?P<path>[^)]+)\)")


@dataclass(frozen=True)
class DoctorResult:
    root: Path
    checked: list[str]
    missing: list[str]
    broken_references: list[str]
    surface_drift: list[str]

    @property
    def ok(self) -> bool:
        return not (self.missing or self.broken_references or self.surface_drift)


def default_root() -> Path:
    return Path(__file__).resolve().parents[1]


def normalize_markdown_target(reference: str) -> str | None:
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

    vault_anchor = "/home/lucas/Dropbox/Obsidian Vault/Agent Products/github/accounting-ops-public/"
    if target.startswith(vault_anchor):
        target = target.removeprefix(vault_anchor)

    if target.startswith(("_method-wiki/", "tracks/", "templates/", "skills/", "books/", "context/", "examples/", "archive/")):
        return target
    return None


def extract_doc_references(content: str) -> list[str]:
    references: list[str] = []
    for match in BACKTICK_PATH_PATTERN.finditer(content):
        references.append(match.group("path"))
    for match in MARKDOWN_LINK_PATTERN.finditer(content):
        normalized = normalize_markdown_target(match.group("path"))
        if normalized is not None:
            references.append(normalized)
    return sorted(set(references))


def check_broken_references(root: Path) -> list[str]:
    broken: list[str] = []
    for doc in REFERENCE_DOCS:
        doc_path = root / doc
        if not doc_path.exists():
            continue
        content = doc_path.read_text(encoding="utf-8")
        for reference in extract_doc_references(content):
            if not (root / reference).exists():
                broken.append(f"{doc} -> {reference}")
    return sorted(set(broken))


def check_surface_drift(root: Path) -> list[str]:
    drift: list[str] = []
    for path in root.rglob("*.md"):
        if "archive" in path.parts:
            continue
        try:
            relative = path.relative_to(root).as_posix()
        except ValueError:
            relative = str(path)
        content = path.read_text(encoding="utf-8")
        for term in BANNED_SURFACE_TERMS:
            if term in content:
                drift.append(f"{relative} -> {term}")
    return sorted(set(drift))


def check_accounting_ops(root: Path | None = None) -> DoctorResult:
    product_root = (root or default_root()).resolve()
    missing = [
        relative_path
        for relative_path in REQUIRED_PATHS
        if not (product_root / relative_path).exists()
    ]
    return DoctorResult(
        root=product_root,
        checked=list(REQUIRED_PATHS),
        missing=missing,
        broken_references=check_broken_references(product_root),
        surface_drift=check_surface_drift(product_root),
    )


def render_result(result: DoctorResult) -> str:
    lines = [
        "# accounting-ops doctor",
        "",
        f"Root: {result.root}",
        f"Checked: {len(result.checked)}",
        f"Missing: {len(result.missing)}",
        f"Broken references: {len(result.broken_references)}",
        f"Surface drift: {len(result.surface_drift)}",
        "",
    ]

    if result.ok:
        lines.append("Status: OK")
        return "\n".join(lines)

    lines.append("Status: FAIL")
    lines.append("")

    if result.missing:
        lines.append("Missing required paths:")
        lines.extend(f"- {relative_path}" for relative_path in result.missing)
        lines.append("")

    if result.broken_references:
        lines.append("Broken references:")
        lines.extend(f"- {reference}" for reference in result.broken_references)
        lines.append("")

    if result.surface_drift:
        lines.append("Surface drift:")
        lines.extend(f"- {item}" for item in result.surface_drift)

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
