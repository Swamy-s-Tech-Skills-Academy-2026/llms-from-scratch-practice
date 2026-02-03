# Git Commands Reference

**Project**: LLMs From Scratch Practice (STSA 2026)  
**Purpose**: Core Git commands for day-to-day work  
**Default Branch**: `main`  
**Current Working Branch**: `swamy/30jan-work`

---

## 📋 Status & Inspection

```powershell
# Short status
git status -s

# Full status with branch info
git status

# Show unstaged changes
git diff

# Show staged changes
git diff --cached

# Show commit history
git log --oneline --graph --all --decorate

# Show last 5 commits
git log --oneline -5

# Show files changed in last commit
git show --stat
```

---

## 🌿 Branching & Navigation

```powershell
# List all branches (local and remote)
git branch -a

# List local branches only
git branch

# Create and switch to new branch
git checkout -b swamy/feature-name

# Switch to existing branch
git checkout main
git checkout swamy/30jan-work

# Delete local branch (after merge)
git branch -d swamy/old-branch

# Delete local branch (force)
git branch -D swamy/old-branch

# Show current branch
git branch --show-current
```

---

## ✅ Staging & Committing

```powershell
# Stage all changes
git add .

# Stage specific file
git add README.md

# Stage specific folder
git add notebooks/ch02/

# Commit with message
git commit -m "docs: clarify uv setup"

# Commit with detailed message
git commit -m "feat: add attention mechanism notebook" -m "- Implemented self-attention from scratch
- Added visualization of attention weights
- Included personal learning notes"

# Amend last commit (before push)
git commit --amend -m "Updated message"

# Stage and commit in one step
git commit -am "fix: typo in README"
```

**Commit Message Conventions**:
- `docs:` - Documentation changes
- `feat:` - New notebook or feature
- `fix:` - Bug fixes or corrections
- `refactor:` - Code restructuring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

---

## 🔄 Remote Operations

```powershell
# Show remotes
git remote -v

# Add remote (if needed)
git remote add origin https://github.com/Swamy-s-Tech-Skills-Academy-2026/llms-from-scratch-practice.git

# Fetch latest from all remotes
git fetch --all

# Fetch from origin
git fetch origin

# Pull latest from main
git pull origin main

# Pull latest from current branch
git pull

# Push current branch to origin
git push origin swamy/30jan-work

# Push and set upstream (first time)
git push -u origin swamy/30jan-work

# Push all branches
git push --all origin

# Force push (use with extreme caution!)
git push --force origin swamy/30jan-work
```

---

## 🧹 Undo (Safe)

```powershell
# Unstage files (keeps changes)
git restore --staged .

# Discard changes in a file (use with care)
git restore README.md
```

