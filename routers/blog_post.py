from fastapi import APIRouter

router = APIRouter(prefix="/blog", tags=["blog"])


@router.post("/")
def create_post():
    return {"message": "create_post"}
