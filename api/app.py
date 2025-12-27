from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator import run_task
import json
from pathlib import Path

app = FastAPI(title="IntelliTask Orchestrator")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (safe for local dev)
    allow_credentials=True,
    allow_methods=["*"],  # allow POST, GET, OPTIONS
    allow_headers=["*"],
)

STORE = Path("memory/task_store.json")

class TaskRequest(BaseModel):
    task: str

@app.post("/task")
def create_task(req: TaskRequest):
    return run_task(req.task)

@app.get("/task/{task_id}")
def get_task(task_id: str):
    if not STORE.exists():
        return {"error": "No tasks found"}

    data = json.loads(STORE.read_text())
    return data.get(task_id, {"error": "Task not found"})
