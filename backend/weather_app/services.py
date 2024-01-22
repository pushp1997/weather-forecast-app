import httpx

from weather_app.models import Location, WeatherData
from weather_app.constants import (
    OPENWEATHER_API_KEY,
    OPENWEATHER_RESPONSE_LIMIT,
    OPENWEATHER_GEO_CODE_URL,
    OPENWEATHER_CURRENT_WEATHER_URL,
)


class WeatherService:
    async def get_location_coordinates(self, location_name: str) -> Location:
        # Make an API request to OpenWeatherMap's geocoding endpoint
        response = None

        async with httpx.AsyncClient() as client:
            client.params = {
                "appid": OPENWEATHER_API_KEY,
                "limit": OPENWEATHER_RESPONSE_LIMIT,
                "q": location_name.strip().lower(),
            }
            response = await client.get(OPENWEATHER_GEO_CODE_URL)

        # Check response status and parse JSON data
        if not response.json() or response.status_code != 200:
            return None

        location_data = response.json()[0]
        return Location(
            name=location_data["name"],
            lat=location_data["lat"],
            lon=location_data["lon"]
        )

    async def get_current_weather(self, location: Location) -> WeatherData:
        # Make an API request to OpenWeatherMap's current weather endpoint
        response = None

        async with httpx.AsyncClient() as client:
            client.params = {
                "appid": OPENWEATHER_API_KEY,
                "lat": location.lat,
                "lon": location.lon
            }
            response = await client.get(OPENWEATHER_CURRENT_WEATHER_URL)

        # Check response status and parse JSON data
        if not response or response.status_code != 200:
            return None

        weather_data = response.json()
        return WeatherData(
            name=weather_data["name"],
            temperature=weather_data["main"].get("temp"),
            feels_like=weather_data["main"].get("feels_like"),
            temp_min=weather_data["main"].get("temp_min"),
            temp_max=weather_data["main"].get("temp_max"),
            pressure=weather_data["main"].get("pressure"),
            humidity=weather_data["main"].get("humidity"),
            visibility=weather_data["visibility"],
            wind_speed=weather_data["wind"].get("speed"),
            wind_deg=weather_data["wind"].get("deg"),
            rain_1h=weather_data.get("rain").get("1h") if weather_data.get("rain") else None,
            snow_1h=weather_data.get("snow").get("1h") if weather_data.get("snow") else None,
            clouds=weather_data["clouds"].get("all"),
        )
