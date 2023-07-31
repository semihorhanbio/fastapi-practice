from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def index():
    return {"message": "hello semih"}


@app.get("/blog/all")
def get_all_blogs():
    return {"data": "all blogs"}


@app.get("/blog/{id}")
def get_blog(id: int):
    return {"data": f"Blog with id {id}"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
