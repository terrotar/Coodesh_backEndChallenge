
import pytest

from fastapi.testclient import TestClient

from app.main import api

import random
import string


client = TestClient(api)


host = 'http://0.0.0.0:5000'


# ROUTES


# GET


# /
def test_get_root():
    url = f'{host}/'
    response = client.get(url)

    assert response.text == '"Back-end Challenge 2021 🏅 - Space Flight News"'


# /articles
def test_get_articles():
    url = f'{host}/articles'
    response = client.get(url)

    assert 'items' in response.text


# /articles/{id}
def test_get_article_by_id():
    id = random.randint(1, 10000)
    url = f'{host}/articles/{id}'
    response = client.get(url)

    assert response.status_code == 200


# PUT


# /articles/{id}

# Success
def test_put_article():

    id = random.randint(1, 10000)

    letters = string.ascii_lowercase
    title_generator = ''.join(random.choice(letters) for i in range(10))

    url = f'{host}/articles/{id}'
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

    response = client.put(url, json=test_article)

    assert response.status_code == 200


# Error --> Invalid ID
def test_put_article_invalid_id():

    id = random.randint(1000000000, 99999999999)

    letters = string.ascii_lowercase
    title_generator = ''.join(random.choice(letters) for i in range(10))

    url = f'{host}/articles/{id}'
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

    response = client.put(url, json=test_article)

    assert response.status_code == 404


# Error --> Title already exists
def test_put_article_invalid_title():

    # First generate a successful update article
    id = random.randint(1, 10000)

    letters = string.ascii_lowercase
    title_generator = ''.join(random.choice(letters) for i in range(10))

    url = f'{host}/articles/{id}'
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

    response = client.put(url, json=test_article)

    # Check if is possible to update another article with the same title
    if response.status_code == 200:

        id = random.randint(1, 10000)

        url = f'{host}/articles/{id}'

        response = client.put(url, json=test_article)

        assert response.text == f'"Already exists Article with title {title_generator}"'


# POST


# /articles/

# Success
def test_post_article():
    letters = string.ascii_lowercase
    title_generator = ''.join(random.choice(letters) for i in range(10))

    url = f'{host}/articles/'
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


# Invalid Title
def test_post_article_invalid_title():
    letters = string.ascii_lowercase
    title_generator = ''.join(random.choice(letters) for i in range(10))

    url = f'{host}/articles/'
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

    response = client.post(url, json=test_article)

    assert response.status_code == 404


# DELETE


# /articles/{id}

# Success
def test_delete_article():
    id = random.randint(1, 10000)
    url = f'{host}/articles/{id}'
    response = client.delete(url)

    assert response.status_code == 200


# Invalid ID
def test_delete_article_invalid_id():
    id = random.randint(1000000000, 99999999999)
    url = f'{host}/articles/{id}'
    response = client.delete(url)

    assert response.status_code == 400


# UPDATE DATABASE


# /articles/update
def test_update_database():
    url = f'{host}/articles/update/'
    response = client.get(url)

    assert response.status_code == 200
