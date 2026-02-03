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

## 🧹 Undo & Reset (Use Carefully)

```powershell
# Unstage all files (keeps changes in working directory)
git restore --staged .

# Unstage specific file
git restore --staged README.md

# Discard changes in working directory (CANNOT be undone!)
git restore README.md

# Discard all uncommitted changes (DANGEROUS!)
git restore .

# Reset to last commit (keeps changes staged)
git reset --soft HEAD~1

# Reset to last commit (keeps changes unstaged)
git reset HEAD~1

# Reset to last commit (DISCARDS all changes!)
git reset --hard HEAD~1

# Revert a specific commit (creates new commit)
git revert <commit-hash>
```

---

## 🔍 Viewing Changes & History

```powershell
# Show diff between branches
git diff main..swamy/30jan-work

# Show files changed between branches
git diff --name-only main..swamy/30jan-work

# Show commit history with graphs
git log --oneline --graph --all

# Show commits by author
git log --author="Swamy"

# Show commits in date range
git log --since="2026-01-01" --until="2026-02-03"

# Show commits that modified a specific file
git log -- notebooks/ch02/01_main-chapter-code/01_ch02.ipynb

# Search commit messages
git log --grep="attention"

# Show who modified each line of a file
git blame README.md
```

---

## 🏷️ Tags (For Milestones)

```powershell
# Create annotated tag
git tag -a v0.1.0 -m "Completed Chapter 2"

# Create lightweight tag
git tag ch02-complete

# List all tags
git tag

# Push tag to remote
git push origin v0.1.0

# Push all tags
git push --tags

# Delete local tag
git tag -d v0.1.0

# Delete remote tag
git push origin --delete v0.1.0

# Checkout specific tag
git checkout v0.1.0
```

---

## 🔀 Merging & Pull Requests

```powershell
# Merge branch into current branch
git merge swamy/30jan-work

# Merge with no fast-forward (creates merge commit)
git merge --no-ff swamy/30jan-work

# Abort merge if conflicts
git merge --abort

# Show merge conflicts
git diff --name-only --diff-filter=U

# After resolving conflicts
git add .
git commit -m "merge: resolve conflicts between main and swamy/30jan-work"
```

**Pull Request Workflow**:
1. Push your branch: `git push -u origin swamy/30jan-work`
2. Go to GitHub repository
3. Click "Compare & pull request"
4. Fill in PR description
5. Request review (if team-based)
6. Merge when approved

---

## 📦 Stashing (Temporary Storage)

```powershell
# Save current changes without committing
git stash

# Save with descriptive message
git stash save "WIP: attention mechanism implementation"

# List all stashes
git stash list

# Apply most recent stash (keeps stash)
git stash apply

# Apply most recent stash (removes stash)
git stash pop

# Apply specific stash
git stash apply stash@{2}

# Delete specific stash
git stash drop stash@{0}

# Delete all stashes
git stash clear

# Show stash contents
git stash show -p stash@{0}
```

---

## 🔧 Configuration

```powershell
# Show all config
git config --list

# Set user name (global)
git config --global user.name "Swamy"

# Set user email (global)
git config --global user.email "swamy@example.com"

# Set default branch name
git config --global init.defaultBranch main

# Set default editor
git config --global core.editor "code --wait"

# Enable color output
git config --global color.ui auto

# Set line endings (Windows)
git config --global core.autocrlf true
```

---

## 🚀 Common Workflows for This Repository

### Starting New Chapter Work
```powershell
# 1. Ensure you're on main and up to date
git checkout main
git pull origin main

# 2. Create feature branch
git checkout -b swamy/ch03-transformers

# 3. Work on notebooks, make changes

# 4. Stage and commit
git add notebooks/ch03/
git commit -m "feat: add transformer architecture notebook"

# 5. Push to remote
git push -u origin swamy/ch03-transformers
```

### Daily Work Routine
```powershell
# Morning: Update your branch
git checkout swamy/30jan-work
git pull origin swamy/30jan-work

# Work on notebooks...

# Afternoon: Commit progress
git add .
git status
git commit -m "wip: self-attention implementation progress"
git push
```

### Syncing with Main
```powershell
# Get latest main changes
git checkout main
git pull origin main

# Switch back to your branch
git checkout swamy/30jan-work

# Merge main into your branch
git merge main

# Or rebase (cleaner history)
git rebase main

# Push updated branch
git push
```

### Before Creating PR
```powershell
# 1. Check status
git status

# 2. Review changes
git diff main..swamy/30jan-work

# 3. Run tests locally
uv run pytest

# 4. Ensure no linting issues
uv run black --check src/
uv run flake8 src/

# 5. Push final changes
git push

# 6. Create PR on GitHub
```

---

## 🆘 Emergency Commands

```powershell
# Undo last commit (keep changes)
git reset --soft HEAD~1

# Completely reset to remote state
git fetch origin
git reset --hard origin/main

# Recover deleted branch (if you know last commit)
git checkout -b recovered-branch <commit-hash>

# Find lost commits (reflog)
git reflog
git checkout <commit-hash>

# Clean untracked files (preview first!)
git clean -n
git clean -f

# Remove ignored files too
git clean -fdx
```

---

## 📚 Additional Resources

- [Official Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Oh Shit, Git!?!](https://ohshitgit.com/) - Common mistakes and fixes

