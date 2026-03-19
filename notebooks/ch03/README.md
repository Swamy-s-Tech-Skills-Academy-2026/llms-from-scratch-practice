# Chapter 3: Coding Attention Mechanisms

## Phase 3: Transformer Architecture

## Focus
This chapter is where I'm building intuition for the core mechanism that makes Transformers work: **self-attention**.

## Learning Goals
- Understand the difference between self-attention and causal self-attention.
- Implement scaled dot-product attention from scratch.
- Build multi-head attention modules.
- Visualize attention weights so I can see what the model is focusing on.

## Notebooks

### Main Chapter
- `01_attention_mechanisms.ipynb` — Building self-attention step-by-step (simple → causal → multi-head).
- `02_multihead-attention.ipynb` — Compact cheat-sheet: data loading + both MHA implementation strategies in one place.
- `exercise-solutions.ipynb` — My solutions to exercises 3.1, 3.2, and 3.3.

### Bonus Sections
- `02_bonus_efficient-multihead-attention/mha-implementations.ipynb` — Wrapper vs weight-split MHA comparison.
- `03_understanding-buffers/understanding-buffers.ipynb` — Why `register_buffer` is the right way to handle the causal mask.

## Supporting Files
- `small-text-sample.txt` — Short text excerpt used as input for the dataloader demos in ch03 notebooks.
