# Reference Documentation

**Project**: LLMs From Scratch Practice (STSA 2026)  
**Purpose**: Quick reference guides for commands and workflows used in this repo  
**Last Updated**: January 22, 2026

---

## 📚 Available Reference Documents

| Document | Purpose | Key Topics |
|----------|---------|------------|
| [Git Commands](git-commands-reference.md) | Version control | Status, commits, branches, remotes |
| [Python Commands](python-commands-reference.md) | Python development | uv, venv, pytest, formatting |
| [PowerShell Commands](powershell-commands-reference.md) | Windows shell basics | File ops, search, env vars |
| [Troubleshooting Guide](troubleshooting-guide.md) | Common issues | uv, Python, pytest, paths |

---

## 🎯 Quick Navigation

**Set up environment:**
- → [Python Commands - uv](python-commands-reference.md#using-uv)

**Run tests:**
- → [Python Commands - pytest](python-commands-reference.md#testing-pytest)

**Format code:**
- → [Python Commands - Formatting](python-commands-reference.md#code-formatting)

**Troubleshoot uv/Python:**
- → [Troubleshooting Guide](troubleshooting-guide.md)

---

## 🚀 Common Workflows

### 1. First-Time Setup
```powershell
cd D:\STSA-2026\llms-from-scratch-practice
uv sync --group dev
```

### 2. Run Tests
```powershell
uv run pytest
```

### 3. Format Code
```powershell
uv run black .
uv run isort .
```

