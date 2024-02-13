import os
import time
from workers.WikiWorker import WikiWorker
from pipelines.Orchestrator import PipelineExecutor


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    pipeline_location = os.path.join(
        dir_path, "pipelines/wiki_finance_scraper.yaml"
    )
    pipe_executor = PipelineExecutor(pipeline_location)
    pipe_executor.process_pipeline()

    for i in range(20):
        # place a marker to indicate the end of the queue
        pipe_executor._queues["SymbolQueue"].put("DONE")
        # need 1 "DONE" for each worker because once a worker has taken a "DONE" from the queue,
        # the others won't see it anymore.

    pipe_executor._join_workers()


if __name__ == "__main__":
    scraper_start_time = time.time()
    main()
    print(f"Extraction time took: {time.time() - scraper_start_time} seconds")
