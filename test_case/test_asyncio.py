import asyncio
import threading
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_all(session, urls):
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(fetch(session, url))
        tasks.append(task)
    return await asyncio.gather(*tasks)

def fetch_all_threaded(urls, loop):
    async def run_in_loop():
        async with aiohttp.ClientSession(loop=loop) as session:
            return await fetch_all(session, urls)

    return loop.run_until_complete(run_in_loop())

if __name__ == '__main__':
    urls = [
        'https://jsonplaceholder.typicode.com/posts/1',
        'https://jsonplaceholder.typicode.com/posts/2',
        'https://jsonplaceholder.typicode.com/posts/3'
    ]

    loop = asyncio.get_event_loop()
    results = fetch_all_threaded(urls, loop)
    print(results)