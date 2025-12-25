# main.py
import os

from crewai import Agent, Task, Crew, LLM
from langchain_ollama import ChatOllama

# 🔑 THIS IS THE KEY FIX
# Use CrewAI's LLM with Ollama
llm = LLM(model="ollama/qwen2.5:1.5b")

agent = Agent(
    role="AI Explainer",
    goal="Explain concepts clearly and concisely",
    backstory="You are a fully offline AI running via Ollama.",
    llm=llm,
    verbose=True
)

task = Task(
    description="Explain what CrewAI is in one short sentence.",
    expected_output="A single concise sentence explaining CrewAI.",
    agent=agent
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True
)

result = crew.kickoff()

print("\n=== FINAL RESULT ===")
print(result)
