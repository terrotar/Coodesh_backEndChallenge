
from fastapi import APIRouter

import httpx


router = APIRouter(tags=['Article'],
                   prefix='/articles')


# SpaceFlight News APi Shortcut
space_flight = httpx.get('https://api.spaceflightnewsapi.net/v3/documentation')


# GET

# Article by ID
@router.get('articles/{article_id}')
async def get_article_by_id(article_id: int):
    print(space_flight.text)
