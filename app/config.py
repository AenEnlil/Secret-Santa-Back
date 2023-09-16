from functools import lru_cache
from typing import Dict, Type

from app.settings.app import ApplicationSettings
from app.settings.base import EnvironmentTypes, ApplicationBaseSettings
from app.settings.development import DevelopmentSettings
from app.settings.production import ProductionSettings

envs: Dict[EnvironmentTypes, Type[ApplicationSettings]] = {
    EnvironmentTypes.dev: DevelopmentSettings,
    EnvironmentTypes.production: ProductionSettings
}


@lru_cache
def get_settings() -> ApplicationSettings:
    environment = ApplicationBaseSettings().env
    settings = envs[environment]
    return settings()
