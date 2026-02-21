# Bonus: Efficient Multi-Head Attention Implementations

**Purpose**: Comparing different ways to implement multi-head attention to understand trade-offs in performance and readability.

## What's in this folder

### mha-implementations.ipynb

I'm exploring two main implementation strategies:

- **Wrapper approach**: Stack multiple `CausalAttention` heads and concatenate their outputs. Simple to read but less efficient at scale.
- **Weight-split approach**: Use a single set of `W_query`, `W_key`, `W_value` matrices and split them across heads using tensor reshaping. More efficient because all heads share one forward pass.

**Key questions I'm working through**:
- Why does the weight-split approach produce the same result with fewer operations?
- What does `view` + `transpose` actually do to the tensor shape?
- How do I verify both approaches give equivalent outputs?

## Source Attribution

Concepts derived from *Build a Large Language Model From Scratch* (Raschka), Chapter 3.
Implementation is my own reconstruction for learning purposes, not a copy of the source material.
