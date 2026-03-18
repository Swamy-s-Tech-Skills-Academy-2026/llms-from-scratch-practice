# Contributing

This repo is primarily **Swamy’s personal learning workspace** (STSA 2026). If you fork or collaborate, please follow these rules.

## Figures and images (mandatory)

- **Do not** hotlink or embed figures from the book’s companion site or publisher assets (e.g. cover art, chapter diagrams hosted on third-party CDNs).
- **Do not** copy image files from the book or companion materials into this repository.
- **Do** use short **text placeholders** (e.g. “Figure from the book — see book or companion site for diagram”) or **your own** original diagrams (e.g. draw in Excalidraw, Mermaid, or matplotlib from your own code).

This keeps the project aligned with **zero-copy** practice and avoids redistributing copyrighted visuals.

## Notebook outputs before push (recommended)

Committed notebooks should **not** include large embedded binary blobs (e.g. base64 `image/png` from matplotlib) unless you intentionally want them versioned.

**Clear outputs** from one notebook:

```powershell
uv run python tools/clear_notebook_outputs.py notebooks/ch04/01_gpt-model-implementation.ipynb
```

Or use Jupyter: **Kernel → Restart & Clear Output**, then save.

**Clear all notebooks** under `notebooks/` (repo root):

```powershell
uv run python tools/clear_notebook_outputs.py
```

Optional: only one chapter, e.g. `uv run python tools/clear_notebook_outputs.py notebooks/ch04`.

## Code and docs

- Follow `.cursor/rules/` (zero-copy, source-material read-only, educational tone).
- Python in `src/` should pass CI: `black`, `isort`, `flake8`, `pytest`.
- For markdown link checking, run Lychee via Docker:

```powershell
docker run --rm -v "${PWD}:/workspace" -w /workspace lycheeverse/lychee --config /workspace/.lychee.toml /workspace
```
