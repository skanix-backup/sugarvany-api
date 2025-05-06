from fastapi import APIRouter, Depends

from sugarvany_api.application.health_service import HealthService
from sugarvany_api.domain.health import HealthResponse

router = APIRouter()


@router.get("/ping", response_model=HealthResponse)
async def health_check(
    health_service: HealthService = Depends(lambda: HealthService()),
) -> HealthResponse:
    """Health check endpoint."""
    return await health_service.check_health()
