from fastapi import FastAPI
from loguru import logger

from api.config import get_config
from api.routers import all_routers


def create_api() -> FastAPI:
    config = get_config()

    app = FastAPI(title=config.APP_NAME)

    for router in all_routers:
        app.include_router(router.router, prefix=router.prefix, tags=router.tags)
        logger.info(f"Registered routes at {router.prefix}")

    return app
