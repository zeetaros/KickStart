import time
from multiprocessing import Queue
from workers.WikiWorker import WikiWorker
from workers.FinanceWorker import FinanceWorker, FinanceScheduler


def main():
    wiki = WikiWorker()
    symbol_queue = Queue()
    counter = 0
    nb_workers = 10
    current_workers = []
    for i in range(nb_workers):
        # getting workers ready to consume the queue
        scheduler = FinanceScheduler(input_queue=symbol_queue)
        current_workers.append(scheduler)

    for symbol in wiki.get_sp_500_companies():
        symbol_queue.put(symbol)
        # once a symbol is put in the queue, the workers set up earlier will pick it up
        counter += 1

    print(f"Fetched {counter} symbols")

    for i in range(len(current_workers)):
        # place a marker to indicate the end of the queue
        symbol_queue.put("DONE")
        # need 1 "DONE" for each worker because once a worker has taken a "DONE" from the queue,
        # the others won't see it anymore.

    for i in range(len(current_workers)):
        current_workers[i].join()


if __name__ == "__main__":
    scraper_start_time = time.time()
    main()
    print(f"Extraction time took: {time.time() - scraper_start_time} seconds")
