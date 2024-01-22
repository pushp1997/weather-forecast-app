from pydantic import BaseModel


class Location(BaseModel):
    name: str
    lat: float
    lon: float


class WeatherData(BaseModel):
    name: str
    temperature: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: float
    humidity: float
    visibility: float
    wind_speed: float
    wind_deg: float
    rain_1h: float | None = None
    snow_1h: float | None = None
    clouds: int
