from fastapi import FastAPI, Response, status
from fastapi.responses import (
    HTMLResponse,
    PlainTextResponse,
    RedirectResponse,
    FileResponse,
)
from pathlib import Path
import uvicorn

app = FastAPI()


@app.get("/html", response_class=HTMLResponse)
async def get_html():
    return """
        <html>
            <head>
                <title>Hello world!</title>
            </head>
            <body>
                <h1>Hello world!</h1>
            </body>
        </html>
    """


@app.get("/text", response_class=PlainTextResponse)
async def get_text():
    return "Hello world!"


@app.get("/redirect")
async def redirect():
    return RedirectResponse("/", status_code=status.HTTP_301_MOVED_PERMANENTLY)


@app.get("/cat")
async def get_cat():
    root_directory = Path(__file__).parent.parent.parent
    picture_path = root_directory / "assets" / "cat.jpg"
    return FileResponse(picture_path)


@app.get("/xml")
async def get_xml():
    content = """<?xml version="1.0" encoding="UTF-8"?>
        <Hello>World</Hello>
    """
    return Response(content=content, media_type="application/xml")


if __name__ == "__main__":
    uvicorn.run("custom_response:app", host="127.0.0.1", port=8000, reload=True)
