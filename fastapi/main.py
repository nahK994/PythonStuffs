from random import randrange
from fastapi import FastAPI, HTTPException, status
from models import Post
from typing import List

app = FastAPI()

my_posts: List[Post] = []
def get_post_item(id:int):
    for i in my_posts:
        if i.id == id:
            return i
    return None


@app.get("/posts")
def get_posts():
    return my_posts

@app.get("/posts/{id}")
def get_post(id: int):
    item = get_post_item(id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")
    return item

@app.post("/post", status_code=status.HTTP_201_CREATED)
def create_post(payload: Post):
    payload.id = randrange(0,1000)
    my_posts.append(payload)
    return payload.model_dump()

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    item = get_post_item(id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")
    my_posts.remove(item)
    return

@app.put("/posts/{id}", status_code=status.HTTP_200_OK)
def update_post(id: int, post: Post):
    item = get_post_item(id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")
    item.content = post.content
    item.title = post.title
    return item