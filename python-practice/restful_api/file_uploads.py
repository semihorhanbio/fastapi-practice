from fastapi import FastAPI, File, UploadFile
import uvicorn

app = FastAPI()


@app.post("/files")
async def upload_files(files: list[UploadFile] = File(...)):
    return [
        {"file_name": file.filename, "content_type": file.content_type}
        for file in files
    ]


if __name__ == "__main__":
    uvicorn.run("file_uploads:app", host="127.0.0.1", port=8000, reload=True)
