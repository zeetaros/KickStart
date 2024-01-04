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
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def worker(inq, outq):
    # NOTE: <<< BATCHING >>>
    # each element in the queue is a tuple (start, end) for the mini batch
    # the worker then generates all the numbers in the mini batch;
    # in this way, no longer insert 1 number at a time to the queue

    # likewise, all primes in the mini batch are wrapped in a list
    # before being put into the output queue;
    # communication only happens once per mini batch
    while val := inq.get():
        start, end = val
        primes = []
        for n in range(start, end):
            if is_prime(n):
                primes.append(n)
        outq.put(primes)
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
    for i in range(4):
        inq.put((i * MAX_NUMBER // 4, (i + 1) * MAX_NUMBER // 4))

    for _ in range(4):
        inq.put(None)

    # NOTE: <<< LOAD BALANCE >>>
    # when creating the mini batches, this implementation has not
    # fully considered the load balance;
    # for the case of finding primes, the bigger the number the longer it takes
    # hence, the process handling the last batch takes significantly longer

    finish = 0
    # stop when getting 4 None from the input queue
    while finish < 4:
        if n := outq.get():
            primes.extend(n)
        else:
            finish += 1

    print(f"Total time: {time.time() - start} seconds")
    print(f"Total primes: {len(primes)}")
