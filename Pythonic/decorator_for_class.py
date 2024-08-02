"""
Decorator for class
"""


def add_str(cls):
    def __str__(self):
        """
        write custom __str__ method for the class
        """
        return str(self.__dict__)

    # NOTE: overwrite the __str__ method of the class
    cls.__str__ = __str__
    return cls


@add_str
class MyObject:
    def __init__(self, a, b):
        self.a = a
        self.b = b


# NOTE: this is equivalent to:
#       MyObject = add_str(MyObject)
# this decorator overwrites the __str__ method of MyObject class
# and returns the class itself

# NOTE: this is similar to the implementation of dataclass

o = MyObject(1, 2)
print(o)
