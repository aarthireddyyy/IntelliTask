const runBtn = document.getElementById("runBtn");
const taskInput = document.getElementById("taskInput");
const statusDiv = document.getElementById("status");
const outputDiv = document.getElementById("output");

const API_URL = "http://127.0.0.1:8000";

runBtn.addEventListener("click", async () => {
  const task = taskInput.value.trim();
  if (!task) return alert("Please enter a task");

  statusDiv.classList.remove("hidden");
  statusDiv.textContent = "⏳ Running task...";
  outputDiv.classList.add("hidden");

  try {
    const res = await fetch(`${API_URL}/task`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ task })
    });

    const data = await res.json();
    const taskId = data.task_id;

    pollStatus(taskId);

  } catch (err) {
    statusDiv.textContent = "❌ Error starting task";
  }
});

async function pollStatus(taskId) {
  const interval = setInterval(async () => {
    const res = await fetch(`${API_URL}/task/${taskId}`);
    const data = await res.json();

    statusDiv.textContent = `Status: ${data.status}`;

    if (data.status === "completed") {
      clearInterval(interval);
      outputDiv.classList.remove("hidden");
      outputDiv.textContent = data.output;
    }

    if (data.status === "failed") {
      clearInterval(interval);
      statusDiv.textContent = "❌ Task failed";
    }
  }, 3000);
}
