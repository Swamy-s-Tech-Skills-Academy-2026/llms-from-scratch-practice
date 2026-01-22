# PowerShell Commands Reference

**Project**: GenAI Email & Report Drafting System  
**Date**: January 15, 2026  
**Purpose**: PowerShell commands and project-specific scripts

---

## 📁 File System Operations

### List Files & Directories

```powershell
# List files in current directory
Get-ChildItem
dir
ls

# List files with details
Get-ChildItem -Force

# List specific file types
Get-ChildItem *.py
Get-ChildItem -Filter "*.md"

# List recursively
Get-ChildItem -Recurse

# List with specific depth
Get-ChildItem -Depth 2

# List only directories
Get-ChildItem -Directory

# List only files
Get-ChildItem -File
```

### Navigate Directories

```powershell
# Change directory
Set-Location src/backend
cd src/backend

# Go to parent directory
Set-Location ..
cd ..

# Go to home directory
Set-Location ~
cd ~

# Go to previous directory
Set-Location -

# Show current directory
Get-Location
pwd
```

### Create & Delete

```powershell
# Create directory
New-Item -ItemType Directory -Name "new_folder"
mkdir new_folder

# Create file
New-Item -ItemType File -Name "file.txt"

# Create file with content
"Content here" | Out-File file.txt

# Delete file
Remove-Item file.txt

# Delete file (force - for read-only/hidden files)
Remove-Item -Force file.txt

# Delete directory (recursive)
Remove-Item -Recurse -Force folder_name

# Delete with confirmation
Remove-Item file.txt -Confirm
```

### Copy & Move

```powershell
# Copy file
Copy-Item source.txt destination.txt

# Copy directory (recursive)
Copy-Item -Recurse source_folder destination_folder

# Move file
Move-Item source.txt destination.txt

# Rename file
Rename-Item old_name.txt new_name.txt
```

---

## 🔍 Search & Filter

### Find Files

```powershell
# Find files by name
Get-ChildItem -Recurse -Filter "*.py"

# Find files matching pattern
Get-ChildItem -Recurse | Where-Object { $_.Name -like "*test*" }

# Find files by size
Get-ChildItem -Recurse | Where-Object { $_.Length -gt 1MB }

# Find recent files (modified in last 24 hours)
Get-ChildItem -Recurse | Where-Object { $_.LastWriteTime -gt (Get-Date).AddDays(-1) }
```

### Search File Contents

```powershell
# Search in single file
Select-String -Pattern "error" -Path app.py

# Search in multiple files
Select-String -Pattern "import flask" -Path *.py

# Search recursively
Get-ChildItem -Recurse -Filter "*.py" | Select-String -Pattern "def "

# Case-insensitive search
Select-String -Pattern "ERROR" -Path *.log -CaseSensitive:$false

# Show context lines
Select-String -Pattern "error" -Path *.py -Context 2
```

---

## 🌍 Environment Variables

### View & Set

```powershell
# View all environment variables
Get-ChildItem Env:

# View specific variable
$env:PATH
$env:FLASK_ENV

# Set environment variable (session only)
$env:FLASK_ENV = "development"
$env:DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/genai_email_report"
$env:JWT_SECRET_KEY = "your-secret-key"
$env:GEMINI_API_KEY = "your-api-key"

# Set multiple variables
$env:FLASK_ENV = "development"
$env:FLASK_DEBUG = "1"

# Remove environment variable
Remove-Item Env:FLASK_ENV
```

### Persistent Variables

```powershell
# Set user environment variable (permanent)
[Environment]::SetEnvironmentVariable("FLASK_ENV", "development", "User")

# Set system environment variable (requires admin)
[Environment]::SetEnvironmentVariable("FLASK_ENV", "development", "Machine")

# Read persistent variable
[Environment]::GetEnvironmentVariable("FLASK_ENV", "User")
```

---

## 📜 Project-Specific Scripts

### Repository Health & Quality

```powershell
# Navigate to repo root
cd D:\SrivariHSSPL-2026\genai-email-report-drafting

# Quick health check
.\tools\psscripts\Quick-HealthCheck.ps1

# Get repository statistics
.\tools\psscripts\Get-RepoStats.ps1

# Get file statistics
.\tools\psscripts\Get-FileStats.ps1

# Get Markdown summary
.\tools\psscripts\Get-MarkdownSummary.ps1
```

### Content Compliance

```powershell
# Test content compliance (Zero-Copy policy)
.\tools\psscripts\Test-ContentCompliance.ps1

# Verify Zero-Copy policy
.\tools\psscripts\Verify-ZeroCopy.ps1

# Find duplicate content
.\tools\psscripts\Find-DuplicateContent.ps1

# Compare documentation files
.\tools\psscripts\Compare-DocFiles.ps1
```

### Documentation & Diagrams

```powershell
# Export Mermaid diagrams to PNG
.\tools\psscripts\Export-Diagrams.ps1

# Validate file references
.\tools\psscripts\Validate-FileReferences.ps1

# Run Markdown lint and Lychee link checker
.\tools\psscripts\Run-MarkdownLintAndLychee.ps1
```

### Run All Scripts

```powershell
# Execute all PowerShell scripts
.\tools\psscripts\Run-AllPSScripts.ps1
```

---

## 🔧 Process & System

### Process Management

```powershell
# List running processes
Get-Process

# Find specific process
Get-Process python
Get-Process | Where-Object { $_.ProcessName -like "*node*" }

# Kill process by name
Stop-Process -Name python

# Kill process by ID
Stop-Process -Id 1234

# Find process using port
Get-NetTCPConnection -LocalPort 5000 | Select-Object OwningProcess
netstat -ano | findstr :5000
```

### System Information

```powershell
# PowerShell version
$PSVersionTable

# System info
Get-ComputerInfo | Select-Object WindowsVersion, OsArchitecture

# Memory usage
Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 10 Name, @{N='Memory(MB)';E={[math]::Round($_.WorkingSet/1MB,2)}}

# Disk space
Get-PSDrive -PSProvider FileSystem
```

---

## 📝 Text Processing

### Read & Write Files

```powershell
# Read file content
Get-Content app.py

# Read first N lines
Get-Content app.py -Head 10

# Read last N lines
Get-Content app.py -Tail 10

# Write to file (overwrite)
"Content" | Out-File file.txt

# Append to file
"More content" | Add-Content file.txt

# Write without BOM (UTF-8)
"Content" | Out-File file.txt -Encoding utf8NoBOM
```

### String Operations

```powershell
# Replace in file
(Get-Content app.py) -replace "old_text", "new_text" | Set-Content app.py

# Count lines
(Get-Content app.py | Measure-Object -Line).Lines

# Count words
(Get-Content README.md | Measure-Object -Word).Words

# Find and display matches
Select-String -Pattern "def \w+" -Path *.py | ForEach-Object { $_.Matches.Value }
```

### File Statistics

```powershell
# Count total files in directory tree
Get-ChildItem -Path . -Recurse -File | Measure-Object | Select-Object Count

# Count files by type
(Get-ChildItem -Recurse -Filter "*.py").Count
(Get-ChildItem -Recurse -Filter "*.md").Count
(Get-ChildItem -Recurse -Filter "*.tsx").Count

# Get file size summary
Get-ChildItem -Recurse -File | Measure-Object -Property Length -Sum | 
  Select-Object @{N='TotalSizeMB';E={[math]::Round($_.Sum/1MB,2)}}

# Count files by extension
Get-ChildItem -Recurse -File | Group-Object Extension | 
  Select-Object Name, Count | Sort-Object Count -Descending
```

### Output Management

```powershell
# Limit command output to first N lines (prevents context overflow)
npm ci 2>&1 | Select-Object -First 50
pytest tests/ -v 2>&1 | Select-Object -First 200
git diff 2>&1 | Select-Object -First 100

# Limit output with Where-Object filtering
Get-Process | Where-Object {$_.WorkingSet -gt 100MB} | Select-Object -First 20

# Common use cases for CI/build output limiting
python -m pytest tests/ -v --cov=. 2>&1 | Select-Object -First 200
npm run build 2>&1 | Select-Object -First 100
docker compose logs 2>&1 | Select-Object -First 50

# Note: 2>&1 redirects errors to output stream before limiting
```

---

## 🚀 Running Commands

### Execute Programs

```powershell
# Run Python
python app.py

# Run Python module
python -m pytest

# Run npm
npm run dev

# Run with arguments
python app.py --debug --port 5001

# Run and capture output
$output = python app.py 2>&1
```

### Command Execution

```powershell
# Run multiple commands (sequential)
python -m black . ; python -m isort .

# Run multiple commands (stop on error)
python -m black --check . && python -m isort --check-only .

# Run in background
Start-Process python -ArgumentList "app.py" -NoNewWindow

# Run and wait
Start-Process python -ArgumentList "app.py" -Wait
```

---

## 📊 Output Formatting

### Format Output

```powershell
# Table format
Get-ChildItem | Format-Table Name, Length, LastWriteTime

# List format
Get-ChildItem | Format-List

# Custom columns
Get-ChildItem | Select-Object Name, @{N='Size(KB)';E={[math]::Round($_.Length/1KB,2)}}

# Sort output
Get-ChildItem | Sort-Object Length -Descending

# Filter output
Get-ChildItem | Where-Object { $_.Length -gt 1000 }
```

### Export Data

```powershell
# Export to CSV
Get-ChildItem | Export-Csv files.csv -NoTypeInformation

# Export to JSON
Get-ChildItem | ConvertTo-Json | Out-File files.json

# Export to clipboard
Get-ChildItem | Out-String | Set-Clipboard
```

---

## 🔄 Complete Workflows

### Backend Development Setup

```powershell
# 1. Navigate to backend
cd D:\SrivariHSSPL-2026\genai-email-report-drafting\src\backend

# 2. Create virtual environment
python -m venv .venv

# 3. Activate virtual environment
.venv\Scripts\Activate.ps1

# 4. Install dependencies
pip install -r requirements.txt

# 5. Set environment variables
$env:DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/genai_email_report"
$env:JWT_SECRET_KEY = "your-secret-key-here"
$env:GEMINI_API_KEY = "your-gemini-api-key"

# 6. Run application
python app.py
```

### Frontend Development Setup

```powershell
# 1. Navigate to frontend
cd D:\SrivariHSSPL-2026\genai-email-report-drafting\src\frontend

# 2. Install dependencies
npm install

# 3. Start development server
npm run dev
```

### Pre-Commit Quality Check

```powershell
# Navigate to backend
cd D:\SrivariHSSPL-2026\genai-email-report-drafting\src\backend

# Run all checks
python -m black --check .
python -m isort --check-only .
flake8 .
pytest -v

# Fix formatting issues
python -m black .
python -m isort .
```

---

## 📊 Quick Reference Card

```powershell
# File System
Get-ChildItem                     # List files (ls, dir)
Set-Location path                 # Change directory (cd)
New-Item -ItemType Directory      # Create folder (mkdir)
Remove-Item -Recurse -Force       # Delete folder

# Search
Select-String -Pattern "text"     # Search in files (grep)
Get-ChildItem -Recurse -Filter    # Find files

# Environment
$env:VAR = "value"                # Set variable
Get-ChildItem Env:                # List all variables

# Process
Get-Process                       # List processes
Stop-Process -Name name           # Kill process

# Text
Get-Content file.txt              # Read file (cat)
"text" | Out-File file.txt        # Write file

# Project Scripts
.\tools\psscripts\Quick-HealthCheck.ps1
.\tools\psscripts\Run-MarkdownLintAndLychee.ps1
.\tools\psscripts\Test-ContentCompliance.ps1
```

---

**Last Updated**: January 15, 2026  
**Repository**: genai-email-report-drafting
