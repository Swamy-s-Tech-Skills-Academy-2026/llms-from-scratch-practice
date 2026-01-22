# Repository Structure & Design Philosophy

This document captures the **current layout** of the repo and the **target structure** we will grow into as implementation work starts.

---

## 🗂️ Current Repository Layout

```text
.
├── docs/               # Study notes and planning docs
├── src/                # Implementation code (currently empty)
├── README.md           # Entry point for the repo
└── LICENSE
```

---

## 🎯 Target Layout (Planned)

As the code evolves, we will introduce a modular `src/` layout similar to:

```text
.
├── data/               # Datasets and preprocessing artifacts
├── src/                # Core implementation code (engine room)
│   ├── config/         # Configuration files
│   ├── tokenization/   # Tokenizer implementations
│   ├── model/          # GPT / Transformer architecture code
│   ├── training/       # Training loops, loss functions
│   ├── evaluation/     # Metrics and analysis
│   ├── utils/          # Logging, seeding, checkpoints
│   └── main.py         # Entry point
├── notebooks/          # Exploratory notebooks and experiments
└── README.md           # This file
```

---

## Folder Guide (Planned)

| Folder | Purpose |
| :--- | :--- |
| **`src/`** | The "engine room". Contains pure, reusable Python modules. |
| **`notebooks/`** | Jupyter notebooks for interactive learning, data inspection, and visual debugging. |
| **`data/`** | Stores raw text data and processed `.bin` files. |

### `src/` Detailed Structure (Planned)

```text
src/
├── __init__.py
├── config/
│   ├── __init__.py
│   ├── model_config.py        # Model hyperparameters
│   ├── training_config.py     # Training-related configs
│   └── tokenizer_config.py    # Tokenizer settings
├── tokenization/
│   ├── __init__.py
│   ├── bpe.py                 # Byte Pair Encoding implementation
│   ├── vocab.py               # Vocabulary handling
│   └── tokenizer.py           # High-level tokenizer interface
├── model/
│   ├── __init__.py
│   ├── embeddings.py          # Token + positional embeddings
│   ├── attention.py           # Self-attention & multi-head attention
│   ├── feedforward.py         # FFN blocks
│   ├── transformer_block.py   # GPT block
│   └── gpt.py                 # Full GPT model
├── training/
│   ├── __init__.py
│   ├── dataset.py             # Dataset & dataloader logic
│   ├── loss.py                # Cross-entropy, etc.
│   ├── optimizer.py           # Optimizer setup
│   ├── scheduler.py           # Learning rate schedulers
│   └── trainer.py             # Training loop
├── evaluation/
│   ├── __init__.py
│   ├── metrics.py             # Perplexity, loss tracking
│   └── generation.py          # Text generation & sampling
├── utils/
│   ├── __init__.py
│   ├── seed.py                # Reproducibility
│   ├── logging.py             # Lightweight logging
│   └── checkpoint.py          # Save / load model state
└── main.py                    # Entry point (train / eval switch)
```

---

## Design Principles

1. **Modularity**: Each folder encapsulates a specific domain of the problem.
2. **Traceability**: The structure mirrors the learning path.
3. **Simplicity**: Modules are organized to support reuse.

As the project grows, this structure may evolve.