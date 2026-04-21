from langchain_google_genai import ChatGoogleGenerativeAI
from app.core.config import settings

def create_gemini_model():
    return ChatGoogleGenerativeAI(
        model=settings.GEMINI_CHAT_MODEL,
        api_key=settings.GEMINI_API_KEY
    )
