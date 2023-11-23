import time
from threading import Thread, Lock


class Singleton(type):
    """
    Only one instance; A single point of access for a resource
    Uses:
        - Network manager
        - Database access
        - Logging
        - Configuration
        - Utility class(es)

    Cons:
        - Breaks single responsibility
        - Testability issues as it needs to handle multiple situations
        - State for life
    """
    _instances = {}
    _lock = Lock()

    def __call__(self, *args, **kwargs):
        with self._lock:
            if self not in self._instances:
                instance = super().__call__(*args, **kwargs)
                time.sleep(1)  # add this in as the machine needs some time to provision resource when creating the 1st instance
                self._instances[self] = instance 
        return self._instances[self]
    

class NetworkDriver(metaclass=Singleton):
    def log(self):
        # print out the instance of the class
        print(f"{self}\n")

def create_singleton():
    singleton = NetworkDriver()
    singleton.log()
    return singleton

if __name__ == "__main__":
    # single thread
    print("\n------ single thread -----\n")
    s1 = create_singleton()
    s2 = create_singleton()

    # multi thread
    print("\n------ multi-thread -----\n")
    p1 = Thread(target=create_singleton())
    p2 = Thread(target=create_singleton())

    """
    example output (without Lock):
        <__main__.NetworkDriver object at 0x7fbdb191cd90>
        <__main__.NetworkDriver object at 0x7fbdb191c040>
        
        ** different memory addresses

    example output (with Lock):
        <__main__.NetworkDriver object at 0x7fcc9891cd00>
        <__main__.NetworkDriver object at 0x7fcc9891cd00>

        ** same memory addresses
    """