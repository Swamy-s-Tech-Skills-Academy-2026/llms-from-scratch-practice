# Bonus: Understanding PyTorch Buffers

**Purpose**: Clarifying why `register_buffer` is used in the causal attention mask, and what goes wrong without it.

## What's in this folder

### understanding-buffers.ipynb

The causal attention class uses `self.register_buffer("mask", ...)` rather than a plain attribute. This confused me — why not just use `self.mask = ...`?

This notebook works through the answer step by step:

1. Build `CausalAttentionWithoutBuffers` — works on CPU
2. Move it to GPU — the mask stays on CPU and crashes
3. Fix it manually with `.to(device)` — works but is tedious
4. Build `CausalAttentionWithBuffer` using `register_buffer` — clean solution
5. Show that buffers are also saved and restored via `state_dict`

**My takeaway**: Buffers are non-trainable tensors that travel with the model. They're not parameters (no gradients), but they need to be on the right device and preserved in checkpoints.

## Source Attribution

Concepts derived from *Build a Large Language Model From Scratch* (Raschka), Chapter 3 bonus material.
Implementation rebuilt in my own words to build genuine understanding.
