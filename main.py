from crewai import Crew
from app.agents import researcher, writer
from app.tasks import research_task, write_task

def run():
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, write_task],
        verbose=True
    )

    result= crew.kickoff()
    print("\nFINAL OUTPUT:\n", result)

if __name__ == "__main__":
    run()
        