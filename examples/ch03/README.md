# Practice Examples: Chapter 3 — Attention Mechanisms

## What's Here

These are my personal practice scripts for Chapter 3. I rebuild each attention variant from memory until the shapes and math feel natural.

| # | File | Topic |
| :--- | :--- | :--- |
| 01 | `01_attention-examples.py` | Scaled dot-product, simple self-attention, causal attention, MHA wrapper, shape cheat sheet |
| 02 | `02_efficient_attention_examples.py` | Naive loop vs vectorised MHA vs PyTorch SDPA — timing and shape walkthrough |
| 03 | `03_buffers_examples.py` | `register_buffer` vs plain attribute — device-awareness, state_dict visibility |

## How to Run

```powershell
# From repo root, with venv active:
uv run python examples/ch03/01_attention-examples.py
uv run python examples/ch03/02_efficient_attention_examples.py
uv run python examples/ch03/03_buffers_examples.py
```

## Alignment with Other Layers

This chapter is the practice layer in the repo's three-layer learning pattern.

| Layer | Location |
| :--- | :--- |
| Theory      | `reading-notes/ch03_attention_mechanisms.md` |
| Implementation (main)  | `notebooks/ch03/01_attention_mechanisms.ipynb` |
| Implementation (bonus) | `notebooks/ch03/02_bonus_efficient-multihead-attention/` |
| Implementation (bonus) | `notebooks/ch03/03_understanding-buffers/` |
| Practice    | This folder |

## Source Attribution

Concepts from *Build a Large Language Model From Scratch* (Raschka), Chapter 3.  
All code is my own reconstruction — not copied from source-material.
