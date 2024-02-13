import threading


class SquaredSumWorker(threading.Thread):
    def __init__(self, n, **kwargs):
        # call initialisation method of all parent classes
        super(SquaredSumWorker, self).__init__()
        self._n = n

        # start the threads
        self.start()

    def _calculate_sum_squares(self):
        sum_squares = 0
        for i in range(self._n):
            sum_squares += i**2

        print(sum_squares)

    # override the run method in threading.Thread
    def run(self):
        self._calculate_sum_squares()
