import multiprocessing

from sugarvany_api.core.config import get_settings

settings = get_settings()

# Server configuration
HOST = "0.0.0.0"
PORT = 8000

# Worker configuration
WORKERS = (
    multiprocessing.cpu_count() * 2 + 1
)  # Formula for optimal worker count

# Logging configuration
LOG_LEVEL = "info"
LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(asctime)s - %(name)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    },
    "loggers": {
        "uvicorn": {"handlers": ["default"], "level": LOG_LEVEL},
        "uvicorn.error": {
            "handlers": ["default"],
            "level": LOG_LEVEL,
        },
        "uvicorn.access": {
            "handlers": ["default"],
            "level": LOG_LEVEL,
        },
    },
}
