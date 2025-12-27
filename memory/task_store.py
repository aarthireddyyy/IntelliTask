import json
from pathlib import Path
from datetime import datetime

STORE = Path("memory/task_store.json")

def _load_store():
    if not STORE.exists() or STORE.read_text().strip() == "":
        return {}
    try:
        return json.loads(STORE.read_text())
    except json.JSONDecodeError:
        return {}

def _save_store(store: dict):
    STORE.write_text(json.dumps(store, indent=2))

def create_task(task_id: str, task_text: str):
    store = _load_store()
    store[task_id] = {
        "task": task_text,
        "status": "pending",
        "output": None,
        "error": None,
        "started_at": None,
        "ended_at": None,
        "duration_sec": None
    }
    _save_store(store)

def update_task(task_id: str, **updates):
    store = _load_store()
    store[task_id].update(updates)
    _save_store(store)
