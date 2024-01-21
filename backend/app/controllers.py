from .models import Location, WeatherData
import httpx
from .constants import (
    OPENWEATHER_API_KEY,
    OPENWEATHER_RESPONSE_LIMIT,
    OPENWEATHER_GEO_CODE_URL,
    OPENWEATHER_CURRENT_WEATHER_URL
)


async def get_location_coordinates(location_name: str) -> Location:
    response = None

    async with httpx.AsyncClient() as client:
        client.base_url = OPENWEATHER_GEO_CODE_URL
        client.params = {
            "appid": OPENWEATHER_API_KEY,
            "limit": OPENWEATHER_RESPONSE_LIMIT,
            "q": location_name.strip().lower()
        }
        response = await client.get()

    if not response or response.status_code != 200:
        return None

    location_data = response.json()[0]
    return Location(
        name=location_data["name"],
        lat=location_data["lat"],
        lon=location_data["lon"]
    )


async def get_current_weather(loc: Location) -> WeatherData:
    async with httpx.AsyncClient() as client:
        client.base_url = OPENWEATHER_CURRENT_WEATHER_URL
        client.params = {
            "appid": OPENWEATHER_API_KEY,
            "lat": loc.lat,
            "lon": loc.lon
        }
        response = await client.get()

    if not response or response.status_code != 200:
        return None

    weather_data = response.json()
    return WeatherData(
        name=weather_data["name"],
        main=weather_data["main"],
        wind=weather_data["wind"],
        visibility=weather_data["visibility"],
        rain=weather_data.get("rain"),
        snow=weather_data.get("snow"),
        clouds=weather_data["clouds"]
    )
