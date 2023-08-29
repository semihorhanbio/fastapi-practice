from fastapi import FastAPI, Depends, Query, HTTPException, status
from ..pydantic_models.model_inheritance import Post

app = FastAPI()
db = {}


async def pagination(
    skip: int = Query(0, ge=0), limit: int = Query(10, ge=0)
) -> tuple[int, int]:
    capped_limit = min(100, limit)
    return (skip, capped_limit)


async def get_post_or_404(id: int) -> Post:
    try:
        return db.posts[id]
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.get("/items")
async def list_items(p: tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}


@app.get("/things")
async def list_things(p: tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}


@app.get("/posts/{id}")
async def get_post(post: Post = Depends(get_post_or_404)):
    return post


@app.patch("/posts/{id}")
async def update_post(post_update: Post, post: Post = Depends(get_post_or_404)):
    updated_post = post.model_copy(update=post_update.model_dump())
    db.posts[post.id] = updated_post
    return updated_post


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post: Post = Depends(get_post_or_404)):
    db.posts.pop(post.id)
