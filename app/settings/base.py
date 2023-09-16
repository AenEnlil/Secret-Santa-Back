import os
from enum import Enum

from pydantic.v1 import BaseSettings


class EnvironmentTypes(Enum):
    dev: str = 'dev'
    production: str = "production"


class ApplicationBaseSettings(BaseSettings):
    env: EnvironmentTypes = os.getenv("env") or EnvironmentTypes.dev
