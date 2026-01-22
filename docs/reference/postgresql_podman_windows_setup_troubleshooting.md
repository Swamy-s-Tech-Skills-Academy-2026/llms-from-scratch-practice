# PostgreSQL with Podman on Windows

<!-- markdownlint-disable MD040 -->

This document provides a **single, end‑to‑end guide** covering **setup, verification, and troubleshooting** for running PostgreSQL in a Podman (Docker‑compatible) environment on **Windows**, and connecting to it from **VS Code**.

It consolidates all steps and lessons learned so you can follow it linearly or jump directly to troubleshooting.

---

## 1. Prerequisites

### Required Software

* Windows 10/11
* Podman Desktop or Podman CLI (WSL2 / Podman Machine)
* VS Code
* VS Code PostgreSQL extension (`ms-ossdata.vscode-postgresql`)

Verify Podman:

```powershell
podman --version
```

Verify Podman Machine:

```powershell
podman machine list
```

---

## 2. Start Podman Machine

Podman runs containers **inside a Linux VM** on Windows.

```powershell
podman machine start
```

Verify:

```powershell
podman machine info
```

---

## 3. PostgreSQL via docker-compose (Podman compatible)

Example service definition:

```yaml
services:
  postgres:
    image: postgres:16-alpine
    container_name: genai_email_report_postgres
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: genai_email_report
    ports:
      - "5432:5432"
    volumes:
      - genai_email_report_data:/var/lib/postgresql/data
      - ./init:/docker-entrypoint-initdb.d
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  genai_email_report_data:
```

Start services:

```powershell
docker-compose up -d
```

---

## 4. Verify PostgreSQL Container

```powershell
podman ps
```

Expected:

```
STATUS: Up (healthy)
PORTS: 0.0.0.0:5432->5432/tcp
```

Check logs:

```powershell
podman logs genai_email_report_postgres
```

Look for:

```
database system is ready to accept connections
```

---

## 5. Identify the Correct Host IP (CRITICAL)

On Windows, **localhost is unreliable with Podman**.

### Step 1: SSH into Podman VM

```powershell
podman machine ssh
```

### Step 2: Find external VM IP

```bash
ip addr show
```

Example output:

```
eth0 inet 172.21.112.132/20
```

➡ **Use the `eth0` IP (example: `172.21.112.132`)**

Exit VM:

```bash
exit
```

---

## 6. VS Code PostgreSQL Connection Settings

Use the following values:

| Field    | Value                                  |
| -------- | -------------------------------------- |
| Server   | `<Podman-VM-IP>` (e.g. 172.21.112.132) |
| Port     | 5432                                   |
| Username | postgres                               |
| Password | postgres                               |
| Database | genai_email_report                     |
| SSL      | **Disable**                            |

Click **Test Connection** → **Save & Connect**.

---

## 7. Why SSL Must Be Disabled (Local Dev)

Default PostgreSQL container images:

* Do **not** enable SSL
* Do **not** generate certificates

If SSL is forced, you will see:

```
server does not support SSL, but SSL was required
```

✔ Disabling SSL is correct for **local development**.

---

## 8. Sanity Checks (Optional but Recommended)

### From inside container

```powershell
podman exec -it genai_email_report_postgres psql -U postgres -d genai_email_report
```

### From VM

```powershell
podman machine ssh
psql -h 127.0.0.1 -U postgres -d genai_email_report
```

---

## 9. Common Errors & Troubleshooting

### ❌ `docker` command not found

**Cause:** Docker Desktop not installed
**Fix:** Use `podman` or install Docker CLI only

---

### ❌ VS Code cannot connect to `localhost`

**Cause:** Podman runs inside a VM
**Fix:** Use Podman machine IP (`eth0`)

---

### ❌ `connection timed out`

**Cause:** Wrong host or port not exposed
**Fix:**

* Verify `ports: "5432:5432"`
* Verify Podman machine running

---

### ❌ `server does not support SSL`

**Cause:** Client forcing SSL
**Fix:** Disable SSL in VS Code

---

### ❌ Tables not visible

**Cause:** Connected to wrong database
**Fix:** Ensure `genai_email_report` selected

---

## 10. Best Practices

* Always use **Podman VM IP**, not localhost
* Keep DB credentials in `.env`
* Create a **non‑postgres app user** for application access
* Use migrations (Flyway / Alembic) for schema changes
* Enable SSL only in staging/production

---

## 11. Final Architecture Summary

```
VS Code (Windows)
   ↓
Podman VM (eth0 IP)
   ↓
PostgreSQL Container (5432)
```

This is the correct mental model for Podman on Windows.

---

## 12. Next Enhancements (Optional)

* pgAdmin or Adminer container
* Role‑based DB access
* Backup & restore strategy
* CI‑ready compose profile

---

**Status:** This setup is now production‑grade for local development.
