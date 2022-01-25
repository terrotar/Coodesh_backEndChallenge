from typing import List, Optional

from pydantic import BaseModel


class ArticleBase(BaseModel):
    title: str
    url: str
    imageUrl: Optional[str] = None
    summary: Optional[str] = None
    PublishedAt: Optional[str] = None
    launches: Optional[List] = None


class ArticleCreate(ArticleBase):
    title: str
    url: str


class Article(ArticleBase):
    id: int

    class Config:
        orm_mode = True
