"""
Practice Examples: Mixture of Experts (Chapter 4, Topic 7)
===========================================================
Three-Layer Architecture — Layer 3: Practice

MoE replaces a single FFN with multiple expert FFNs and a learned router.
Only top-k experts process each token, keeping active FLOPs low while
total parameter count grows. This example has two parts:
  1. Router mechanics — simulating top-k soft routing by hand
  2. Module demo      — instantiating SparseMoEFeedForward from src/ and
                        verifying it produces the correct output shape

Attribution: Concepts from *Build a Large Language Model From Scratch* (Raschka),
Chapter 4 / bonus folder 07_moe. Code is my own reconstruction for practice.
"""

from __future__ import annotations

import torch
import torch.nn.functional as F

from src.model import SparseMoEFeedForward


def section(title: str) -> None:
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print("=" * 60)


def main() -> None:
    torch.manual_seed(42)

    section("1. MoE Router Mechanics (8 experts, top-2)")
    emb_dim = 32
    num_experts = 8
    top_k = 2

    # Simulate routing a single token with a random router weight matrix
    x = torch.randn(1, 1, emb_dim)
    router_weight = torch.randn(emb_dim, num_experts)
    logits = x @ router_weight  # (1, 1, num_experts)
    probs = F.softmax(logits, dim=-1)
    top_probs, top_indices = torch.topk(probs, top_k, dim=-1)

    print(f"Softmax probabilities (all {num_experts} experts):")
    print(f"  {probs.squeeze().detach().numpy().round(3)}")
    print(f"Selected expert indices (top-{top_k}): {top_indices.squeeze().tolist()}")
    print(f"Their weights (re-normalised):         {top_probs.squeeze().detach().numpy().round(3)}")
    print("  My observation: the router concentrates most probability mass on one expert.")

    section("2. SparseMoEFeedForward: Forward Pass Shape Check")
    hidden_dim = 64
    moe_block = SparseMoEFeedForward(
        emb_dim=emb_dim,
        hidden_dim=hidden_dim,
        num_experts=num_experts,
        top_k=top_k,
    )
    batch, seq = 2, 5
    x_batch = torch.randn(batch, seq, emb_dim)
    out = moe_block(x_batch)

    print(f"Input  shape: {tuple(x_batch.shape)}")
    print(f"Output shape: {tuple(out.shape)}")
    assert out.shape == x_batch.shape, "SparseMoEFeedForward must preserve (B, T, C) shape"
    print("  Shape verified — MoE FFN is a drop-in replacement for a standard FFN.")

    section("3. Capacity vs Active Params Illustration")
    print(f"Experts: {num_experts}   Active per token: {top_k}")
    total_expert_params = num_experts * (emb_dim * hidden_dim + hidden_dim * emb_dim)
    active_params = top_k * (emb_dim * hidden_dim + hidden_dim * emb_dim)
    print(f"Total expert params:  {total_expert_params:,}")
    print(f"Active params / token:{active_params:,}  ({100 * top_k / num_experts:.0f}% of total)")
    pct_dormant = 100 * (1 - top_k / num_experts)
    print(f"  My takeaway: {pct_dormant:.0f}% of expert capacity is dormant per token.")


if __name__ == "__main__":
    main()
