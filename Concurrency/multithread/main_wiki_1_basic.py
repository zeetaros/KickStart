import time
from workers.WikiWorker import WikiWorker
from workers.FinanceWorker import FinanceWorker


def main():
    wiki = WikiWorker()
    current_workers = []
    symbols = [s for s in wiki.get_sp_500_companies()]
    print(f"Fetched {len(symbols)} symbols")

    for symbol in symbols:
        finance_worker = FinanceWorker(symbol=symbol)
        current_workers.append(finance_worker)

    for i in range(len(current_workers)):
        current_workers[i].join()


if __name__ == "__main__":
    scraper_start_time = time.time()
    main()
    print(f"Extraction time took: {time.time() - scraper_start_time} seconds")
