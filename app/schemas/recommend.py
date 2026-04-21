from typing import List
from pydantic import BaseModel, Field


class RecommendRequest(BaseModel):
    customer_id: str
    top_n: int = Field(default=3, ge=1)


class RecommendResponse(BaseModel):
    recommended_services: List[str]
