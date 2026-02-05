# MOSS Backend

FastAPI-based backend for the MOSS personal assistant.

## Quick start (development)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Configuration

| Variable | Default | Description |
| --- | --- | --- |
| `MOSS_ENV` | `development` | Environment name |
| `MOSS_DATABASE_URL` | `sqlite:///./moss.db` | SQLAlchemy database URL |
| `MOSS_LOG_LEVEL` | `INFO` | Logging level |
