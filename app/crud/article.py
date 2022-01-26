
# Pydantic Schemas
from ..database import schemas
from typing import Optional

# Session
from sqlalchemy.orm import Session

# Class Article
from ..database import models


# GET

# Article by ID
def get_article_by_id(id: int, db: Session):
    return db.query(models.Article).filter(models.Article.id == id).first()


# DELETE


# Article
def delete_article(id: int, db: Session):
    db_article = db.query(models.Article).filter(models.Article.id == id).first()
    db.delete(db_article)
    db.commit()
    return db_article
