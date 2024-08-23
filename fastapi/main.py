from fastapi import FastAPI
from models import Post

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Hello World!!"
    }

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/post")
def create_post(payload: Post):
    return payload.model_dump()