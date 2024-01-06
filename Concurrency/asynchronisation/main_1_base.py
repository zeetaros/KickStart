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
    # create a task which the programme can work on when resource is available
    # the result is not guaranteed to return until calling "await"
    task = asyncio.create_task(async_sleep(1))
    await async_sleep(2) 
    # "await" gives control back to event loop 
    # indicating no resource is required for this operation
    # until the result is returned; so resource can be released immediately
    # to continue the next operation.
    await task
    await print_hello()
    result = await return_hello()
    print(result)


if __name__ == "__main__":
    start_time = time.time()
    # start an event loop
    asyncio.run(main())
    print(f"Operation took: {time.time() - start_time} seconds")
