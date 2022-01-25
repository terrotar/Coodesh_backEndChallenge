
# Imports

# FastAPI
from fastapi import FastAPI
# Routers
from .routers import article
# Database
from .database import models
from .database.database import engine


# Create tables mapped by ORM inside models
models.Base.metadata.create_all(bind=engine)


# FastAPI instance
api = FastAPI()


# Article's router
api.include_router(article.router)


# Root => Welcome Back-end Challenge 2021
@api.get('/', tags=['Welcome Back-end Challenge'])
async def root():
    return "Back-end Challenge 2021 🏅 - Space Flight News"
