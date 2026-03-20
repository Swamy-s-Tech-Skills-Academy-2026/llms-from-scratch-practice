"""
Practice Examples: Grouped-Query Attention (Chapter 4, Topic 4)
================================================================
Three-Layer Architecture — Layer 3: Practice

I'm building intuition for how GQA trades KV cache memory for a minor
reduction in model expressiveness. This example has two parts:
  1. Memory arithmetic — computing MHA vs GQA cache footprint by hand
  2. Module demo   — instantiating GroupedQueryAttention from src/ and
                     verifying it produces the expected output shape

Attribution: Concepts from *Build a Large Language Model From Scratch* (Raschka),
Chapter 4 / bonus folder 04_gqa. Code is my own reconstruction for practice.
"""

from __future__ import annotations

import torch

from src.model import (
    GroupedQueryAttention,
    estimate_gqa_kv_cache_bytes,
    estimate_mha_kv_cache_bytes,
)


def section(title: str) -> None:
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print("=" * 60)


def main() -> None:
    # Representative LLM-scale numbers (similar to LLaMA-7B)
    batch_size = 1
    seq_len = 4_096
    n_layers = 32
    emb_dim = 4_096
    n_heads = 32
    n_kv_groups = 8  # GQA with 8 KV heads instead of 32
    bytes_per_elem = 2  # fp16 / bf16

    section("1. KV-Cache Memory: MHA vs GQA")
    mha_bytes = estimate_mha_kv_cache_bytes(
        batch_size, seq_len, emb_dim, n_layers, n_heads, bytes_per_elem
    )
    gqa_bytes = estimate_gqa_kv_cache_bytes(
        batch_size, seq_len, emb_dim, n_layers, n_kv_groups, n_heads, bytes_per_elem
    )
    print(f"MHA KV-cache ({n_heads} KV heads): {mha_bytes / 1024**2:>8.1f} MB")
    print(f"GQA KV-cache ({n_kv_groups:>2} KV groups): {gqa_bytes / 1024**2:>8.1f} MB")
    reduction = (1 - gqa_bytes / mha_bytes) * 100
    print(f"Memory reduction:              {reduction:.1f}%")
    print(f"  My takeaway: halving KV heads from 32→{n_kv_groups} cuts cache by {reduction:.0f}%.")

    section("2. GroupedQueryAttention: Forward Pass Shape Check")
    # Small dimensions for a fast demo — same ratios as above
    emb_dim_small = 64
    n_heads_small = 8
    n_kv_small = 2  # 4 query heads per KV group
    batch, seq = 2, 10

    gqa = GroupedQueryAttention(
        emb_dim=emb_dim_small,
        n_heads=n_heads_small,
        n_kv_groups=n_kv_small,
    )
    x = torch.randn(batch, seq, emb_dim_small)
    out = gqa(x)
    print(f"Input  shape: {tuple(x.shape)}")
    print(f"Output shape: {tuple(out.shape)}")
    assert out.shape == x.shape, "GroupedQueryAttention must preserve (B, T, C) shape"
    print("  Shape verified — GQA preserves (batch, seq, emb_dim).")


if __name__ == "__main__":
    main()
