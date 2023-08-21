from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()


@app.get("/")
async def get_request_object(request: Request):
    return {"path": request.url.path}


if __name__ == "__main__":
    uvicorn.run("request_object:app", host="0.0.0.0", port=8000, reload=True)
