import os

from pydantic.v1 import BaseSettings


class ApplicationSettings(BaseSettings):
    MONGO_URL: str = os.getenv("MONGO_URL")
    DATABASE_NAME: str = "santa"

    TESTING: bool = 0
