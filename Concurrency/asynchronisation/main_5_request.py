"""
Show async v.s. sync requests
"""
import time
import requests
import asyncio
import aiohttp


async def get_url_response(url):
    """
    This async context managers give the opportunity for the event loop to 
    continue running other operations while the request is being made.
    It takes back the control after it gets the html response and it's ready to proceed.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


def get_url_with_requests(url):
    """
    This blocks the event loop until the request is made and the response is received.
    """
    return requests.get(url).text


async def main():
    urls = [
        "https://google.com",
        "https://python.org",
        "https://stackoverflow.com",
        "https://www.apple.com",
    ]

    start_time = time.time()
    sync_responses = []
    for url in urls:
        sync_responses.append(get_url_with_requests(url))

    end_time = time.time()
    print(f"Sync operation took: {end_time - start_time} seconds")

    start_time = time.time()
    async_responses = []
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(get_url_response(url)))
    await asyncio.gather(*tasks)  # unpack the list of tasks

    print(f"Async operation took: {time.time() - start_time} seconds")


if __name__ == "__main__":
    asyncio.run(main())
    
