"""
Practice Examples: DeltaNet / Linear Attention (Chapter 4, Topic 8)
====================================================================
Three-Layer Architecture — Layer 3: Practice

DeltaNet is a linear-recurrent attention alternative. Instead of growing
a KV-cache with sequence length, it maintains a fixed-size recurrent state
matrix of shape (n_heads, head_dim, head_dim). This example has two parts:
  1. Gating mechanics  — demonstrating per-element sigmoid gating as used in
                         Gated DeltaNet (replaces softmax with a bounded gate)
  2. State-size demo   — using estimate_deltanet_state_bytes from src/ to
                         compare fixed recurrent memory vs MHA KV-cache

Attribution: Concepts from *Build a Large Language Model From Scratch* (Raschka),
Chapter 4 / bonus folder 08_deltanet. Code is my own reconstruction for practice.
"""

from __future__ import annotations

import torch
import torch.nn as nn

from src.model import estimate_deltanet_state_bytes, estimate_mha_kv_cache_bytes


def section(title: str) -> None:
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print("=" * 60)


def main() -> None:
    torch.manual_seed(42)

    section("1. Gated Attention: Sigmoid vs Softmax")
    emb_dim = 16
    x = torch.randn(1, 1, emb_dim)

    query_layer = nn.Linear(emb_dim, emb_dim)
    gate_layer = nn.Linear(emb_dim, emb_dim)

    q = query_layer(x)
    gate = torch.sigmoid(gate_layer(x))
    gated_q = q * gate

    print(f"Raw query snippet  (first 4): {q.squeeze()[:4].detach().numpy().round(3)}")
    print(f"Gate values        (first 4): {gate.squeeze()[:4].detach().numpy().round(3)}")
    print(f"Gated query result (first 4): {gated_q.squeeze()[:4].detach().numpy().round(3)}")
    print("  My takeaway: the gate selects how much of each query dimension to retain.")
    print("  Unlike softmax (sums to 1 across tokens), sigmoid gates per-element independently.")

    section("2. Recurrent State Size: DeltaNet vs MHA KV-Cache")
    # Representative Llama-style numbers
    batch_size = 1
    emb_dim_large = 4_096
    n_layers = 32
    n_heads = 32
    bytes_per_elem = 2  # fp16

    # DeltaNet: fixed-size state regardless of sequence length
    deltanet_state = estimate_deltanet_state_bytes(
        batch_size, emb_dim_large, n_layers, n_heads, bytes_per_elem
    )

    # MHA: cache grows with sequence length
    mha_at_1k = estimate_mha_kv_cache_bytes(
        batch_size, 1_024, emb_dim_large, n_layers, n_heads, bytes_per_elem
    )
    mha_at_8k = estimate_mha_kv_cache_bytes(
        batch_size, 8_192, emb_dim_large, n_layers, n_heads, bytes_per_elem
    )
    mha_at_64k = estimate_mha_kv_cache_bytes(
        batch_size, 65_536, emb_dim_large, n_layers, n_heads, bytes_per_elem
    )

    print(f"DeltaNet recurrent state (constant): {deltanet_state / 1024**2:>8.1f} MB")
    print(f"MHA KV-cache at T=  1,024:           {mha_at_1k / 1024**2:>8.1f} MB")
    print(f"MHA KV-cache at T=  8,192:           {mha_at_8k / 1024**2:>8.1f} MB")
    print(f"MHA KV-cache at T= 65,536:           {mha_at_64k / 1024**2:>8.1f} MB")
    print(
        f"\n  DeltaNet memory stays at {deltanet_state / 1024**2:.1f} MB no matter how long"
        " the sequence grows — that is the core advantage."
    )


if __name__ == "__main__":
    main()
