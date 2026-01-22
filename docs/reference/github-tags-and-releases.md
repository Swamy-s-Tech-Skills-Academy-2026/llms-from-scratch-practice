# GitHub Tags and Releases

<!-- markdownlint-disable MD031 MD032 MD040 MD012 -->

**Project**: GenAI Email & Report Drafting System  
**Date**: January 17, 2026  
**Purpose**: Conceptual guide on Git Tags vs GitHub Releases

---

In GitHub, **Tags** and **Releases** are closely related concepts used to **mark, package, and distribute specific versions of your code**, but they serve different purposes and operate at different levels of abstraction.

---

## 1. Tags in Git

### What is a Tag?

A **tag** is a **Git object** that points to a specific commit, typically used to mark a meaningful point in the repository’s history—most commonly a **version**.

### Primary Use

* Mark **immutable checkpoints** in code history
* Identify versions such as `v1.0.0`, `v2.1.3`
* Enable easy checkout of a known-good state

### Types of Tags

1. **Lightweight Tag**

   * Just a pointer to a commit
   * No metadata

   ```bash
   git tag v1.0.0
   ```

2. **Annotated Tag** (recommended)

   * Stored as a full Git object
   * Includes author, date, and message

   ```bash
   git tag -a v1.0.0 -m "Initial stable release"
   ```

### Key Characteristics

* Immutable by convention
* Used by CI/CD pipelines
* Exists at the Git level (independent of GitHub UI)

---

## 2. Releases in GitHub

### What is a Release?

A **release** is a **GitHub feature** built on top of a **tag**, intended for **human consumption and distribution**.

### Primary Use (GitHub Releases)

* Package code for **end users**
* Publish **release notes**
* Attach **binary artifacts** (ZIPs, installers, JARs, Docker manifests)

### What a Release Adds on Top of a Tag

* Title and rich Markdown description
* Changelog / release notes
* Binary assets
* Pre-release flag (`alpha`, `beta`, `rc`)
* Latest release indicator

### Example Workflow

1. Create a tag (`v1.2.0`)
2. Create a GitHub Release based on that tag
3. Upload build artifacts
4. Share release URL with users/customers

---

## 3. Tags vs Releases – Clear Comparison

| Aspect             | Tag         | Release                |
| ------------------ | ----------- | ---------------------- |
| Layer              | Git (VCS)   | GitHub (Platform)      |
| Points to Commit   | Yes         | Yes (via tag)          |
| Metadata           | Minimal     | Rich (notes, assets)   |
| Binary Attachments | No          | Yes                    |
| CI/CD Usage        | Very common | Common                 |
| End-user Focus     | No          | Yes                    |
| Required Together? | No          | Release requires a tag |

---

## 4. Typical Usage Patterns (Real Projects)

### Backend / Enterprise Systems

* **Tags**: Every version used by CI/CD (`v1.3.2`)
* **Releases**: Only for production or customer-facing drops

### Libraries / SDKs

* **Tags**: For versioning
* **Releases**: For changelog, binaries, and adoption clarity

### Internal Microservices

* **Tags only** (often no GitHub Releases)
* Artifacts stored in Docker Registry or Artifactory

---

## 5. Architect-Level Guidance (When to Use What)

**Use Tags when:**

* You need a stable reference for builds or rollbacks
* You want CI pipelines to trigger on versions
* You are managing internal deployments

**Use Releases when:**

* You distribute software to users or customers
* You need auditable version notes
* You ship binaries or installers
* You want visibility and governance

---

## 6. Best Practices

* Follow **Semantic Versioning**: `vMAJOR.MINOR.PATCH`
* Always use **annotated tags**
* Automate release notes via CI
* Treat tags as **immutable**
  triggering re-tagging in production pipelines

---

### One-Line Summary

> **A Tag marks a version in Git; a Release packages and communicates that version to people.**

---

## 7. Tag-Based CI/CD Pipelines (Industry Standard)

### What is a Tag-Based CI/CD Pipeline?

A **tag-based CI/CD pipeline** is a deployment strategy where **builds and releases are triggered only when a Git tag is created**, not on every commit.

This ensures that **only explicitly versioned code** is promoted to higher environments (QA, UAT, Production).

---

## Why Tag-Based Pipelines Matter (Architect View)

| Problem                      | Without Tags     | With Tags     |
| ---------------------------- | ---------------- | ------------- |
| Accidental production deploy | Possible         | Prevented     |
| Version traceability         | Weak             | Strong        |
| Rollback                     | Manual guesswork | Exact version |
| Audit & compliance           | Poor             | Excellent     |
| Release governance           | Ad-hoc           | Controlled    |

**Key Principle:**

> *Commits are for developers. Tags are for releases.*

---

## Typical Flow (End-to-End)

### 1️⃣ Development Phase

* Developers push code to `main` / `develop`
* CI runs:
  * Build
  * Unit tests
  * Static analysis
* **No production deployment**

---

### 2️⃣ Create a Release Tag

```bash
git tag -a v1.4.0 -m "Production release v1.4.0"
git push origin v1.4.0
```

This action signals:

* Code is **approved**
* Version is **immutable**
* Ready for **promotion**

---

### 3️⃣ CI/CD Trigger (on Tag)

Pipeline trigger rule:

```yaml
on:
  push:
    tags:
      - "v*"
```

Triggered steps:

1. Checkout tagged commit
2. Build artifacts
3. Run full test suite
4. Package binaries / Docker images
5. Deploy to:
   * Staging
   * Production (manual approval optional)

---

### 4️⃣ Artifact Versioning

| Artifact Type | Version            |
| ------------- | ------------------ |
| Docker Image  | `myapp:v1.4.0`     |
| JAR / ZIP     | `myapp-1.4.0.jar`  |
| Helm Chart    | `1.4.0`            |
| Release Notes | Linked to `v1.4.0` |

---

## Environment Promotion Strategy

```
Commit → CI
       ↓
     Tag v1.4.0
       ↓
   Build Once
       ↓
   QA → UAT → PROD
```

**Critical Rule:**

> *Same artifact promoted across environments (no rebuilds).*

---

## Rollback Strategy (Huge Advantage)

If production fails:

```bash
Deploy artifact: v1.3.2
```

✔ No rebuild
✔ No guesswork
✔ Proven binary

This is **why tags are mandatory in mature systems**.

---

## Example: GitHub Actions (Conceptual)

Using **GitHub Actions**:

```yaml
name: Release Pipeline

on:
  push:
    tags:
      - "v*"

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: mvn clean package
      - run: docker build -t myapp:${{ github.ref_name }} .
      - run: docker push myapp:${{ github.ref_name }}
```

---

## Best Practices (Interview-Ready)

✅ Use **annotated tags only**
✅ Enforce **semantic versioning**
✅ Protect `main` branch
✅ Restrict who can create tags
✅ Automate changelogs from commits
✅ Never retag production versions

---

## When NOT to Use Tag-Based Pipelines

* Rapid prototyping
* Internal experiments
* Feature previews

In those cases, **branch-based or commit-based pipelines** are acceptable.

---

## One-Line Interview Answer

> **“We trigger production deployments only on Git tags, ensuring immutable, versioned, auditable releases with safe rollback.”**

---

## 8. Project Strategy: Tag & Release for Dual Workflows

This section outlines the specific strategy for the **GenAI Email & Report Drafting System**, which contains two distinct workflows: `ci-frontend.yml` and `ci-python.yml`.

### 1. Core Design Decision

We have **one repository** with **two deployable concerns**:
* Frontend (React)
* Backend (Python/Flask)

**Decision:** **Unified Versioning**
We will version them **together** using a single tag.

**Why?**
* Frontend tightly depends on backend API contracts.
* Simpler governance and release management.
* Avoids accidental incompatibility between frontend and backend versions.

### 2. Unified Tag Strategy

**Format:** `vMAJOR.MINOR.PATCH` (e.g., `v1.0.0`)

**Meaning:**
* One tag = **one system release**
* Both workflows react to the **same tag**

### 3. Workflow Trigger Strategy

**Frontend Workflow (`ci-frontend.yml`)**
```yaml
on:
  push:
    tags:
      - "v*"
```

**Backend Workflow (`ci-python.yml`)**
```yaml
on:
  push:
    tags:
      - "v*"
```

**Result:** One tag triggers both pipelines, guaranteeing compatibility.

### 4. Selective Execution (Optimization)

To avoid unnecessary runs during Pull Requests, we use `paths` filters:

**Frontend:**
```yaml
on:
  push:
    tags: ["v*"]
  pull_request:
    paths: ["src/frontend/**"]
```

**Backend:**
```yaml
on:
  push:
    tags: ["v*"]
  pull_request:
    paths: ["src/backend/**"]
```

### 5. Release Creation Strategy

**Goal:** Only ONE GitHub Release per tag.

**Approach:**
Instead of having both workflows try to create a release (resulting in race conditions or duplicates), we use a **Coordinator Workflow**.

### 6. Release-Orchestrator Workflow

We recommend creating `.github/workflows/release.yml`:

**Responsibility:**
* Trigger on tag `v*`
* Create the GitHub Release entry
* Aggregate artifacts (if any)
* Publish Release Notes

### 7. Version Ownership Rule

| Component | Responsibility |
| -- | -- |
| **Tag** | Architect / Lead (Manual Trigger) |
| **Frontend CI** | Build & Test Frontend |
| **Backend CI** | Build & Test Backend |
| **Release** | Orchestrator (Create GitHub Release) |

### 8. Example End-to-End Flow

```
feature/* → PR → main
                 ↓
          git tag v0.2.0
                 ↓
        ┌───────────────┐
        │   Tag Push    │
        └───────────────┘
          ↓           ↓
   ci-frontend    ci-python
          ↓           ↓
       FE OK       BE OK
              ↓
        GitHub Release v0.2.0
          (Orchestrator)
```

### 9. When to Split Versions?

We might move to `frontend-v1.2.0` and `backend-v1.4.0` **only when**:
* Frontend & backend deploy independently to completely different targets (e.g., Mobile App vs Cloud API).
* They have vastly different release cadences.

For now, independent versioning is **over-engineering**.

### 10. Strategy Summary

> **“We use a unified semantic version tag per system release. Both frontend and backend pipelines trigger on the same tag, ensuring API compatibility, while release orchestration is centralized to maintain governance.”**

---

## 9. Implementation Guide & Release Governance

This section details the architect-approved "Target State" for our CI/CD pipelines to align with the unified tag strategy.

### Target State (What We Want)

| Event               | Frontend CI | Backend CI | Release  |
| ------------------- | ----------- | ---------- | -------- |
| PR to `main`        | ✅           | ✅          | ❌        |
| Push to `main`      | ✅           | ✅          | ❌        |
| **Tag push (`v*`)** | ✅           | ✅          | ✅        |
| Manual trigger      | ✅           | ✅          | Optional |

**This ensures:**
* Continuous validation on `main`.
* **Only tagged versions represent releases**.
* Frontend & backend are always released together.

### High-Level Flow

```
PR → main
   ↓
CI (frontend + backend)
   ↓
git tag v0.1.0
   ↓
CI (frontend + backend)
   ↓
Release workflow (release.yml)
```

### 1. Minimal Changes to EXISTING Workflows

To implement this, we only ADD tag triggers to our existing workflows. We do **not** remove existing triggers.

**Updated `ci-frontend.yml` (`on:` section):**
```yaml
on:
  workflow_dispatch:
  push:
    branches: [main]
    tags: ["v*"]     # <-- Added
    paths:
      - 'src/frontend/**'
      - '.github/workflows/ci-frontend.yml'
  pull_request:
    branches: [main]
    paths:
      - 'src/frontend/**'
      - '.github/workflows/ci-frontend.yml'
```

**Updated `ci-python.yml` (`on:` section):**
```yaml
on:
  workflow_dispatch:
  push:
    branches: [main]
    tags: ["v*"]     # <-- Added
    paths:
      - 'src/backend/**'
      - '.github/workflows/ci-python.yml'
  pull_request:
    branches: [main]
    paths:
      - 'src/backend/**'
      - '.github/workflows/ci-python.yml'
```

### 2. Why We Do NOT Create Releases in These Workflows?

**Critical Architecture Rule:**
> *CI pipelines validate code. Release pipelines create versions.*

If frontend and backend both try to create a GitHub Release, we risk **race conditions**, **duplicate releases**, and **broken governance**. Therefore, we separate concerns.

### 3. The Release Workflow (`release.yml`)

We use a dedicated workflow that:
* Runs **only on tags**.
* Creates the GitHub Release.
* Acts as the single source of truth for release artifacts.

### 4. Versioning Discipline (Non-Negotiable)

| Version  | Meaning                |
| -------- | ---------------------- |
| `v0.1.0` | First end-to-end MVP   |
| `v0.2.0` | New GenAI features     |
| `v0.2.1` | Bug fix                |
| `v1.0.0` | Portfolio-grade stable |

**Rule:** Never retag. Never delete tags (traceability).

### 5. Step-by-Step Release Process

1. **Pull latest main:**
   ```bash
   git checkout main
   git pull origin main
   ```

2. **Create and push tag:**
   ```bash
   git tag -a v0.1.0 -m "Initial MVP release"
   git push origin v0.1.0
   ```

3. **Automated Actions:**
   * Frontend CI runs validation.
   * Backend CI runs validation.
   * Release workflow creates the GitHub Release.
   * Release notes are auto-generated.

### 6. Interview-Ready Explanation

> **“We run frontend and backend CI on every PR and main push. Production releases are triggered only by semantic version tags, which activate both pipelines and a dedicated release workflow to ensure traceability, immutability, and governance.”**

---

## 10. Troubleshooting: Why Tags / Releases Are Not Visible

If you have set up the workflows but are not seeing the release pipeline trigger, follow this precise diagnostic checklist.

### 1. Most Common Cause: Tag Was Never Pushed

Creating a tag **locally** is not enough. GitHub Actions respond only to **pushed** tags.

**❌ This does NOT trigger anything:**
```bash
git tag v0.1.0
```

**✅ This is mandatory:**
```bash
git push origin v0.1.0
```
*Or to push all tags:* `git push origin --tags`

**Verification:**
Run `git ls-remote --tags origin`. If you do not see `refs/tags/v0.1.0`, GitHub never received the tag.

### 2. Verify Tag Exists on GitHub

Go to your repository → **Code** tab → look for **“Tags”** near the branch selector.
* **Expected:** `v0.1.0`
* **If missing:** Workflows will never trigger.

### 3. Check Tag Name Format

Your workflows are configured to trigger only on:
```yaml
tags:
  - "v*"
```

| Status | Tag Example |
| :--- | :--- |
| **✅ Valid** | `v0.1.0`, `v1.0.0`, `v0.2.0-beta` |
| **❌ Invalid** | `0.1.0`, `release-1`, `version1` |

### 4. Verify Workflow Files

Each workflow must be in its own file in `.github/workflows/`:
1. `ci-frontend.yml`
2. `ci-python.yml`
3. `release.yml`

**🚨 Critical Rule:** Do not combine these into a single file. GitHub will silently ignore them.

### 5. Check Workflows Are Enabled

Go to **Repo → Actions → Workflows** and ensure all three workflows are enabled. New workflows may sometimes default to disabled in forked or restricted repositories.

### 6. Expected End-to-End Behavior

When you run:
```bash
git tag -a v0.1.0 -m "Initial MVP release"
git push origin v0.1.0
```

You should see:
1. **GitHub UI (Code):** The tag `v0.1.0` appears.
2. **GitHub UI (Actions):** Three workflows trigger (Frontend CI, Python CI, Release).
3. **GitHub UI (Releases):** A new release "GenAI Email & Report Drafting v0.1.0" is created.

### 7. One-Minute Self-Test

Run these commands in your terminal:
```bash
git status
git branch
git tag
git ls-remote --tags origin
```
*If `git tag` shows the tag locally but `ls-remote` does not show it on origin, you have a **push issue**.*

### 8. Architect-Level Rule

> **“GitHub Actions do not react to intent. They react only to pushed Git objects.”**



