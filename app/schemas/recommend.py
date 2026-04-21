"""Pydantic models for recommendation endpoint payloads."""

from typing import List
from pydantic import BaseModel, Field


class RecommendRequest(BaseModel):
    """Incoming payload for recommendation generation."""

    customer_id: str
    top_n: int = Field(default=3, ge=1)


class RecommendResponse(BaseModel):
    """Outgoing payload containing recommended services."""

    recommended_services: List[str]
