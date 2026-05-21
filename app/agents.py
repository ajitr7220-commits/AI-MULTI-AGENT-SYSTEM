from crewai import Agent
from app.llm import get_llm
from app.tools import simple_search

llm = get_llm()

researcher = Agent(
    role="AI Researcher",
    goal="Find accurate and useful imformation",
    backstory="Expert in research and analysis",
    tools=[simple_search],
    llm=llm,
    verbose=True

)

writer = Agent(
    role="content Writer",
    goal="write structured and engaging content",
    backstory="Tech content specialist",
    llm=llm,
    verbose=True
)