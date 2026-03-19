# Chapter 3: Efficient Multi-Head Attention Implementations
## Reflection Date: March 19, 2026

I built multi-head attention from scratch in the main chapter. The bonus notebook showed me three different ways to implement MHA — each mathematically equivalent but with different memory and speed profiles. My goal here is to understand *why* they differ.

## Implementation 1: Naive (Three Separate Projections)

This is what I built first. Three separate `nn.Linear` layers for Q, K, and V, each projecting `(B, T, d_model)` → `(B, T, d_model)`:

```python
q = self.query(x)   # (B, T, d_model)
k = self.key(x)     # (B, T, d_model)
v = self.value(x)   # (B, T, d_model)
```

Then split each into heads and compute attention per head. The code is the clearest, but it has three separate `nn.Linear` layers that can't be fused.

## Implementation 2: Combined QKV Projection

A single `nn.Linear(d_model, 3 * d_model)` produces all three projections in one matrix multiply:

```python
qkv = self.qkv(x)                          # (B, T, 3*d_model)
q, k, v = qkv.split(d_model, dim=-1)       # each (B, T, d_model)
```

My takeaway: this is **more hardware-efficient** because a single large matrix-multiply is faster than three small ones on modern GPUs. The weight matrices are concatenated but the result is identical.

## Implementation 3: PyTorch's `F.scaled_dot_product_attention`

PyTorch ≥ 2.0 provides a fused CUDA kernel for attention that uses **FlashAttention** under the hood when available:

```python
out = F.scaled_dot_product_attention(q, k, v, is_causal=True)
```

This is **memory-optimal** because FlashAttention avoids materialising the full `(T, T)` attention weight matrix in HBM. Instead, it computes attention in tiles that fit in fast on-chip SRAM.

## Comparison Table

| Implementation | FLOPs | Peak Memory | Code Clarity |
|:--------------|:------|:-----------|:------------|
| Naive (3 Linear) | Same | Highest (stores Q, K, V separately) | Clearest |
| Combined QKV | Same | Lower (one fused projection) | Good |
| `F.scaled_dot_product_attention` | Same* | Lowest (no T×T matrix in HBM) | Most concise |

*FLOPs are identical; FlashAttention reduces **memory I/O**, not arithmetic ops.

## What I Still Find Confusing

I understand *what* FlashAttention does (tiled SRAM computation to avoid HBM reads of the attention matrix), but I haven't worked through the mathematical proof that the tiled result equals the full attention matrix. That is on my list for a deeper revision pass.
