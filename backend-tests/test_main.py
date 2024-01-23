from backend.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root_handler():
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == "Server is running!"
