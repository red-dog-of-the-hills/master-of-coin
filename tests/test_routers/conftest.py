from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient

from api.main import create_api


@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    api = create_api()

    with TestClient(api) as client:
        yield client
