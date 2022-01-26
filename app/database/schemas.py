from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel


class ArticleBase(BaseModel):
    id: int
    featured: Optional[str] = None
    title: str
    url: str
    imageUrl: Optional[str] = None
    newsSite: Optional[str] = None
    summary: Optional[str] = None
    publishedAt: Optional[datetime] = None
    launches: Optional[List] = None
    events: Optional[List] = None


class ArticleCreate(ArticleBase):
    title: str
    url: str


class Article(ArticleBase):

    class Config:
        orm_mode = True
