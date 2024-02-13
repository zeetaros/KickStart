import time
from workers.SleepyWorkers import SleepyWorker
from workers.SquaredSumWorkers import SquaredSumWorker


def main():
    calc_start_time = time.time()
    current_workers = []

    for i in range(5):
        maximum_value = (i + 1) * 100000
        squared_sum_worker = SquaredSumWorker(n=maximum_value)
        current_workers.append(squared_sum_worker)

    for i in range(len(current_workers)):
        # block the thread when it finishes, prevent it from proceeding.
        current_workers[i].join()

    print(
        f"\nCalculating sum of squares took: {round(time.time() - calc_start_time, 1)}"
    )

    sleep_start_time = time.time()
    current_threads = []
    for seconds in range(1, 6):
        sleepy_worker = SleepyWorker(seconds=seconds)


if __name__ == "__main__":
    main()
