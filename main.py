from crewai import Task, Crew
from agents.manager import create_manager
from agents.researcher import create_researcher
from agents.analyst import create_analyst
from agents.writer import create_writer

manager = create_manager()
researcher = create_researcher()
analyst = create_analyst()
writer = create_writer()

task_input = "Analyze Zomato's top competitors in India."

planning_task = Task(
    description=f"Break the following task into clear steps:\n{task_input}",
    expected_output="A clear list of subtasks.",
    agent=manager
)

research_task = Task(
    description=(
        "Identify the top 3–5 food delivery competitors of Zomato in India. "
        "Include pricing model, geographic reach, and key features."
    ),
    expected_output="Structured competitor information.",
    agent=researcher
)

analysis_task = Task(
    description=(
        "Compare Zomato with its competitors. "
        "Create a comparison table highlighting differences."
    ),
    expected_output="A clean comparison table.",
    agent=analyst
)

writing_task = Task(
    description=(
        "Write a markdown report summarizing the competitor analysis. "
        "Include a table and short insights."
    ),
    expected_output="A professional markdown report.",
    agent=writer
)

crew = Crew(
    agents=[manager, researcher, analyst, writer],
    tasks=[planning_task, research_task, analysis_task, writing_task],
    verbose=True
)

result = crew.kickoff()

print("\n=== FINAL RESULT ===")
print(result)
