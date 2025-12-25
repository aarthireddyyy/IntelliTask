from crewai import Agent, LLM
from tools.file_writer import write_report

def create_writer():
    llm = LLM(model="ollama/qwen2.5:1.5b")

    return Agent(
        role="Report Writer",
        goal="Write and save a professional markdown report",
        backstory="You write concise, executive-ready reports.",
        tools=[write_report],
        llm=llm,
        verbose=True
    )
