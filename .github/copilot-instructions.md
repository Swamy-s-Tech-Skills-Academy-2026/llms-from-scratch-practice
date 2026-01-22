# Copilot Instructions (STSA 2026)

**Version**: 1.2  
**Last Updated**: January 22, 2026  
**Environment**: Windows, PowerShell, Python 3.12+, Jupyter Notebooks  
**Note**: All commands and scripts should use PowerShell syntax. File paths use Windows format.

This repository is a **learning workspace** for building a GPT-style LLM from scratch.
Please follow these guidelines when generating or modifying code and docs:

- **Educational first**: Prioritize clarity, correctness, and explainability over performance.
- **From scratch mindset**: Avoid heavy abstractions; keep logic explicit and inspectable.
- **Small, focused changes**: Make minimal edits that are easy to review.
- **Document intent**: Update docs when structure, behavior, or learning flow changes.
- **Avoid production framing**: This is not a deployment-ready repo.
- **Respect attribution**: Keep references to the book where appropriate.
- **Simple stack**: Prefer plain Python and PyTorch fundamentals.

## Code Style Guidelines

### Python Code
- **Follow PEP 8** style guide
- **Meaningful variable names**: Use descriptive names (e.g., `token_embeddings` instead of `te`, `attention_weights` instead of `aw`)
- **Type hints**: Use type hints where appropriate, especially in `src/` modules
- **Comments**: Comment liberally to explain the *why* of the operation, not just the *how* of the Python code
- **No hardcoded paths**: Use `pathlib` or relative paths

### Code Comments Philosophy
- Explain the **conceptual reason** for the operation (e.g., "We normalize here to prevent gradient explosion")
- Explain the **mathematical mapping** (e.g., "`mu` represents the population mean in this distribution")
- Not just syntax explanation (avoid: "This creates a list")

## Notebook Guidelines

- **Structure**: Use clear headers and logical flow (Import → Load Data → Process → Analyze → Visualize → Conclusion)
- **Markdown Cells**: Explain the concept before writing code
- **Math Notation**: Use LaTeX for mathematical expressions (e.g., `$P(x|y) = \frac{P(y|x)P(x)}{P(y)}$`)
- **Reproducibility**: Set random seeds for reproducible results (`np.random.seed(42)`, `torch.manual_seed(42)`)
- **Visualizations**: Include titles, labels, and legends for all plots
- **Testing**: Ensure "Restart Kernel & Run All" passes without errors
- **No Hidden State**: Avoid variables defined in deleted cells
- **Sequential Execution**: Ensure all cells run sequentially without errors

## Source Material Handling (CRITICAL)

The `source-material/` folder is a **READ-ONLY staging area** for raw author content:

### 🚫 NEVER:
- Modify, overwrite, or delete any file in `source-material/`
- Copy-paste directly from `source-material/` into notebooks or docs
- Treat `source-material/` as a working directory

### ✅ ALWAYS:
- Read from `source-material/` to understand concepts
- **Synthesize content in your own words** before publishing
- Publish synthesized content to educational folders (`notebooks/`, `docs/reading-notes/`, `docs/`)
- Add citations when referencing specific definitions, theorems, or concepts
- Apply zero-copy policy during both creation and review

### Migration Workflow:
1. **Read** from `source-material/` (transcripts, PDFs, scratch notes)
2. **Synthesize** - write in your own words (DO NOT copy-paste)
3. **Publish** to educational folders (`notebooks/`, `docs/reading-notes/`, etc.)
4. **Cite** when relying on specific sources

See `.cursor/rules/08_source-material-rules.mdc` for complete guidelines.

## Documentation Location Standards

- **Review reports**: All code review, notebook review, and fix summary reports MUST be created in `docs/reviews/`
- **Reference materials**: General reference docs (git, PowerShell, Python commands) go in `docs/reference/`
- **Study plans**: Learning roadmaps and study guides go in `docs/`
- **Reading notes**: Synthesized study notes go in `docs/reading-notes/`
- **Never create review documentation in the root directory**

## Quality Assurance Checklist

### Python Scripts (`src/`)
- [ ] Follows PEP 8 style guide
- [ ] Type hints used for function arguments and return types
- [ ] Docstrings included for all functions and classes
- [ ] No hardcoded paths (use `pathlib` or relative paths)
- [ ] All imports properly organized (stdlib → third-party → local)

### Jupyter Notebooks (`notebooks/`)
- [ ] **"Restart Kernel & Run All"** passes without errors
- [ ] Logical flow: Import → Load Data → Process → Analyze → Visualize → Conclusion
- [ ] No hidden state (all variables defined in currently existing cells)
- [ ] Markdown cells clearly explain concepts before code
- [ ] All visualizations have titles, axis labels, and legends
- [ ] Random seeds set for reproducibility (`torch.manual_seed(42)`, `np.random.seed(42)`)

### Content Review (Zero-Copy Policy)
- [ ] **Originality Check**: Content is synthesized, not copied from source material
- [ ] **Citation**: Specific definitions, theorems, and formulas are cited
- [ ] **Understanding**: Content demonstrates comprehension, not just rephrasing

## 🚀 Environment Setup

**Python Environment (Windows PowerShell):**
```powershell
# Navigate to project
cd D:\STSA-2026\llms-from-scratch-practice

# Sync dependencies (creates .venv automatically)
uv sync --group dev

# Activate virtual environment (optional - uv run works without activation)
.venv\Scripts\Activate.ps1

# Run commands without activation
uv run pytest
uv run jupyter lab
```

**Jupyter Notebooks:**
```powershell
# Launch Jupyter Lab
uv run jupyter lab

# Or Jupyter Notebook
uv run jupyter notebook
```

## 🧠 Prompt Engineering Tips

When asking Copilot for help:
- **Specify concepts clearly**: "Explain how self-attention works in transformers"
- **Request specific implementations**: "Implement tokenization using regex patterns"
- **Ask for mathematical explanations**: "Explain the attention mechanism using LaTeX formulas"
- **Request educational code**: "Write well-commented code that explains each step"
- **Specify libraries**: "Implement using PyTorch tensors and operations"

## Project Focus

- **Mathematical Accuracy**: Ensure all formulas and mathematical interpretations are correct
- **Code Quality**: Use clear, well-commented Python code with meaningful variable names
- **Visualization**: Use Matplotlib for clear visualizations of model behavior, attention patterns, etc.
- **Educational Value**: Every code block should teach something about LLM internals
