from crewai.tools import tool

@tool
def simple_search(query: str) -> str:
    """Search the internet for a given query."""
    return "result"
