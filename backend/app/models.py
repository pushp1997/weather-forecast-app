class Location:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon


class WeatherData:
    def __init__(self, name, main, wind, visibility, rain, snow, clouds):
        self.name = name
        self.temperature = main.get("temp")
        self.feels_like = main.get("feels_like")
        self.temp_min = main.get("temp_min")
        self.temp_max = main.get("temp_max")
        self.pressure = main.get("pressure")
        self.humidity = main.get("humidity")
        self.visibility = visibility
        self.wind_speed = wind.get("speed")
        self.wind_deg = wind.get("deg")
        self.rain_1h = rain.get("1h") if rain else None
        self.snow_1h = snow.get("1h") if snow else None
        self.clouds = clouds.get("all")
