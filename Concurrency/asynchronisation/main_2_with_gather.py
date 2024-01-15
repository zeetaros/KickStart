import asyncio
import time


async def async_sleep(id):
    print("Before sleep >>>", id)
    await asyncio.sleep(5)
    print(">>>After sleep", id)


async def print_hello():
    print("Hello")


async def return_hello():
    return "Hello there"


async def main():
    task = asyncio.create_task(async_sleep(1))
    """
    Having the below set up will schedule the operations sequentially

    await async_sleep(2) 
    await print_hello()
    await task
    result = await return_hello()

    but not in parallel. To schedule the operations in parallel, use asyncio.gather
    """
    await asyncio.gather(async_sleep(2), print_hello(), task, return_hello())
    # this give better concurrent nature


if __name__ == "__main__":
    start_time = time.time()
    # start an event loop
    asyncio.run(main())
    print(f"Operation took: {time.time() - start_time} seconds")
