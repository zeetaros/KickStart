import importlib  # internal library

import yaml
from multiprocessing import Queue


class PipelineExecutor:
    def __init__(self, pipeline_location):
        self._pipeline_location = pipeline_location
        self._queues = {}
        self._workers = {}

    def _load_pipeline(self):
        with open(self._pipeline_location, "r") as f:
            self._pipeline = yaml.safe_load(f)

    def _initialise_queues(self):
        for queue in self._pipeline["queues"]:
            self._queues[queue["name"]] = Queue()
        print(f"initialised queues: {self._queues}")

    def _initialise_workers(self):
        # 'workers' is a list of dictionaries
        for worker in self._pipeline["workers"]:
            module = importlib.import_module(worker["module"])
            worker_class_ = getattr(module, worker["class"])
            # NOTE: doing the above is similar to:
            # from workers.FinanceWorker import FinanceWorker

            input_queue = worker.get("input_queue")
            output_queues = worker.get("output_queues")
            worker_name = worker["name"]
            nb_threads = worker.get("threads", 1)  # default to 1 thread

            init_params = {
                "input_queue": self._queues[input_queue]
                if input_queue
                else None,
                "output_queues": [
                    self._queues[queue] for queue in output_queues
                ]
                if output_queues
                else None,
            }

            self._workers[worker_name] = []
            for i in range(nb_threads):
                self._workers[worker_name].append(
                    worker_class_(**init_params)  # unpack the dictionary
                )

    def _join_workers(self):
        for worker_name in self._workers:
            for worker_thread in self._workers[worker_name]:
                worker_thread.join()

    def process_pipeline(self):
        self._load_pipeline()
        self._initialise_queues()
        self._initialise_workers()
