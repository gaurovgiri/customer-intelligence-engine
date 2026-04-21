from app.services.recommend_service import RecommendService
from app.api.deps import get_recommendation_service
from fastapi import APIRouter, Depends


router = APIRouter(prefix="/recommend", tags=['recommend'])


@router.post("")
def recommend(customer_id: str, recommend_service:RecommendService=Depends(get_recommendation_service)):
    return {"recommended_services": recommend_service.recommend(customer_id)}