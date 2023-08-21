from enum import Enum
from fastapi import FastAPI, Path, Query
import uvicorn

app = FastAPI()


class UserType(str, Enum):
    STANDARD = "standard"
    ADMIN = "admin"


class UsersFormat(str, Enum):
    SHORT = "short"
    FULL = "full"


@app.get("/users")
async def get_user(
    format: UsersFormat, page: int = Query(1, gt=0), size: int = Query(10, le=100)
):
    return {"format": format, "page": page, "size": size}


@app.get("/users/{type}/{id}")
async def get_user(type: UserType, id: int = Path(..., ge=1)):
    return {"type": type, "id": id}


@app.get("/license-plates/{license}")
async def get_license_plate(license: str = Path(..., regex=r"^\w{2}-\d{3}-\w{2}$")):
    return {"license": license}


if __name__ == "__main__":
    uvicorn.run("path_parameters:app", host="0.0.0.0", port=8000, reload=True)
