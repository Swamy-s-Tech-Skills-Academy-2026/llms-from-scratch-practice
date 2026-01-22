# Python Commands Reference

**Project**: GenAI Email & Report Drafting System  
**Date**: January 15, 2026  
**Purpose**: Python, pip, pytest, and code quality tool commands

---

## 📦 Package Management (pip)

### Install Dependencies

```powershell
# Install from requirements.txt (recommended - uses pinned versions)
pip install -r requirements.txt

# Install specific package
pip install flask

# Install with exact version (recommended for reproducibility)
pip install flask==3.1.0

# Install in editable mode (development)
pip install -e .

# Install dev dependencies from pyproject.toml
pip install -e ".[dev]"

# Upgrade package (use with caution - may break compatibility)
pip install --upgrade flask
```

### Current Pinned Versions (requirements.txt)

```text
# Flask Core
Flask==3.1.0
Flask-SQLAlchemy==3.1.1
Flask-Migrate==4.0.7
Flask-JWT-Extended==4.7.1
flask-limiter==3.8.0
flask-cors==5.0.0

# Database
psycopg2-binary==2.9.10
SQLAlchemy==2.0.36

# Security
Werkzeug==3.1.3

# Testing & Code Quality
pytest==8.3.4
pytest-cov==6.0.0
pytest-asyncio==0.25.2
black==24.10.0
isort==5.13.2
flake8==7.1.1

# Utilities
python-dotenv==1.0.1

# AI Integration
google-generativeai==0.8.3
```

### Using uv (Faster Alternative)

```powershell
# Create virtual environment with uv
uv venv

# Activate virtual environment (Windows)
.venv\Scripts\Activate.ps1

# Install dependencies with uv
uv pip install -r requirements.txt --link-mode=copy

# Install specific package
uv pip install flask
```

### List & Inspect Packages

```powershell
# List installed packages
pip list

# Show package details
pip show flask

# List outdated packages
pip list --outdated

# Export installed packages
pip freeze > requirements.txt
```

---

## 🧪 Testing (pytest)

### Run Tests

```powershell
# Run all tests (module mode - recommended for path resolution)
python -m pytest

# Run all tests (direct command)
pytest

# Run with verbose output
python -m pytest -v

# Run specific test file
pytest tests/test_auth.py

# Run specific test class
pytest tests/test_auth.py::TestUserRegistration

# Run specific test function
pytest tests/test_auth.py::TestUserRegistration::test_register_success

# Run tests matching pattern
pytest -k "test_login"

# Run tests with markers
pytest -m "not slow"
```

### Test Coverage

```powershell
# Run with coverage
pytest --cov=.

# Coverage with terminal report
pytest --cov=. --cov-report=term-missing

# Coverage with HTML report
pytest --cov=. --cov-report=html

# Coverage for specific module
pytest --cov=services --cov-report=term-missing
```

### Test Options

```powershell
# Show short traceback
pytest --tb=short

# Show local variables on failure
pytest --tb=long

# Stop on first failure
pytest -x

# Stop after N failures
pytest --maxfail=3

# Show print statements
pytest -s

# Run last failed tests
pytest --lf

# Run tests in parallel (requires pytest-xdist)
pytest -n auto
```

---

## 🎨 Code Formatting (Black)

### Check & Format

```powershell
# Check formatting (no changes)
python -m black --check .

# Check with diff output
python -m black --check --diff .

# Format all files
python -m black .

# Format specific file
python -m black app.py

# Format specific directory
python -m black src/backend/

# Format with line length
python -m black --line-length 120 .
```

### Configuration

Black configuration in `pyproject.toml`:

```toml
[tool.black]
line-length = 120
target-version = ['py312']
include = '\.pyi?$'
exclude = '''
/(
    \.git
  | \.venv
  | venv
  | __pycache__
)/
'''
```

---

## 📋 Import Sorting (isort)

### Check & Sort

```powershell
# Check import sorting (no changes)
python -m isort --check-only .

# Check with diff output
python -m isort --check-only --diff .

# Sort imports in all files
python -m isort .

# Sort specific file
python -m isort app.py

# Sort specific directory
python -m isort src/backend/

# Check specific directory with diff (useful for local diagnosis)
python -m isort src/backend/ --check-only --diff
```

### isort Configuration

isort configuration in `pyproject.toml`:

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

---

## 🔍 Linting (flake8)

### Run Linter

```powershell
# Lint all files
flake8 .

# Lint specific file
flake8 app.py

# Lint with specific config
flake8 --config=.flake8 .

# Lint with custom line length
flake8 --max-line-length=120 .

# Lint with complexity check
flake8 --max-complexity=10 .

# Show only specific error codes
flake8 --select=E501,W503 .

# Ignore specific error codes
flake8 --ignore=E501,W503 .
```

### flake8 Configuration

`.flake8` configuration file:

```ini
[flake8]
max-line-length = 120
max-complexity = 10
exclude = .git,__pycache__,.venv,venv
ignore = E203,W503
```

---

## 🔧 Virtual Environment

### Create & Manage

```powershell
# Create virtual environment
python -m venv .venv

# Activate (Windows PowerShell)
.venv\Scripts\Activate.ps1

# Activate (Windows CMD)
.venv\Scripts\activate.bat

# Deactivate
deactivate

# Remove virtual environment
Remove-Item -Recurse -Force .venv
```

### Check Python Version

```powershell
# Show Python version
python --version

# Show Python path
python -c "import sys; print(sys.executable)"

# Show installed Python locations
where python
```

---

## 🚀 Running the Application

### Flask Development Server

```powershell
# Set environment variables
$env:FLASK_ENV = "development"
$env:DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/genai_email_report"
$env:JWT_SECRET_KEY = "your-secret-key"
$env:GEMINI_API_KEY = "your-api-key"

# Run Flask app
python app.py

# Run with debug mode
$env:FLASK_DEBUG = "1"
python app.py

# Run on specific port
python -c "from app import create_app; create_app().run(host='0.0.0.0', port=5001)"
```

### Flask CLI

```powershell
# Set Flask app
$env:FLASK_APP = "app:create_app"

# Run development server
flask run

# Run on specific host/port
flask run --host=0.0.0.0 --port=5000

# Run with debug mode
flask run --debug

# Show routes
flask routes

# Open shell
flask shell
```

---

## 🗄️ Database Migrations (Flask-Migrate)

### Initialize & Migrate

```powershell
# Initialize migrations folder
flask db init

# Create migration
flask db migrate -m "Initial migration"

# Apply migrations
flask db upgrade

# Rollback last migration
flask db downgrade

# Show migration history
flask db history

# Show current revision
flask db current
```

---

## 🔄 Complete CI Workflow

### Pre-Commit Checks (Production-Tested Commands)

```powershell
# Navigate to backend directory
cd src/backend

# Ensure virtual environment is activated
.venv\Scripts\Activate.ps1

# 1. Check syntax errors (critical - stop if fails)
python -m flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

# 2. Check code style (E501: line length, max 120 chars)
python -m flake8 . --count --max-complexity=10 --max-line-length=120 --statistics

# 3. Check Black formatting (dry-run, no changes)
python -m black --check .

# 4. Apply Black formatting (if needed)
python -m black .

# 5. Check import sorting (dry-run, no changes)
python -m isort --check-only .

# 6. Apply import sorting (if needed)
python -m isort .

# 7. Run full test suite with coverage
pytest tests/ -v --cov=. --cov-report=term-missing

# Expected output: 131 passed, 93% coverage
```

### One-Liner Check (Mimics GitHub Actions CI)

```powershell
# All checks in one command - must all pass
python -m flake8 . --count --select=E9,F63,F7,F82 && python -m flake8 . --count --max-complexity=10 --max-line-length=120 && python -m black --check . && python -m isort --check-only . && pytest tests/ -v --cov=. --cov-report=term-missing
```

### Virtual Environment Isolation (Critical)

```powershell
# Install dependencies in virtual environment (not system Python)
# Method 1: Using activated venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Method 2: Direct venv Python (Windows - no activation needed)
.venv\Scripts\python.exe -m pip install -r requirements.txt

# Method 3: Using uv (faster alternative)
uv pip install -r requirements.txt --link-mode=copy

# Verify installation in correct environment
.venv\Scripts\python.exe -m pip list
```

### CI Workflow Validation (Local Testing)

```powershell
# Step 1: Ensure dependencies are installed in venv
cd d:\SrivariHSSPL-2026\genai-email-report-drafting\src\backend
.venv\Scripts\python.exe -m pip install -r requirements.txt

# Step 2: Run linting checks (matches GitHub Actions)
python -m flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
python -m flake8 . --count --max-complexity=10 --max-line-length=120 --statistics

# Step 3: Run formatting checks
python -m black --check .
python -m isort --check-only .

# Step 4: Run tests with coverage
cd d:\SrivariHSSPL-2026\genai-email-report-drafting\src\backend
pytest tests/ -v --cov=. --cov-report=term-missing

# Expected Results:
# - flake8 syntax: 0 errors
# - flake8 style: 0 errors
# - black: "All done! ✨"
# - isort: No output (means pass)
# - pytest: 131 passed, 93% coverage
```

### Fixing Common Flake8 Violations

```powershell
# E501: Line too long (max 120 characters)
# Solution: Split long lines into multi-line strings or expressions

# Example - Before (line 235, >120 chars):
user_message = "Google Gemini AI blocked prompt due to safety filters..."

# Example - After (multi-line string):
user_message = (
    "Google Gemini AI blocked the prompt due to safety filters. "
    "Please rephrase your request with different wording."
)

# Verify fix
python -m flake8 services/gemini_service.py
```

---

## 📊 Quick Reference Card

```powershell
# Package Management
pip install -r requirements.txt    # Install dependencies
pip list                           # List packages
pip freeze > requirements.txt      # Export packages

# Testing
pytest                             # Run all tests
pytest -v                          # Verbose output
pytest --cov=.                     # With coverage
pytest -k "pattern"                # Match pattern

# Code Quality
python -m black .                  # Format code
python -m isort .                  # Sort imports
flake8 .                           # Lint code

# Virtual Environment
python -m venv .venv               # Create venv
.venv\Scripts\Activate.ps1         # Activate (Windows)
deactivate                         # Deactivate

# Flask
python app.py                      # Run server
flask run                          # Run with CLI
flask db upgrade                   # Apply migrations
```

---

**Last Updated**: January 15, 2026  
**Repository**: genai-email-report-drafting
