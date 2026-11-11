# Screenshot Action Inbox — Backend

## Phase 2: FastAPI foundation

Implemented:
- FastAPI application factory (`app/main.py`)
- Validated environment-based settings (`app/core/config.py`)
- Logging setup (`app/core/logging.py`)
- Consistent JSON error handlers (`app/core/exceptions.py`)
- Typed health endpoint (`app/api/routes/health.py`, `app/schemas/health.py`)
- Configuration and API tests (`tests/`)

Screenshot upload, SQLite persistence, extraction and tasks are planned for later phases.

## Requirements

Python 3.11 or newer.

## Local installation

Run these commands from `screenshot-action-inbox/backend`:

```bash
python -m venv .venv
# Activate the virtual environment for your operating system
python -m pip install -e ".[dev]"
python -m uvicorn app.main:app --reload
```

Alternative installation: `python -m pip install -r requirements.txt`.

## Endpoints

- `GET http://127.0.0.1:8000/health` should return:

```json
{"status":"ok","service":"screenshot-action-inbox"}
```

- `http://127.0.0.1:8000/docs` hosts Swagger UI.

## Testing

```bash
python -m pytest -q
```

The tests cover health responses, expected and unexpected API errors, configuration defaults, overrides and invalid values. These tests are committed but have not yet been run in CI.

## Environment variables

`app/core/config.py` reads OS environment variables and an optional `backend/.env` file, and validates values using Pydantic Settings. The root `.env.example` is a safe reference; copy it to `backend/.env` for local use. The `.env` file is gitignored. Do not upload secrets, private screenshots or production data.
