"""
Updating a script from using multithread to multiprocess
"""
import time
from multiprocessing import Process


def check_value_in_list(x):
    for i in range(10**8):
        i in x  # return boolean


if __name__ == "__main__":
    start_time = time.time()
    nb_processes = 4
    comparison_list = [1, 2, 3]
    processes = []

    for i in range(nb_processes):
        p = Process(
            target=check_value_in_list, args=(comparison_list,)
        )  # NOTE: have to include a commas in 'args'
        processes.append(p)

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print(f"M-Processing took: {time.time() - start_time} seconds")
