from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    APP_NAME: str = "Sugarvany API"
    DEBUG: bool = False
    API_V1_STR: str = "/api/v1"

    class Config:
        env_file = ".env.development"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings."""
    return Settings()
