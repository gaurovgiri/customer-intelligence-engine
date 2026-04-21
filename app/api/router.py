from app.api.v1.router import router as v1_routes
from fastapi import APIRouter

router = APIRouter(prefix="")
router.include_router(v1_routes)
