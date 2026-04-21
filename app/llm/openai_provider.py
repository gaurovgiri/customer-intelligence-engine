"""OpenAI chat model provider creation utilities."""

from langchain_openai import ChatOpenAI
from app.core.config import settings


def create_openai():
    """Create a ChatOpenAI client using configured model and API key."""
    return ChatOpenAI(
        model=settings.OPENAI_CHAT_MODEL,
        api_key=settings.OPENAI_API_KEY
    )