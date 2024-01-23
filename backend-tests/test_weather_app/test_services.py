import pytest

from backend.weather_app.models import Location
from backend.weather_app.services import WeatherService


@pytest.mark.asyncio
async def test_get_location_coordinates_success():
    weather_service = WeatherService()

    location_name = "London"
    retrieved_location = await weather_service.get_location_coordinates(
        location_name
    )

    # Check if the returned Location object is valid
    assert retrieved_location is not None
    assert retrieved_location.name == location_name
    assert retrieved_location.lat == 51.5073219
    assert retrieved_location.lon == -0.1276474


@pytest.mark.asyncio
async def test_get_location_coordinates_invalid_location():
    weather_service = WeatherService()

    location_name = "Invalid Location"
    retrieved_location = await weather_service.get_location_coordinates(
        location_name
    )

    # Check if the returned Location object is invalid
    assert retrieved_location is None


@pytest.mark.asyncio
async def test_get_current_weather_success():
    weather_service = WeatherService()

    location_name = "San Francisco"
    location = Location(name=location_name, lat=37.7749, lon=-122.4194)
    weather_data = await weather_service.get_current_weather(location)

    # Check if the returned WeatherData object is valid
    assert weather_data is not None
    assert weather_data.name == location_name
    assert isinstance(weather_data.temperature, float)
    assert isinstance(weather_data.feels_like, float)
    assert isinstance(weather_data.temp_min, float)
    assert isinstance(weather_data.temp_max, float)
    assert isinstance(weather_data.pressure, float)
    assert isinstance(weather_data.humidity, float)
    assert isinstance(weather_data.visibility, float)
    assert isinstance(weather_data.wind_speed, float)
    assert isinstance(weather_data.wind_deg, float)
    assert isinstance(weather_data.clouds, int)


@pytest.mark.asyncio
async def test_get_current_weather_error():
    weather_service = WeatherService()

    location_name = "Invalid Location"
    location = Location(name=location_name, lat=100, lon=200)
    weather_data = await weather_service.get_current_weather(location)

    # Check if the returned WeatherData object is invalid
    assert weather_data is None
