# S.M.A.R.T. Prompt Framework for GitHub Copilot Coding Agents

**LLMs From Scratch Practice Edition**

This guide is for writing useful coding-agent prompts for this repository.

## Purpose

Use prompts that keep work aligned with the actual repository:

- educational, not production-oriented
- Python-first, notebook-aware, Windows PowerShell-friendly
- grounded in the repo's current structure
- strict about zero-copy from `source-material/`

## The S.M.A.R.T. Framework

```text
S - Specific Role Definition
M - Mission-Critical Requirements
A - Audience-Aware Communication
R - Response Format Control
T - Task-Oriented Constraints
```

## Repo-Specific Interpretation

### Specific Role Definition

Choose a role that fits the repo, for example:

- Python learning-workspace maintainer
- notebook reviewer for LLM fundamentals
- educational content editor for study notes
- transformer implementation reviewer

Avoid roles tied to nonexistent stacks such as frontend engineer, Flask API architect, or cloud integration specialist unless the repo actually grows in that direction.

### Mission-Critical Requirements

State exactly what must change.

Good examples:

- align a Chapter 4 example script with the reusable `src/model/` implementation
- review a notebook for zero-copy risks and rewrite copied content in learner-owned form
- add tests for a new model utility in `src/`
- ensure a chapter topic has matching note, notebook, and example coverage

### Audience-Aware Communication

Assume the audience is learning LLM internals.

Prompts should prefer:

- explicit reasoning over abstraction
- meaningful names over shorthand
- educational comments only when they add conceptual value
- first-person learning voice in notes and notebook markdown when writing learner-facing material

### Response Format Control

Ask for outputs that fit this repo:

- small patches
- clear validation steps
- concise file-by-file reasoning only when needed
- repo-specific checks such as `uv run pytest`, markdown validation, or notebook review notes

### Task-Oriented Constraints

Include the constraints that matter here:

- `source-material/` is read-only
- zero-copy policy is mandatory
- use PowerShell examples
- preserve chapter structure and numbering
- avoid unrelated stack assumptions
- keep edits easy to review

## Prompt Template

```markdown
ROLE:
You are a [repo-appropriate role].

MISSION:
[One or two sentences stating the exact outcome.]

CONTEXT:
- Topic: [chapter, notebook, example, or module]
- Files in scope: [specific paths]
- Current issue: [bug, mismatch, redundancy, zero-copy concern, missing coverage]

CONSTRAINTS:
- `source-material/` is read-only
- zero-copy policy is mandatory
- use Windows PowerShell commands
- preserve the repo's educational tone and structure

SUCCESS CRITERIA:
- [measurable check 1]
- [measurable check 2]
- [measurable check 3]

VALIDATION:
- `uv run pytest`
- any file-specific or notebook-specific verification needed
```

## Good Prompt Patterns

### For Code Tasks

Use prompts like:

- "Refactor `src/model/ch04_variants.py` for clarity without changing behavior, then run the existing Python checks."
- "Add focused tests for a new GPT utility and keep the implementation learner-readable."
- "Review Chapter 4 reusable modules for style and CI issues only; do not expand scope into notebooks."

### For Notebook Tasks

Use prompts like:

- "Check this notebook for hidden state, copied source-material cells, and missing markdown explanation."
- "Rewrite the notebook cell content in learner-owned wording while preserving the same concept and output."
- "Keep code explicit and inspectable; avoid turning the notebook into a library abstraction layer."

### For Documentation Tasks

Use prompts like:

- "Rewrite this note in Swamy's first-person learning voice."
- "Remove production framing and keep the explanation focused on intuition and revision."
- "Update the doc so it reflects the current repo structure and command set."

## Bad Prompt Patterns

Avoid prompts like:

- "Build the backend and frontend for this project"
- "Apply enterprise N-tier best practices to the app"
- "Integrate JWT auth and REST APIs"
- "Add cloud deployment guidance" 

Those instructions do not fit this repository.

## Validation Guidance

When prompts involve code or structural edits, prefer checks already used by this repo:

```powershell
uv run pytest
uv run black --check --diff src
uv run isort --check-only --diff src
uv run flake8 src --count --max-complexity=10 --max-line-length=100 --statistics
./tools/psscripts/Verify-ZeroCopy.ps1
```

Use only the checks relevant to the task.

## Quality Checklist

Before using a prompt, make sure it:

- names the real files and folders in this repo
- does not assume nonexistent architecture layers
- explicitly respects zero-copy rules
- defines what success looks like
- asks for validation that can actually be run here
- matches the repo's educational purpose

## Summary

A good prompt for this repo is concrete, chapter-aware, zero-copy-safe, and educationally useful.

A bad prompt imports assumptions from unrelated projects and sends the agent toward work that does not belong in this workspace.
