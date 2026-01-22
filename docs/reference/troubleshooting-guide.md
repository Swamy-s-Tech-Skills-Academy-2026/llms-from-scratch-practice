# Troubleshooting Guide

**Project**: LLMs From Scratch Practice (STSA 2026)  
**Purpose**: Common setup and runtime issues

---

## Issue 1: `uv` not found

**Symptoms:**
```
uv: command not found
```

**Fix (Windows PowerShell):**
```powershell
irm https://astral.sh/uv/install.ps1 | iex
uv --version
```

---

## Issue 2: Wrong Python Version

**Symptoms:**
```
ERROR: Python 3.12+ is required
```

**Fix:**
```powershell
python --version
py -3.12 --version
```

---

## Issue 3: Missing Dependencies

**Symptoms:**
```
ModuleNotFoundError: No module named 'torch'
```

**Fix:**
```powershell
cd D:\STSA-2026\llms-from-scratch-practice
uv sync --group dev
```

---

## Issue 4: Import Errors During Tests

**Symptoms:**
```
ImportError: attempted relative import with no known parent package
```

**Fix:**
```powershell
uv run pytest
```

---

## Issue 5: Reset the Virtual Environment

**Use when dependencies are corrupted or out of sync.**

```powershell
cd D:\STSA-2026\llms-from-scratch-practice
Remove-Item -Recurse -Force .venv
uv sync --group dev
```

