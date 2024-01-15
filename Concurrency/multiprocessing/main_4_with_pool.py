"""
Using Pool to simplify the code without using Queue
"""
import time
from multiprocessing import Pool, cpu_count
from functools import partial  # use to pass multiple arguments to Pool


def square(x):
    return x**2 + 3


def take_power(power, constant, x):
    # NOTE: to use partial later on, the argument order matters
    # the args intended for pre-assignment needs to be in the front
    return x**power + constant


if __name__ == "__main__":
    start_time = time.time()
    comparison_list = [1, 2, 3, 79000000, 49000000]

    nb_processes = cpu_count()
    print(f"There are {nb_processes} CPUs available.\n")
    nb_processes_to_use = max(1, cpu_count() - 1)

    power = 2
    constant = 3
    partial_function = partial(take_power, power, constant)

    # 1. use context manager to handle
    # 2. create a pool of processes;
    #    when there are tasks, a process will be taken out from the pool;
    #    once it finished the task, it is back in the pool and available again.
    with Pool(nb_processes_to_use) as mp_pool:
        result = mp_pool.map(square, comparison_list)
        result2 = mp_pool.map(partial_function, comparison_list)

    print(result)
    print(result2)

    print(f"\nM-Processing took: {time.time() - start_time} seconds")
