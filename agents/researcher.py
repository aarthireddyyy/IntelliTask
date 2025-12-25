from crewai import Agent, LLM
from tools.search_tool import search_web

def create_researcher():
    llm = LLM(model="ollama/qwen2.5:1.5b")

    return Agent(
        role="Market Researcher",
        goal="Identify Zomato competitors in India using web search",
        backstory=(
            "You are a market research analyst. "
            "You find factual, verifiable competitor information."
        ),
        tools=[search_web],  # ✅ now valid
        llm=llm,
        verbose=True
    )
