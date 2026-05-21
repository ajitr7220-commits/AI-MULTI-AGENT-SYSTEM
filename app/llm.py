from crewai import LLM
from config.settings import MODEL

def get_llm():
    return LLM(
        model=f"groq/{MODEL}"
    )
    
