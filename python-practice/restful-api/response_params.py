from fastapi import FastAPI, Response, status
from pydantic import BaseModel
import uvicorn


class Post(BaseModel):
    title: str


app = FastAPI()


@app.get("/")
async def custom_header(response: Response):
    response.headers["Custom-Header"] = "Custom-Header-Value"
    return {"hello": "world"}


@app.get("/cookie")
async def custom_cookie(response: Response):
    response.set_cookie("cookie-name", "cookie-value", max_age=86400)
    return {"hello": "developer"}


# Dummy database
posts = {
    1: Post(title="Hello"),
}


@app.put("/posts/{id}")
async def update_or_create_post(id: int, post: Post, response: Response):
    if id not in posts:
        response.status_code = status.HTTP_201_CREATED
    posts[id] = post
    return posts[id]


if __name__ == "__main__":
    uvicorn.run("response_params:app", host="0.0.0.0", port=8000, reload=True)
