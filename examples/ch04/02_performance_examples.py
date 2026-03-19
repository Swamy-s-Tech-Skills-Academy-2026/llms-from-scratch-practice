"""
Practice Examples: Performance Analysis (Chapter 4, Topic 2)
=============================================================
Three-Layer Architecture — Layer 3: Practice

My goal here is to go beyond just counting parameters — I want to develop
intuition for how compute cost (FLOPs) and memory cost scale with architecture
choices like model depth, embedding dimension, and context length.

Topics practised here:
  1. Counting parameters in the real GPT-124M model (via GPTModel + GPTConfig)
  2. Estimating weights memory footprint
  3. Estimating FLOPs for a single forward pass (simplified rule-of-thumb)
  4. Seeing how FLOPs scale with context length

Attribution: Concepts from *Build a Large Language Model From Scratch* (Raschka),
Chapter 4 / bonus folder 02_performance-analysis. Code is my own reconstruction
for practice purposes.
"""

from __future__ import annotations

from src.model import GPTConfig, GPTModel


def section(title: str) -> None:
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print("=" * 60)


def estimate_forward_flops(config: GPTConfig, seq_len: int) -> int:
    """Rough FLOPs estimate for one forward pass.

    Using the standard transformer rule-of-thumb:
      FLOPs ≈ 12 × T × d_model² × n_layers
    This accounts for:
      - QKV projections:   3 × 2 × T × d_model²
      - Attention scores:  2 × T² × d_model  (≈ small vs d_model² for large d)
      - Output proj:       2 × T × d_model²
      - FFN (4× expand):   2 × 2 × T × 4 × d_model² = 16T d_model²
    Dominant term is ~12T d_model² per layer.
    """
    return 12 * seq_len * config.emb_dim**2 * config.n_layers


def main() -> None:
    # --- GPT-124M configuration (matches GPT-2 small) ---
    gpt124m_cfg = GPTConfig(
        vocab_size=50_257,
        context_length=1_024,
        emb_dim=768,
        n_heads=12,
        n_layers=12,
    )

    section("1. Real GPT-124M Parameter Count")
    model = GPTModel(gpt124m_cfg)
    total_params = sum(p.numel() for p in model.parameters())
    print(f"Total parameters:        {total_params:>15,}")
    print("  (expected ~124M for GPT-2 small)")

    section("2. Weights Memory Footprint")
    fp32_mb = total_params * 4 / (1024**2)
    fp16_mb = total_params * 2 / (1024**2)
    print(f"fp32 (4 bytes / param): {fp32_mb:>10.1f} MB")
    print(f"fp16 (2 bytes / param): {fp16_mb:>10.1f} MB")
    print(f"  My takeaway: even at fp16, weights alone need ~{fp16_mb:.0f} MB VRAM.")

    section("3. FLOPs for One Forward Pass (T=1024)")
    flops = estimate_forward_flops(gpt124m_cfg, seq_len=1024)
    gflops = flops / 1e9
    print(f"Estimated FLOPs:  {flops:>18,}")
    print(f"                  {gflops:>15.1f} GFLOPs")
    print("  Rule-of-thumb: FLOPs ≈ 12 × T × d_model² × n_layers")

    section("4. How FLOPs Scale with Context Length")
    print(f"{'Context Length':>16}  {'GFLOPs':>10}")
    print("-" * 30)
    for context in [128, 256, 512, 1024, 2048]:
        f = estimate_forward_flops(gpt124m_cfg, seq_len=context) / 1e9
        print(f"{context:>16,}  {f:>10.1f}")
    print("  I notice FLOPs scale linearly with T — that comes from the d_model²")
    print("  term dominating over the T² attention term at large d_model.")


if __name__ == "__main__":
    main()
