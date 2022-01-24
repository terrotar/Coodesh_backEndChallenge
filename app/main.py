
# Imports

# FastAPI
from fastapi import FastAPI
# Routers
from app.routers import article


# FastAPI instance
api = FastAPI()


# Article's router
api.include_router(article.router)
