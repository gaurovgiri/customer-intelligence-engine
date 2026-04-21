"""Top-level API router composition."""

from app.api.v1.router import router as v1_routes
from fastapi import APIRouter

router = APIRouter(prefix="/api")
router.include_router(v1_routes)
