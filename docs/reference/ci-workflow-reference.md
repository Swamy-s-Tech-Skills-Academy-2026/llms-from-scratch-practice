# CI/CD Workflow Reference

<!-- markdownlint-disable MD031 MD032 MD040 MD012 -->

**Project**: GenAI Email & Report Drafting System  
**Date**: January 15, 2026  
**Purpose**: Continuous Integration workflow commands and troubleshooting

---

## 📋 Table of Contents

1. [GitHub Actions CI Workflow](#github-actions-ci-workflow)
2. [Local CI Validation](#local-ci-validation)
3. [Common CI Failures](#common-ci-failures)
4. [Troubleshooting Guide](#troubleshooting-guide)
5. [Quick Reference](#quick-reference)

---

## 🔄 GitHub Actions CI Workflow

### Workflow File Location

`.github/workflows/lint-and-test.yml`

### Workflow Steps

The CI workflow runs automatically on:
- Every push to any branch
- Every pull request to `main` branch

**Steps:**
1. ✅ Checkout repository
2. ✅ Set up Python 3.12
3. ✅ Install dependencies from `requirements.txt`
4. ✅ Lint with flake8 (syntax & style)
5. ✅ Check formatting with Black
6. ✅ Check import sorting with isort
7. ✅ Run tests with pytest and coverage

---

## 🧪 Local CI Validation

### Complete Local Validation Script

Run these commands **before pushing** to ensure CI passes:

```powershell
# Navigate to backend directory
cd D:\SrivariHSSPL-2026\genai-email-report-drafting\src\backend

# Ensure virtual environment is activated
.venv\Scripts\Activate.ps1

# Step 1: Check critical syntax errors (E9, F63, F7, F82)
Write-Host "🔍 Checking for syntax errors..." -ForegroundColor Cyan
python -m flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

# Step 2: Check code style (line length, complexity)
Write-Host "🔍 Checking code style..." -ForegroundColor Cyan
python -m flake8 . --count --max-complexity=10 --max-line-length=120 --statistics

# Step 3: Check Black formatting
Write-Host "🎨 Checking Black formatting..." -ForegroundColor Cyan
python -m black --check .

# Step 4: Check isort import sorting
Write-Host "📋 Checking import sorting..." -ForegroundColor Cyan
python -m isort --check-only .

# Step 5: Run full test suite
Write-Host "🧪 Running test suite..." -ForegroundColor Cyan
pytest tests/ -v --cov=. --cov-report=term-missing

Write-Host "✅ All CI checks passed!" -ForegroundColor Green
```

### One-Command Validation

```powershell
# All checks in single command (fails fast)
python -m flake8 . --count --select=E9,F63,F7,F82 && python -m flake8 . --count --max-complexity=10 --max-line-length=120 && python -m black --check . && python -m isort --check-only . && pytest tests/ -v --cov=. --cov-report=term-missing
```

---

## 🚨 Common CI Failures

### 1. Flake8 E501: Line Too Long

**Error:**
```
./services/gemini_service.py:235:121: E501 line too long (146 > 120 characters)
```

**Fix:**
```python
# ❌ Before (line too long)
user_message = "Google Gemini AI blocked the prompt due to safety filters. Please rephrase your request with different wording."

# ✅ After (multi-line string)
user_message = (
    "Google Gemini AI blocked the prompt due to safety filters. "
    "Please rephrase your request with different wording."
)
```

**Validate Fix:**
```powershell
python -m flake8 services/gemini_service.py
# Expected output: (no output = success)
```

---

### 2. Black Formatting Issues

**Error:**
```
would reformat services/gemini_service.py
Oh no! 💥 💔 💥
1 file would be reformatted, 28 files would be left unchanged.
```

**Fix:**
```powershell
# Apply Black formatting
python -m black .

# Verify formatting
python -m black --check .
# Expected output: "All done! ✨ 🍰 ✨"
```

---

### 3. Import Sorting Issues

**Error:**
```
ERROR: services/gemini_service.py Imports are incorrectly sorted and/or formatted.
```

**Fix:**
```powershell
# Apply isort
python -m isort .

# Verify sorting
python -m isort --check-only .
# Expected output: (no output = success)
```

---

### 4. Test Failures Due to Missing Dependencies

**Error:**
```
ModuleNotFoundError: No module named 'flask_limiter'
```

**Fix:**
```powershell
# Ensure dependencies are installed in virtual environment
.venv\Scripts\python.exe -m pip install -r requirements.txt

# Verify installation
.venv\Scripts\python.exe -m pip show flask-limiter

# Run tests
pytest tests/ -v
```

**Root Cause:**
- Dependencies installed in system Python instead of virtual environment
- Virtual environment not activated
- Missing packages in `requirements.txt`

**Prevention:**
```powershell
# Always use venv Python explicitly
.venv\Scripts\python.exe -m pip install -r requirements.txt

# Or ensure venv is activated
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## 🛠️ Troubleshooting Guide

### Scenario 1: CI Passing Locally but Failing on GitHub

**Possible Causes:**
1. Different Python version (local: 3.12.10, CI: 3.12.x)
2. Different package versions (pip vs uv)
3. Platform differences (Windows local vs Linux CI)
4. Missing files in git (not committed)

**Solution:**
```powershell
# Check Python version matches CI
python --version  # Should be 3.12.x

# Verify requirements.txt is committed
git status

# Run exact CI commands locally
python -m flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
python -m flake8 . --count --max-complexity=10 --max-line-length=120 --statistics
python -m black --check .
python -m isort --check-only .
pytest tests/ -v --cov=. --cov-report=term-missing
```

---

### Scenario 2: Flake8 Reports Errors After Code Changes

**Diagnosis:**
```powershell
# Find specific violations
python -m flake8 . --show-source

# Check specific file
python -m flake8 services/gemini_service.py --show-source

# Count violations by type
python -m flake8 . --statistics
```

**Common Violations:**

| Code | Description | Fix |
|------|-------------|-----|
| E501 | Line too long (>120 chars) | Split into multi-line string/expression |
| E302 | Expected 2 blank lines | Add blank lines between functions |
| E303 | Too many blank lines | Remove extra blank lines |
| F401 | Unused import | Remove unused import |
| F841 | Unused variable | Remove or prefix with `_` |
| W503 | Line break before binary operator | Reformat expression |

---

### Scenario 3: Tests Pass Locally but Fail on CI

**Possible Causes:**
1. **Environment variables missing**: CI needs `.env` secrets configured in GitHub Settings
2. **Database connection**: CI uses test database, not local PostgreSQL
3. **File paths**: Windows paths (`\`) vs Linux paths (`/`)
4. **Timezone differences**: `datetime.utcnow()` may behave differently

**Solution:**
```powershell
# Check test isolation
pytest tests/ -v --tb=short

# Check for hardcoded paths
grep -r "D:\\" tests/
grep -r "C:\\" tests/

# Verify environment variables
pytest tests/ -v --showlocals

# Run with coverage to find missing test cases
pytest tests/ --cov=. --cov-report=term-missing
```

---

### Scenario 4: Black and isort Conflicts

**Issue:** Black reformats code, then isort breaks it

**Solution:** Configure isort to be Black-compatible

**pyproject.toml:**
```toml
[tool.isort]
profile = "black"
line_length = 120
multi_line_output = 3
include_trailing_comma = true
force_grid_wrap = 0
use_parentheses = true
ensure_newline_before_comments = true
```

**Verify compatibility:**
```powershell
# Apply both in order
python -m black .
python -m isort .

# Check both pass
python -m black --check .
python -m isort --check-only .
```

---

## 📊 Quick Reference

### ✅ Success Indicators

| Check | Success Output |
|-------|----------------|
| flake8 syntax | `0` (zero errors) |
| flake8 style | `0` (zero errors) |
| black --check | `All done! ✨ 🍰 ✨` |
| isort --check-only | (no output) |
| pytest | `131 passed, 93% coverage` |

### ⚠️ Warning Signs (Non-blocking)

- **DeprecationWarning**: `datetime.datetime.utcnow()` - Future Python versions will remove this
- **LegacyAPIWarning**: `Query.get()` - SQLAlchemy 2.0 recommends `Session.get()`
- **pytest-asyncio**: Unset fixture loop scope - Configure in `pyproject.toml`

These warnings don't fail CI but should be addressed in future updates.

---

### 🔧 Environment Setup Checklist

```powershell
# 1. Check Python version
python --version  # Should be 3.12.10

# 2. Verify virtual environment exists
Test-Path .venv  # Should return True

# 3. Activate virtual environment
.venv\Scripts\Activate.ps1

# 4. Install dependencies
pip install -r requirements.txt

# 5. Verify critical packages
pip show flask flask-limiter pytest flake8 black isort

# 6. Check .python-version file
Get-Content .python-version  # Should be 3.12.10

# 7. Run health check
pytest tests/smoke_test.py -v
```

---

### 📝 Pre-Push Checklist

Before pushing to GitHub:

- [ ] Virtual environment activated
- [ ] All dependencies installed
- [ ] Code formatted with Black
- [ ] Imports sorted with isort
- [ ] No flake8 violations
- [ ] All tests passing (131 tests)
- [ ] Coverage ≥90% (currently 93%)
- [ ] Changes committed to git
- [ ] Commit message follows conventions

**Quick validation:**
```powershell
# Run all checks
cd src/backend
python -m black . && python -m isort . && python -m flake8 . && pytest tests/ -v --cov=. --cov-report=term-missing

# If all pass, commit and push
git add .
git commit -m "Your commit message"
git push origin branch-name
```

---

### 🎯 CI Success Criteria

| Metric | Target | Current Status |
|--------|--------|----------------|
| Syntax Errors | 0 | ✅ 0 |
| Style Violations | 0 | ✅ 0 |
| Black Formatting | 100% compliant | ✅ Pass |
| Import Sorting | 100% compliant | ✅ Pass |
| Tests Passing | 100% (131 tests) | ✅ 131/131 |
| Code Coverage | ≥90% | ✅ 93% |
| Build Time | <5 minutes | ✅ ~1 minute |

---

## 📚 Additional Resources

- **Flake8 Documentation**: [https://flake8.pycqa.org/](https://flake8.pycqa.org/)
- **Black Documentation**: [https://black.readthedocs.io/](https://black.readthedocs.io/)
- **isort Documentation**: [https://pycqa.github.io/isort/](https://pycqa.github.io/isort/)
- **pytest Documentation**: [https://docs.pytest.org/](https://docs.pytest.org/)
- **GitHub Actions**: [https://docs.github.com/actions](https://docs.github.com/actions)

---

## 🔄 Related Documentation

- [Python Commands Reference](python-commands-reference.md) - Python, pip, pytest commands
- [Git Commands Reference](git-commands-reference.md) - Git workflow commands
- [Setup Guide](../04_setup.md) - Initial project setup
- [Technical Documentation](../05_technical.md) - Technical implementation details

---

**Last Updated**: January 15, 2026  
**Session**: Comprehensive CI workflow validation and documentation  
**Status**: All 131 tests passing, 93% coverage, 0 flake8 violations

