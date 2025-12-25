from crewai import Agent, LLM

def create_analyst():
    llm = LLM(model="ollama/qwen2.5:1.5b")

    return Agent(
        role="Business Analyst",
        goal="Compare competitors based on pricing, reach, and strengths",
        backstory=(
            "You are a business analyst. "
            "You structure comparisons clearly and logically."
        ),
        llm=llm,
        verbose=True
    )
