"""
Updating a script from using multithread to multiprocess
"""
import time
from threading import Thread


def check_value_in_list(x):
    for i in range(10**8):
        i in x  # return boolean


if __name__ == "__main__":
    start_time = time.time()
    nb_threads = 4
    comparison_list = [1, 2, 3]
    threads = []

    for i in range(nb_threads):
        t = Thread(
            target=check_value_in_list, args=(comparison_list,)
        )  # NOTE: have to include a commas in 'args'
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print(f"M-Threading took: {time.time() - start_time} seconds")
