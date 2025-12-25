import json
from pathlib import Path

STORE = Path("memory/task_store.json")

def save_task(task_id: str, data: dict):
    # Ensure file exists and is valid JSON
    if not STORE.exists() or STORE.read_text().strip() == "":
        store = {}
    else:
        try:
            store = json.loads(STORE.read_text())
        except json.JSONDecodeError:
            store = {}

    store[task_id] = data

    STORE.write_text(json.dumps(store, indent=2))
