
# Router
from fastapi import APIRouter, Depends, HTTPException

# Database and Model
from ..database import database, schemas

# Session
from sqlalchemy.orm import Session

# Article Generator
from ..crud import article_gen, article


# Article Router
router = APIRouter(tags=['Article'],
                   prefix='/articles')


# POST

# Add Article
@router.post('/', response_model=schemas.Article)
async def create_article(obj: schemas.ArticleCreate, db: Session = Depends(database.get_db)):

    db_article = article.get_article_by_title(obj.title, db)

    if db_article is not None:
        raise HTTPException(status_code=404,
                            detail='Article with the same title has already been created')

    return article.add_article(obj, db)


# GET


# Update Database with Space Flight News API
@router.get('/update')
async def update_database(db: Session = Depends(database.get_db)):
    qtd_articles = article_gen.total_articles()
    all_articles = article_gen.generator_articles(qtd_articles)
    try:
        article_gen.update_articles(db, all_articles, qtd_articles)
    except Exception as e:
        # print(f'Failed to update database\n{e}')
        raise HTTPException(status_code=404,
                            detail=f'Failed to update database\n{e}')
    finally:
        return 'Database updated with Space Flight News API Articles.'


# Article by ID
@router.get('/{id}', response_model=schemas.Article)
async def article_by_id(id: int, db: Session = Depends(database.get_db)):

    obj = article.get_article_by_id(id, db)
    if obj is not None:
        return obj

    raise HTTPException(status_code=404,
                        detail=f"Article {id} not found")


# Delete Article
@router.delete('/{id}', response_model=schemas.Article)
async def delete_article(id: int, db: Session = Depends(database.get_db)):

    obj = article.get_article_by_id(id, db)
    if obj is not None:
        obj = article.delete_article(id, db)
        return obj

    raise HTTPException(status_code=404,
                        detail=f"Article {id} not found")
