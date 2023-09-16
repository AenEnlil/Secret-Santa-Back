
from app.settings.app import ApplicationSettings


class DevelopmentSettings(ApplicationSettings):
    debug: bool = True
