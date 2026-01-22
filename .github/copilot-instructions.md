# GitHub Copilot Instructions for "Build a Large Language Model (From Scratch)"

**Version**: 1.0  
**Last Updated**: January 21, 2026  
**Repository**: `LLMs-from-scratch-practice`

**Environment**: Windows, PowerShell  
**Note**: All commands and scripts should use PowerShell syntax. File paths use Windows format.

---

## 🎯 Repository Purpose

**Build a Large Language Model (From Scratch)** is an educational repository documenting the hands-on implementation of a GPT-style LLM from first principles, based on Sebastian Raschka's book.

### What This Repository Provides
- **Core Implementation**: Manual implementation of Tokenization, Attention, and Transformer Blocks.
- **Educational Clarity**: Code optimized for readability and conceptual understanding over raw performance.
- **From-Scratch Philosophy**: Minimal reliance on external libraries; "no magic" frameworks.

### Target Audience
- Learners seeking deep understanding of LLM internals.
- Engineers moving from using APIs to understanding architectures.

---

## 📁 Repository Structure

> **📖 Single Source of Truth**: For complete and up-to-date repository structure, see [docs/01_repository-structure.md](../docs/01_repository-structure.md)

**Quick Reference:**

- `src/config/` - Model and Training configurations
- `src/tokenization/` - BPE, Vocabulary, Tokenizer logic
- `src/model/` - Neural network architecture (Embeddings, Attention, GPT Blocks)
- `src/training/` - Training loops, loss functions, optimization logic
- `src/evaluation/` - Metrics and generation scripts
- `src/utils/` - Logging, seeding, checkpoints
- `src/main.py` - Main entry point
- `data/` - Raw and processed datasets
- `notebooks/` - Exploratory notebooks and experiments
- `docs/` - Project documentation and study plans

---

## 🔧 Development Guidelines

### Zero-Copy Policy
- All code must be original and written to maximize understanding.
- Avoid copying complex blocks without analyzing them line-by-line.
- Comments should explain the *concept*, not just the syntax.

### Project Focus & Philosophy
1.  **From Principles**: Avoid high-level abstractions like `transformers.Trainer` or `accelerate`. We implement the "magic" ourselves.
2.  **Educational Clarity**: Code should be readable and educational first, optimized second.
3.  **Explain "Why"**: When generating code, briefly explain the *concept* behind it (e.g., "We use `tril` here to implement causal masking so tokens can't attend to the future").

### Constraints (CRITICAL)
- **Forbidden Character**: **NEVER** use the replacement character "" (U+FFFD) in any output, file, comment, or documentation. Ensure all text is properly encoded (UTF-8).
- **No Magic**: Do not use pre-built models from `huggingface/transformers` for the *core implementation*. We are building the architecture manually.

### Code Quality Standards
- **Python**: Use modern Python (3.10+) features.
- **Type Hinting**: Always use type hints (`def func(x: Tensor) -> Tensor:`).
- **Docstrings**: Include clear docstrings explaining inputs. **CRITICAL: Document Tensor Shapes** (e.g., `Shape: (batch_size, seq_len, d_model)`).
- **PyTorch**: Use `torch` for tensor operations.

### File Naming
- **Python Modules**: Use lowercase with underscores: `transformer_block.py`, `multi_head_attention.py`
- **Classes**: Use PascalCase: `GPTModel`, `CausalSelfAttention`
- **Variables**: Use snake_case with descriptive names: `batch_size`, `token_embeddings`

### Integration Standards
- **Imports**: Logical grouping (Standard lib -> Third party -> Local).
- **No Circular Imports**: Keep module dependencies clean (e.g., `model` imports `config`, but `config` does not import `model`).

---

## 🧠 Workflow & Study Plan

### Recommended Workflow
1.  **Understand**: Read the concept in the book or documentation.
2.  **Explore**: Use `notebooks/` to prototype small components.
3.  **Implement**: Move hardened logic into `src/` (e.g., `model/` or `tokenization/`) as reusable modules.
4.  **Verify**: Write simple assertions or tests to verify shapes and outputs.

### Running Code
- **Scripts**: Run modules as scripts using the `-m` flag to resolve imports correctly.
  ```powershell
  python -m training.trainer
  ```

---

## 📞 Support

- **Documentation**: See `docs/` for study plans and structure guides.
- **Issues**: If you encounter a divergence/instability in training, check `docs/study_plan.md` for troubleshooting checkpoints.
