import os

from api.config import Environment, get_config


def pytest_sessionstart() -> None:
    get_config.cache_clear()
    os.environ["APP_ENV"] = Environment.TEST.value
