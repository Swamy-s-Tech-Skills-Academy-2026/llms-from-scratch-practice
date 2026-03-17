# Chapter 4: Implementing a GPT Model from Scratch

**Phase**: Implementation (Layer 2 — Simulation)

## Focus

This chapter is where I'm assembling the full GPT architecture from the ground up: feed-forward
blocks, multi-head attention, layer normalization, and the full transformer stack. The bonus
notebooks are my way of exploring the inference ideas that show up in modern LLM systems: KV
cache, grouped query attention, multi-head latent attention, sliding window attention, mixture
of experts, and DeltaNet.

## Learning Goals

- Understand the architecture of GPT-2 and GPT-3 style models, especially how feed-forward
  blocks, output heads, and GELU activations fit together.
- Estimate model size and GPU memory requirements before training.
- Build intuition for KV cache and why naive autoregressive decoding becomes quadratic.
- Understand how grouped query attention reduces KV cache memory with a trade-off in head
  expressiveness.
- Explore multi-head latent attention as one route to compressing KV representations.
- Implement sliding window attention masks and see how they keep per-layer compute bounded.
- Trace a mixture-of-experts router through Top-K gating, sparse dispatch, and load-balancing
  questions.
- Understand how DeltaNet uses gating and selective state updates instead of full softmax
  attention.

## Notebooks

### Main Chapter

| # | Notebook | Topic |
| :--- | :--- | :--- |
| 01 | `01_gpt-model-implementation.ipynb` | Full GPT architecture: FeedForward, GELU, stacked blocks |
| 02 | `02_performance-analysis.ipynb` | FLOPs analysis, parameter count, VRAM estimation by dtype |

### Bonus Topics

| # | Notebook | Topic |
| :--- | :--- | :--- |
| 03 | `03_kv-cache-implementation.ipynb` | KV Cache: concat pattern, shape growth, decode speedup |
| 04 | `04_gqa-implementation.ipynb` | Grouped Query Attention vs vanilla MHA — cache size math |
| 05 | `05_mla-implementation.ipynb` | Multi-head Latent Attention — latent KV compression ratio |
| 06 | `06_swa-implementation.ipynb` | Sliding Window Attention — mask construction and sparsity |
| 07 | `07_moe-implementation.ipynb` | Mixture of Experts — Top-K router, sparse dispatch |
| 08 | `08_deltanet-implementation.ipynb` | DeltaNet — gated token interaction, sigmoid gate |

### Exercises

| # | Notebook | Topic |
| :--- | :--- | :--- |
| — | `exercise-solutions.ipynb` | Parameter count verification, weight tying, output shape checks |

## Supporting Files

- `reading-notes/ch04_01_gpt_model_architecture.md` through `ch04_08_deltanet.md` — theory layer
- `examples/ch04/` — runnable practice scripts for all eight topics
- `source-material/ch04/` — read-only staging (do not modify)
