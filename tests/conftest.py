from typing import Generator

from fastapi.testclient import TestClient
from pytest import fixture

from api.main import app


@fixture()
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as client:
        yield client
