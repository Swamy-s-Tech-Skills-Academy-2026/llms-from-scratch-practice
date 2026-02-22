"""PDF → Markdown converter (raw extraction).

This script extracts text from a PDF into Markdown for *personal study*.
In this repo, treat the output as a staging artifact: synthesize into your
own words before publishing as reading notes to respect the Zero-Copy Policy.

Usage (PowerShell, from repo root):
  uv run python tools/pyscripts/pdf_to_md.py --input "D:\\path\\file.pdf"
  uv run python tools/pyscripts/pdf_to_md.py --input "source-material\\livesessions" --recursive

Defaults:
- Output goes to docs/exports/<pdf-stem>.md
- Refuses to write output under source-material/ unless explicitly allowed
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
from pathlib import Path

from pypdf import PdfReader


def _is_within(child: Path, parent: Path) -> bool:
    try:
        child.resolve().relative_to(parent.resolve())
        return True
    except Exception:
        return False


def _clean_text(text: str) -> str:
    # Normalize weird PDF whitespace without being too aggressive.
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    # Remove trailing spaces per line.
    text = "\n".join(line.rstrip() for line in text.split("\n"))
    return text.strip()


def pdf_to_markdown(input_pdf: Path, output_md: Path) -> None:
    reader = PdfReader(str(input_pdf))

    output_md.parent.mkdir(parents=True, exist_ok=True)

    now = dt.datetime.now().astimezone()

    lines: list[str] = []
    lines.append(f"# Raw PDF Extract: {input_pdf.stem}")
    lines.append("")
    lines.append(f"- Source file: `{input_pdf.name}`")
    lines.append(f"- Pages: {len(reader.pages)}")
    lines.append(f"- Extracted at: {now:%Y-%m-%d %H:%M %Z}")
    lines.append("")
    lines.append(
        "> This is an automated extraction from a PDF for personal study. "
        "Please **synthesize** into original notes before publishing to `reading-notes/` "
        "to respect the repository's Zero-Copy Policy."
    )

    for page_index, page in enumerate(reader.pages, start=1):
        try:
            raw = page.extract_text() or ""
        except Exception:
            raw = ""

        text = _clean_text(raw)
        if not text:
            continue

        lines.append("")
        lines.append(f"## Page {page_index}")
        lines.append("")
        lines.extend(text.split("\n"))

    output_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Convert PDF(s) to Markdown (raw extraction).")

    parser.add_argument(
        "--input",
        required=True,
        type=Path,
        help="Path to a .pdf file or a directory containing PDFs",
    )

    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Directory to write Markdown files (default: docs/exports)",
    )

    parser.add_argument(
        "--recursive",
        action="store_true",
        help="If input is a directory, search recursively for PDFs.",
    )

    parser.add_argument(
        "--allow-source-material-output",
        action="store_true",
        help=(
            "Allow writing output under source-material/. "
            "(Not recommended; source-material is intended as read-only.)"
        ),
    )

    return parser


def main() -> int:
    parser = build_arg_parser()
    args = parser.parse_args()

    workspace_root = Path(__file__).resolve().parents[1]
    source_material_dir = workspace_root / "source-material"

    output_dir: Path
    if args.output_dir is None:
        output_dir = workspace_root / "docs" / "exports"
    else:
        output_dir = args.output_dir

    if _is_within(output_dir, source_material_dir) and not args.allow_source_material_output:
        raise SystemExit(
            "Refusing to write output under source-material/. "
            "Pass --allow-source-material-output if you really want this."
        )

    input_path: Path = args.input
    if not input_path.exists():
        raise SystemExit(f"Input path not found: {input_path}")

    pdf_files: list[Path] = []
    if input_path.is_file():
        if input_path.suffix.lower() != ".pdf":
            raise SystemExit("Input file must be a .pdf")
        pdf_files = [input_path]
    else:
        pattern = "**/*.pdf" if args.recursive else "*.pdf"
        pdf_files = sorted(input_path.glob(pattern))

    if not pdf_files:
        raise SystemExit(f"No PDF files found at: {input_path}")

    for pdf in pdf_files:
        out_md = output_dir / f"{pdf.stem}.md"
        pdf_to_markdown(pdf, out_md)
        print(f"Wrote Markdown: {out_md}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
