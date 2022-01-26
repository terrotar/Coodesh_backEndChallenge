
# Router
from fastapi import APIRouter, Depends

# Database and Model
from ..database import database

# Session
from sqlalchemy.orm import Session

# Article Generator
from ..crud.article_gen import total_articles, generator_articles, update_articles

# Request API
import httpx


# Article Router
router = APIRouter(tags=['Article'],
                   prefix='/articles')


# GET


# Update Database with Space Flight News API
@router.get('/update')
async def update_database(db: Session = Depends(database.get_db)):
    qtd_articles = total_articles()
    all_articles = generator_articles(qtd_articles)
    try:
        update_articles(db, all_articles, qtd_articles)
    except Exception as e:
        print(f'Failed to update database\n{e}')
    finally:
        return 'Database updated with Space Flight News API Articles.'
