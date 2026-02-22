# Python Tools

**Location**: `tools/pyscripts/`

These are small Python utilities for extracting/staging content and supporting my learning workflow.
They are designed to be run inside the repo’s virtual environment.

## Tools

### `pdf_to_md.py`

Raw PDF → Markdown extraction (staging artifact).

```powershell
uv run python tools/pyscripts/pdf_to_md.py --input "source-material\livesessions" --output-dir "docs\exports\livesessions"
```

### `pdf_to_markdown.py`

Single PDF → Markdown (one file in, one file out). Uses PyMuPDF when available, else pypdf.  
**Default:** if you omit the output path, the `.md` file is created in the **same folder** as the PDF (same stem, `.md` extension).

```powershell
# Output in same folder as PDF
uv run python tools/pyscripts/pdf_to_markdown.py "source-material/some-handout.pdf"

# Or specify output path
uv run python tools/pyscripts/pdf_to_markdown.py path/to/file.pdf path/to/output.md
```

### `pptx_to_md.py`

Raw PPTX → Markdown extraction (staging artifact). Optionally extracts embedded images.

```powershell
uv run python tools/pyscripts/pptx_to_md.py --input "C:\path\deck.pptx" --extract-images --include-notes
```
