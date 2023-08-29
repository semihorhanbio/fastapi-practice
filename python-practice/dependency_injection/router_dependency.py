from fastapi import APIRouter, Depends, FastAPI
from path_dependency import secret_header

router = APIRouter()


@router.get("/route1")
async def router_route1():
    return {"route": "route1"}


@router.get("/route2")
async def router_route2():
    return {"route": "route2"}


app = FastAPI()

app.include_router(router, prefix="/router", dependencies=[Depends(secret_header)])
