from fastapi.testclient import TestClient
from backend.main import app


client = TestClient(app)


def test_get_weather_success():
    response = client.get("/weather/London")
    assert response.status_code == 200
    assert "name" in response.json()
    assert "temperature" in response.json()


def test_get_weather_location_not_found():
    response = client.get("/weather/NonExistentLocation")
    assert response.status_code == 404
    assert response.json() == {'detail': 'Location not found'}
