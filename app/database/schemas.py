from typing import Dict, List, Optional
from datetime import datetime

from pydantic import BaseModel


class ArticleBase(BaseModel):
    featured: Optional[bool] = None
    title: str
    url: str
    imageUrl: str
    newsSite: Optional[str] = None
    summary: Optional[str] = None
    publishedAt: datetime
    launches: Optional[Dict] = None
    events: Optional[Dict] = None


class ArticleCreate(ArticleBase):
    title: str
    url: str


class Article(ArticleBase):
    id: int

    class Config:
        orm_mode = True
