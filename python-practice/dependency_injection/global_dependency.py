from fastapi import Depends, FastAPI
from path_dependency import secret_header

app = FastAPI(dependencies=[Depends(secret_header)])


@app.get("/route1")
async def route1():
    return {"route": "route1"}


@app.get("/route2")
async def route2():
    return {"route": "route2"}
