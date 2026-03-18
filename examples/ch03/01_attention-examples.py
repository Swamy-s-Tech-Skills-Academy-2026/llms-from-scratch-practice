"""
Practice Examples: Attention Mechanisms (Chapter 3)
====================================================
Three-Layer Architecture — Layer 3: Practice

I'm practising the attention building blocks here — starting simple and
building up to Multi-Head Attention (MHA). The goal is to type each class
from memory until the shapes and math feel natural.

Topics practised here:
  1. Scaled dot-product attention score (one query vs all keys)
  2. Simple self-attention (all tokens attend to all tokens)
  3. Single-head causal attention with mask
  4. Multi-Head Attention — wrapper approach
  5. Shape sanity checks (the part I always forget)

Attribution: Concepts from *Build a Large Language Model From Scratch* (Raschka),
Chapter 3. Code is my own reconstruction for practice purposes.
"""

from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F

torch.manual_seed(42)


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------


def section(title: str) -> None:
    """Print a visible section header."""
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print("=" * 60)


# Shared 6-token input (same as ch03 notebook examples)
# Each row is a 3-dimensional token embedding
INPUTS = torch.tensor(
    [
        [0.43, 0.15, 0.89],  # "Your"    — x^(1)
        [0.55, 0.87, 0.66],  # "journey" — x^(2)
        [0.57, 0.85, 0.64],  # "starts"  — x^(3)
        [0.22, 0.58, 0.33],  # "with"    — x^(4)
        [0.77, 0.25, 0.10],  # "one"     — x^(5)
        [0.05, 0.80, 0.55],  # "step"    — x^(6)
    ]
)  # shape: (6, 3)


# ---------------------------------------------------------------------------
# 1. Scaled dot-product score for one query
# ---------------------------------------------------------------------------


def example_single_query_attention() -> None:
    """Compute attention scores for query token x^(2) against all keys.

    Why: Before vectorising, I want to understand the scalar score for one
    (query, key) pair: score = (q · k) / sqrt(d_k).
    The scaling prevents softmax saturation when d_k is large.
    """
    section("1. Scaled dot-product — single query")

    d_in, d_out = 3, 2
    torch.manual_seed(42)

    # Learned projection weights (no bias, as in Raschka's implementation)
    W_query = nn.Parameter(torch.rand(d_in, d_out))
    W_key = nn.Parameter(torch.rand(d_in, d_out))
    W_value = nn.Parameter(torch.rand(d_in, d_out))

    # Pick x^(2) as our query token
    x_2 = INPUTS[1]  # shape: (3,)

    query_2 = x_2 @ W_query  # shape: (d_out,)
    keys = INPUTS @ W_key  # shape: (6, d_out)
    values = INPUTS @ W_value  # shape: (6, d_out)

    # Raw attention scores: one scalar per key
    raw_scores = query_2 @ keys.T  # shape: (6,)

    # Scale by 1/sqrt(d_k) to keep variance in check
    d_k = query_2.shape[-1]
    scaled_scores = raw_scores / (d_k**0.5)

    attention_weights_2 = F.softmax(scaled_scores, dim=-1)
    context_vec_2 = attention_weights_2 @ values  # shape: (d_out,)

    print(f"Query (x^2):          {query_2.detach()}")
    print(f"Raw scores:           {raw_scores.detach()}")
    print(f"Scaled scores:        {scaled_scores.detach()}")
    print(f"Attention weights:    {attention_weights_2.detach()}")
    print(f"Context vector x^2:  {context_vec_2.detach()}")
    print(f"Weights sum to 1.0: {attention_weights_2.sum().item():.6f}")


# ---------------------------------------------------------------------------
# 2. Simple self-attention — all queries at once (vectorised)
# ---------------------------------------------------------------------------


class SimpleSelfAttention(nn.Module):
    """Self-attention without masking — every token attends to every token.

    This is the 'SelfAttention_v2' variant using nn.Linear (no bias).
    The difference from v1 (nn.Parameter) is only implementation style —
    both produce the same outputs when weights are equivalent.
    """

    def __init__(self, d_in: int, d_out: int) -> None:
        super().__init__()
        # nn.Linear stores weights as (d_out, d_in) internally, but acts as x @ W.T
        self.W_query = nn.Linear(d_in, d_out, bias=False)
        self.W_key = nn.Linear(d_in, d_out, bias=False)
        self.W_value = nn.Linear(d_in, d_out, bias=False)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """x: (seq_len, d_in) → context_vecs: (seq_len, d_out)."""
        queries = self.W_query(x)  # (seq_len, d_out)
        keys = self.W_key(x)
        values = self.W_value(x)

        d_k = keys.shape[-1]
        # Attention matrix: (seq_len, seq_len)
        scores = (queries @ keys.T) / (d_k**0.5)
        weights = F.softmax(scores, dim=-1)
        return weights @ values  # (seq_len, d_out)


def example_simple_self_attention() -> None:
    """Run SimpleSelfAttention on our 6-token input."""
    section("2. Simple self-attention (no mask)")

    torch.manual_seed(42)
    d_in, d_out = 3, 2
    attn = SimpleSelfAttention(d_in, d_out)

    with torch.no_grad():
        out = attn(INPUTS)

    print(f"Input shape : {INPUTS.shape}")
    print(f"Output shape: {out.shape}")
    print(f"Context vectors:\n{out}")

    assert out.shape == (6, d_out), "Shape mismatch!"
    print("✓ Output shape correct: (seq_len=6, d_out=2)")


# ---------------------------------------------------------------------------
# 3. Causal self-attention — mask future tokens
# ---------------------------------------------------------------------------


class CausalAttention(nn.Module):
    """Single-head causal self-attention.

    Adds a causal mask so position t can only attend to positions 0..t.
    This is essential for autoregressive (GPT-style) generation.

    Why register_buffer instead of self.mask = ...?
    Buffers travel with the model to the correct device automatically and
    are saved/restored in state_dict — without being trainable parameters.
    """

    def __init__(
        self,
        d_in: int,
        d_out: int,
        context_length: int,
        dropout: float = 0.0,
        qkv_bias: bool = False,
    ) -> None:
        super().__init__()
        self.d_out = d_out
        self.W_query = nn.Linear(d_in, d_out, bias=qkv_bias)
        self.W_key = nn.Linear(d_in, d_out, bias=qkv_bias)
        self.W_value = nn.Linear(d_in, d_out, bias=qkv_bias)
        self.dropout = nn.Dropout(dropout)

        # Upper-triangular mask: 1 in positions we want to hide (future tokens)
        mask = torch.triu(torch.ones(context_length, context_length), diagonal=1)
        self.register_buffer("mask", mask)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """x: (batch, seq_len, d_in) → (batch, seq_len, d_out)."""
        b, seq_len, _ = x.shape
        queries = self.W_query(x)
        keys = self.W_key(x)
        values = self.W_value(x)

        d_k = keys.shape[-1]
        scores = (queries @ keys.transpose(-2, -1)) / (d_k**0.5)

        # Apply causal mask: fill future positions with -inf so softmax → 0
        scores = scores.masked_fill(self.mask[:seq_len, :seq_len].bool(), float("-inf"))
        weights = F.softmax(scores, dim=-1)
        weights = self.dropout(weights)
        return weights @ values


def example_causal_attention() -> None:
    """Run CausalAttention and verify the mask is working."""
    section("3. Causal self-attention (GPT-style)")

    torch.manual_seed(42)
    batch = INPUTS.unsqueeze(0)  # (1, 6, 3) — add batch dimension
    d_in, d_out, ctx_len = 3, 2, 6

    attn = CausalAttention(d_in, d_out, context_length=ctx_len, dropout=0.0)

    with torch.no_grad():
        out = attn(batch)

    print(f"Input shape : {batch.shape}")
    print(f"Output shape: {out.shape}")
    print(f"Context vectors:\n{out[0]}")

    # Confirm mask is upper-triangular
    print(f"\nCausal mask:\n{attn.mask[:6, :6].int()}")
    assert out.shape == (1, 6, d_out)
    print("\n✓ Causal attention output shape correct: (batch=1, seq=6, d_out=2)")


# ---------------------------------------------------------------------------
# 4. Multi-Head Attention — wrapper approach
# ---------------------------------------------------------------------------


class MultiHeadAttentionWrapper(nn.Module):
    """MHA via stacked CausalAttention heads (wrapper approach).

    Simple to understand: run num_heads independent attention heads,
    concatenate their outputs along the last dimension.

    Trade-off: each head is a separate forward pass — less efficient than
    the weight-split approach at scale, but easier to reason about.
    """

    def __init__(
        self, d_in: int, d_out: int, context_length: int, num_heads: int, dropout: float = 0.0
    ) -> None:
        super().__init__()
        # Each head projects to d_out dimensions; final output is num_heads * d_out
        self.heads = nn.ModuleList(
            [CausalAttention(d_in, d_out, context_length, dropout) for _ in range(num_heads)]
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """x: (batch, seq_len, d_in) → (batch, seq_len, num_heads * d_out)."""
        return torch.cat([head(x) for head in self.heads], dim=-1)


def example_multihead_attention() -> None:
    """Run MultiHeadAttentionWrapper and check output shapes."""
    section("4. Multi-Head Attention (wrapper approach)")

    torch.manual_seed(42)
    batch = INPUTS.unsqueeze(0)  # (1, 6, 3)
    d_in, d_out_per_head = 3, 1  # 2 heads × 1 dim each → 2 total output dims
    num_heads = 2
    ctx_len = 6

    mha = MultiHeadAttentionWrapper(
        d_in, d_out_per_head, context_length=ctx_len, num_heads=num_heads, dropout=0.0
    )

    with torch.no_grad():
        out = mha(batch)

    expected_d_out = num_heads * d_out_per_head
    print(f"Input shape : {batch.shape}")
    print(f"Output shape: {out.shape}")  # (1, 6, 2)
    print(f"Context vectors:\n{out[0]}")

    assert out.shape == (
        1,
        6,
        expected_d_out,
    ), f"Expected (1, 6, {expected_d_out}), got {out.shape}"
    print(f"\n✓ Output shape correct: (batch=1, seq=6, d_out={expected_d_out})")


# ---------------------------------------------------------------------------
# 5. Shape sanity-check cheat sheet
# ---------------------------------------------------------------------------


def example_shape_cheatsheet() -> None:
    """Print the expected tensor shapes at each step of self-attention.

    Why: I keep forgetting whether keys.T or keys.transpose(-2,-1) and
    which dimension softmax goes over. This makes it explicit.
    """
    section("5. Shape cheat sheet")

    batch_size, seq_len, d_in, d_out = 2, 6, 3, 4
    x = torch.rand(batch_size, seq_len, d_in)
    W_q = nn.Linear(d_in, d_out, bias=False)
    W_k = nn.Linear(d_in, d_out, bias=False)

    with torch.no_grad():
        q = W_q(x)
        k = W_k(x)
        scores = q @ k.transpose(-2, -1)  # (batch, seq_len, seq_len)
        weights = F.softmax(scores / (d_out**0.5), dim=-1)

    print(f"x          : {tuple(x.shape)}       (batch, seq_len, d_in)")
    print(f"queries    : {tuple(q.shape)}       (batch, seq_len, d_out)")
    print(f"keys       : {tuple(k.shape)}       (batch, seq_len, d_out)")
    print(f"scores     : {tuple(scores.shape)}  (batch, seq_len, seq_len)")
    print(f"weights    : {tuple(weights.shape)} (batch, seq_len, seq_len)")
    print("\nKey rule: softmax over dim=-1 (over key dimension, not query dimension)")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


if __name__ == "__main__":
    print("Attention Mechanisms Practice Examples — Chapter 3")
    example_single_query_attention()
    example_simple_self_attention()
    example_causal_attention()
    example_multihead_attention()
    example_shape_cheatsheet()
    print("\nAll examples completed successfully.")
