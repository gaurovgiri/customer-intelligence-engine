from app.llm.gemini_provider import create_gemini_model
from app.llm.openai_provider import create_openai

class LLMFactory:

    @staticmethod
    def create(provider: str):
        if provider.upper() == "GEMINI":
            return create_gemini_model()
        
        elif provider.upper() == "OPENAI":
            return create_openai()
        
        raise ValueError(f"Unknown provider: {provider}")