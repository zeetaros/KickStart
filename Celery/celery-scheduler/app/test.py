import celery
from celery import Celery

app = Celery()

@app.task()
def print_hello():
    logger = print_hello.get_logger()
    logger.info("Hello")