# LLMs From Scratch Practice Task Prompt

## Context

You are working in **LLMs From Scratch Practice**, a learner-owned repository for building intuition about GPT-style language models from first principles.

This repository is not a web app and not a production system. The main assets are:

- `reading-notes/` for theory written in Swamy's first-person learning voice
- `notebooks/` for interactive implementations and experiments
- `examples/` for runnable practice scripts
- `src/` for reusable Python modules
- `source-material/` for read-only raw reference material

## Primary Objective

Complete the requested task while preserving the repository's educational goals:

- clarity over cleverness
- explicit logic over abstraction
- learner-owned synthesis over copy-paste
- small, reviewable changes over broad rewrites

## Mandatory Repository Rules

### Zero-Copy Policy

- `source-material/` is read-only
- do not copy text, code, or notebook content directly from `source-material/`
- if content is inspired by source material, rewrite it in original words and structure
- citations are acceptable when referring to concepts, but published content must be transformative

### Three-Layer Alignment

When a topic is introduced or updated, keep the learning layers aligned when applicable:

- theory: `reading-notes/`
- implementation: `notebooks/`
- practice: `examples/`

### Environment Expectations

- use Windows PowerShell examples
- use Python 3.12+
- prefer `uv` commands for setup and execution
- treat notebook execution state carefully and avoid hidden-state assumptions

## Task Execution Checklist

For any substantial task, verify the following where relevant:

1. The content matches the actual repository structure and purpose.
2. The writing sounds like personal learning notes instead of courseware or product documentation.
3. No content was copied from `source-material/`.
4. Any code in `src/` follows PEP 8 and uses meaningful names.
5. Any notebook changes preserve a readable teaching flow.
6. Any tests or validation steps relevant to the change are run.

## Review Focus Areas

When reviewing files, prioritize:

- technical correctness
- educational clarity
- repo-structure consistency
- zero-copy compliance
- alignment between notes, notebooks, examples, and reusable code
- CI safety for tracked checks

## Output Requirements

When reporting findings or progress:

- be concrete about file paths and problems
- separate confirmed issues from assumptions or tooling noise
- prefer actionable fixes over abstract commentary
- if a check was not run, say so explicitly

## Example Task Framing

Use this structure when preparing a repo-specific task for a coding agent:

```markdown
ROLE: You are a Python learning-workspace maintainer focused on educational clarity and repo hygiene.

MISSION: [State the exact task in one or two sentences.]

CONTEXT:
- Topic area: [chapter or feature]
- Affected layers: [reading-notes / notebooks / examples / src]
- Constraints: [zero-copy, Windows PowerShell, learner voice, etc.]

SUCCESS CRITERIA:
- [specific measurable check 1]
- [specific measurable check 2]
- [specific measurable check 3]

VALIDATION:
- `uv run pytest`
- any notebook or file-specific verification needed for the task
```

## What To Avoid

- do not introduce unrelated stacks or product assumptions
- do not describe nonexistent frontend, backend, database, or cloud layers
- do not rewrite large sections of the repo unless the task requires it
- do not treat source-material as publishable output
