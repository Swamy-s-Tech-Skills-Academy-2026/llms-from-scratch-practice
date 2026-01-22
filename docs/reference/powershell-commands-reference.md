# PowerShell Commands Reference

**Project**: LLMs From Scratch Practice (STSA 2026)  
**Purpose**: Useful PowerShell commands for working in this repo

---

## 📁 File System Basics

```powershell
# List files
Get-ChildItem
dir
ls

# Change directory
cd D:\STSA-2026\llms-from-scratch-practice

# Create folder
New-Item -ItemType Directory -Name "data"

# Create file
New-Item -ItemType File -Name "notes.md"

# Remove file or folder
Remove-Item notes.md
Remove-Item -Recurse -Force .venv
```

---

## 🔍 Search

```powershell
# Find files by extension
Get-ChildItem -Recurse -Filter "*.py"

# Search inside files
Get-ChildItem -Recurse -Filter "*.md" | Select-String -Pattern "uv sync"
```

---

## 🌍 Environment Variables

```powershell
# Show PATH
$env:PATH

# Set a variable (session only)
$env:PYTHONPATH = "D:\STSA-2026\llms-from-scratch-practice\src"

# Remove a variable (session only)
Remove-Item Env:PYTHONPATH
```

