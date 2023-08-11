from fastapi import APIRouter
from typing import Optional
from fastapi import status, Response
from enum import Enum

router = APIRouter(prefix="/blog", tags=["blog"])


@router.get(
    "/blog/all",
    summary="Retrieve all blogs",
    description="This api call simulates fetching all blogs",
    response_description="The list of all blogs",
)
def get_all_blogs(page=1, page_size: Optional[int] = None):
    return {"message": f"All {page_size} blogs on page {page}"}


@router.get(
    "/blog/{id}/comments/{comment_id}",
    tags=["comment"],
    response_description="The list of comment based on blog id",
)
def get_comment(
    id: int, comment_id: int, valid: bool = True, username: Optional[str] = None
):
    """
    Simulates retrieving a comment of a blog
    - **id** mandatory path parameter
    - **comment_id** mandatory path parameter
    - **bool** optional query parameter
    - **username** optional query parameter
    """
    return {
        "message": f"Blog with id {id} and comment id {comment_id} and valid {valid} and username {username}"
    }


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@router.get(
    "/blog/type/{type}",
    response_description="The list of blog based on type",
)
def get_blog_type(type: BlogType):
    """
    Simulates retrieving a blog type
    - **type** mandatory path parameter
    """
    return {"data": f"Blog type {type.name}"}


@router.get("/blog/{id}", response_description="The list of blog based on id")
def get_blog(id: int, response: Response):
    """
    Simulates retrieving a blog
    - **id** mandatory path parameter
    """
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"data": f"Blog with id {id} not found"}
    return {"data": f"Blog with id {id}"}
