from fastapi import FastAPI, Header, Cookie
import uvicorn

app = FastAPI()


@app.get("/")
async def get_header(user_agent: str = Header(...)):
    return {"user_agent": user_agent}


@app.get("/cookie")
async def get_cookie(hello: str | None = Cookie(None)):
    return {"hello": hello}


if __name__ == "__main__":
    uvicorn.run("headers_cookies:app", host="0.0.0.0", port=8000, reload=True)
