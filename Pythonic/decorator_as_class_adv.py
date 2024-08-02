"""
(Advanced) Using class to write a decorator
"""

import time


class Decorator:
    def timeit(func):
        """
        A helper function for the class without "self".
        This can be used as a decorator for this class's methods.
        """

        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            print(f"Time taken: {time.time() - start_time}")
            return result

        return wrapper

    @timeit
    def add(self, a, b):
        return a + b

    # NOTE: this uses the decoractor defined in the class for its own method

    """
    The below allows the decorator to be used externally
    WARNING: to enable this, this line has to be defined at the end of the class
    """
    timeit = staticmethod(timeit)

    # NOTE: this is equivalent to using @staticmethod to decorate the method


@Decorator.timeit
def sub(a, b):
    return a - b


d = Decorator()

print(d.add(1, 2))
print(sub(1, 2))
