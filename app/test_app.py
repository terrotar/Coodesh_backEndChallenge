
import pytest

from fastapi.testclient import TestClient

from app.main import api

import random
import string


client = TestClient(api)


# ROUTES


# GET


# /
def test_get_root():
    url = 'http://127.0.0.1:8000/'
    response = client.get(url)

    assert response.text == '"Back-end Challenge 2021 🏅 - Space Flight News"'


# /articles
def test_get_articles():
    url = 'http://127.0.0.1:8000/articles/'
    response = client.get(url)

    assert 'items' in response.text


# /articles/{id}
def test_get_article_by_id():
    id = random.randint(1, 10000)
    url = f'http://127.0.0.1:8000/articles/{id}'
    response = client.get(url)

    assert response.status_code == 200


# POST


# /articles
def test_post_article():

    letters = string.ascii_lowercase
    title_generator = ''.join(random.choice(letters) for i in range(10))

    url = 'http://127.0.0.1:8000/articles/'
    test_article = {
        "featured": True,
        "title": f"{title_generator}",
        "url": "string",
        "imageUrl": "string",
        "newsSite": "string",
        "summary": "string",
        "publishedAt": "2022-01-27T18:45:11.758Z",
        "launches": {},
        "events": {}
    }

    response = client.post(url, json=test_article)

    assert response.status_code == 200


# DELETE


# /articles/{id}
def test_delete_article():
    id = random.randint(1, 10000)
    url = f'http://127.0.0.1:8000/articles/{id}'
    response = client.delete(url)

    assert response.status_code == 200


# UPDATE DATABASE
def test_update_database():
    url = 'http://127.0.0.1:8000/articles/update/'
    response = client.get(url)

    assert response.status_code == 200
