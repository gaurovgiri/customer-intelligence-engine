"""Version 1 API router definitions."""

from app.api.v1.endpoints.users import router as user_routes
from app.api.v1.endpoints.chat import router as chat_routes
from app.api.v1.endpoints.recommend import router as recommend_routes
from fastapi import APIRouter

router = APIRouter(prefix="/v1", tags=['v1'])
router.include_router(user_routes)
router.include_router(chat_routes)
router.include_router(recommend_routes)
