from app.llm.factory import LLMFactory
from app.services.memory_service import MemoryService
from app.services.chat_service import ChatService
from app.core.config import settings


memory = MemoryService()
llm = LLMFactory.create(settings.PROVIDER)


def get_chat_service() -> ChatService:
    return ChatService(
        llm=llm,
        memory=memory
    )

def get_memory_service() -> MemoryService:
    return memory