"""
Practice Examples: Multi-Head Latent Attention (Chapter 4, Topic 5)
====================================================================
Three-Layer Architecture — Layer 3: Practice

MLA is DeepSeek's innovation: instead of caching full K and V tensors,
it caches a compressed latent vector and reconstructs K/V on demand.
This example has two parts:
  1. Memory arithmetic — computing MHA vs MLA cache footprint by hand
  2. Module demo   — instantiating MultiHeadLatentAttention from src/ and
                     verifying forward pass shape (both standard and cached)

Attribution: Concepts from *Build a Large Language Model From Scratch* (Raschka),
Chapter 4 / bonus folder 05_mla. Code is my own reconstruction for practice.
"""

from __future__ import annotations

import torch

from src.model import (
    MultiHeadLatentAttention,
    estimate_mha_kv_cache_bytes,
    estimate_mla_kv_cache_bytes,
)


def section(title: str) -> None:
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print("=" * 60)


def main() -> None:
    # Representative numbers
    batch_size = 1
    seq_len = 4_096
    n_layers = 32
    emb_dim = 4_096
    n_heads = 32
    latent_dim = 512  # compressed KV dimension (much smaller than emb_dim)
    bytes_per_elem = 2  # fp16

    section("1. KV-Cache Memory: MHA vs MLA")
    mha_bytes = estimate_mha_kv_cache_bytes(
        batch_size, seq_len, emb_dim, n_layers, n_heads, bytes_per_elem
    )
    mla_bytes = estimate_mla_kv_cache_bytes(
        batch_size, seq_len, latent_dim, n_layers, bytes_per_elem
    )
    print(f"MHA cache (stores K+V, emb_dim={emb_dim}): {mha_bytes / 1024**2:>8.1f} MB")
    print(f"MLA cache (stores latent, dim={latent_dim}):   {mla_bytes / 1024**2:>8.1f} MB")
    pct = (mla_bytes / mha_bytes) * 100
    print(f"MLA uses only {pct:.1f}% of MHA's cache.")
    print(f"  My takeaway: trading ~{pct:.0f}% memory for extra up/down-projection compute.")

    section("2. MultiHeadLatentAttention: Forward Pass Shape Check")
    emb_dim_small = 64
    n_heads_small = 8
    latent_small = 16  # compressed dim
    batch, seq = 2, 6

    mla = MultiHeadLatentAttention(
        emb_dim=emb_dim_small,
        n_heads=n_heads_small,
        latent_dim=latent_small,
    )
    x = torch.randn(batch, seq, emb_dim_small)
    out = mla(x)
    print(f"Input  shape: {tuple(x.shape)}")
    print(f"Output shape: {tuple(out.shape)}")
    assert out.shape == x.shape, "MLA must preserve (B, T, C) shape"
    print("  Shape verified — MLA preserves (batch, seq, emb_dim).")

    section("3. MLA Cached Inference (Simulated Auto-Regressive)")
    mla.reset_cache()
    prompt = torch.randn(1, 4, emb_dim_small)
    next_tok = torch.randn(1, 1, emb_dim_small)

    out_prompt = mla(prompt, use_cache=True)
    out_next = mla(next_tok, use_cache=True)
    print(f"Prompt output shape:    {tuple(out_prompt.shape)}")
    print(f"Next-token output shape:{tuple(out_next.shape)}")
    print("  Cache grows step by step — only the latent vector is stored.")


if __name__ == "__main__":
    main()
