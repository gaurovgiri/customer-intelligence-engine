"""Recommendation endpoint handlers."""

from app.services.recommend_service import RecommendService
from app.api.deps import get_recommendation_service
from fastapi import APIRouter, Depends
from app.schemas.recommend import RecommendRequest, RecommendResponse


router = APIRouter(prefix="/recommend", tags=['recommend'])


@router.post("", response_model=RecommendResponse)
def recommend(req: RecommendRequest, recommend_service:RecommendService=Depends(get_recommendation_service)):
    """Return top service recommendations for a customer."""
    return {
        "recommended_services": recommend_service.recommend(req.customer_id, n=req.top_n)
    }