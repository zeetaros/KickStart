from celery import Celery, shared_task, group
from celery.utils.log import get_task_logger

app = Celery()
logger = get_task_logger(__name__)

@app.task()
def print_hello():
    logger.info("Hello")

@app.task()
def add(x, y):
    return x + y


@app.task()
def error_handler(request, exc, traceback):
    print('Task {0} raised exception: {1!r}\n{2!r}'.format(
          request.id, exc, traceback))


