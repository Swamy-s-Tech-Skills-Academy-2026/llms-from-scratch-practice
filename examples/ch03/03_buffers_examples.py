"""
Chapter 3 — Bonus: Understanding PyTorch Buffers

My personal practice for understanding the difference between:
  - `nn.Parameter`  — trainable weights (included in model.parameters())
  - `torch.Tensor`  — plain attribute (not saved in state_dict, not on correct device)
  - `register_buffer` — non-trainable persistent tensor (saved, device-aware)

Why this matters for LLMs: the causal attention mask and the RoPE cosine/sine
tables are both "fixed at init time, needed at forward time" — classic buffer use cases.
If I forget register_buffer and the mask stays on CPU while model moves to GPU,
I get a device mismatch error in the forward pass.

Reference: notebooks/ch03/03_understanding-buffers/understanding-buffers.ipynb
"""

import torch
import torch.nn as nn

# ─────────────────────────────────────────────────────────────
# Approach A: Mask stored as a plain Python attribute
#             (breaks when calling .to(device) or .cuda())
# ─────────────────────────────────────────────────────────────


class AttentionWithPlainTensor(nn.Module):
    """
    I initially did this and got burned: the causal_mask attribute is
    NOT moved when I call model.to('cuda'), so the forward pass fails with
    a RuntimeError about tensors on different devices.
    """

    def __init__(self, seq_len: int) -> None:
        super().__init__()
        self.w_q = nn.Linear(16, 16, bias=False)
        # ❌  plain attribute — NOT device-aware, NOT in state_dict
        self.causal_mask = torch.tril(torch.ones(seq_len, seq_len))

    def forward(self, q: torch.Tensor, k: torch.Tensor, v: torch.Tensor) -> torch.Tensor:
        # self.causal_mask stays on CPU even if model.to('cuda') was called
        scores = torch.bmm(q, k.transpose(1, 2))
        scores = scores.masked_fill(self.causal_mask == 0, float("-inf"))
        weights = torch.softmax(scores, dim=-1)
        return torch.bmm(weights, v)


# ─────────────────────────────────────────────────────────────
# Approach B: Mask stored via register_buffer (correct approach)
# ─────────────────────────────────────────────────────────────


class AttentionWithBuffer(nn.Module):
    """
    Using register_buffer ensures:
      1. The mask moves with the model when .to(device)/.cuda() is called
      2. The mask is saved and loaded in state_dict (persistent=True, default)
      3. The mask never appears in model.parameters() — not updated by an optimiser

    This is the pattern I should use for every fixed tensor in a module.
    """

    def __init__(self, seq_len: int) -> None:
        super().__init__()
        self.w_q = nn.Linear(16, 16, bias=False)
        # ✅  register_buffer — device-aware, in state_dict
        self.register_buffer(
            "causal_mask",
            torch.tril(torch.ones(seq_len, seq_len)),
        )

    def forward(self, q: torch.Tensor, k: torch.Tensor, v: torch.Tensor) -> torch.Tensor:
        # self.causal_mask is guaranteed to be on the same device as q
        scores = torch.bmm(q, k.transpose(1, 2))
        scores = scores.masked_fill(self.causal_mask == 0, float("-inf"))
        weights = torch.softmax(scores, dim=-1)
        return torch.bmm(weights, v)


# ─────────────────────────────────────────────────────────────
# Approach C: Non-persistent buffer
# ─────────────────────────────────────────────────────────────


class AttentionWithNonPersistentBuffer(nn.Module):
    """
    For tensors that can be recomputed cheaply (e.g., RoPE sin/cos tables),
    I can set persistent=False.  The buffer still moves with the model but
    is NOT saved to disk in state_dict, saving checkpoint file size.
    """

    def __init__(self, seq_len: int) -> None:
        super().__init__()
        self.w_q = nn.Linear(16, 16, bias=False)
        # persistent=False: device-aware but NOT in state_dict
        self.register_buffer(
            "causal_mask",
            torch.tril(torch.ones(seq_len, seq_len)),
            persistent=False,
        )

    def forward(self, q: torch.Tensor, k: torch.Tensor, v: torch.Tensor) -> torch.Tensor:
        scores = torch.bmm(q, k.transpose(1, 2))
        scores = scores.masked_fill(self.causal_mask == 0, float("-inf"))
        weights = torch.softmax(scores, dim=-1)
        return torch.bmm(weights, v)


# ─────────────────────────────────────────────────────────────
# Demo helpers
# ─────────────────────────────────────────────────────────────


def demo_state_dict_visibility(seq_len: int = 8) -> None:
    """
    Shows which approach appears in state_dict.
    My takeaway: plain attribute = invisible; buffer = visible; non-persistent = invisible.
    """
    print("\n=== state_dict key visibility ===")
    plain = AttentionWithPlainTensor(seq_len)
    buffered = AttentionWithBuffer(seq_len)
    non_persistent = AttentionWithNonPersistentBuffer(seq_len)

    print(f"  Plain tensor keys  : {list(plain.state_dict().keys())}")
    print(f"  Buffer keys        : {list(buffered.state_dict().keys())}")
    print(f"  Non-persistent keys: {list(non_persistent.state_dict().keys())}")


def demo_parameters_vs_buffers(seq_len: int = 8) -> None:
    """
    Buffer does NOT appear in model.parameters() — the optimiser ignores it.
    Parameter DOES appear — the optimiser updates it.
    """
    print("\n=== parameters() vs buffers() ===")
    model = AttentionWithBuffer(seq_len)

    param_names = [name for name, _ in model.named_parameters()]
    buffer_names = [name for name, _ in model.named_buffers()]
    print(f"  Parameters (trainable) : {param_names}")
    print(f"  Buffers (fixed)        : {buffer_names}")


def demo_buffer_values(seq_len: int = 6) -> None:
    """Print the causal mask so I can visually confirm the lower-triangular shape."""
    print("\n=== Causal mask content ===")
    model = AttentionWithBuffer(seq_len)
    print(model.causal_mask)
    print("  Lower-triangular: each token only attends to itself and earlier tokens.")


def demo_forward_pass(seq_len: int = 8) -> None:
    """
    Quick sanity check: buffered model produces a valid output shape
    and the masked positions produce zero weight (after softmax of -inf → 0).
    """
    print("\n=== Forward pass sanity check ===")
    batch, d = 2, 16
    q = torch.randn(batch, seq_len, d)
    k = torch.randn(batch, seq_len, d)
    v = torch.randn(batch, seq_len, d)

    model = AttentionWithBuffer(seq_len)
    model.eval()
    with torch.no_grad():
        out = model(q, k, v)
    print(f"  Input shape  : {tuple(q.shape)}")
    print(f"  Output shape : {tuple(out.shape)}")
    print(f"  Output has NaN: {out.isnan().any().item()}")


if __name__ == "__main__":
    print("Chapter 3 Bonus: Understanding PyTorch Buffers")
    print("=" * 55)

    SEQ = 8
    demo_state_dict_visibility(SEQ)
    demo_parameters_vs_buffers(SEQ)
    demo_buffer_values(SEQ)
    demo_forward_pass(SEQ)

    print("\nMy takeaway: always use register_buffer for masks, position")
    print("tables, and any fixed tensor that must travel with the model.")
