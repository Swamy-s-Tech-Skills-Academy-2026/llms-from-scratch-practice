# Docker Commands Reference

**Project**: GenAI Email & Report Drafting System  
**Date**: January 15, 2026  
**Purpose**: Docker/Podman and Compose commands for local development

---

## 🐳 Docker/Podman Compose (Recommended)

Use the same Compose file with Podman by replacing `docker compose` with `podman compose` in the commands below.

### Start Services

```powershell
# Navigate to infra directory
cd infra

# Start all services (detached mode)
docker compose up -d

# Start with build
docker compose up -d --build

# Start specific service
docker compose up -d postgres

# Start and follow logs
docker compose up
```

### Stop Services

```powershell
# Stop all services
docker compose down

# Stop and remove volumes (WARNING: deletes data)
docker compose down -v

# Stop specific service
docker compose stop postgres

# Restart services
docker compose restart
```

### View Status & Logs

```powershell
# Show running containers
docker compose ps

# Show all containers (including stopped)
docker compose ps -a

# View logs (all services)
docker compose logs

# View logs (specific service)
docker compose logs postgres

# Follow logs in real-time
docker compose logs -f

# Follow logs for specific service
docker compose logs -f postgres

# Show last N lines
docker compose logs --tail=100
```

---

## 🗄️ PostgreSQL Container

### Connect to Database

```powershell
# Execute psql in container
docker compose exec postgres psql -U postgres -d genai_email_report

# Execute single command
docker compose exec postgres psql -U postgres -d genai_email_report -c "SELECT * FROM users;"

# Run SQL file
docker compose exec -T postgres psql -U postgres -d genai_email_report < infra/database/schema.sql
```

### Database Operations

```powershell
# List databases
docker compose exec postgres psql -U postgres -c "\l"

# List tables
docker compose exec postgres psql -U postgres -d genai_email_report -c "\dt"

# Describe table
docker compose exec postgres psql -U postgres -d genai_email_report -c "\d users"

# Check table counts
docker compose exec postgres psql -U postgres -d genai_email_report -c "SELECT COUNT(*) FROM users;"
```

### Backup & Restore

```powershell
# Backup database
docker compose exec postgres pg_dump -U postgres genai_email_report > backup.sql

# Restore database
docker compose exec -T postgres psql -U postgres -d genai_email_report < backup.sql

# Backup specific table
docker compose exec postgres pg_dump -U postgres -t users genai_email_report > users_backup.sql
```

---

## 🐋 Docker/Podman Commands (General)

### Container Management

```powershell
# List running containers
docker ps

# List all containers
docker ps -a

# Start container
docker start <container_name>

# Stop container
docker stop <container_name>

# Remove container
docker rm <container_name>

# Remove all stopped containers
docker container prune
```

### Image Management

```powershell
# List images
docker images

# Pull image
docker pull postgres:13

# Remove image
docker rmi postgres:13

# Remove unused images
docker image prune

# Remove all unused images
docker image prune -a
```

### Volume Management

```powershell
# List volumes
docker volume ls

# Inspect volume
docker volume inspect genai_postgres_data

# Remove volume (WARNING: deletes data)
docker volume rm genai_postgres_data

# Remove unused volumes
docker volume prune
```

### Network Management

```powershell
# List networks
docker network ls

# Inspect network
docker network inspect genai_network

# Remove network
docker network rm genai_network
```

---

## 🔧 Docker Compose File Reference

### Project docker-compose.yml

Location: `infra/docker-compose.yml`

```yaml
services:
  postgres:
    image: postgres:13
    container_name: genai_postgres
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: genai_email_report
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./database/schema.sql:/docker-entrypoint-initdb.d/schema.sql
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  postgres_data:
```

### Environment Variables

Create `.env` file in `infra/` directory:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=genai_email_report
```

---

## 🚀 Quick Setup Workflow

### First Time Setup

```powershell
# 1. Navigate to infra directory
cd infra

# 2. Start PostgreSQL
docker compose up -d

# 3. Verify container is running
docker compose ps

# 4. Check logs for any errors
docker compose logs postgres

# 5. Verify database is ready
docker compose exec postgres psql -U postgres -c "\l"

# 6. Apply schema (if not auto-loaded)
docker compose exec -T postgres psql -U postgres -d genai_email_report < database/schema.sql
```

### Daily Development

```powershell
# Start services
cd infra && docker compose up -d

# ... do development work ...

# Stop services (preserves data)
docker compose stop

# Or stop and remove containers (preserves data in volume)
docker compose down
```

### Clean Reset (Delete All Data)

```powershell
# Stop and remove containers + volumes
cd infra
docker compose down -v

# Restart fresh
docker compose up -d
```

---

## 🔍 Troubleshooting

### Container Won't Start

```powershell
# Check logs for errors
docker compose logs postgres

# Check container status
docker compose ps -a

# Remove and recreate
docker compose down
docker compose up -d
```

### Port Already in Use

```powershell
# Find process using port 5432
netstat -ano | findstr :5432

# Or use different port in docker-compose.yml
ports:
  - "5433:5432"

# Connect with new port
$env:DATABASE_URL = "postgresql://postgres:postgres@localhost:5433/genai_email_report"
```

### Database Connection Failed

```powershell
# Verify container is running
docker compose ps

# Check PostgreSQL is ready
docker compose exec postgres pg_isready -U postgres

# Test connection
docker compose exec postgres psql -U postgres -c "SELECT 1;"

# Check container IP
docker inspect genai_postgres | Select-String IPAddress
```

### Volume Issues

```powershell
# List volumes
docker volume ls

# Inspect volume
docker volume inspect infra_postgres_data

# Remove volume (resets database)
docker compose down -v
docker compose up -d
```

---

## 📊 Quick Reference Card

```powershell
# Docker Compose
docker compose up -d              # Start services
docker compose down               # Stop services
docker compose ps                 # Show status
docker compose logs -f            # Follow logs
docker compose exec postgres psql # Database shell

# Container Operations
docker ps                         # List running
docker ps -a                      # List all
docker stop <name>                # Stop container
docker rm <name>                  # Remove container

# Database
docker compose exec postgres psql -U postgres -d genai_email_report
docker compose exec postgres pg_dump -U postgres genai_email_report > backup.sql

# Cleanup
docker compose down -v            # Remove with volumes
docker system prune               # Clean unused resources
```

---

**Last Updated**: January 15, 2026  
**Repository**: genai-email-report-drafting
