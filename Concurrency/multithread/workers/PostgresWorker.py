import os
import threading
from queue import Empty
from sqlalchemy import create_engine
from sqlalchemy.sql import text


class PostgresWorker:
    def __init__(self, symbol, price, extracted_time) -> None:
        self._symbol = symbol
        self._price = price
        self._extracted_time = extracted_time

        # get database creds from env vars
        self._PG_USER = os.environ.get("PG_USER") or ""
        self._PG_PWD = os.environ.get("PG_PWD") or ""
        self._PG_HOST = os.environ.get("PG_HOST") or "localhost"
        self._PG_DB = os.environ.get("PG_DB") or "postgres"

        self._engine = create_engine(
            f"postgresql://{self._PG_USER}:{self._PG_PWD}@{self._PG_HOST}/{self._PG_DB}"
        )

    def insert_into_db(self):
        """_summary_
        Do insertion of price to the Postgres database
        """
        insert_query = self._create_insert_query()

        with self._engine.connect() as conn:
            conn.execute(
                text(insert_query),
                {
                    "symbol": self._symbol,
                    "price": self._price,
                    "extracted_time": self._extracted_time,
                },
            )

    def _create_insert_query(self):
        sql_query = """INSERT INTO prices (symbol, price, extracted_time)
         VALUES (:symbol, :price, :extracted_time)"""
        return sql_query


class PostgresMasterScheduler(threading.Thread):
    def __init__(self, input_queue, **kwargs):
        if "output_queues" in kwargs:
            del kwargs["output_queues"]
        # call initialisation method of all parent classes
        super(PostgresMasterScheduler, self).__init__(**kwargs)
        self._input_queue = input_queue

        # start the threads
        self.start()

    def run(self):
        while True:
            try:
                val = self._input_queue.get(timeout=10)
            except Empty:
                print("Timeout, no more data to process")
            # NOTE: this is an alternative way to exit the worker
            # stop waiting for new items if the queue is empty for 10 seconds

            # in this case, we don't need to put a "DONE" marker in the queue
            if val == "DONE":
                break

            symbol, price, extracted_time = val
            postgres_worker = PostgresWorker(
                symbol=symbol, price=price, extracted_time=extracted_time
            )
            postgres_worker.insert_into_db()
