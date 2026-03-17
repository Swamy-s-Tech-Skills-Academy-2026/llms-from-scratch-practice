# Python Tools

**Location**: `tools/pyscripts/`

These are small Python utilities for extracting/staging content and supporting my learning workflow.
They are designed to be run inside the repo’s virtual environment.

## Tools

### `pdf_to_md.py`

Canonical raw PDF → Markdown extractor for this repo's staging workflow.

- Best for: repo-aligned extraction into `docs/exports/`
- Safety: refuses to write under `source-material/` unless explicitly allowed
- Supports directories and recursive scans

```powershell
uv run python tools/pyscripts/pdf_to_md.py --input "source-material\livesessions" --output-dir "docs\exports\livesessions"
```

### `pdf_to_markdown.py`

Single PDF → Markdown convenience tool for one-off conversions. Uses PyMuPDF when available, else pypdf.  

- Best for: ad hoc single-file extraction
- Default: if you omit the output path, the `.md` file is created in the **same folder** as the PDF
- Safety: now refuses to write under `source-material/` unless `--allow-source-material-output` is passed

If I am doing repo staging work, `pdf_to_md.py` is the preferred tool. I keep `pdf_to_markdown.py` for quick one-off conversions where the simpler positional interface is useful.

```powershell
# Output in same folder as PDF
uv run python tools/pyscripts/pdf_to_markdown.py "source-material/some-handout.pdf"

# Or specify output path
uv run python tools/pyscripts/pdf_to_markdown.py path/to/file.pdf path/to/output.md

# If I intentionally want to write under source-material/ (not recommended)
uv run python tools/pyscripts/pdf_to_markdown.py path/to/file.pdf path/to/output.md --allow-source-material-output
```

### `pptx_to_md.py`

Raw PPTX → Markdown extraction (staging artifact). Optionally extracts embedded images.

```powershell
uv run python tools/pyscripts/pptx_to_md.py --input "C:\path\deck.pptx" --extract-images --include-notes
```
