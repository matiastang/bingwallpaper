# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a FastAPI-based web service that provides a redirecting API for Microsoft Bing daily wallpapers. The service fetches Bing wallpaper information and redirects to the actual image URLs, with Redis caching for performance.

## Common Commands

### Development Setup
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip3 install -r requirements.txt

# Generate requirements (after adding new dependencies)
pip3 freeze > requirements.txt
```

### Running the Service

**Python direct startup:**
```bash
# Local environment (uses .env)
python3 main.py

# Production environment (uses .env.prod)
python3 main.py --env=prod
```

**Uvicorn startup:**
```bash
# Development with auto-reload
uvicorn main:server --reload

# Production with specific env file
uvicorn main:server --port 8000 --env-file .env.prod
```

**Gunicorn startup:**
```bash
# Using parameters
gunicorn -w 2 -b 127.0.0.1:8000 -k uvicorn.workers.UvicornWorker main:server

# Using config file
gunicorn -c gunicorn_config.py main:server
```

### Code Quality Tools
```bash
# Sort imports
isort .

# Auto-format code
autopep8 --max-line-length=120 --diff

# Lint code
flake8 --max-line-length=120

# Run pre-commit hooks
pre-commit run --all-files
```

## Architecture

### Application Structure
- **main.py** - Entry point, creates FastAPI server instance and registers middleware/routes
- **app/server/** - Contains FastAPI singleton pattern implementation with Redis integration
- **app/config/** - Pydantic settings management for environment configuration
- **app/router/** - API route definitions, wallpaper endpoints in `wallpaper/api.py`
- **app/middleware/** - Custom middleware (request timing)
- **app/errors/** - Custom error handlers
- **app/types/** - Type definitions and response models
- **app/utils/** - Utility functions for Redis and time operations

### Key Components

**FastAPI Server Setup:**
- Uses singleton pattern in `app/server/app_server.py`
- Lifespan context manager handles Redis connection setup/teardown
- Daily log rotation with 7-day retention

**Configuration Management:**
- Environment-based config using pydantic-settings
- Supports `.env`, `.env.prod`, `.env.test` files
- Redis URL and key prefix configuration

**Wallpaper API Logic:**
- Fetches from `https://cn.bing.com/HPImageArchive.aspx`
- Caches responses in Redis with daily expiration
- Returns 302 redirects to actual Bing image URLs
- Cache key: 'last' for the most recent wallpaper

### Environment Files
- `.env` - Local development
- `.env.prod` - Production
- `.env.test` - Testing

Required environment variables:
- `APP_*` - Application configuration
- `REDIS_URL` - Redis connection string
- `REDIS_KEY_PREFIX` - Cache key prefix

### Dependencies
Built with FastAPI ecosystem:
- **fastapi** - Web framework
- **uvicorn** - ASGI server
- **gunicorn** - Production WSGI server with Uvicorn workers
- **redis** - Caching layer
- **pydantic** - Data validation and settings
- **loguru** - Structured logging
- **requests** - HTTP client for Bing API

### Deployment
- Supports Docker deployment (Dockerfile included)
- Gunicorn config uses CPU count * 2 + 1 workers
- Background deployment with nohup for cloud servers