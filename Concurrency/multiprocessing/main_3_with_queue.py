"""
Using queue to distribute tasks
"""
import time
from multiprocessing import Process, Queue


def check_value_in_list(x, i, nb_processes, queue):
    """
    Improvement: split out workload over different segments
                 workload distributed using queues
    """
    max_number_to_check = 10**8
    # below way of splitting: equal batch size with process 1 take 1st batch and so on.
    lower_bound = int(i * max_number_to_check / nb_processes)
    upper_bound = int((i + 1) * max_number_to_check / nb_processes)
    nb_of_hits = 0
    for i in range(lower_bound, upper_bound):
        if i in x:
            nb_of_hits += 1
    queue.put((lower_bound, upper_bound, nb_of_hits))


if __name__ == "__main__":
    start_time = time.time()
    nb_processes = 4
    comparison_list = [1, 2, 3, 79000000, 49000000]
    inq = Queue()
    processes = []

    for i in range(nb_processes):
        p = Process(
            target=check_value_in_list,
            args=(comparison_list, i, nb_processes, inq),
        )  # NOTE: have to include a commas in 'args'
        processes.append(p)

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    inq.put("DONE")

    while True:
        val = inq.get()
        if val == "DONE":
            break
        lower, upper, nb_hits = val
        print(
            f"Between {lower} and {upper}, there are {nb_hits} values in the list."
        )

    print(f"M-Processing took: {time.time() - start_time} seconds")
