"""
PDF to Markdown Converter
Extracts text content from PDF files and formats as markdown.
"""

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
    header += f"**Extracted**: Auto-generated from PDF\n\n"
    header += "---\n"
    
    full_content = header + content

    # Output path: use provided path, or same folder as PDF with .md extension
    output_file = Path(output_path) if output_path else (pdf_file.parent / f"{pdf_file.stem}.md")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(full_content, encoding='utf-8')
    print(f"Saved to: {output_file}")

    return full_content


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pdf_to_markdown.py <pdf_file> [output_file]")
        print("  If output_file is omitted, creates <pdf_stem>.md in the same folder as the PDF.")
        print("\nAvailable libraries:")
        print(f"  PyMuPDF: {'✓' if HAS_PYMUPDF else '✗'}")
        print(f"  pypdf: {'✓' if HAS_PYPDF else '✗'}")
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        pdf_to_markdown(pdf_path, output_path)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
