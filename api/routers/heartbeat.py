from fastapi import APIRouter

from api.config import Settings

router = APIRouter()


@router.get("/")
def heartbeat(settings: Settings) -> dict[str, bool | str]:
    return {"status": True, "mode": settings.APP_ENV.value}
