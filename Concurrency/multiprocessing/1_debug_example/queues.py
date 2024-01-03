import time
from multiprocessing import Queue, Process

MAX_NUMBER = 100000


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:  # bitwise AND
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True


def worker(inq, outq):
    while n := inq.get():
        if is_prime(n):
            outq.put(n)
    outq.put(None)


if __name__ == "__main__":
    primes = []
    start = time.time()
    inq = Queue()
    outq = Queue()

    # NOTE: <<< SPEED-UP RATIO >>>
    # by using 4 parallel processes, the speed-up ratio expected is 4x
    # however, if it is significantly less than 4x,
    # it means improvement of the implementation is needed.
    workers = [Process(target=worker, args=(inq, outq)) for _ in range(4)]

    for w in workers:
        w.start()

    # Put all the numbers into the input queue
    for i in range(1, MAX_NUMBER):
        inq.put(i)

    for _ in range(4):
        inq.put(None)

    # NOTE: <<< COMMUNICATION COST >>>
    # however, this implementation has high communication cost
    # because it does 1 communication per number;
    # to speed up, we can first put a batch of numbers into a list
    # then put the list into the queue

    finish = 0
    # stop when getting 4 None from the input queue
    while finish < 4:
        if n := outq.get():
            primes.append(n)
        else:
            finish += 1

    print(f"Total time: {time.time() - start} seconds")
    print(f"Total primes: {len(primes)}")
