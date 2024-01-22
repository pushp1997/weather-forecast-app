from fastapi import FastAPI

from weather_app.controllers import router

app = FastAPI()

app.include_router(router)


@app.get("/")
async def root():
    return "Server is running!"
