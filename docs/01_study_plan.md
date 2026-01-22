# Recommended Learning Order (Aligned to the Book)

## Phase 1: Language Modeling Foundations

**Goal:** Understand what an LLM learns

You should deeply understand:

- What a language model predicts
- Why next-token prediction works
- Perplexity and cross-entropy loss

**Checkpoint:**

- You can explain why predicting the next token leads to emergent language behavior.

## Phase 2: Tokenization (Often Underestimated)

**Goal:** Understand how text becomes numbers

Focus on:

- Byte Pair Encoding (BPE)
- Vocabulary size tradeoffs
- Token distribution effects

**Checkpoint:**

- You can explain why "unhappiness" becomes multiple tokens and why that matters.

## Phase 3: Transformer Architecture (Core of the Book)

**Goal:** Master the GPT architecture

Key components:

- Token embeddings + positional embeddings
- Multi-Head Self-Attention
- Feed-Forward Networks
- LayerNorm & residual connections
- Causal masking

**Checkpoint:**

- You can draw the GPT block from memory and explain data flow through it.

## Phase 4: Training a GPT-Like Model

**Goal:** Understand how learning happens

You will learn:

- Forward vs backward pass
- Loss curves and instability
- Learning rate schedules
- Weight initialization

**Checkpoint:**

- You understand why training can diverge and how to diagnose it.

## Phase 5: Pretraining vs Finetuning

**Goal:** Understand model adaptation

- Pretraining on large corpora
- Finetuning for tasks
- Overfitting risks
- Evaluation strategies

**Checkpoint:**

- You can explain why finetuning is cheap relative to pretraining.

---

# 4. How You Should Study This Book (Very Important)

**Do NOT:**

- Blindly run notebooks
- Skip math explanations
- Treat code as “magic”

**DO:**

- Rewrite parts of the code yourself
- Change hyperparameters intentionally
- Break the model and fix it
- Add logging and visualizations

**Golden Rule:**

- If you cannot explain why a line of code exists, you have not learned it.

---

# 5. Suggested Weekly Study Plan (Realistic)

| Week | Focus |
| :--- | :--- |
| 1 | Language modeling + tokenization |
| 2 | Attention & transformer blocks |
| 3 | Full GPT architecture |
| 4 | Training loop & optimization |
| 5 | Pretraining experiments |
| 6 | Finetuning & evaluation |

*This assumes 1–2 hours/day, which is sustainable.*
