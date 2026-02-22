# My Notes: Attention Mechanisms (Chapter 3)

**Date**: February 22, 2026

Chapter 3 is the chapter I've been building toward. Tokenization (Ch 2) gets text into a tensor; attention (Ch 3) is how the model actually *relates* those tensors to each other. I'm writing this down to lock in the mental model before moving to the full GPT block.

---

## What problem does attention solve?

My simple answer: embeddings are static, but meaning is contextual.

The word "bank" has one embedding vector — always the same number, regardless of whether the sentence is about rivers or finance. Attention fixes this by letting each token *look at* other tokens and update its representation based on what it sees.

I keep reminding myself: **attention is not about remembering the past — it's about relating tokens within the current context window**.

---

## Self-Attention in my own words

For each token, we compute three vectors:
- **Query (Q)**: "What am I looking for?"
- **Key (K)**: "What do I offer?"
- **Value (V)**: "What is my actual content?"

The attention score between two tokens is the dot product of Q and K. We scale by $\frac{1}{\sqrt{d_k}}$ to prevent the scores from growing too large (which would push the softmax into a nearly one-hot region, killing gradients).

$$\text{Attention}(Q, K, V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right) V$$

The output for each token is a *weighted average* of all value vectors — weighted by how much that token attends to every other token.

---

## Why causal masking?

In a GPT-style model, the prediction for token $t$ must only depend on tokens $0, 1, \ldots, t-1$ — not future tokens. Without masking, the model would trivially "cheat" by looking ahead.

The implementation is an upper-triangular mask filled with $-\infty$ applied before the softmax. After softmax, those positions become 0, so they contribute nothing to the output.

I still confuse myself on which triangle to mask. My memory aid: **mask the upper right** (positions where column index > row index, i.e., future tokens).

---

## Multi-Head Attention

Instead of one attention function, we run $h$ attention heads in parallel — each with its own Q, K, V projections. The outputs are concatenated and projected once more.

$$\text{MHA}(X) = \text{Concat}(\text{head}_1, \ldots, \text{head}_h)W^O$$

**Why multiple heads?** Each head can learn a different type of relationship (syntactic, semantic, positional, co-reference, etc.). A single head can only focus on one type of pattern at a time.

Two implementation strategies I explored in my notebooks:
1. **Wrapper approach**: Run $h$ separate `CausalAttention` modules, concatenate outputs. Simple but less efficient.
2. **Weight-split approach**: Use one large Q/K/V matrix, reshape and split across heads internally. Same result, fewer operations.

---

## Things I still need to solidify

- I'm still not fully comfortable with the `view` + `transpose` tensor reshaping in the weight-split MHA. I need to trace through shapes by hand again.
- Why does scaling by $\sqrt{d_k}$ specifically help? I understand the intuition (dot products grow with dimension), but I want to derive it from the variance of the dot product distribution.
- The connection between attention weights and "what the model actually learned" — attention maps don't directly tell you about importance in a clean way.

---

## My takeaway for the chapter

Attention is the mechanism that transforms a sequence of static embeddings into context-aware representations. The self, causal, and multi-head variants are just incremental refinements of the same dot-product idea. Now I need to put it inside a full transformer block.

---

## Reference

Synthesized from personal implementation work in `notebooks/ch03/`.  
Concepts informed by *Build a Large Language Model From Scratch* (Raschka), Chapter 3.
