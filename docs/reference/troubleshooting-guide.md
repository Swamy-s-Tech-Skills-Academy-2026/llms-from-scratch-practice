# Troubleshooting Guide

<!-- markdownlint-disable MD031 MD032 MD040 MD012 -->

**Project**: GenAI Email & Report Drafting System  
**Date**: January 15, 2026  
**Purpose**: Common issues and solutions for development

---

## 📋 Table of Contents

1. [Backend Issues](#backend-issues)
2. [Frontend Issues](#frontend-issues)
3. [Database Issues](#database-issues)
4. [CI/CD Issues](#cicd-issues)
5. [Development Environment](#development-environment)

---

## 🐍 Backend Issues

### Issue 1: ModuleNotFoundError

**Symptoms:**
```
ModuleNotFoundError: No module named 'flask_limiter'
ModuleNotFoundError: No module named 'google.generativeai'
```

**Root Cause:**
- Dependencies not installed in virtual environment
- Wrong Python interpreter being used
- System Python vs virtual environment Python

**Solution:**

```powershell
# Method 1: Ensure venv is activated
cd D:\SrivariHSSPL-2026\genai-email-report-drafting\src\backend
.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Method 2: Use venv Python directly (no activation needed)
.venv\Scripts\python.exe -m pip install -r requirements.txt

# Verify installation
.venv\Scripts\python.exe -m pip list

# Check which Python is being used
python -c "import sys; print(sys.executable)"
# Should output: D:\...\genai-email-report-drafting\.venv\Scripts\python.exe
```

**Prevention:**
- Always activate virtual environment before running commands
- Use explicit `.venv\Scripts\python.exe` when scripting
- Never use system Python for project development

---

### Issue 2: Flake8 E501 - Line Too Long

**Symptoms:**
```
./services/gemini_service.py:235:121: E501 line too long (146 > 120 characters)
```

**Root Cause:**
- Code line exceeds 120 character limit
- Long string literals or function calls
- Deeply nested expressions

**Solution:**

```python
# ❌ Before (146 characters)
user_message = "Google Gemini AI blocked the prompt due to safety filters. Please rephrase your request with different wording."

# ✅ After (multi-line string)
user_message = (
    "Google Gemini AI blocked the prompt due to safety filters. "
    "Please rephrase your request with different wording."
)

# ❌ Before (long function call)
logger.error("API key error", extra={"correlation_id": correlation_id, "error": "Invalid API key"})

# ✅ After (multi-line with proper formatting)
logger.error(
    "API key error",
    extra={
        "correlation_id": correlation_id,
        "error": "Invalid API key"
    }
)
```

**Verification:**
```powershell
# Check specific file
python -m flake8 services/gemini_service.py

# Check all files
python -m flake8 .
```

---

### Issue 3: Flask Server Won't Start

**Symptoms:**
```
Error: Could not locate a Flask application
Error: Failed to find Flask application or factory
```

**Root Cause:**
- `FLASK_APP` environment variable not set
- Wrong directory (not in `src/backend/`)
- Missing dependencies

**Solution:**

```powershell
# Set FLASK_APP environment variable
$env:FLASK_APP = "app.py"

# Navigate to correct directory
cd D:\SrivariHSSPL-2026\genai-email-report-drafting\src\backend

# Ensure venv is activated
.venv\Scripts\Activate.ps1

# Run Flask server
python app.py

# Alternative: Use Flask CLI
flask run
```

---

### Issue 4: Database Connection Error

**Symptoms:**
```
sqlalchemy.exc.OperationalError: could not connect to server
psycopg2.OperationalError: connection refused
```

**Root Cause:**
- PostgreSQL not running
- Wrong connection string
- Database doesn't exist
- Firewall blocking connection

**Solution:**

```powershell
# Check if PostgreSQL is running (Docker/Podman Compose)
cd D:\SrivariHSSPL-2026\genai-email-report-drafting\infra
podman compose ps
# or: docker compose ps

# Start PostgreSQL if not running
podman compose up -d
# or: docker compose up -d

# Check database connection
podman compose exec postgres psql -U postgres -d genai_email_report
# or: docker compose exec postgres psql -U postgres -d genai_email_report

# Verify DATABASE_URL in .env file
Get-Content src\backend\.env | Select-String "DATABASE_URL"
# Should be: DATABASE_URL=postgresql://postgres:postgres@localhost:5432/genai_email_report

# Test connection from Python
python -c "from sqlalchemy import create_engine; engine = create_engine('postgresql://postgres:postgres@localhost:5432/genai_email_report'); conn = engine.connect(); print('✅ Connection successful')"
```

---

### Issue 5: JWT Token Errors

**Symptoms:**
```
401 Unauthorized: Missing Authorization Header
422 Unprocessable Entity: Invalid token
```

**Root Cause:**
- JWT_SECRET_KEY not set
- Token expired
- Invalid token format
- Missing Bearer prefix

**Solution:**

```powershell
# Verify JWT_SECRET_KEY in .env
Get-Content src\backend\.env | Select-String "JWT_SECRET_KEY"

# Generate new secret key
python -c "import secrets; print(secrets.token_hex(32))"

# Update .env file
# JWT_SECRET_KEY=your-generated-secret-key

# Test JWT token generation
python -c "
from flask import Flask
from flask_jwt_extended import JWTManager, create_access_token

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
jwt = JWTManager(app)

with app.app_context():
    token = create_access_token(identity=1)
    print(f'✅ Token generated: {token[:20]}...')
"
```

---

### Issue 6: Gemini API Errors

**Symptoms:**
```
google.api_core.exceptions.PermissionDenied: API key not valid
google.api_core.exceptions.ResourceExhausted: Quota exceeded
```

**Root Cause:**
- Invalid API key
- API key not set
- Quota/rate limit exceeded
- Internet connection issue

**Solution:**

```powershell
# Verify API key in .env
Get-Content src\backend\.env | Select-String "GEMINI_API_KEY"

# Test API key validity
python -c "
import google.generativeai as genai
import os

genai.configure(api_key='your-api-key')
model = genai.GenerativeModel('gemini-3-flash-preview')
response = model.generate_content('Hello')
print(f'✅ API key valid: {response.text[:50]}...')
"

# Check API quota in Google Cloud Console
# https://console.cloud.google.com/apis/api/generativelanguage.googleapis.com/quotas

# Test with health check endpoint
curl http://localhost:5000/api/health
```

---

## ⚛️ Frontend Issues

### Issue 1: Frontend Won't Start

**Symptoms:**
```
Error: Cannot find module 'vite'
Error: Port 5173 is already in use
```

**Root Cause:**
- Dependencies not installed
- Port conflict
- Node.js version mismatch

**Solution:**

```powershell
# Navigate to frontend directory
cd D:\SrivariHSSPL-2026\genai-email-report-drafting\src\frontend

# Install dependencies
npm install

# If port conflict, use different port
npm run dev -- --port 5174

# Clean install (if corrupted)
Remove-Item -Recurse -Force node_modules
Remove-Item package-lock.json
npm install

# Check Node.js version
node --version  # Should be v16+ or v18+
```

---

### Issue 2: API Connection Errors

**Symptoms:**
```
Network Error: Failed to fetch
CORS Error: Access blocked by CORS policy
```

**Root Cause:**
- Backend not running
- Wrong API URL
- CORS not configured

**Solution:**

```powershell
# Verify backend is running
curl http://localhost:5000/health

# Check VITE_API_BASE_URL in .env
Get-Content src\frontend\.env
# Should be: VITE_API_BASE_URL=http://localhost:5000/api

# Restart frontend dev server after changing .env
npm run dev

# Check CORS configuration in backend
# File: src/backend/app.py
# CORS(app, resources={r"/api/*": {"origins": "*"}})
```

---

### Issue 3: TypeScript Errors

**Symptoms:**
```
error TS2339: Property 'user' does not exist on type
error TS2345: Argument of type 'string' is not assignable to parameter
```

**Root Cause:**
- Type definitions missing
- Incorrect type annotations
- Outdated type definitions

**Solution:**

```powershell
# Reinstall dependencies
npm install

# Check TypeScript version
npx tsc --version  # Should be ~5.9.3

# Validate TypeScript configuration
npx tsc --noEmit

# Fix type errors by updating type definitions
# File: src/frontend/src/types/index.ts
```

---

### Issue 4: ESLint Configuration Error

**Symptoms:**
```
ConfigError: The config file must export an array | object | function.
```

**Root Cause:**
- Mixing old `defineConfig` (deprecated in some contexts) with new flat config.
- `eslint.config.js` syntax incompatible with current dependencies.

**Solution:**
Update `src/frontend/eslint.config.js` to use `tseslint.config`:

```javascript
import js from '@eslint/js'
import globals from 'globals'
import reactHooks from 'eslint-plugin-react-hooks'
import reactRefresh from 'eslint-plugin-react-refresh'
import tseslint from 'typescript-eslint'

export default tseslint.config(
  { ignores: ['dist'] },
  {
    extends: [js.configs.recommended, ...tseslint.configs.recommended],
    files: ['**/*.{ts,tsx}'],
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
    },
    // ... plugins and rules
  },
)
```

---

## 🗄️ Database Issues

### Issue 1: Docker/Podman Compose PostgreSQL Not Starting

**Symptoms:**
```
ERROR: Container not healthy
ERROR: Port 5432 already in use
```

**Root Cause:**
- Port conflict (another PostgreSQL running)
- Docker/Podman not running
- Invalid configuration

**Solution:**

```powershell
# Check if Docker or Podman is running
docker --version
docker compose version
# Or Podman
podman --version
podman compose version

# Check port usage
netstat -ano | findstr :5432

# Stop conflicting PostgreSQL service
# Option 1: Stop local PostgreSQL service
Stop-Service postgresql-x64-13  # Adjust version as needed

# Option 2: Use different port in docker-compose.yml
# ports:
#   - "5433:5432"

# Restart Docker/Podman Compose
cd D:\SrivariHSSPL-2026\genai-email-report-drafting\infra
docker compose down
docker compose up -d
podman compose down
podman compose up -d

# Check service health
docker compose ps
podman compose ps
# Should show "healthy" status
```

---

### Issue 2: Database Schema Not Created

**Symptoms:**
```
ProgrammingError: relation "users" does not exist
```

**Root Cause:**
- Database not initialized
- Schema not applied
- Using wrong database

**Solution:**

```powershell
# Check if database exists
cd D:\SrivariHSSPL-2026\genai-email-report-drafting\infra
docker compose exec postgres psql -U postgres -l
podman compose exec postgres psql -U postgres -l

# Connect to database
docker compose exec postgres psql -U postgres -d genai_email_report
podman compose exec postgres psql -U postgres -d genai_email_report

# Check if tables exist
\dt

# If tables don't exist, run Flask app to create them
cd ..\src\backend
.venv\Scripts\Activate.ps1
python app.py
# Tables will be created automatically via SQLAlchemy
```

---

### Issue 3: Data Not Persisting

**Symptoms:**
- Data disappears after Docker restart
- Tables empty after restart

**Root Cause:**
- Docker volume not configured
- Using `docker compose down -v` (or `podman compose down -v`) deletes volumes

**Solution:**

```powershell
# Check Docker volumes
docker volume ls | Select-String "genai_email_report"

# Stop containers without deleting volumes
cd D:\SrivariHSSPL-2026\genai-email-report-drafting\infra
docker compose down  # ✅ Preserves data
podman compose down  # ✅ Preserves data

# NEVER use this unless you want to delete data:
# docker compose down -v  # ❌ Deletes all data!
# podman compose down -v  # ❌ Deletes all data!

# Backup database
docker compose exec postgres pg_dump -U postgres genai_email_report > backup.sql
podman compose exec postgres pg_dump -U postgres genai_email_report > backup.sql

# Restore database
docker compose exec -T postgres psql -U postgres genai_email_report < backup.sql
podman compose exec -T postgres psql -U postgres genai_email_report < backup.sql
```

---

## 🔄 CI/CD Issues

### Issue 1: GitHub Actions Failing Locally Passing

**Symptoms:**
- Tests pass locally
- CI fails on GitHub

**Root Cause:**
- Environment variable differences
- Python version mismatch
- Platform differences (Windows vs Linux)

**Solution:**

```powershell
# Run exact CI commands locally
cd D:\SrivariHSSPL-2026\genai-email-report-drafting\src\backend

# Match CI environment
$env:FLASK_ENV = "testing"
$env:DATABASE_URL = "sqlite:///:memory:"

# Run CI checks
python -m flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
python -m flake8 . --count --max-complexity=10 --max-line-length=120 --statistics
python -m black --check .
python -m isort --check-only .
pytest tests/ -v --cov=. --cov-report=term-missing

# Check Python version matches CI
python --version  # Should be 3.12.x
```

---

### Issue 2: Coverage Threshold Not Met

**Symptoms:**
```
TOTAL coverage: 87% (target: 90%)
```

**Root Cause:**
- New code not tested
- Test files not covering all branches
- Edge cases missing

**Solution:**

```powershell
# Generate coverage report with missing lines
pytest tests/ --cov=. --cov-report=term-missing

# Generate HTML coverage report
pytest tests/ --cov=. --cov-report=html
# Open htmlcov/index.html in browser

# Focus on uncovered lines
# Add tests for missing coverage areas
```

---

### Issue 3: isort Import Sorting Failure

**Symptoms:**
```
ERROR: ... Imports are incorrectly sorted and/or formatted.
```

**Root Cause:**
- New imports added without sorting
- Manual edits disrupting import order

**Solution:**

```powershell
# Navigate to backend directory
cd D:\SrivariHSSPL-2026\genai-email-report-drafting\src\backend

# Check for issues (diff view)
python -m isort . --check-only --diff

# Automatically fix all files
python -m isort .
```

---

## 💻 Development Environment

### Issue 1: Virtual Environment Not Activating

**Symptoms:**
```
.venv\Scripts\Activate.ps1 : cannot be loaded because running scripts is disabled
```

**Root Cause:**
- PowerShell execution policy restriction

**Solution:**

```powershell
# Check execution policy
Get-ExecutionPolicy

# Set execution policy for current user
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Activate virtual environment
.venv\Scripts\Activate.ps1

# Verify activation
python -c "import sys; print(sys.executable)"
```

---

### Issue 2: Python Version Mismatch

**Symptoms:**
```
ERROR: This package requires Python 3.12+
SyntaxError: invalid syntax (Python 3.9)
```

**Root Cause:**
- Wrong Python version installed
- Multiple Python versions
- Python not in PATH

**Solution:**

```powershell
# Check Python version
python --version

# Check .python-version file
Get-Content D:\SrivariHSSPL-2026\genai-email-report-drafting\.python-version
# Should be: 3.12.10

# Find all Python installations
where.exe python

# Use specific Python version
py -3.12 --version

# Create venv with specific version
py -3.12 -m venv .venv
```

---

### Issue 3: uv Installation Issues

**Symptoms:**
```
uv: command not found
```

**Root Cause:**
- uv not installed
- uv not in PATH

**Solution:**

```powershell
# Install uv (Windows PowerShell)
irm https://astral.sh/uv/install.ps1 | iex

# Verify installation
uv --version

# Add to PATH if needed
$env:PATH += ";$env:USERPROFILE\.cargo\bin"

# Use uv to create .venv and install dependencies
cd D:\STSA-2026\llms-from-scratch-practice
uv sync
uv sync --group dev
```

---

## 📝 Quick Diagnostic Commands

### Backend Health Check

```powershell
cd D:\SrivariHSSPL-2026\genai-email-report-drafting\src\backend

# Check Python version
python --version

# Check virtual environment
Test-Path .venv

# Check dependencies
.venv\Scripts\python.exe -m pip list

# Check Flask app
python -c "from app import create_app; print('✅ App imports successfully')"

# Run smoke test
pytest tests/smoke_test.py -v
```

### Frontend Health Check

```powershell
cd D:\SrivariHSSPL-2026\genai-email-report-drafting\src\frontend

# Check Node.js version
node --version

# Check dependencies
npm list --depth=0

# Check TypeScript
npx tsc --noEmit

# Build check (dry run)
npm run build
```

### Database Health Check

```powershell
cd D:\SrivariHSSPL-2026\genai-email-report-drafting\infra

# Check Docker/Podman Compose status
docker compose ps
podman compose ps

# Check PostgreSQL health
docker compose exec postgres pg_isready -U postgres
podman compose exec postgres pg_isready -U postgres

# Check database connection
docker compose exec postgres psql -U postgres -d genai_email_report -c "SELECT 1;"
podman compose exec postgres psql -U postgres -d genai_email_report -c "SELECT 1;"
```

### Full System Health Check

```powershell
# Run all health checks
cd D:\SrivariHSSPL-2026\genai-email-report-drafting

Write-Host "🔍 Checking Backend..." -ForegroundColor Cyan
cd src\backend
python --version
.venv\Scripts\python.exe -m pip list | Select-String "Flask|pytest"

Write-Host "🔍 Checking Frontend..." -ForegroundColor Cyan
cd ..\frontend
node --version
npm list --depth=0 | Select-String "react|vite"

Write-Host "🔍 Checking Database..." -ForegroundColor Cyan
cd ..\..\infra
docker compose ps
podman compose ps

Write-Host "✅ Health check complete!" -ForegroundColor Green
```

---

## 🆘 Getting Help

### Documentation

1. [Setup Guide](../04_setup.md) - Initial installation
2. [Technical Documentation](../05_technical.md) - Implementation details
3. [Python Commands Reference](python-commands-reference.md) - Python commands
4. [CI Workflow Reference](ci-workflow-reference.md) - CI/CD workflows

### Community Resources

- **Flask**: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- **React**: [https://react.dev/](https://react.dev/)
- **PostgreSQL**: [https://www.postgresql.org/docs/](https://www.postgresql.org/docs/)
- **Google Gemini**: [https://ai.google.dev/](https://ai.google.dev/)

---

**Last Updated**: January 15, 2026  
**Maintained By**: Viswanatha Swamy P K  
**Status**: Validated with real troubleshooting scenarios

