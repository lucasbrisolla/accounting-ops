#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
ORDERED_LIST_RE = re.compile(r"^\d+\.\s+")
TABLE_OF_CONTENTS_RE = re.compile(r"^\s*#{0,6}\s*\[?Table of Contents\]?", re.IGNORECASE)
SEC_SECTION_RE = re.compile(r"^(PART\s+[IVXLC]+|ITEM\s+\d+[A-Z.]*)\b", re.IGNORECASE)


def is_blank(line: str) -> bool:
    return not line.strip()


def is_table_line(line: str) -> bool:
    stripped = line.strip()
    return stripped.startswith("|") and stripped.endswith("|")


def is_list_line(line: str) -> bool:
    stripped = line.lstrip()
    return stripped.startswith(("- ", "* ", "+ ")) or bool(ORDERED_LIST_RE.match(stripped))


def is_heading(line: str) -> bool:
    return bool(HEADING_RE.match(line))


def is_structural(line: str) -> bool:
    stripped = line.strip()
    return (
        is_blank(line)
        or is_table_line(line)
        or is_list_line(line)
        or is_heading(line)
        or bool(SEC_SECTION_RE.match(stripped))
    )


def looks_like_heading_continuation(line: str) -> bool:
    stripped = line.strip()
    if not stripped or is_structural(line):
        return False
    return stripped[0].islower() or stripped[0].isdigit() or stripped.startswith(("(", "[", '"', "'"))


def normalize_inline_spacing(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text


def rejoin_broken_headings(lines: list[str]) -> list[str]:
    output: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        match = HEADING_RE.match(line)
        if not match:
            output.append(line)
            i += 1
            continue

        prefix, body = match.groups()
        current = body.strip()
        j = i + 1
        while j < len(lines) and looks_like_heading_continuation(lines[j]):
            current = normalize_inline_spacing(f"{current} {lines[j].strip()}")
            j += 1

        output.append(f"{prefix} {current}".rstrip())
        i = j

    return output


def should_join_paragraph_lines(current: str, nxt: str) -> bool:
    current_stripped = current.strip()
    next_stripped = nxt.strip()

    if not current_stripped or not next_stripped:
        return False
    if is_structural(current) or is_structural(nxt):
        return False
    if current_stripped.endswith((".", "!", "?", ":", ";")):
        return False
    if current_stripped.endswith(("-", "/", "(")):
        return True
    if next_stripped[0].islower():
        return True
    if next_stripped.startswith(("(", "[", '"', "'")):
        return True
    if len(current_stripped.split()) <= 6:
        return True
    return False


def rejoin_paragraphs(lines: list[str]) -> list[str]:
    output: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if is_structural(line) or is_blank(line):
            output.append(line)
            i += 1
            continue

        current = line.strip()
        j = i + 1
        while j < len(lines) and should_join_paragraph_lines(current, lines[j]):
            current = normalize_inline_spacing(f"{current} {lines[j].strip()}")
            j += 1

        output.append(current)
        i = j

    return output


def drop_repeated_toc(lines: list[str]) -> list[str]:
    output: list[str] = []
    previous_was_toc = False
    for line in lines:
        if TABLE_OF_CONTENTS_RE.match(line.strip()):
            if previous_was_toc:
                continue
            previous_was_toc = True
            output.append("## Table of Contents")
            continue
        previous_was_toc = False
        output.append(line)
    return output


def collapse_blank_lines(lines: list[str]) -> list[str]:
    output: list[str] = []
    blank_streak = 0
    for line in lines:
        if is_blank(line):
            blank_streak += 1
            if blank_streak <= 1:
                output.append("")
            continue
        blank_streak = 0
        output.append(line.rstrip())
    return output


def clean_markdown(text: str) -> str:
    lines = text.splitlines()
    lines = drop_repeated_toc(lines)
    lines = rejoin_broken_headings(lines)
    lines = rejoin_paragraphs(lines)
    lines = collapse_blank_lines(lines)
    cleaned = "\n".join(lines).strip()
    return f"{cleaned}\n" if cleaned else ""


def default_output_path(input_path: Path) -> Path:
    return input_path.with_suffix(f"{input_path.suffix}.clean.md")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Clean SEC markdown exported from datamule or similar tools.")
    parser.add_argument("input", type=Path, help="Path to the raw markdown file.")
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Optional output path. Defaults to <input>.clean.md",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path: Path = args.input
    output_path = args.output or default_output_path(input_path)

    raw = input_path.read_text(encoding="utf-8")
    cleaned = clean_markdown(raw)
    output_path.write_text(cleaned, encoding="utf-8")
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
