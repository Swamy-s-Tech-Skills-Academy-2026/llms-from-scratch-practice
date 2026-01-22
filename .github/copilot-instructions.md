# Copilot Instructions (STSA 2026)

This repository is a **learning workspace** for building a GPT-style LLM from scratch.
Please follow these guidelines when generating or modifying code and docs:

- **Educational first**: Prioritize clarity, correctness, and explainability over performance.
- **From scratch mindset**: Avoid heavy abstractions; keep logic explicit and inspectable.
- **Small, focused changes**: Make minimal edits that are easy to review.
- **Document intent**: Update docs when structure, behavior, or learning flow changes.
- **Avoid production framing**: This is not a deployment-ready repo.
- **Respect attribution**: Keep references to the book where appropriate.
- **Simple stack**: Prefer plain Python and PyTorch fundamentals.

## Notebook Guidelines

- **Structure**: Use clear headers and logical flow (Import → Load Data → Process → Analyze → Visualize)
- **Markdown Cells**: Explain the concept before writing code
- **Math Notation**: Use LaTeX for mathematical expressions (e.g., `$P(x|y) = \frac{P(y|x)P(x)}{P(y)}$`)
- **Reproducibility**: Set random seeds for reproducible results (`np.random.seed(42)`, `torch.manual_seed(42)`)
- **Visualizations**: Include titles, labels, and legends for all plots
- **Testing**: Ensure "Restart Kernel & Run All" passes without errors
- **No Hidden State**: Avoid variables defined in deleted cells

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
