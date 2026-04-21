"""Factory methods for creating configured chat model clients."""

from app.llm.gemini_provider import create_gemini_model
from app.llm.openai_provider import create_openai

class LLMFactory:
    """Create LLM clients based on provider identifiers."""

    @staticmethod
    def create(provider: str):
        """Instantiate the configured chat model provider."""
        if provider.upper() == "GEMINI":
            return create_gemini_model()
        
        elif provider.upper() == "OPENAI":
            return create_openai()
        
        raise ValueError(f"Unknown provider: {provider}")