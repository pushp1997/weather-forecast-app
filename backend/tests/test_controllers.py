import pytest
from app.controllers import get_current_weather, get_location_coordinates
from app.models import Location
import app.constants as constants


@pytest.mark.asyncio
async def test_get_location_coordinates_valid():
    location = await get_location_coordinates("London")
    assert location is not None
    assert location.name == "London"


@pytest.mark.asyncio
async def test_get_location_coordinates_invalid():
    location = await get_location_coordinates("InvalidLocation")
    assert location is not None


@pytest.mark.asyncio
async def test_get_current_weather():
    location = Location(name="London", lat=51.5074, lon=-0.1278)
    weather_data = await get_current_weather(location)
    print(weather_data)
    assert weather_data is not None
    assert weather_data.name == "London"


@pytest.mark.asyncio
async def test_get_current_weather_invalid_location():
    location = Location(name="InvalidLocation", lat=0, lon=0)
    weather_data = await get_current_weather(location)
    assert weather_data is None


@pytest.mark.asyncio
async def test_get_current_weather_no_api_key():
    location = Location(name="London", lat=51.5074, lon=-0.1278)
    original_api_key = constants.OPENWEATHER_API_KEY
    constants.OPENWEATHER_API_KEY = None
    weather_data = await get_current_weather(location)
    assert weather_data is None
    constants.OPENWEATHER_API_KEY = original_api_key
