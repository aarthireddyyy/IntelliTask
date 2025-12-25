from crewai import Agent, LLM

def create_researcher():
    llm = LLM(model="ollama/qwen2.5:1.5b")

    return Agent(
        role="Market Researcher",
        goal="Identify Zomato competitors in India and gather factual information",
        backstory=(
            "You are a market research analyst. "
            "You focus only on verifiable facts and avoid assumptions."
        ),
        llm=llm,
        verbose=True
    )
