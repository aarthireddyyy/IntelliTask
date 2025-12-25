from crewai.tools import tool
import requests

@tool("Web Search Tool")
def search_web(query: str) -> str:
    """
    Search the web for factual information.
    """
    url = "https://duckduckgo.com/html/"
    params = {"q": query}
    response = requests.post(url, data=params, timeout=10)

    if response.status_code != 200:
        return "Search failed."

    return response.text[:2000]
