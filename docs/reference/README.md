# Reference Documentation

<!-- markdownlint-disable MD032 MD012 -->

**Project**: GenAI Email & Report Drafting System  
**Purpose**: Quick reference guides for development commands and workflows  
**Last Updated**: January 15, 2026

---

## 📚 Available Reference Documents

Podman users can replace `docker compose` with `podman compose` in all Compose-related commands.

### Command References

| Document | Purpose | Key Topics |
|----------|---------|------------|
| [Git Commands](git-commands-reference.md) | Git workflow and version control | Status, commits, branches, merging, tagging |
| [Python Commands](python-commands-reference.md) | Python development and testing | pip, pytest, Black, isort, flake8, venv |
| [PowerShell Commands](powershell-commands-reference.md) | Windows PowerShell scripting | File operations, environment variables, processes |
| [Node.js Commands](nodejs-commands-reference.md) | Frontend development | npm, package management, build scripts |
| [Docker Commands](docker-commands-reference.md) | Container management | Docker/Podman Compose, PostgreSQL, networking |
| [Tags vs Releases](github-tags-and-releases.md) | GitHub Concepts | Git Tags, GitHub Releases, semantic versioning |

### Workflow Guides

| Document | Purpose | Key Topics |
|----------|---------|------------|
| [CI/CD Workflow](ci-workflow-reference.md) | Continuous Integration workflows | GitHub Actions, local validation, troubleshooting |
| [Troubleshooting Guide](troubleshooting-guide.md) | Common issues and solutions | Backend, frontend, database, CI/CD issues |

---

## 🎯 Quick Navigation

### I want to

**Work with Git:**
- → [Git Commands Reference](git-commands-reference.md)
- Check status, commit changes, manage branches, push/pull

**Run Tests:**
- → [Python Commands Reference](python-commands-reference.md#testing-pytest)
- pytest commands, coverage reports, test options

**Fix Linting Errors:**
- → [CI/CD Workflow Reference](ci-workflow-reference.md#common-ci-failures)
- flake8 violations, Black formatting, isort issues

**Set Up Environment:**
- → [Python Commands Reference](python-commands-reference.md#virtual-environment)
- Virtual environment creation, activation, dependency installation

**Manage Database:**
- → [Docker Commands Reference](docker-commands-reference.md)
- PostgreSQL with Docker/Podman Compose, connection, backup/restore

**Build Frontend:**
- → [Node.js Commands Reference](nodejs-commands-reference.md)
- npm install, build, dev server, TypeScript compilation

**Troubleshoot Issues:**
- → [Troubleshooting Guide](troubleshooting-guide.md)
- Common errors, diagnostic commands, solutions

**Validate Before Push:**
- → [CI/CD Workflow Reference](ci-workflow-reference.md#local-ci-validation)
- Pre-commit checks, CI validation scripts

---

## 🚀 Common Workflows

### 1. Starting Development

Please refer to the **[Setup Guide](../04_setup.md)** for the authoritative start-up instructions.

**References:**
- [Python Commands - Virtual Environment](python-commands-reference.md#virtual-environment)
- [Node.js Commands - Development Server](nodejs-commands-reference.md)
- [Docker Commands - Compose](docker-commands-reference.md)

---

### 2. Running Tests

```powershell
# Backend tests with coverage
cd src\backend
pytest tests/ -v --cov=. --cov-report=term-missing

# Expected: 131 passed, 93% coverage
```

**References:**
- [Python Commands - Testing](python-commands-reference.md#testing-pytest)
- [CI/CD Workflow - Local Validation](ci-workflow-reference.md#local-ci-validation)

---

### 3. Pre-Commit Validation

```powershell
# Complete CI validation
cd src\backend

# 1. Check syntax errors
python -m flake8 . --count --select=E9,F63,F7,F82

# 2. Check style
python -m flake8 . --count --max-complexity=10 --max-line-length=120

# 3. Format code
python -m black .
python -m isort .

# 4. Run tests
pytest tests/ -v --cov=. --cov-report=term-missing
```

**References:**
- [CI/CD Workflow - Pre-Commit Checks](ci-workflow-reference.md#complete-local-validation-script)
- [Python Commands - Code Quality](python-commands-reference.md#code-formatting-black)

---

### 4. Fixing Flake8 Violations

```powershell
# Find violations
python -m flake8 . --show-source

# Fix line length (E501)
# Split long lines into multi-line strings

# Apply formatting
python -m black .
python -m isort .

# Verify fix
python -m flake8 .
```

**References:**
- [CI/CD Workflow - Common Failures](ci-workflow-reference.md#common-ci-failures)
- [Troubleshooting - Flake8 E501](troubleshooting-guide.md#issue-2-flake8-e501---line-too-long)

---

### 5. Database Management

```powershell
# Start PostgreSQL
cd infra
docker compose up -d

# Check health
docker compose ps

# Connect to database
docker compose exec postgres psql -U postgres -d genai_email_report

# Backup database
docker compose exec postgres pg_dump -U postgres genai_email_report > backup.sql
```

**References:**
- [Docker Commands - PostgreSQL](docker-commands-reference.md)
- [Troubleshooting - Database Issues](troubleshooting-guide.md#database-issues)

---

### 6. Committing Changes

```powershell
# Check status
git status

# Stage changes
git add .

# Commit with message
git commit -m "Fix: Description of changes"

# Push to branch
git push origin branch-name
```

**References:**
- [Git Commands - Commits](git-commands-reference.md#committing-changes)
- [Git Commands - Pushing](git-commands-reference.md#pushing-changes)

---

## 🎓 Learning Path

### For New Contributors

1. **Start Here:** [Troubleshooting Guide](troubleshooting-guide.md)
   - Common issues and quick fixes
   - Environment setup checklist

2. **Then Review:** [Python Commands Reference](python-commands-reference.md)
   - Testing, formatting, linting
   - Virtual environment management

3. **Next:** [CI/CD Workflow Reference](ci-workflow-reference.md)
   - Pre-commit validation
   - CI success criteria

4. **Finally:** [Git Commands Reference](git-commands-reference.md)
   - Branching strategies
   - Commit conventions

### For Experienced Developers

- **Quick Start:** [CI/CD Workflow - Quick Reference](ci-workflow-reference.md#quick-reference)
- **Common Tasks:** [Python Commands - Quick Reference Card](python-commands-reference.md#quick-reference-card)
- **Troubleshooting:** [Troubleshooting - Quick Diagnostic Commands](troubleshooting-guide.md#quick-diagnostic-commands)

---

## 📊 Command Cheat Sheet

### Most Used Commands

```powershell
# Backend
cd src\backend
.venv\Scripts\Activate.ps1               # Activate venv
python app.py                            # Start server
pytest tests/ -v                         # Run tests
python -m flake8 .                       # Lint code

# Frontend
cd src\frontend
npm install                              # Install deps
npm run dev                              # Start dev server
npm run build                            # Build for prod

# Database
cd infra
docker compose up -d                     # Start PostgreSQL
docker compose ps                        # Check status
docker compose logs postgres             # View logs

# Git
git status                               # Check status
git add .                                # Stage all
git commit -m "message"                  # Commit
git push origin branch                   # Push
```

---

## 🔍 Search Tips

### Finding Commands

Use your editor's search (Ctrl+F) to find specific commands:

- **pytest**: Search "pytest" in [Python Commands](python-commands-reference.md)
- **docker compose / podman compose**: Search "docker compose" or "podman compose" in [Docker Commands](docker-commands-reference.md)
- **flake8**: Search "flake8" in [CI/CD Workflow](ci-workflow-reference.md)
- **git commit**: Search "commit" in [Git Commands](git-commands-reference.md)

### Finding Solutions

Use descriptive error messages to search:

- **"ModuleNotFoundError"**: [Troubleshooting - Backend Issues](troubleshooting-guide.md#backend-issues)
- **"E501 line too long"**: [CI/CD - Common Failures](ci-workflow-reference.md#1-flake8-e501-line-too-long)
- **"Connection refused"**: [Troubleshooting - Database Issues](troubleshooting-guide.md#database-issues)
- **"CORS error"**: [Troubleshooting - Frontend Issues](troubleshooting-guide.md#frontend-issues)

---

## 📝 Document Conventions

### Command Format

All commands use PowerShell syntax (Windows 11 environment):

```powershell
# Comments explain what the command does
CommandName -Parameter Value

# Multi-line commands use backticks
CommandName `
    -Parameter1 Value1 `
    -Parameter2 Value2
```

### File Paths

- **Windows format**: `D:\SrivariHSSPL-2026\genai-email-report-drafting\`
- **Relative paths**: `src\backend\`, `docs\reference\`
- **Virtual environment**: `.venv\Scripts\Activate.ps1`

### Expected Outputs

Commands include expected outputs:

```powershell
# Command
python --version

# Expected output:
# Python 3.12.10
```

---

## 🔗 Related Documentation

### Project Documentation

- [Main README](../../README.md) - Project overview
- [Setup Guide](../04_setup.md) - Initial installation
- [Usage Guide](../04_usage.md) - How to use the application
- [Technical Documentation](../05_technical.md) - Implementation details
- [Architecture Plan](../06_architecture_plan.md) - System architecture

### External Resources

- **Flask**: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- **React**: [https://react.dev/](https://react.dev/)
- **pytest**: [https://docs.pytest.org/](https://docs.pytest.org/)
- **PostgreSQL**: [https://www.postgresql.org/docs/](https://www.postgresql.org/docs/)
- **Docker**: [https://docs.docker.com/](https://docs.docker.com/)

---

## 🆕 Recent Updates

### January 15, 2026

- ✅ Added [CI/CD Workflow Reference](ci-workflow-reference.md)
- ✅ Added [Troubleshooting Guide](troubleshooting-guide.md)
- ✅ Updated [Python Commands Reference](python-commands-reference.md) with production-tested workflows
- ✅ Validated all commands with actual session execution
- ✅ Added real-world troubleshooting scenarios

**Session Highlights:**
- Fixed flake8 E501 violations in `gemini_service.py`
- Resolved virtual environment dependency installation issues
- All 131 tests passing with 93% coverage
- Complete CI workflow validation

---

## 💡 Tips for Success

1. **Activate Virtual Environment:** Always ensure `.venv` is activated before running Python commands
2. **Use Tab Completion:** PowerShell supports tab completion for paths and commands
3. **Check Documentation First:** Most issues are documented in the Troubleshooting Guide
4. **Run Tests Locally:** Always validate CI checks locally before pushing
5. **Keep Commands Handy:** Bookmark commonly used reference documents

---

## 📞 Support

**Issues:** Use GitHub Issues for bug reports  
**Documentation:** This reference directory for quick lookups  
**Technical Details:** See [Technical Documentation](../05_technical.md)

---

**Maintained By**: Viswanatha Swamy P K  
**Last Updated**: January 15, 2026  
**Status**: Comprehensive and production-validated

