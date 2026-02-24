# Repository Structure & Design Philosophy

This document captures the **current layout** of the repo and the **target structure** we will grow into as implementation work starts.

---

## 🗂️ Current Repository Layout

```text
.
├── examples/                      # Synthesized practice examples (Three-Layer Architecture)
├── notebooks/                     # Synthesized, hands-on learning notebooks
│   ├── ch02/                      # Chapter 2: Working with Text Data
│   │   ├── 01_main-chapter-code/  # Core tokenization + dataloader
│   │   ├── 02_bonus_bytepair-encoder/
│   │   ├── 03_bonus_embedding-vs-matmul/
│   │   ├── 04_bonus_dataloader-intuition/
│   │   └── 05_bpe-from-scratch/
│   └── ch03/                      # Chapter 3: Attention Mechanisms
│       ├── 01_attention_mechanisms.ipynb   # Main: §3.3 simple → §3.6 MHA
│       ├── 02_multihead-attention.ipynb    # MHA + data-loading quick reference
│       ├── exercise-solutions.ipynb        # Ex 3.1, 3.2, 3.3
│       ├── small-text-sample.txt           # Sample text for dataloader demos
│       ├── 02_bonus_efficient-multihead-attention/
│       │   ├── mha-implementations.ipynb  # Wrapper vs weight-split comparison
│       │   └── README.md
│       └── 03_understanding-buffers/
│           ├── understanding-buffers.ipynb # Plain attr vs register_buffer demo
│           └── README.md
├── reading-notes/                 # Synthesized theory notes (Swamy's voice)
│   ├── ch01_reading-strategy.md              # Ch01: personal reading strategy
│   ├── ch02_decoder_only_transformer_flow.md # Ch02: decoder-only data flow
│   └── ch03_attention_mechanisms.md          # Ch03: self-attention, causal mask, MHA
├── docs/                          # Study plans, structure docs, and reviews
│   ├── reference/                 # Git, PowerShell, Python command references
│   ├── reviews/                   # Code/notebook review reports
│   ├── 01_repository-structure.md
│   └── 01_study_plan.md
├── source-material/               # READ-ONLY staging area (raw author content)
│   ├── ch01/
│   ├── ch02/
│   └── ch03/
├── src/                           # Reusable Python modules (engine room)
│   ├── __init__.py
│   └── main.py
├── tests/                         # CI smoke tests
│   └── test_smoke.py
├── pyproject.toml                 # Project dependencies (uv)
├── .python-version                # Python version pin (3.12)
├── README.md                      # Entry point for the repo
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
| **`notebooks/`** | Jupyter notebooks for interactive learning, data inspection, and visual debugging (organized by chapter, e.g. `notebooks/ch02`, `notebooks/ch03`). |
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