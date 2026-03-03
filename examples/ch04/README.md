# Practice Examples: Chapter 4 — Implementing a GPT Model from Scratch

## Three-Layer Architecture — Layer 3: Practice

## What's Here

These are my personal practice scripts for Chapter 4 and its bonus topics. The goal is to
build muscle memory for GPT architecture components and the key inference optimizations that
modern LLMs rely on.

| # | File | Topic |
| :--- | :--- | :--- |
| 01 | `01_gpt_model_examples.py` | FeedForward block, GELU activation, tensor shape verification |
| 02 | `02_performance_examples.py` | Parameter counting, VRAM memory estimation (fp32 vs fp16) |
| 03 | `03_kv_cache_examples.py` | KV Cache concatenation logic — avoiding quadratic re-computation |
| 04 | `04_gqa_examples.py` | MHA vs GQA KV cache memory comparison (head count effect) |
| 05 | `05_mla_examples.py` | MLA latent-space KV compression vs standard MHA storage cost |
| 06 | `06_swa_examples.py` | Sliding Window Attention mask construction and visualization |
| 07 | `07_moe_examples.py` | MoE router: Top-K expert selection via softmax gating |
| 08 | `08_deltanet_examples.py` | Gated attention: sigmoid gate applied to Query vectors |

## How to Run

```powershell
# From repo root, with venv active:
uv run python examples/ch04/01_gpt_model_examples.py
uv run python examples/ch04/02_performance_examples.py
uv run python examples/ch04/03_kv_cache_examples.py
uv run python examples/ch04/04_gqa_examples.py
uv run python examples/ch04/05_mla_examples.py
uv run python examples/ch04/06_swa_examples.py
uv run python examples/ch04/07_moe_examples.py
uv run python examples/ch04/08_deltanet_examples.py
```

## Alignment with Other Layers

| Layer | Location |
| :--- | :--- |
| Theory (reading notes) | `reading-notes/ch04_01_gpt_model_architecture.md` – `ch04_08_deltanet.md` |
| Implementation (notebooks) | `notebooks/ch04/01_gpt-model-implementation.ipynb` – `08_deltanet-implementation.ipynb` |
| Practice | This folder |

## Source Attribution

Concepts from *Build a Large Language Model From Scratch* (Raschka), Chapter 4 and bonus sections.  
Additional bonus topics reference DeepSeek V2/V3, Gemma 2/3, and Qwen3-Next architectures.  
All code is my own reconstruction — not copied from source-material.
