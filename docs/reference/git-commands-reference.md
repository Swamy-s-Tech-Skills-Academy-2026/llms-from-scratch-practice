# Git Commands Reference

**Project**: LLMs From Scratch Practice (STSA 2026)  
**Purpose**: Core Git commands for day-to-day work

---

## 📋 Status & Inspection

```powershell
# Short status
git status -s

# Full status
git status

# Show changes
git diff

# Show staged changes
git diff --cached
```

---

## 🌿 Branching

```powershell
# List branches
git branch

# Create and switch
git checkout -b feature/your-branch

# Switch branches
git checkout main
```

---

## ✅ Staging & Committing

```powershell
# Stage all changes
git add .

# Stage specific file
git add README.md

# Commit
git commit -m "Docs: clarify uv setup"
```

---

## 🔄 Remotes

```powershell
# Show remotes
git remote -v

# Fetch latest
git fetch origin

# Pull latest
git pull origin main

# Push current branch
git push origin feature/your-branch
```

---

## 🧹 Undo (Safe)

```powershell
# Unstage files (keeps changes)
git restore --staged .

# Discard changes in a file (use with care)
git restore README.md
```

