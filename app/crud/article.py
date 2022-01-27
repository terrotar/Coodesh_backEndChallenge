
# Pydantic Schemas
from ..database import schemas

# Session
from sqlalchemy.orm import Session

# Class Article
from ..database import models


# POST


# Add Article
def add_article(article: schemas.ArticleCreate, db: Session):

    new_article = models.Article(
                featured=article.featured,
                title=article.title,
                url=article.url,
                imageUrl=article.imageUrl,
                newsSite=article.newsSite,
                summary=article.summary,
                publishedAt=article.publishedAt,
                launches=article.launches,
                events=article.events
            )

    db.add(new_article)
    db.commit()
    db.refresh(new_article)

    return new_article


# GET


# Article by Title
def get_article_by_title(title: str, db: Session):
    return db.query(models.Article).filter(models.Article.title == title).first()


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
