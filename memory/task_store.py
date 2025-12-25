import json
from pathlib import Path

STORE = Path("memory/task_store.json")

def save_task(task_id: str, data: dict):
    if STORE.exists():
        store = json.loads(STORE.read_text())
    else:
        store = {}

    store[task_id] = data
    STORE.write_text(json.dumps(store, indent=2))
