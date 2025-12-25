from crewai import Agent, LLM

def create_writer():
    llm = LLM(model="ollama/qwen2.5:1.5b")

    return Agent(
        role="Report Writer",
        goal="Write a concise markdown report summarizing the analysis",
        backstory=(
            "You write professional, executive-ready reports."
        ),
        llm=llm,
        verbose=True
    )
