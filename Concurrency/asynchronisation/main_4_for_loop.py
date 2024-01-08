import asyncio
import time


async def async_sleep(id):
    print("Before sleep >>>", id)
    n = max(2, id)
    for i in range(1, n):
        yield i
        await asyncio.sleep(i)
    print(">>>After sleep", id)


async def print_hello():
    print("Hello")


async def return_hello():
    return "Hello there"


async def main():
    # Async For loop doesn't mean the items in the loop are executed concurrently
    # It merely add a concurrent option to the entire loop itself,
    # which can be run concurrently with other tasks
    # The items in the loop are still executed sequentially.
    async for k in async_sleep(5):
        print(k)


if __name__ == "__main__":
    start_time = time.time()
    # start an event loop
    asyncio.run(main())
    print(f"Operation took: {time.time() - start_time} seconds")
