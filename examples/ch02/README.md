# Practice Examples: Chapter 2 — Working with Text Data

## Three-Layer Architecture — Layer 3: Practice

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

| Layer | File |
| :--- | :--- |
| Theory      | `reading-notes/ch02_decoder_only_transformer_flow.md` |
| Implementation | `notebooks/ch02/01_main-chapter-code/01_ch02.ipynb` |
| Practice    | This folder |

## Source Attribution

Concepts from *Build a Large Language Model From Scratch* (Raschka), Chapter 2.  
All code is my own reconstruction — not copied from source-material.
