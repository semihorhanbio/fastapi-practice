from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def hello_word():
    return {"hello": "world"}


if __name__ == "__main__":
    uvicorn.run("first_endpoint:app", host="0.0.0.0", port=8000, reload=True)
