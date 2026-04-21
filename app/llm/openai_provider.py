from langchain_openai import ChatOpenAI
from app.core.config import settings


def create_openai():
    return ChatOpenAI(
        model=settings.OPENAI_CHAT_MODEL,
        api_key=settings.OPENAI_API_KEY
    )