import time
import threading


def calc_sum_squares(n):
    """
    To speed up this part, multiprocessing is a better choice
    because it's computational intensive. 
    For threading in Python, only 1 thread can be run at a time due to GIL.
    """
    sum_sq = 0
    for i in range(n):
        sum_sq += i ** 2
    print(sum_sq)

def sleep_1():
    sleep_start_time = time.time()
    current_threads = []
    for seconds in range(1, 6):
        t = threading.Thread(target=time.sleep, args=(seconds,))
        # start the thread
        t.start()
        # block the loop iteration until the thread is finished
        # this is almost no difference to not using multi-thread
        t.join()
        current_threads.append(t)

    print(f"\nSleep took: {round(time.time() - sleep_start_time, 1)}")


def sleep_2():
    sleep_start_time = time.time()
    current_threads = []
    for seconds in range(1, 6):
        t = threading.Thread(target=time.sleep, args=(seconds,))
        # start the thread
        t.start()

        current_threads.append(t)

    # the previous loop continues on different thread.
    # only when the loop has finished did we block the thread - this is means the loop is running simultaneously
    for i in range(len(current_threads)):
        current_threads[i].join()

    print(f"\nSleep took: {round(time.time() - sleep_start_time, 1)}")


def main():
    calc_start_time = time.time()
    current_threads = []

    for i in range(5):
        maximum_value = (i + 1) * 100000
        t = threading.Thread(target=calc_sum_squares, args=(maximum_value, ))
        # start the thread
        t.start()

        current_threads.append(t)

    for i in range(len(current_threads)):
        # block the thread when it finishes, prevent it from proceeding.
        current_threads[i].join()

    print(f"\nCalculating sum of squares took: {round(time.time() - calc_start_time, 1)}")

    # sleep_1() # this takes 15 sec
    sleep_2() # this takes 5 sec

if __name__ == "__main__":
    main()