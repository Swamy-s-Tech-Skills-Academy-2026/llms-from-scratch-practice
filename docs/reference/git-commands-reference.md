# Git Commands Reference

**Project**: GenAI Email & Report Drafting System  
**Date**: January 15, 2026  
**Purpose**: Git commands for repository management and version control

---

## 📋 Status & Inspection Commands

### Check Repository Status

```powershell
# Short status (concise output)
git status --short

# Porcelain status (script-friendly)
git status --porcelain

# Full status with detailed information
git status

# Check status of specific folder
git status docs/diagrams/
```

**Use cases:**

- Quickly see modified, staged, and untracked files
- Verify working tree cleanliness before commits
- Check branch status relative to remote

---

### View Commit History

```powershell
# Last 5 commits (one line each)
git log --oneline -5

# Last 10 commits with graph
git log --oneline --graph -10

# Full commit details
git log -3

# Commits affecting specific file
git log --oneline -- docs/diagrams/README.md

# Commits by author
git log --author="Viswanatha Swamy" --oneline
```

**Output format:**

```text
f61c3fd (HEAD -> swamy/12jan-work) Add CI pipeline workitem documentation
ed06fe0 (origin/swamy/12jan-work) Update architecture diagrams
```

---

### Check File Changes

```powershell
# Show modified files (uncommitted)
git diff --name-only

# Show modified files (staged)
git diff --cached --name-only

# Show all changes with diff
git diff

# Summarize changes by file
git diff --stat

# Show changes in specific file
git diff README.md
```

---

### List Tracked Files

```powershell
# All tracked files
git ls-files

# Specific pattern
git ls-files docs/diagrams/*.png

# Untracked files
git ls-files --others --exclude-standard

# Show file status
git ls-files --stage
```

**Example output:**

```text
docs/diagrams/system-architecture-requirements.png
docs/diagrams/system-architecture-simple.png
docs/diagrams/system-architecture.png
```

---

## 🔄 Remote Operations

### Check Remote Configuration

```powershell
# View remote repositories
git remote -v

# Show remote details
git remote show origin

# List all remotes
git remote
```

**Example output:**

```text
origin  https://github.com/Srivari-Hema-SSPL-2026/genai-email-report-drafting.git (fetch)
origin  https://github.com/Srivari-Hema-SSPL-2026/genai-email-report-drafting.git (push)
```

---

## ✅ Commands Executed During Workspace Review (Jan 14, 2026)

These are the key commands actually executed during the deep-dive review and quality validation.

### Quality & Compliance Scripts

```powershell
# Find repeated headings / likely duplicate content
./tools/psscripts/Find-DuplicateContent.ps1

# Validate Markdown + links (markdownlint-cli2 + lychee)
./tools/psscripts/Run-MarkdownLintAndLychee.ps1
```

### Repository Inspection

```powershell
# Verify repo remote points to the canonical GitHub URL
git remote -v

# Confirm working tree cleanliness
git status --porcelain

# Summarize deltas by file
git diff --stat
```

### Miscellaneous (PowerShell)

```powershell
# List documentation files (used for filename verification)
dir docs/*.md
```

---

### Sync with Remote

```powershell
# Fetch latest changes (doesn't merge)
git fetch origin

# Pull latest changes (fetch + merge)
git pull origin swamy/12jan-work

# Push local commits to remote
git push origin swamy/12jan-work

# Push with upstream tracking
git push -u origin swamy/12jan-work

# Force push (use with caution!)
git push --force origin swamy/12jan-work
```

---

## 📝 Staging & Committing

### Stage Files

```powershell
# Stage specific file
git add docs/diagrams/system-architecture.png

# Stage all PNG files
git add docs/diagrams/*.png

# Stage all changes in directory
git add docs/

# Stage all modified files
git add -u

# Stage all files (new + modified)
git add .

# Interactive staging
git add -p
```

---

### Commit Changes

```powershell
# Commit with message
git commit -m "docs: update architecture diagrams"

# Commit with detailed message
git commit -m "docs: migrate diagrams from inline Mermaid to PNG references

- Export all 4 diagrams to PNG (419.74 KB total)
- Update markdown files with image references
- Add mermaid-config.json for consistent exports
- Create Export-Diagrams.ps1 automation script
- Update .gitattributes for binary handling
"

# Commit all tracked changes
git commit -a -m "fix: resolve path references"

# Amend last commit
git commit --amend --no-edit

# Amend with new message
git commit --amend -m "New message"
```

---

## 🌿 Branch Management

### View Branches

```powershell
# List local branches
git branch

# List all branches (local + remote)
git branch -a

# List remote branches
git branch -r

# Show current branch
git branch --show-current

# Verbose (shows tracking info)
git branch -vv
```

---

### Create & Switch Branches

```powershell
# Create new branch
git branch feature/new-feature

# Switch to branch
git checkout swamy/12jan-work

# Create and switch in one command
git checkout -b feature/new-feature

# Switch to previous branch
git checkout -

# Delete local branch
git branch -d feature/old-feature

# Force delete (unmerged changes)
git branch -D feature/old-feature
```

---

## 🔍 Inspection & Debugging

### Check File Information

```powershell
# Show file at specific commit
git show HEAD:docs/README.md

# Show commit details
git show f61c3fd

# Show changes in commit
git show --stat f61c3fd

# Show file history
git log --follow docs/diagrams/README.md
```

---

### Compare Changes

```powershell
# Compare branches
git diff main..swamy/12jan-work

# Compare current branch to main using merge-base (shows what your branch adds on top of main)
git diff main...HEAD

# List only changed files compared to main (merge-base)
git diff --name-only main...HEAD

# Summary of changed files compared to main (merge-base)
git diff --stat main...HEAD

# Compare with remote
git diff origin/main

# Compare specific files
git diff main swamy/12jan-work -- docs/README.md

# Compare a specific file/path compared to main (merge-base)
git diff main...HEAD -- docs/reports/01_final-report.md
git diff --name-only main...HEAD -- docs/reference

# Show word-level diff
git diff --word-diff
```

---

## 🔧 Useful Combinations

### Pre-Commit Workflow

```powershell
# 1. Check what changed
git status --short

# 2. Review specific changes
git diff docs/diagrams/

# 3. Stage changes
git add docs/diagrams/*.png
git add docs/*.md
git add .gitattributes

# 4. Verify staged files
git status

# 5. Commit with message
git commit -m "docs: add diagram exports"

# 6. Push to remote
git push origin swamy/12jan-work
```

---

### Verification Before Push

```powershell
# 1. Check current status
git status

# 2. Review recent commits
git log --oneline -5

# 3. Verify remote configuration
git remote -v

# 4. Check branch relationship
git branch -vv

# 5. Push
git push origin swamy/12jan-work
```

---

### Post-Migration Verification

```powershell
# 1. Verify PNG files tracked
git ls-files docs/diagrams/*.png

# 2. Check file sizes
git ls-files -s docs/diagrams/*.png

# 3. Verify no uncommitted changes
git status --short

# 4. Check remote sync status
git status
```

**Expected output:**

```text
On branch swamy/12jan-work
Your branch is up to date with 'origin/swamy/12jan-work'.

nothing to commit, working tree clean
```

---

## 🚀 Advanced Operations

### Stash Changes

```powershell
# Save changes temporarily
git stash

# Save with message
git stash save "WIP: diagram exports"

# List stashes
git stash list

# Apply most recent stash
git stash apply

# Apply and remove stash
git stash pop

# Clear all stashes
git stash clear
```

---

### Reset & Undo

```powershell
# Unstage file (keep changes)
git reset HEAD docs/README.md

# Unstage all (keep changes)
git reset HEAD

# Discard local changes in file
git checkout -- docs/README.md

# Discard all local changes
git reset --hard HEAD

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1
```

---

### Clean Up

```powershell
# Show what would be removed
git clean -n

# Remove untracked files
git clean -f

# Remove untracked files and directories
git clean -fd

# Remove ignored files too
git clean -fdx
```

---

## 📊 Repository Information

### Statistics

```powershell
# Count commits
git rev-list --count HEAD

# Show contributors
git shortlog -sn

# File history statistics
git log --stat

# Show largest files
git rev-list --objects --all | git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | awk '/^blob/ {print substr($0,6)}' | sort --numeric-sort --key=2 | tail -10
```

---

### Search & Find

```powershell
# Search in commit messages
git log --grep="diagram"

# Search in code
git log -S"mermaid" --oneline

# Find commits that changed file
git log --all -- docs/diagrams/README.md

# Find deleted files
git log --diff-filter=D --summary
```

---

## 🎯 Project-Specific Commands

### Diagram Migration Workflow

```powershell
# 1. Check PNG files exist
Get-ChildItem docs\diagrams\*.png | Select-Object Name

# 2. Stage diagram files
git add docs/diagrams/*.png
git add docs/diagrams/README.md
git add docs/diagrams/mermaid-config.json

# 3. Stage updated markdown
git add README.md
git add docs/*.md

# 4. Stage config files
git add .gitattributes

# 5. Stage automation script
git add tools/psscripts/Export-Diagrams.ps1

# 6. Verify staged files
git status

# 7. Commit
git commit -m "docs: migrate diagrams from inline Mermaid to PNG references"

# 8. Push
git push origin swamy/12jan-work
```

---

### CI Workflow Verification

```powershell
# 1. Check workflow files
git ls-files .github/workflows/*.yml

# 2. View last CI commit
git log --oneline --grep="CI" -5

# 3. Check if workflows changed
git diff main..swamy/12jan-work .github/workflows/
```

---

## 🔐 Best Practices

### Before Committing

1. **Review changes:**

   ```powershell
   git status
   git diff
   ```

2. **Stage selectively:**

   ```powershell
   git add -p  # Interactive staging
   ```

3. **Write descriptive messages:**

   ```powershell
   git commit -m "type: brief description
   
   - Detail 1
   - Detail 2
   - Detail 3
   "
   ```

### Before Pushing

1. **Verify commits:**

   ```powershell
   git log --oneline -5
   ```

2. **Check branch status:**

   ```powershell
   git status
   git branch -vv
   ```

3. **Ensure working tree is clean:**

   ```powershell
   git status --short  # Should be empty
   ```

---

## 📚 Commit Message Convention

**Format:**

```text
<type>: <brief description>

<detailed description>
- <change 1>
- <change 2>
- <change 3>
```

**Types:**

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting)
- `refactor:` - Code refactoring
- `test:` - Test additions/changes
- `chore:` - Build process, dependencies
- `ci:` - CI changes (automated testing workflows)

**Examples:**

```powershell
# Good commit message
git commit -m "docs: migrate diagrams from inline Mermaid to PNG references

- Export all 4 diagrams to PNG (419.74 KB total)
- Update markdown files with image references
- Add mermaid-config.json for consistent exports
- Create Export-Diagrams.ps1 automation script
- Update .gitattributes for binary handling
- Preserve ASCII fallbacks in collapsible sections
"

# Feature addition
git commit -m "feat: add email generation with tone selection

- Implement professional, formal, casual, friendly tones
- Add tone validation in prompt engine
- Update frontend UI with tone selector dropdown
- Add backend API endpoint for tone-based generation
"

# Bug fix
git commit -m "fix: resolve path reference issues in diagram exports

- Correct relative paths in README.md (docs/diagrams/)
- Fix paths in docs/*.md files (diagrams/)
- Update Export-Diagrams.ps1 script parameter handling
"
```

---

## 🛠️ Troubleshooting

### Common Issues

#### Your branch is ahead of origin by X commits

```powershell
git push origin swamy/12jan-work
```

#### Your branch has diverged

```powershell
git pull --rebase origin swamy/12jan-work
git push origin swamy/12jan-work
```

#### Untracked files present

```powershell
git clean -n  # Preview
git clean -f  # Remove
```

#### Failed to push (rejected)

```powershell
git pull origin swamy/12jan-work
# Resolve conflicts if any
git push origin swamy/12jan-work
```

---

## 📖 Quick Reference Card

```powershell
# Status & Info
git status                      # Working tree status
git log --oneline -5           # Recent commits
git branch -vv                 # Branch tracking info

# Staging & Committing
git add <file>                 # Stage file
git commit -m "message"        # Commit staged changes
git commit -a -m "message"     # Stage all + commit

# Remote Sync
git fetch origin               # Fetch changes
git pull origin <branch>       # Fetch + merge
git push origin <branch>       # Push commits

# Branch Operations
git branch                     # List branches
git checkout <branch>          # Switch branch
git checkout -b <new-branch>   # Create + switch

# Inspection
git diff                       # Uncommitted changes
git diff --cached              # Staged changes
git show HEAD                  # Last commit details

# Undo Operations
git reset HEAD <file>          # Unstage file
git checkout -- <file>         # Discard changes
git reset --soft HEAD~1        # Undo commit, keep changes
```

---

**Last Updated**: January 13, 2026  
**Branch**: swamy/12jan-work  
**Repository**: genai-email-report-drafting
