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

## 🎯 Repository Purpose

This repo is for building intuition by implementing a GPT-style model step-by-step.

## 🧱 Three-Layer Learning Architecture (REQUIRED)

For each topic/algorithm, create and keep three aligned artifacts:

- **Theory**: Reading notes in `docs/reading-notes/` with local numbering and the algorithm name.
- **Implementation**: Notebook in `notebooks/` with the matching algorithm name and a `-implementation` suffix.
- **Practice**: Examples in `examples/` with the matching algorithm name and a `-examples` suffix.

**Numbering rule**: Use local sequence numbering (`01`, `02`, …) within each folder, and keep the three files aligned per topic.

### What This Repository Provides

- **Structured Learning Material**: Notes on tokenization, attention, transformers, and training
- **Python Implementations**: LLM concepts implemented using PyTorch from scratch
- **Hands-on Practice**: Chapter-by-chapter notebooks for interactive learning
- **Reusable Code**: Modular implementations in `src/` for building components

### Repository Structure by Purpose

- **`docs/reading-notes/`**: Theory (Textbook style) - Synthesized study notes
- **`notebooks/`**: Simulation (Lab style) - Hands-on experiments chapter-by-chapter
- **`src/`**: Reusable Code - Modular implementations (tokenization, model, training)
- **`source-material/`**: Staging area for raw content (Read-Only)

## Target Audience

- Learners practicing LLM fundamentals (tokenization → embeddings → attention → training loops)
- Anyone prioritizing correctness and clarity over production optimizations

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

## 🎓 Learning Tone & Voice (Swamy's Style)

When writing notebooks and learning notes, use **Swamy's personal learning tone**:

### First-Person Voice
- Use "I'm learning...", "I'm revising...", "I want to be able to..."
- Write as personal notes, not formal instruction
- Example: "I'm building intuition for attention by working through this example"

### Reflection-Oriented
- Include intent, confusion, or takeaways
- Use phrases like "I noticed...", "I still need to...", "My takeaway:..."
- Acknowledge gaps or areas needing more practice
- Example: "I noticed I confuse embeddings with encodings, so I'm writing this down"

### Personal Journey, Not Instruction
- Prefer "my notes", "my understanding", "my revision"
- **Avoid lecturer/course framing**: Never say "this course" or "the instructor"
- Write as if documenting your own learning process
- Example: "My understanding: tokenization splits text, but I need to practice BPE more"

### Style Guidelines
- **Keep it concise and honest**: Acknowledge what you don't know yet
- **Use simple, clear language**: Avoid formal teaching tone
- **Show learning process**: Include confusion, realizations, and next steps
- **Be authentic**: Write as you're actually learning, not teaching

### Example Phrasing
- ✅ "I'm building intuition for self-attention by implementing it step-by-step"
- ✅ "I noticed I mix up query and key roles, so I'm clarifying this here"
- ✅ "My takeaway: layer normalization stabilizes training, but I need to understand why"
- ✅ "I still need to practice backpropagation through attention - adding this to my revision list"
- ❌ "This course teaches attention mechanisms" (too formal, lecturer tone)
- ❌ "The instructor explains that..." (course framing)
- ❌ "We will learn about..." (instructional, not personal)

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
