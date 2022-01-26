

# Pydantic Schemas
from ..database import schemas
from typing import Optional

# Session
from sqlalchemy.orm import Session
import httpx

# Class Article
from ..database import models


# Get Total number of Articles in API
def total_articles():
    total_articles = httpx.get('https://api.spaceflightnewsapi.net/v3/articles/count')
    total_articles = total_articles.json()
    return total_articles


# Get all Articles Objects
def generator_articles(total_articles: int):

    all_articles = httpx.get(f'https://api.spaceflightnewsapi.net/v3/articles?_limit={total_articles}')

    for article in all_articles.json():
        yield article
    # return all_articles.json()


# Update Database with Article Generator
def update_articles(db: Session, all_articles: dict, qtd_articles: int):

    for article in range(0, qtd_articles):
        article = next(all_articles)
        # print(type(article['publishedAt']))

        check_article = db.query(models.Article).filter(models.Article.title == article['title']).first()
        if check_article is None:

            new_article = models.Article(
                featured=article['featured'],
                title=article['title'],
                url=article['url'],
                imageUrl=article['imageUrl'],
                newsSite=article['newsSite'],
                summary=article['summary'],
                publishedAt=article['publishedAt'],
                launches=article['launches'],
                events=article['events']
            )

            db.add(new_article)
            db.commit()
            db.refresh(new_article)

        else:
            pass
