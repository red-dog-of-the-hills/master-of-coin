import os

import pytest

from api.config import Environment, get_config


@pytest.fixture(scope="session", autouse=True)
def set_environment() -> None:
    get_config.cache_clear()
    os.environ["APP_ENV"] = Environment.TEST.value
