from fastapi import FastAPI, Form
import uvicorn

app = FastAPI()


@app.post("/users")
def create_user(name: str = Form(...), age: int = Form(...)):
    return {"name": name, "age": age}


if __name__ == "__main__":
    uvicorn.run("form_data:app", host="127.0.0.1", port=8000, reload=True)
