# LLMs From Scratch Practice (STSA 2026)

This repository is **Swamy's hands-on learning workspace** for building a GPT-style Large Language Model (LLM) from first principles.  
The content was migrated from a separate learning repo and customized here for the STSA 2026 cohort.

The primary goal is **deep conceptual and practical understanding**, not production deployment.

---

## ⚠️ Disclaimer (Important)

- This repository is **strictly for educational and self-learning purposes**.
- It is **not intended for production use**, commercial deployment, or benchmarking against state-of-the-art models.
- The implementations may:
  - Be simplified for clarity
  - Omit optimizations required for large-scale or distributed training
  - Differ from industry-grade or research-grade LLM systems
- Any mistakes, deviations, or interpretations are **entirely my own**.

This repository is **not affiliated with or endorsed by the author or publisher** of the referenced book.

If you are seeking **production-ready LLMs**, **enterprise AI systems**, or **large-scale training pipelines**, this repository is **not suitable**.

---

## 🎯 Objectives

Through this repository, I aim to:

- Understand the fundamentals of **language modeling**
- Implement **tokenization**, **self-attention**, and **transformer blocks**
- Build a **GPT-like architecture** incrementally
- Learn how **pretraining and finetuning** work in practice
- Develop intuition around **training dynamics**, optimization, and failure modes
- Build the capability to **read, analyze, and reason about modern LLM research papers**

---

## 📚 Learning Source & Attribution

This repository is **inspired by and conceptually derived from** the book:

> **Build a Large Language Model (From Scratch)**  
> *Sebastian Raschka*

The official book and reference materials are available here:  
<https://amzn.to/4fqvn0D>

All implementations in this repository are **independent re-implementations** created for learning purposes.  
While the learning flow, architectural ideas, and concepts follow the book, the code, experiments, and explanations here are my own.

---

## 🧠 Learning Philosophy

- No “black-box” abstractions
- Minimal reliance on high-level frameworks
- Strong emphasis on:
  - Mathematical intuition
  - Code-level transparency
  - Experimental learning (breaking, modifying, and fixing models)
- Every major component should be explainable in terms of:
  - *Why it exists*
  - *What problem it solves*
  - *What trade-offs it introduces*

---

## 🛠️ Setup & Installation

This project uses **[uv](https://github.com/astral-sh/uv)** for fast Python package management.

### 1. Install `uv`
Follow the [official installation guide](https://docs.astral.sh/uv/getting-started/installation/) if you haven't already.

### 2. Initialize Project (Only If Starting Fresh)
If you are creating a brand-new repo, initialize `pyproject.toml` with:
```bash
uv init
```
This repository already includes `pyproject.toml`, so you can skip this step here.

### 3. Sync Dependencies

| Group | What it includes | When to install |
|:------|:----------------|:----------------|
| *(base)* | `numpy`, `torch`, `tiktoken` | Always — core learning dependencies |
| `dev` | pytest, black, isort, flake8, jupyter, ipykernel, matplotlib, nbformat | Recommended for all development and notebook work |
| `tools` | pypdf, pymupdf, python-pptx | Only if using extraction scripts in `tools/pyscripts/` |
| `bpe-experiments` | transformers, requests, tqdm | Only if running BPE comparison experiments (ch02 bonus) |

```powershell
# 1. Install base runtime dependencies only
uv sync

# 2. Install dev tools (recommended — needed for tests, notebooks, CI)
uv sync --group dev

# 3. Install tools group (only if using PDF/PPTX extraction scripts)
uv sync --group dev --group tools

# 4. Install BPE experiments group (only for ch02 bonus BPE notebooks)
uv sync --group dev --group bpe-experiments

# 5. Install everything at once
uv sync --group dev --group tools --group bpe-experiments

# 6. Install ALL groups (shorthand — equivalent to option 5)
uv sync --all-groups

# 7. Troubleshooting: Use copy mode if you see "Failed to hardlink files"
uv sync --link-mode=copy
```

### 4. Run Commands (No Activation Needed)
```bash
uv run pytest
```

### 5. Activate Environment (Optional)
```bash
# Windows (PowerShell)
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate
```

### 6. Useful `uv` Commands
```bash
# Add a runtime dependency
uv add numpy

# Add a dev dependency
uv add --group dev pytest

# Remove a dependency
uv remove numpy
```

---

## Prerequisites (Be Honest With Yourself)

This repository assumes **foundational competency** in mathematics and programming.  
If any of the areas below feel weak or unfamiliar, it is strongly recommended to **pause and reinforce them before progressing further**.

This project intentionally avoids high-level abstractions; a weak foundation will lead to confusion later—especially when implementing attention mechanisms, backpropagation, and training loops from scratch.

---

### Mathematics

You should be reasonably comfortable with the following concepts.

#### Linear Algebra

- Vectors and matrices
- Matrix multiplication and dot products
- Transpose and basic matrix shapes
- Understanding embeddings as vectors in high-dimensional space

You should be able to answer:

- What does a matrix–vector multiplication represent?
- Why are embeddings stored and manipulated as matrices?

---

#### Probability & Information Theory

- Probability distributions
- Entropy and cross-entropy loss
- Softmax function and its role in normalization
- Log-likelihood and negative log-likelihood

You should be able to answer:

- Why is cross-entropy used for language modeling?
- What problem does softmax solve?

---

#### Calculus (Conceptual Level)

- Gradients and partial derivatives (intuition over formal proofs)
- Chain rule and gradient flow through layers
- High-level understanding of backpropagation

You should be able to answer:

- What does it mean to minimize a loss function?
- How does an error signal update model parameters?

---

### Programming

#### Python

- Strong proficiency with:
  - Functions and classes
  - Loops and conditionals
  - List and dictionary comprehensions
  - Reading and debugging unfamiliar code

You should be able to:

- Trace data flow across multiple function calls
- Modify and extend an existing codebase confidently

---

#### PyTorch Fundamentals

- Tensors and tensor shapes
- Broadcasting rules
- Autograd and gradient computation
- Loss functions and optimizers
- Basic model training loops

You should be able to answer:

- What does `requires_grad=True` do?
- What happens during `loss.backward()`?
- When and why are gradients cleared?

---

### ⚠️ Recommendation

If **two or more areas** above feel uncomfortable:

> **Slow down. Reinforce first. Then proceed.**

A solid foundation will significantly improve comprehension of:

- Self-attention
- Transformer internals
- Training stability and optimization behavior

---

## 🗂️ Repository Structure (Current)

```text
.
├── examples/           # Synthesized practice scripts (ch02, ch03, ch04)
├── notebooks/          # Synthesized learning notebooks (ch02, ch03, ch04)
├── reading-notes/      # Synthesized theory notes (ch01–ch04)
├── source-material/    # READ-ONLY staging area (raw author content)
├── src/                # Reusable Python modules (GPT components)
├── tests/              # Pytest smoke tests and unit tests
├── tools/              # Utility scripts (PDF/PPTX extraction)
├── docs/               # Study plans, structure docs, reviews, reference
├── README.md           # This file
└── LICENSE
```

For a detailed breakdown and the target layout, see [docs/01_repository-structure.md](docs/01_repository-structure.md).

---

## 🚀 Expected Outcomes

By completing this repository, I expect to be able to:

- Implement a GPT-style LLM from scratch
- Explain **self-attention and transformers** both intuitively and mathematically
- Diagnose and reason about training failures and instabilities
- Make informed architectural and optimization decisions
- Confidently transition to advanced topics such as:
  - Scaling laws
  - Efficient training techniques
  - Model compression
  - Inference optimization

---

## 🤝 Contributing (forks / collaborators)

- **Figures**: No hotlinked or copied book images — text placeholders or your own diagrams only. See [CONTRIBUTING.md](CONTRIBUTING.md).
- **Notebooks**: Prefer **cleared outputs** before commit (avoids huge binary blobs in git). Details in [CONTRIBUTING.md](CONTRIBUTING.md).

## 📌 Notes

- This repository will evolve iteratively.
- Code clarity is prioritized over raw performance.
- Experiments may intentionally remain small-scale due to hardware constraints.

---

## 📖 Citation

If you use or reference ideas from this repository, please also cite the original source:

> Raschka, Sebastian. *Build a Large Language Model (From Scratch)*.

---

## 🙏 Acknowledgments

- Sincere thanks to **Sebastian Raschka** for authoring the foundational book and providing a clear, principled learning framework.
- Appreciation to the open-source community for the tools and libraries that make deep learning education accessible.
