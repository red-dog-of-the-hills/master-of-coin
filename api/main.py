from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def heartbeat():
    return {"Status": True}
