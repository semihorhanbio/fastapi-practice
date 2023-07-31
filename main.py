from typing import Optional
from fastapi import FastAPI
from enum import Enum
import uvicorn

app = FastAPI()


@app.get("/")
def index():
    return {"message": "hello semih"}


@app.get("/blog/all")
def get_all_blogs(page=1, page_size: Optional[int] = None):
    return {"message": f"All {page_size} blogs on page {page}"}


@app.get("/blog/{id}/comments/{comment_id}")
def get_comment(
    id: int, comment_id: int, valid: bool = True, username: Optional[str] = None
):
    return {
        "message": f"Blog with id {id} and comment id {comment_id} and valid {valid} and username {username}"
    }


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@app.get("/blog/type/{type}")
def get_blog_type(type: BlogType):
    return {"data": f"Blog type {type.name}"}


@app.get("/blog/{id}")
def get_blog(id: int):
    return {"data": f"Blog with id {id}"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
