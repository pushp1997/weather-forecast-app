from fastapi import APIRouter, HTTPException, status

from weather_app.services import WeatherService
from weather_app.models import WeatherData

router = APIRouter(prefix="/weather")

weather_service = WeatherService()


@router.get("/{location_name}", response_model=WeatherData)
async def get_weather_handler(location_name: str) -> WeatherData:
    location = await weather_service.get_location_coordinates(location_name)

    if not location:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Location not found"
        )

    return weather_service.get_current_weather(location)
