# Flask TODO App

A minimal TODO web app built with Flask and TinyDB.

## Features
- Add tasks.
- Mark tasks as complete.
- Edit task titles.
- Delete tasks.
- Persistent storage in `db.json`.

## Plans
- **Lite**: supports up to **5 tasks**.
- **Pro**: supports **unlimited tasks**.

## Tech Stack
- Python 3
- Flask
- TinyDB
- Jinja2 templates

## Project Layout
```text
Flask-TODO-APP/
├── app.py                # App factory + dev server entry point
├── routes.py             # Blueprint and CRUD routes
├── templates/index.html  # UI template
├── tests/test_app.py     # Pytest suite
├── db.json               # TinyDB data file
└── screenshot/           # UI screenshots
```

## Run Locally
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install flask tinydb pytest
python app.py
```

Open: http://127.0.0.1:5000

## Routes
- `GET /` — list tasks.
- `POST /add` — create a task (`title`).
- `POST /update` — update title (`hiddenField` = id, `inputField` = new title).
- `POST /complete/<todo_id>` — mark task complete.
- `POST /delete/<todo_id>` — delete task.

## Testing
```bash
pytest -q
```

## Notes
- App uses `create_app()` in `app.py` and registers the `todo` blueprint from `routes.py`.
- Task IDs are generated as incrementing integers.
- Blank task titles are ignored.
