# Chapter 3: Understanding PyTorch Buffers
## Reflection Date: March 19, 2026

I kept seeing `register_buffer` in attention implementations and didn't fully understand what it was. After working through the buffers notebook I finally get it — and I now understand why the causal mask in `CausalSelfAttention` is a buffer rather than a parameter.

## Parameters vs Buffers — The Core Distinction

| | `nn.Parameter` | Buffer (`register_buffer`) |
|:--|:--------------|:--------------------------|
| Updated by gradient | ✅ Yes | ❌ No |
| Saved to checkpoint (`state_dict`) | ✅ Yes | ✅ Yes (persistent) or ❌ No |
| Moved with `.to(device)` / `.cuda()` | ✅ Yes | ✅ Yes |
| Appears in `model.parameters()` | ✅ Yes | ❌ No |

My key insight: a buffer is **state that lives on the model but is not trained**. It moves with the model (to GPU) but doesn't accumulate gradients.

## The Causal Mask Is a Buffer

In `CausalSelfAttention.__init__`:

```python
self.register_buffer(
    "causal_mask",
    torch.triu(torch.ones(context_length, context_length), diagonal=1).bool(),
    persistent=False,
)
```

- `persistent=False` means the mask is **not** saved to the checkpoint. This makes sense: it's a deterministic function of `context_length`, so it can always be reconstructed.
- Using `register_buffer` ensures the mask is automatically moved to the same device as the model. Without this, I'd need to manually call `.to(device)` on the mask in `forward()`, which I'd inevitably forget.

## Two Types of Buffers in Practice

1. **Persistent buffers** (`persistent=True`, the default): saved in `state_dict`. Used for running statistics in BatchNorm — the running mean and variance are not parameters but must be checkpointed.
2. **Non-persistent buffers** (`persistent=False`): exist at runtime but aren't saved. Used for reconstructible tensors like the causal mask.

## My Debugging Lesson

Before I understood buffers, I ran into a bug where my causal mask was on CPU but attention tensors were on GPU, causing a device mismatch error. The fix was exactly `register_buffer`. Now I know: **any tensor the model needs for `forward()` that isn't learned should be a registered buffer**.

## What `model.state_dict()` Actually Contains

```python
model.state_dict()  # contains parameters + persistent buffers
model.buffers()     # only buffers (including non-persistent)
model.parameters()  # only learnable parameters (no buffers)
```

I noticed that `model.parameters()` does NOT include even persistent buffers, which is why the optimizer only updates true parameters during training.
