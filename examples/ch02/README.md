# Practice Examples: Chapter 2 — Working with Text Data

## What's Here

These are my personal practice scripts for Chapter 2. The goal is to be able to reproduce these patterns from memory — not just run them once.

| # | File | Topic |
| :--- | :--- | :--- |
| 01 | `01_tokenization-examples.py` | tiktoken encode/decode, token inspection, special tokens, vocabulary size |
| 02 | `02_dataloader-examples.py` | Manual sliding window, `GPTDatasetV1`, DataLoader batches, stride effects |

## How to Run

```powershell
# From repo root, with venv active:
uv run python examples/ch02/01_tokenization-examples.py
uv run python examples/ch02/02_dataloader-examples.py
```

## Alignment with Other Layers

This chapter is the practice layer in the repo's three-layer learning pattern.

| Layer | Files |
| :--- | :--- |
| Theory      | `reading-notes/ch02_01_decoder_only_transformer_flow.md` (overview) |
|             | `reading-notes/ch02_02_byte_pair_encoding.md` (BPE) |
|             | `reading-notes/ch02_03_embeddings_vs_matmul.md` (embedding vs linear) |
|             | `reading-notes/ch02_04_dataloader_intuition.md` (sliding-window) |
| Implementation | `notebooks/ch02/01_main-chapter-code/01_ch02.ipynb` |
| Practice    | This folder |

## Source Attribution

Concepts from *Build a Large Language Model From Scratch* (Raschka), Chapter 2.  
All code is my own reconstruction — not copied from source-material.
