
# Pydantic Schemas
from ..database import schemas
from typing import Optional

# Session
from sqlalchemy.orm import Session
import httpx

# Class Article
from ..database import models


# Get product by id
def get_article_by_id(db: Session, id: int):
    return db.query(models.Article).filter(models.Article.id == id).first()



