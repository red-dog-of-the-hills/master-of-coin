from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def heartbeat() -> dict[str, bool]:
    return {"Status": True}
