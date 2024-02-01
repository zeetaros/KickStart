"""
Using class to write a decorator
"""

import time


class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        """
        this method overwrites the __call__ method of the class
        which this decorator is used on
        """
        start_time = time.time()
        result = self.func(*args, **kwargs)
        print(f"Time taken: {time.time() - start_time}")
        return result


class TimerWithArgs:
    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, func):
        """
        takes a function as an argument instead
        """

        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            print(f"[{self.prefix}] Time taken: {time.time() - start_time}")
            return result

        return wrapper


@Timer
def add(a, b):
    return a + b


# NOTE: this is equivalent to:
#       add = Timer(add)
# it is same as calling Timer over the result of add function
# when it call Timer it invokes the __call__ method of Timer class


@TimerWithArgs(prefix="information")
def sub(a, b):
    return a - b


# NOTE: this is equivalent to:
#       sub = TimerWithArgs(prefix="information")(sub)
# this is like contructing a class TimerWithArgs and invoke its
# __call__ method while passing sub function as an argument

print(add(1, 2))
print(sub(1, 2))
