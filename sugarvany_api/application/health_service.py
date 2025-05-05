from sugarvany_api.domain.health import HealthResponse


class HealthService:
    """Health check service."""

    @staticmethod
    async def check_health() -> HealthResponse:
        """Check application health."""
        return HealthResponse(status="pong") 