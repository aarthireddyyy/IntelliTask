import uuid
from crewai import Task, Crew
from agents.manager import create_manager
from agents.researcher import create_researcher
from agents.analyst import create_analyst
from agents.writer import create_writer
from memory.task_store import save_task

def run_task(user_task: str) -> dict:
    task_id = str(uuid.uuid4())

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

    
    result = crew.kickoff()

# CrewOutput → string
    final_output = str(result)

    save_task(task_id, {
        "task": user_task,
        "status": "completed",
        "output": final_output
    })


    return {
        "task_id": task_id,
        "status": "completed"
    }
