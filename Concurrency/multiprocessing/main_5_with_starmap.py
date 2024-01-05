"""
Using starmap to pass on multiple varying arguments
"""
import time
from multiprocessing import Pool, cpu_count

"""
Example 1
"""


def take_power(x, power):
    # NOTE: to use partial later on, the argument order matters
    # the args intended for pre-assignment needs to be in the front
    return x**power


"""
Example 2
"""


def check_value_in_list(comp_list, lower_bound, upper_bound):
    nb_of_hits = 0
    for i in range(lower_bound, upper_bound):
        if i in comp_list:
            nb_of_hits += 1
    return nb_of_hits


if __name__ == "__main__":
    start_time = time.time()
    nb_processes = cpu_count()
    print(f"There are {nb_processes} CPUs available.\n")
    nb_processes_to_use = max(1, cpu_count() - 1)

    comparison_list = [1, 2, 3]

    """
    Prep for example 1
    """
    power_list = [4, 5, 6]

    prepared_power_list = [
        (comparison_list[i], power_list[i])
        for i in range(len(comparison_list))
    ]

    """
    Prep for example 2
    """
    lower_upper_bounds = [
        (0, 25 * 10**6),
        (25 * 10 * 6, 50 * 10**6),
        (50 * 10**6, 75 * 10 * 6),
        (75 * 10 * 6, 10**8),
    ]

    prepared_checkin_list = [
        (comparison_list, lower_upper_bounds[i][0], lower_upper_bounds[i][1])
        for i in range(len(lower_upper_bounds))
    ]

    with Pool(nb_processes_to_use) as mp_pool:
        result = mp_pool.starmap(take_power, prepared_power_list)
        # same as [take_power(1, 4), take_power(2, 5), take_power(3, 6)]

        result2 = mp_pool.starmap(check_value_in_list, prepared_checkin_list)
        # same passing [([1, 2, 3], 0, 25 * 10**6),
        #               ([1, 2, 3], (25 * 10 * 6, 50 * 10**6),
        #               .....    ]
        # arguments to the function respectively in 4 rounds.

    print(result)
    print(result2)

    print(f"\nM-Processing took: {time.time() - start_time} seconds")
