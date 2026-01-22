# Python Commands Reference

**Project**: LLMs From Scratch Practice (STSA 2026)  
**Purpose**: Python, uv, pytest, and formatting commands used in this repo

---

## 📦 Using uv

```powershell
# Initialize a new project (creates pyproject.toml)
uv init

# Create .venv and install dependencies
uv sync

# Include dev dependencies
uv sync --group dev

# Run a command without activating the venv
uv run pytest

# Add or remove dependencies
uv add numpy
uv add --group dev pytest
uv remove numpy
```

---

## 🧪 Testing (pytest)

```powershell
# Run all tests
uv run pytest

# Verbose
uv run pytest -v

# Run a single file
uv run pytest tests/test_tokenizer.py
```

---

## 🎨 Code Formatting

```powershell
# Format with Black
uv run black .

# Sort imports
uv run isort .

# Lint (if configured)
uv run flake8 .
```

---

## 🧠 Notebooks

```powershell
# Launch Jupyter
uv run jupyter lab
```

---

## 🧰 Python Version Checks

```powershell
python --version
uv run python --version
```

