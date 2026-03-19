"""Single-PDF convenience converter.

This script keeps a simple one-file-in, one-file-out workflow for quick extraction.
Unlike `pdf_to_md.py`, it is not intended for recursive staging runs. It exists for
ad hoc conversions where I want an output path next to the source PDF or at an
explicit destination.

Safety rule: if the resolved output would land under `source-material/`, the script
refuses to write unless I opt in explicitly. That keeps the repo's read-only archive
policy intact.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import pymupdf  # PyMuPDF
    HAS_PYMUPDF = True
except ImportError:
    HAS_PYMUPDF = False

try:
    from pypdf import PdfReader
    HAS_PYPDF = True
except ImportError:
    HAS_PYPDF = False


def _is_within(child: Path, parent: Path) -> bool:
    try:
        child.resolve().relative_to(parent.resolve())
        return True
    except Exception:
        return False


def extract_with_pymupdf(pdf_path: Path) -> str:
    """Extract text using PyMuPDF (preferred for better formatting)."""
    doc = pymupdf.open(pdf_path)
    markdown_content = []

    for page_num, page in enumerate(doc, 1):
        markdown_content.append(f"\n## Slide {page_num}\n")
        text = page.get_text()
        markdown_content.append(text.strip())
        markdown_content.append("\n")

    doc.close()
    return "\n".join(markdown_content)


def extract_with_pypdf(pdf_path: Path) -> str:
    """Extract text using pypdf as fallback."""
    reader = PdfReader(pdf_path)
    markdown_content = []

    for page_num, page in enumerate(reader.pages, 1):
        markdown_content.append(f"\n## Slide {page_num}\n")
        text = page.extract_text()
        markdown_content.append(text.strip())
        markdown_content.append("\n")

    return "\n".join(markdown_content)


def pdf_to_markdown(pdf_path: str, output_path: str | None = None) -> str:
    """
    Convert PDF to markdown format.

    Args:
        pdf_path: Path to the PDF file
        output_path: Optional path to save markdown file.
            If omitted, saves to the same folder as the PDF with the same stem and .md extension.

    Returns:
        Markdown content as string
    """
    pdf_file = Path(pdf_path)

    if not pdf_file.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    # Try PyMuPDF first, fallback to pypdf
    if HAS_PYMUPDF:
        print(f"Extracting with PyMuPDF: {pdf_file.name}")
        content = extract_with_pymupdf(pdf_file)
    elif HAS_PYPDF:
        print(f"Extracting with pypdf: {pdf_file.name}")
        content = extract_with_pypdf(pdf_file)
    else:
        raise ImportError("No PDF library available. Install pymupdf or pypdf: pip install pymupdf")

    # Add header
    header = f"# {pdf_file.stem}\n\n"
    header += f"**Source**: {pdf_file.name}\n"
    header += "**Extracted**: Auto-generated from PDF\n\n"
    header += "---\n"

    full_content = header + content

    # Output path: use provided path, or same folder as PDF with .md extension
    output_file = Path(output_path) if output_path else (pdf_file.parent / f"{pdf_file.stem}.md")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(full_content, encoding='utf-8')
    print(f"Saved to: {output_file}")

    return full_content


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert one PDF to Markdown using a simple convenience workflow."
    )
    parser.add_argument("pdf_file", type=Path, help="Path to the input PDF file")
    parser.add_argument(
        "output_file",
        nargs="?",
        type=Path,
        default=None,
        help="Optional output Markdown path. Default: next to the input PDF with the same stem.",
    )
    parser.add_argument(
        "--allow-source-material-output",
        action="store_true",
        help="Allow writing under source-material/. Not recommended.",
    )
    return parser


if __name__ == "__main__":
    parser = build_arg_parser()
    args = parser.parse_args()

    workspace_root = Path(__file__).resolve().parents[2]
    source_material_dir = workspace_root / "source-material"
    output_path = args.output_file or (args.pdf_file.parent / f"{args.pdf_file.stem}.md")

    if _is_within(output_path, source_material_dir) and not args.allow_source_material_output:
        print(
            "Refusing to write output under source-material/. "
            "Pass --allow-source-material-output if you really want this.",
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        pdf_to_markdown(str(args.pdf_file), str(output_path))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
