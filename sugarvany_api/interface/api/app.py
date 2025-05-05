from fastapi import FastAPI
from sugarvany_api.core.config import get_settings
from sugarvany_api.core.logger import setup_logger
from sugarvany_api.interface.api.router import router

settings = get_settings()
logger = setup_logger()

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
)

app.include_router(router) 