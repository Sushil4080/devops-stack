# DevOps Stack Project 🚀

This is a beginner-friendly DevOps project using Docker Compose.

## Architecture
- Flask backend API
- PostgreSQL database
- Redis cache
- Docker Compose orchestration

## Services

### Backend
- Runs Flask API on port 5000
- Endpoints:
  - `/` → Home
  - `/cache` → Redis counter
  - `/db` → PostgreSQL connection test

### Database
- PostgreSQL 15
- Persistent storage using Docker volumes

### Cache
- Redis 7 for in-memory caching

---

## How to Run

```bash
docker compose up --build
