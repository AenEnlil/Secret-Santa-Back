from fastapi import FastAPI
from .config import get_settings


def get_application() -> FastAPI:
    settings = get_settings()

    application = FastAPI()

    @application.get("/")
    async def root():
        return {"message": "Hello World"}

    return application


app = get_application()
