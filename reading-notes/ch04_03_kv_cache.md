# Chapter 4: Implementing the KV Cache for Faster Inference
## Reflection Date: March 3, 2026

I noticed a massive bottleneck in how we generate text autoregressively. Generating text token-by-token using my standard Multi-Head Attention implementation is incredibly slow, and I finally understand *why*. I'm going to implement a **KV (Key-Value) Cache** to fix it.

## The Problem: Redundant Computations
Let's trace the generation loop for the prompt: `"Time flies"`.
1. I pass in "Time" and "flies". The attention mechanism computes Keys (K), Queries (Q), and Values (V) for *both* tokens. Attention scores are calculated, and the model outputs "fast".
2. Next loop: The prompt is now `"Time flies fast"`.
3. I pass in all three tokens. The model re-computes K, Q, and V for "Time" and "flies" **all over again**, even though they haven't changed!

My takeaway: As the generated sequence gets longer, the number of redundant computations grows quadratically. This is a massive waste of MACs/FLOPs.

## The Solution: KV Cache
The concept makes perfect sense: **I just need to memorize the Key and Value vectors for tokens I've already processed.**
- When generating the *next* token, I only compute the $Q, K, V$ for that single *new* token.
- I then concatenate the new $K$ and $V$ onto the *cached* historical Key and Value tensors.
- The new $Q$ (which is $1 \times d_{\text{out}}$) attends to the full historical $K$ (which is $N \times d_{\text{out}}$).

## The Trade-Off: Time vs. Space
This is a classic Computer Science trade-off. 
- **Time:** Inference speed increases dramatically because $\mathcal{O}(N)$ redundant matrix multiplications are skipped.
- **Space:** I now have to keep these large $K$ and $V$ tensors (across all heads and all layers) persisting in GPU VRAM during inference. This requires significant extra memory.

## Implementation Details Needed
To practice this in my codebase, I need to modify my `MultiHeadAttention` class:
1. Add a mechanism (or a parameter) to skip caching during "training" mode.
2. Initialize `self.k_cache` and `self.v_cache`.
3. Add logic in the `forward` pass to `torch.cat` the newly generated tokens onto the cache along the sequence dimension `dim=1`.

This feels like a huge "level up" in my understanding of how real-world LLMs are actually served in production without timing out. Next step: the notebook lab.
