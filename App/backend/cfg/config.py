import typing as tp
from functools import lru_cache
from logging.config import dictConfig
from pydantic import BaseSettings

from logging_config import logging_config


class Settings(BaseSettings):
    MONGO_HOST: str
    MONGO_PORT: tp.Optional[int]
    MONGO_USER: tp.Optional[str]
    MONGO_PASS: tp.Optional[str]
    MONGO_DB: tp.Optional[str]

    LOG_LEVEL: str = "INFO"

    PROJECT_NAME: str = "Job Clipboard"


@lru_cache
def get_settings():
    """
    n.b. more about @lru_cache https://realpython.com/lru-cache-python/
    """
    settings = Settings()
    logging_config["root"]["level"] = settings.LOG_LEVEL
    dictConfig(logging_config)
    return settings
