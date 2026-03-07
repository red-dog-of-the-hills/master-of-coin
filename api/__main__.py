import uvicorn

from api.config import get_config


def start():
    config = get_config()
    uvicorn.run("api.main:create_api", factory=True, reload=config.reload)


if __name__ == "__main__":
    start()
