from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from backend.weather_app.controllers import router

app = FastAPI()

app.include_router(router)


@app.get("/", response_class=PlainTextResponse,)
async def root():
    return "Server is running!"
