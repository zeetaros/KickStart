import threading
import requests
from bs4 import BeautifulSoup


class WikiWorker:
    def __init__(self, **kwargs) -> None:
        self._url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

    def _extract_company_symbols(self, page_html):
        soup = BeautifulSoup(page_html, "html.parser")
        table = soup.find(id="constituents")
        rows = table.find_all("tr")
        symbols = []
        for row in rows[1:]:
            symbol = row.find("td").text.strip("\n")
            yield symbol
        #     symbols.append(symbol)
        # return symbols

    def get_sp_500_companies(self):
        response = requests.get(self._url)
        if response.status_code != 200:
            print("Error while fetching page")
            return []

        yield from self._extract_company_symbols(response.text)


class WikiScheduler(threading.Thread):
    def __init__(self, output_queues, **kwargs):
        if "input_queue" in kwargs:
            del kwargs["input_queue"]
        self._entries = kwargs.pop("input_values")
        temp_queue = output_queues
        if type(temp_queue) != list:
            temp_queue = [temp_queue]
        self._output_queues = temp_queue
        super(WikiScheduler, self).__init__(**kwargs)
        self.start()

    def run(self):
        for entry in self._entries:
            wiki_worker = WikiWorker(entry)
            counter = 0
            for symbol in wiki_worker.get_sp_500_companies():
                for outq in self._output_queues:
                    outq.put(symbol)
                # once a symbol is put in the queue, the workers set up earlier will pick it up
                counter += 1

            print(f"Fetched {counter} symbols")
