# Local Text World MVP

Step 0 provides a minimal, runnable FastAPI + Jinja2 web UI for a local single-player text game.

## Project Structure

- `app/` - web application code
- `app/templates/` - HTML templates
- `data/` - game content data (to be added from Step 1)
- `tests/` - pytest checks

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open <http://127.0.0.1:8000>.

## Test

```bash
pytest
```
