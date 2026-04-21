"""Dependency providers used by FastAPI route handlers."""

from app.llm.factory import LLMFactory
from app.services.memory_service import MemoryService
from app.services.chat_service import ChatService
from app.services.intent_service import IntentService
from app.services.recommend_service import RecommendService
from app.core.config import settings


memory = MemoryService()
llm = LLMFactory.create(settings.PROVIDER)
intent_service = IntentService.from_path(
    model_path=settings.INTENT_MODEL_PATH,
    threshold=settings.INTENT_CONFIDENCE_THRESHOLD,
)
recommendation_service = RecommendService(settings.RECOMMENDATION_MODEL_PATH)


def get_chat_service() -> ChatService:
    """Create a chat service instance with shared singleton dependencies."""
    return ChatService(
        llm=llm,
        memory=memory,
        intent_service=intent_service,
    )

def get_memory_service() -> MemoryService:
    """Return the shared in-memory conversation store service."""
    return memory

def get_recommendation_service() -> RecommendService:
    """Return the shared recommendation service instance."""
    return recommendation_service
