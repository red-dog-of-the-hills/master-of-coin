from enum import StrEnum
from functools import cache, cached_property
from typing import Annotated

from fastapi import Depends
from pydantic_settings import BaseSettings, SettingsConfigDict


class Environment(StrEnum):
    DEV = "DEV"
    TEST = "TEST"
    PROD = "PROD"


class BaseConfig(BaseSettings):
    APP_NAME: str = "Master of Coin"
    APP_ENV: Environment = Environment.DEV

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @cached_property
    def reload(self) -> bool:
        return self.APP_ENV == Environment.DEV


class DevConfig(BaseConfig):
    APP_ENV: Environment = Environment.DEV


class TestConfig(BaseConfig):
    APP_ENV: Environment = Environment.TEST


class ProdConfig(BaseConfig):
    APP_ENV: Environment = Environment.PROD


CONFIG_MAP = {
    Environment.DEV: DevConfig,
    Environment.TEST: TestConfig,
    Environment.PROD: ProdConfig,
}


@cache
def get_config() -> BaseConfig:
    env = BaseConfig().APP_ENV
    config_class = CONFIG_MAP[env]

    return config_class()


Settings = Annotated[BaseConfig, Depends(get_config)]
