"""
Using function to write a decorator
"""

import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Time taken: {time.time() - start}")
        return result

    return wrapper


@timeit
def my_func(x):
    time.sleep(x)


# NOTE: this is equivalent to:
#       my_func = timeit(my_func)
# this is like running function timeit which takes
# my_func as an argument and returns a wrapper function

my_func(2)
