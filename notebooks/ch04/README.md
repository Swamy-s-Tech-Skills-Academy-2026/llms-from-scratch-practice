# Chapter 4: Implementing a GPT Model from Scratch

**Phase**: Implementation (Layer 2 — Simulation)

## Focus

Building the complete GPT architecture from the ground up — FeedForward blocks, multi-head
attention, layer normalization, and the full Transformer stack. Bonus notebooks explore the
inference optimizations that make production LLMs possible: KV Caching, Grouped Query
Attention, Multi-head Latent Attention, Sliding Window Attention, Mixture of Experts, and
DeltaNet.

## Learning Goals

- Understand the architecture of GPT-2/GPT-3 — how FeedForward blocks, softmax prediction
  heads, and GELU activations fit together
- Estimate model size (parameter count) and GPU memory requirements before training
- Build intuition for KV Cache — why naive autoregressive decoding is quadratic and how caching
  solves it
- Understand how Grouped Query Attention (GQA) reduces KV cache memory with a trade-off in
  head expressiveness
- Explore Multi-head Latent Attention (MLA) — DeepSeek's approach to compressing KV
  representations into a shared latent space
- Implement Sliding Window Attention masks and understand how they limit context length per
  layer while keeping compute linear
- Trace a Mixture of Experts (MoE) router: Top-K gating, load balancing, and sparse
  activation patterns
- Understand DeltaNet's gating mechanism and how selective state updates differ from
  full softmax attention

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
