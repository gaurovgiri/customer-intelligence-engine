"""Pydantic models for chat endpoint request and response payloads."""

from pydantic import BaseModel


class ChatRequest(BaseModel):
    """Incoming payload for chat completion requests."""

    user_id: str
    message: str

class ChatResponse(BaseModel):
    """Outgoing payload for chat completion responses."""

    message: str
    intent: str
    confidence: float