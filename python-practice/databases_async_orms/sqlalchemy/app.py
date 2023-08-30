import contextlib
from collections.abc import Sequence

from fastapi import Depends, FastAPI, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

import schemas
from database import create_all_tables, get_async_session
from models import Post

app = FastAPI()


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    await create_all_tables()
    yield


@app.post(
    "/posts", response_model=schemas.PostRead, status_code=status.HTTP_201_CREATED
)
async def create_post(
    post_create: schemas.PostCreate, session: AsyncSession = Depends(get_async_session)
) -> Post:
    post = Post(**post_create.model_dump())
    session.add(post)
    await session.commit()
    return post
