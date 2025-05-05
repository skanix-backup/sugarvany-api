from fastapi import APIRouter
from sugarvany_api.interface.api.health_router import router as health_router
from sugarvany_api.core.config import get_settings

settings = get_settings()
router = APIRouter(prefix=settings.API_V1_STR)

router.include_router(health_router, tags=["health"]) 