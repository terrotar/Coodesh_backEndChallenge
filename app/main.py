
# Imports

# FastAPI
from fastapi import FastAPI
# Routers
from app.routers import article


# FastAPI instance
api = FastAPI()


# Article's router
api.include_router(article.router)


# Root => Welcome Back-end Challenge 2021
@api.get('/', tags=['Welcome Back-end Challenge'])
async def root():
    return "Back-end Challenge 2021 🏅 - Space Flight News"
