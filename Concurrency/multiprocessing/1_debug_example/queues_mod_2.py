import time
from multiprocessing import Pool

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


if __name__ == "__main__":
    primes = []
    start = time.time()

    with Pool(4) as p:
        primes = [
            n + 1
            for n, prime in enumerate(p.map(is_prime, range(1, MAX_NUMBER)))
            if prime
        ]

    print(f"Total time: {time.time() - start} seconds")
    print(f"Total primes: {len(primes)}")
