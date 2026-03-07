from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def heartbeat() -> dict[str, bool]:
    return {"status": True}
