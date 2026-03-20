"""
Practice Examples: Sliding Window Attention (Chapter 4, Topic 6)
=================================================================
Three-Layer Architecture — Layer 3: Practice

SWA restricts each token to attend only within a local window, bounding
KV-cache memory regardless of total sequence length. This example has two
parts:
  1. Mask visualisation  — showing what the SWA attention mask looks like
  2. Module demo         — instantiating SlidingWindowSelfAttention from src/
                           and verifying shape during cached generation

Attribution: Concepts from *Build a Large Language Model From Scratch* (Raschka),
Chapter 4 / bonus folder 06_swa. Code is my own reconstruction for practice.
"""

from __future__ import annotations

import torch

from src.model import GPTConfig, SlidingWindowSelfAttention, estimate_swa_kv_cache_bytes


def section(title: str) -> None:
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print("=" * 60)


def main() -> None:
    section("1. SWA Attention Mask Visualisation (seq=8, window=3)")
    seq_len = 8
    window_size = 3

    # Causal lower-triangular mask clipped to the local window.
    # Value 1 = "attend", 0 = "masked".
    mask = torch.tril(torch.ones(seq_len, seq_len))
    for i in range(seq_len):
        mask[i, : max(0, i - window_size + 1)] = 0

    print(mask)
    print(
        f"\n  Each row attends to at most {window_size} previous tokens.",
        "\n  Everything outside the window is zeroed out (masked).",
    )

    section("2. KV-Cache Memory: MHA vs SWA")
    batch_size, seq_len_long, emb_dim, n_layers, n_heads = 1, 8_192, 4_096, 32, 32
    bytes_per_elem = 2

    from src.model import estimate_mha_kv_cache_bytes

    mha_bytes = estimate_mha_kv_cache_bytes(
        batch_size, seq_len_long, emb_dim, n_layers, n_heads, bytes_per_elem
    )
    swa_bytes = estimate_swa_kv_cache_bytes(
        batch_size,
        window_size=1_024,
        emb_dim=emb_dim,
        n_layers=n_layers,
        n_heads=n_heads,
        bytes_per_elem=bytes_per_elem,
    )
    print(f"MHA cache (T={seq_len_long:,}):          {mha_bytes / 1024**3:.2f} GB")
    print(f"SWA cache (window={1024:,}): {swa_bytes / 1024**2:.1f} MB  (constant!)")
    print("  My takeaway: SWA cache is bounded by window size, not sequence length.")

    section("3. SlidingWindowSelfAttention: Cached Shape Check")
    cfg = GPTConfig(vocab_size=64, context_length=32, emb_dim=32, n_heads=4, n_layers=2)
    swa_attn = SlidingWindowSelfAttention(cfg, window_size=4)

    prompt = torch.randn(1, 5, cfg.emb_dim)
    step = torch.randn(1, 1, cfg.emb_dim)

    out_prompt = swa_attn(prompt, use_cache=True)
    out_step = swa_attn(step, use_cache=True)
    print(f"Prompt output shape:    {tuple(out_prompt.shape)}")
    print(f"Next-step output shape: {tuple(out_step.shape)}")
    assert out_prompt.shape == prompt.shape
    assert out_step.shape == step.shape
    print("  Shape verified — SWA preserves (batch, seq, emb_dim) at each step.")


if __name__ == "__main__":
    main()
