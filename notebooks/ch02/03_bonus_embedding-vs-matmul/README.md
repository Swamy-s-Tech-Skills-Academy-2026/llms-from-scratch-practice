# Bonus: Embedding Layers vs Matrix Multiplication

**Purpose**: Building intuition for what embedding layers actually do under the hood.

## What I'm Learning Here

I used to think embedding layers were somehow special — a magic lookup table that couldn't be replaced. This section convinced me otherwise.

Key insight: an embedding lookup for a token ID is mathematically identical to multiplying a one-hot encoded vector by a weight matrix. They produce the same output. The embedding layer is just a faster, memory-efficient shortcut.

## What's in This Folder

### `embeddings-and-linear-layers.ipynb`

I work through a side-by-side comparison:
- Build a one-hot encoded input vector manually
- Multiply it by a `nn.Linear` weight matrix
- Pass the same token ID into `nn.Embedding`
- Confirm the outputs are identical

**My takeaway**: Understanding this equivalence helps me reason about what the model is learning. The embedding weights are trainable parameters — just like any other linear layer.

## Source Attribution

Concepts derived from *Build a Large Language Model From Scratch* (Raschka), Chapter 2 bonus material.  
Implementation is my own reconstruction — not a copy of the source-material notebook.
