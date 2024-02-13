import time
from multithread.workers.SleepyWorker import SleepyWorker
from multithread.workers.SquaredSumWorker import SquaredSumWorker


def main():
    calc_start_time = time.time()
    current_workers = []

    for i in range(5):
        maximum_value = (i + 1) * 1000000
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
        sleepy_worker = SleepyWorker(seconds=seconds, daemon=True)
        current_threads.append(sleepy_worker)

    """_note_
    If already set the 'daemon' parameter in the SleepyWorker class,
    then the following code is not necessary.

    setting daemon=True
        - sleep took: 0.0

    not setting daemon but include the following code
        - sleep took: 5.0
    """
    # for i in range(len(current_threads)):
    #     current_threads[i].join()

    print(f"sleep took: {round(time.time() - sleep_start_time, 1)}")


if __name__ == "__main__":
    main()
