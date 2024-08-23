from typing import Optional
from pydantic import BaseModel

class Post(BaseModel):
    id: Optional[int] = -1
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None