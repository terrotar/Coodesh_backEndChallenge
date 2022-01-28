#!/usr/bin/env python


# Asyncio
import asyncio

# Requests
import httpx


# PUT request to endpoint '/articles/update'
async def cron_update_articles(url):

    async with httpx.AsyncClient(timeout=None) as client:

        await client.get(url)
        print('Database was updated successfully')
        await client.aclose()


if __name__ == '__main__':

    asyncio.run(cron_update_articles('http://0.0.0.0:5000/articles/update'))
    print('Database updated successfully')
