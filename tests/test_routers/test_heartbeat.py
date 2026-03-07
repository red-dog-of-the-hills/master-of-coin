from fastapi import status
from fastapi.testclient import TestClient


def test_heartbeat(client: TestClient) -> None:
    response = client.get("/heartbeat")

    assert response.status_code == status.HTTP_200_OK

    data = response.json()

    assert "status" in data
    assert data["status"] is True

    assert "mode" in data
    assert data["mode"] == "TEST"
