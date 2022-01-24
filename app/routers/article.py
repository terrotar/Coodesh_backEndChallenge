
from fastapi import APIRouter


router = APIRouter(tags=['Article'],
                   prefix='/articles')


@router.get('/')
def root():
    return "Back-end Challenge 2021 🏅 - Space Flight News"
