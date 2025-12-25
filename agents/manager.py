from crewai import Agent, LLM

def create_manager():
    llm = LLM(model="ollama/qwen2.5:1.5b")

    return Agent(
        role="Task Manager",
        goal="Plan the task, assign subtasks, and ensure the final output is complete",
        backstory=(
            "You are a senior project manager. "
            "You break complex tasks into steps and verify completion."
        ),
        llm=llm,
        verbose=True
    )
