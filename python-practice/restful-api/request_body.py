from fastapi import FastAPI, Body
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class User(BaseModel):
    name: str
    age: int


class Company(BaseModel):
    name: str


@app.post("/users")
async def create_user(
    user: User, company: Company, priority: int = Body(..., ge=1, le=3)
):
    return {"user": user, "company": company, "priority": priority}


if __name__ == "__main__":
    uvicorn.run("request_body:app", host="0.0.0.0", port=8000, reload=True)
