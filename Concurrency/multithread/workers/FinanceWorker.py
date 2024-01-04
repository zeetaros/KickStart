import time
import random
import threading
import requests
from datetime import datetime
from lxml import html


class FinanceWorker(threading.Thread):
    """_summary_
    A class to scrap the stock price from Yahoo Finance.

    Using the WikiWorker to get S&P 500 company names,
    and then use the FinanceWorker to get the stock price for each company.

    Args:
        threading (_type_): _description_
    """

    def __init__(self, symbol, *args, **kwargs):
        super(FinanceWorker, self).__init__(*args, **kwargs)
        self._symbol = symbol
        base_url = "https://finance.yahoo.com/quote/"
        self._url = f"{base_url}{self._symbol}"
        # start the thread
        self.start()

    def get_price(self):
        """_summary_
        This method is called when the thread is started.
        """
        time.sleep(20 * random.random())
        res = requests.get(self._url)
        if res.status_code != 200:
            print(f"Failed to get {self._symbol}")
            return
        page_content = html.fromstring(res.text)
        price = float(
            page_content.xpath(
                '//*[@id="quote-header-info"]/div[3]/div[1]/div/fin-streamer[1]'
            )[0].text.replace(",", "")
        )
        return price

    # override the run method
    def run(self):
        price = self.get_price()
        print(f"{self._symbol.ljust(5)} price: {price}")


class FinanceScheduler(threading.Thread):
    def __init__(self, input_queue, output_queues=None, **kwargs):
        super(FinanceScheduler, self).__init__(**kwargs)
        # to read from the queue
        self._input_queue = input_queue
        # create output queue if provided
        self._output_queues = output_queues
        # start the thread
        self.start()

    # override the run method
    def run(self):
        while True:
            val = self._input_queue.get()
            # need a exit condition otherwise the thread will keep waiting
            # to get new items in the queue while the queue is empty
            if val == "DONE":
                break

            finance_worker = FinanceWorker(symbol=val)
            price = finance_worker.get_price()
            if self._output_queues is not None:
                for output_queue in self._output_queues:
                    output_queue.put((val, price, datetime.utcnow()))
            else:
                print(f"{val.ljust(5)} price: {price}")
            time.sleep(
                random.random()
            )  # slow the process down for 0-1 seconds
