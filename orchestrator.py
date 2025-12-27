import uuid
from datetime import datetime
from crewai import Task, Crew

from agents.manager import create_manager
from agents.researcher import create_researcher
from agents.analyst import create_analyst
from agents.writer import create_writer
from memory.task_store import create_task, update_task


def run_task(user_task: str) -> dict:
    task_id = str(uuid.uuid4())

    # Create task entry (PENDING)
    create_task(task_id, user_task)

    manager = create_manager()
    researcher = create_researcher()
    analyst = create_analyst()
    writer = create_writer()

    planning = Task(
        description=f"Break the task into clear steps:\n{user_task}",
        expected_output="A clear ordered list of subtasks.",
        agent=manager
    )

    research = Task(
        description="Find top Zomato competitors in India with factual details.",
        expected_output="A structured list of competitors with pricing and reach.",
        agent=researcher
    )

    analysis = Task(
        description="Compare Zomato with competitors in a table.",
        expected_output="A comparison table highlighting differences.",
        agent=analyst
    )

    writing = Task(
        description=(
            "Write a markdown report and save it as "
            f"`{task_id}.md` using the file writer tool."
        ),
        expected_output="A professional markdown report saved to disk.",
        agent=writer
    )

    crew = Crew(
        agents=[manager, researcher, analyst, writer],
        tasks=[planning, research, analysis, writing],
        verbose=True
    )

    start_time = datetime.utcnow()
    update_task(task_id, status="running", started_at=start_time.isoformat())

    try:
        result = crew.kickoff()
        final_output = str(result)

        end_time = datetime.utcnow()
        duration = (end_time - start_time).seconds

        update_task(
            task_id,
            status="completed",
            output=final_output,
            ended_at=end_time.isoformat(),
            duration_sec=duration
        )

    except Exception as e:
        end_time = datetime.utcnow()
        duration = (end_time - start_time).seconds

        update_task(
            task_id,
            status="failed",
            error=str(e),
            ended_at=end_time.isoformat(),
            duration_sec=duration
        )
        raise

    return {
        "task_id": task_id,
        "status": "completed"
    }
