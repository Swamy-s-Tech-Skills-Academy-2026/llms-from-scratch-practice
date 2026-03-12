# My Recommended Learning Order

## Phase 1: Language Modeling Foundations

**Goal:** Understand what an LLM learns

I want to deeply understand:

- What a language model predicts
- Why next-token prediction works
- Perplexity and cross-entropy loss

**Checkpoint:**

- I can explain why predicting the next token leads to emergent language behavior.

## Phase 2: Tokenization (Often Underestimated)

**Goal:** Understand how text becomes numbers

I want to focus on:

- Byte Pair Encoding (BPE)
- Vocabulary size tradeoffs
- Token distribution effects

**Checkpoint:**

- I can explain why "unhappiness" becomes multiple tokens and why that matters.

## Phase 3: Transformer Architecture (Core of the Book)

**Goal:** Master the GPT architecture

Key components I want to revise:

- Token embeddings + positional embeddings
- Multi-Head Self-Attention
- Feed-Forward Networks
- LayerNorm & residual connections
- Causal masking

**Checkpoint:**

- I can draw the GPT block from memory and explain data flow through it.

## Phase 4: Training a GPT-Like Model

**Goal:** Understand how learning happens

I want to understand:

- Forward vs backward pass
- Loss curves and instability
- Learning rate schedules
- Weight initialization

**Checkpoint:**

- I understand why training can diverge and how to diagnose it.

## Phase 5: Pretraining vs Finetuning

**Goal:** Understand model adaptation

- Pretraining on large corpora
- Finetuning for tasks
- Overfitting risks
- Evaluation strategies

**Checkpoint:**

- I can explain why finetuning is cheap relative to pretraining.

---

## 4. How I Want to Study This Book

**I do not want to:**

- Blindly run notebooks
- Skip math explanations
- Treat code as “magic”

**I want to:**

- Rewrite parts of the code yourself
- Change hyperparameters intentionally
- Break the model and fix it
- Add logging and visualizations

**Golden Rule:**

- If I cannot explain why a line of code exists, I have not learned it.

---

## 5. Suggested Weekly Study Plan

| Week | Focus |
| :--- | :--- |
| 1 | Language modeling + tokenization |
| 2 | Attention & transformer blocks |
| 3 | Full GPT architecture |
| 4 | Training loop & optimization |
| 5 | Pretraining experiments |
| 6 | Finetuning & evaluation |

*My assumption here is 1–2 hours/day, which feels sustainable.*
