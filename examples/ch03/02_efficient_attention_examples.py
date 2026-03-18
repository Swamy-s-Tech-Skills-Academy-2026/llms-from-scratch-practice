"""
Chapter 3 — Bonus: Efficient Multi-Head Attention Implementations

My personal practice examples for understanding the performance trade-offs
between different approaches to Multi-Head Attention (MHA):
  - Naive Python loop over heads (easy to read, slow in practice)
  - Stacked tensor approach (single matmul over all heads)
  - PyTorch scaled_dot_product_attention (FlashAttention-style fused kernel)

I'm experimenting here to build intuition about *why* the vectorised version
is faster and how the shapes change as we stack heads.

Reference: notebooks/ch03/02_bonus_efficient-multihead-attention/mha-implementations.ipynb
"""

import time

import torch
import torch.nn as nn
import torch.nn.functional as F

# ─────────────────────────────────────────────────────────────
# Config
# ─────────────────────────────────────────────────────────────

torch.manual_seed(42)

BATCH_SIZE = 4
SEQ_LEN = 64
D_MODEL = 128
NUM_HEADS = 4
HEAD_DIM = D_MODEL // NUM_HEADS  # 32


def make_qkv(batch: int, seq: int, d_model: int) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    """Create random Q, K, V tensors for attention experiments."""
    q = torch.randn(batch, seq, d_model)
    k = torch.randn(batch, seq, d_model)
    v = torch.randn(batch, seq, d_model)
    return q, k, v


# ─────────────────────────────────────────────────────────────
# Approach 1 : Naive loop over heads
# ─────────────────────────────────────────────────────────────


class NaiveMultiHeadAttention(nn.Module):
    """
    I implemented this first because it's the most readable:
    split into heads → attend each head individually → concat.
    It's conceptually clear but runs multiple sequential matmuls.
    """

    def __init__(self, d_model: int, num_heads: int) -> None:
        super().__init__()
        self.num_heads = num_heads
        self.head_dim = d_model // num_heads
        self.w_q = nn.Linear(d_model, d_model, bias=False)
        self.w_k = nn.Linear(d_model, d_model, bias=False)
        self.w_v = nn.Linear(d_model, d_model, bias=False)
        self.w_o = nn.Linear(d_model, d_model, bias=False)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        batch, seq, _ = x.shape
        q = self.w_q(x)  # (B, T, D)
        k = self.w_k(x)
        v = self.w_v(x)

        head_outputs = []
        for h in range(self.num_heads):
            # Slice out the h-th head's chunk along the feature dim
            start = h * self.head_dim
            end = start + self.head_dim
            q_h = q[:, :, start:end]  # (B, T, head_dim)
            k_h = k[:, :, start:end]
            v_h = v[:, :, start:end]

            # Scaled dot-product attention for this single head
            scale = self.head_dim**-0.5
            scores = torch.bmm(q_h, k_h.transpose(1, 2)) * scale  # (B, T, T)
            weights = torch.softmax(scores, dim=-1)
            head_out = torch.bmm(weights, v_h)  # (B, T, head_dim)
            head_outputs.append(head_out)

        # Concat heads and project
        concat = torch.cat(head_outputs, dim=-1)  # (B, T, D)
        return self.w_o(concat)


# ─────────────────────────────────────────────────────────────
# Approach 2 : Vectorised (stacked heads, single matmul)
# ─────────────────────────────────────────────────────────────


class VectorisedMultiHeadAttention(nn.Module):
    """
    Same math as the naive version but reshaped so all heads are processed
    in a single batched matmul.  The shape juggling (view + transpose) is
    the key insight I needed to practice.

    Shape flow:
      (B, T, D) → project → (B, T, D) → view → (B, T, H, d_h) → transpose
      → (B, H, T, d_h) → bmm across (B*H) → (B, H, T, d_h) → merge heads
      → (B, T, D) → output projection
    """

    def __init__(self, d_model: int, num_heads: int) -> None:
        super().__init__()
        self.num_heads = num_heads
        self.head_dim = d_model // num_heads
        self.w_q = nn.Linear(d_model, d_model, bias=False)
        self.w_k = nn.Linear(d_model, d_model, bias=False)
        self.w_v = nn.Linear(d_model, d_model, bias=False)
        self.w_o = nn.Linear(d_model, d_model, bias=False)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        batch, seq, d_model = x.shape
        q = self.w_q(x).view(batch, seq, self.num_heads, self.head_dim).transpose(1, 2)
        k = self.w_k(x).view(batch, seq, self.num_heads, self.head_dim).transpose(1, 2)
        v = self.w_v(x).view(batch, seq, self.num_heads, self.head_dim).transpose(1, 2)
        # q, k, v are now (B, H, T, d_h)

        scale = self.head_dim**-0.5
        scores = torch.matmul(q, k.transpose(-2, -1)) * scale  # (B, H, T, T)
        weights = torch.softmax(scores, dim=-1)
        out = torch.matmul(weights, v)  # (B, H, T, d_h)

        # Merge heads: (B, H, T, d_h) → (B, T, D)
        out = out.transpose(1, 2).contiguous().view(batch, seq, d_model)
        return self.w_o(out)


# ─────────────────────────────────────────────────────────────
# Approach 3 : PyTorch scaled_dot_product_attention (SDPA)
# ─────────────────────────────────────────────────────────────


class SDPAMultiHeadAttention(nn.Module):
    """
    Using torch.nn.functional.scaled_dot_product_attention, which internally
    dispatches to FlashAttention (fused CUDA kernel) when possible.
    This avoids materialising the full (T, T) attention matrix in memory —
    a big deal for long sequences.
    """

    def __init__(self, d_model: int, num_heads: int) -> None:
        super().__init__()
        self.num_heads = num_heads
        self.head_dim = d_model // num_heads
        self.w_q = nn.Linear(d_model, d_model, bias=False)
        self.w_k = nn.Linear(d_model, d_model, bias=False)
        self.w_v = nn.Linear(d_model, d_model, bias=False)
        self.w_o = nn.Linear(d_model, d_model, bias=False)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        batch, seq, d_model = x.shape
        q = self.w_q(x).view(batch, seq, self.num_heads, self.head_dim).transpose(1, 2)
        k = self.w_k(x).view(batch, seq, self.num_heads, self.head_dim).transpose(1, 2)
        v = self.w_v(x).view(batch, seq, self.num_heads, self.head_dim).transpose(1, 2)

        # PyTorch handles scaling + causal mask + memory-efficient kernel selection
        out = F.scaled_dot_product_attention(q, k, v, is_causal=True)  # (B, H, T, d_h)

        out = out.transpose(1, 2).contiguous().view(batch, seq, d_model)
        return self.w_o(out)


# ─────────────────────────────────────────────────────────────
# Demo runner
# ─────────────────────────────────────────────────────────────


def run_forward_pass(model: nn.Module, x: torch.Tensor, label: str) -> None:
    """Time one forward pass and print the output shape."""
    model.eval()
    with torch.no_grad():
        start = time.perf_counter()
        out = model(x)
        elapsed = (time.perf_counter() - start) * 1000
    print(f"  {label:<40} output: {tuple(out.shape)}   time: {elapsed:.2f} ms")


def demo_output_equivalence() -> None:
    """
    I want to verify that naive and vectorised MHA produce the same result
    when they share identical weights.  This sanity-check took me a while to
    get right because of the head-dimension slicing order.
    """
    print("\n=== Output equivalence check ===")
    x = torch.randn(2, 16, D_MODEL)

    naive = NaiveMultiHeadAttention(D_MODEL, NUM_HEADS)
    vec = VectorisedMultiHeadAttention(D_MODEL, NUM_HEADS)

    # Copy weights from naive → vectorised so outputs should match
    vec.w_q.weight.data = naive.w_q.weight.data.clone()
    vec.w_k.weight.data = naive.w_k.weight.data.clone()
    vec.w_v.weight.data = naive.w_v.weight.data.clone()
    vec.w_o.weight.data = naive.w_o.weight.data.clone()

    with torch.no_grad():
        out_naive = naive(x)
        out_vec = vec(x)

    max_diff = (out_naive - out_vec).abs().max().item()
    print(f"  Max absolute difference between naive and vectorised: {max_diff:.2e}")
    print(f"  {'✅ Match (< 1e-5)' if max_diff < 1e-5 else '❌ Mismatch — check weight copying'}")


def demo_timing_comparison() -> None:
    """
    Timing all three approaches on a moderate sequence length.
    My takeaway: the difference will be more pronounced on GPU and longer sequences.
    """
    print("\n=== Timing comparison (CPU) ===")
    x = torch.randn(BATCH_SIZE, SEQ_LEN, D_MODEL)

    naive = NaiveMultiHeadAttention(D_MODEL, NUM_HEADS)
    vec = VectorisedMultiHeadAttention(D_MODEL, NUM_HEADS)
    sdpa = SDPAMultiHeadAttention(D_MODEL, NUM_HEADS)

    run_forward_pass(naive, x, "Naive (loop over heads)")
    run_forward_pass(vec, x, "Vectorised (stacked matmul)")
    run_forward_pass(sdpa, x, "SDPA (PyTorch fused kernel)")


def demo_head_shape_walkthrough() -> None:
    """Walking through the tensor shape transformations explicitly."""
    print("\n=== Shape walkthrough: vectorised head splitting ===")
    x = torch.randn(BATCH_SIZE, SEQ_LEN, D_MODEL)

    w_q = nn.Linear(D_MODEL, D_MODEL, bias=False)
    q = w_q(x)
    print(f"  After projection   : {tuple(q.shape)}  (B, T, D)")

    q_split = q.view(BATCH_SIZE, SEQ_LEN, NUM_HEADS, HEAD_DIM)
    print(f"  After view (split) : {tuple(q_split.shape)}  (B, T, H, d_h)")

    q_heads = q_split.transpose(1, 2)
    print(f"  After transpose    : {tuple(q_heads.shape)}  (B, H, T, d_h)  ← ready for matmul")


if __name__ == "__main__":
    print("Chapter 3 Bonus: Efficient Multi-Head Attention Implementations")
    print("=" * 65)
    demo_head_shape_walkthrough()
    demo_output_equivalence()
    demo_timing_comparison()
    print("\nMy takeaway: SDPA is the production choice; vectorised MHA is")
    print("the best starting point for understanding the shape math.")
