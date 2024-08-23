from random import randrange
from fastapi import FastAPI, HTTPException, status, Depends
from typing import List
from sqlalchemy.orm import Session
from .database import engine, get_db
from . import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/posts", status_code=status.HTTP_200_OK)
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts

@app.get("/posts/{id}", status_code=status.HTTP_200_OK)
def get_post(id: int, db: Session = Depends(get_db)):
    item = db.query(models.Post).filter(models.Post.id == id).first()
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")
    return item

@app.post("/post", status_code=status.HTTP_201_CREATED)
def create_post(payload: schemas.Post, db: Session = Depends(get_db)):
    post = models.Post(**payload.model_dump())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    item = db.query(models.Post).filter(models.Post.id == id)
    if item.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")

    item.delete(synchronize_session=False)
    db.commit()
    return

@app.put("/posts/{id}", status_code=status.HTTP_200_OK)
def update_post(id: int, post: schemas.Post, db: Session = Depends(get_db)):
    item = db.query(models.Post).filter(models.Post.id == id)
    if item.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")
    item.update(post.model_dump(), synchronize_session=False)
    db.commit()
    return item.first()