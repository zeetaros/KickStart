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

    try:
        await asyncio.gather(
            asyncio.wait_for(async_sleep(30), 5),
            task,
            print_hello(),
            return_hello(),
        )
    except asyncio.TimeoutError:
        print("Timeout error")


if __name__ == "__main__":
    start_time = time.time()
    # start an event loop
    asyncio.run(main())
    print(f"Operation took: {time.time() - start_time} seconds")
