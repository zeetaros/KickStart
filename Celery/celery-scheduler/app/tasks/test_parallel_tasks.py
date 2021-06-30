from celery import group, shared_task, app
import time
# from ..tasks.test import add, error_handler


@shared_task
def add(x, y, wait=None, error=0):
    if wait:
        print(f'Processing task... input: {x}, {y}')
        time.sleep(wait)
        if error > 0:
            add.retry()
            raise ValueError
        print(f'Completed task! input: {x}, {y}')
    return x + y

# @app.task(name="test-parallel.add")
@shared_task
def group_add():
    print('kicked off task')
    job = group([
            add.s(2, 2, wait=10),   # 4
            add.s(4, 4, wait=8, error=0),    # 8
            add.s(8, 8, wait=20),   # 16
            add.s(16, 16, wait=5),  # 32
            add.s(32, 32),          # 64
            add.s(64, 64, wait=10),
            add.s(128, 128, wait=2),
    ])
    # result = job.apply_async(link_error=error_handler.s())
    result = job.apply_async(retry=True, retry_policy={
                                                        'max_retries': 3,
                                                        'interval_start': 0,
                                                        'interval_step': 0.2,
                                                        'interval_max': 0.2,
                                                    })
    print('passed job.apply_async!')
    result.ready()  # have all subtasks completed?
    print('passed result.ready!')
    result.successful() # were all subtasks successful?
    print('passed result.successful!')
    # result.get()