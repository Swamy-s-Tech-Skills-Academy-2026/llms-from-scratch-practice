#!/usr/bin/env python3
"""Clear code-cell outputs and execution_count in Jupyter notebooks under notebooks/.

Usage (repo root):
    uv run python tools/clear_notebook_outputs.py
    uv run python tools/clear_notebook_outputs.py notebooks/ch04
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import nbformat


def clear_notebook(path: Path) -> bool:
    nb = nbformat.read(path, as_version=4)
    changed = False
    for cell in nb.cells:
        if cell.cell_type != "code":
            continue
        if getattr(cell, "outputs", None):
            cell.outputs = []
            changed = True
        if cell.get("execution_count") is not None:
            cell["execution_count"] = None
            changed = True
    if changed:
        nbformat.write(nb, path)
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "roots",
        nargs="*",
        default=[],
        help="Directories or .ipynb files (default: notebooks/)",
    )
    args = parser.parse_args()
    # argparse does not apply type= to default=[]; normalize every path here.
    roots = [Path(p) for p in (args.roots or [Path("notebooks")])]
    cleared = 0
    for root in roots:
        if root.is_file() and root.suffix == ".ipynb":
            if clear_notebook(root):
                print(f"Cleared: {root}")
                cleared += 1
            continue
        if not root.is_dir():
            print(f"Skip (not a directory or .ipynb): {root}", file=sys.stderr)
            continue
        for path in sorted(root.rglob("*.ipynb")):
            if clear_notebook(path):
                print(f"Cleared: {path}")
                cleared += 1
    print(f"Done. {cleared} notebook(s) updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
