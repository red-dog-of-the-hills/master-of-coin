import os

import pytest

from api.config import Environment, get_config


def pytest_sessionstart(session: pytest.Session) -> None:
    get_config.cache_clear()
    os.environ["APP_ENV"] = Environment.TEST.value
