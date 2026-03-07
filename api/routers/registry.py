from dataclasses import dataclass
from enum import StrEnum

from fastapi import APIRouter


@dataclass
class RouterConfig:
    router: APIRouter
    prefix: str
    tags: list[str | StrEnum]
