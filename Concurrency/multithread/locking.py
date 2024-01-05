"""
A race condition is when multiple processes try to access the same resource.
Locking can be used to prevent race conditions.

# threading.Lock().acquire()
# threading.Lock().release()
"""

import threading


counter = 0
lock = threading.Lock()


def increment_ver_1():
    global counter  # 'global' allows modifying the global variable but not just change locally
    for i in range(10**6):
        lock.acquire()
        counter += 1
        lock.release()


def increment_ver_2():
    global counter
    for i in range(10**6):
        with lock:
            counter += 1


threads = []

# 4 threads; each thread increment the value by 10
for i in range(4):
    x = threading.Thread(target=increment_ver_2)
    threads.append(x)

for t in threads:
    # without a lock, the race condition occurs when numbers are
    # not read by threads sequentially when we expected so.
    t.start()

for t in threads:
    t.join()

print(f"Counter value: {counter}")
