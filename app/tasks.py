from crewai import Task
from app.agents import researcher, writer

research_task = Task(
    description="Research latest AI trends in 2026",
    agent=researcher,
    expected_output="Bullet point insights"
    
    )

write_task = Task(
    description="convert research into blog",
    agent=writer,
    expected_output="Readable blog post"
)