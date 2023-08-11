from fastapi import FastAPI
from routers import blog_get
import uvicorn

app = FastAPI()
app.include_router(blog_get.router)


@app.get("/")
def index():
    return {"message": "hello semih"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
