import time
from celery import group, shared_task, app
from ..utils.monitoring import check_unload_error, send_notification

def unload(table):
    if check_unload_error():
        raise 

def copy_s3_to_ec2(table):
    pass

@shared_task
def unload_copy(table):
    retry_count = 0
    try:
        unload()
    except:
        unload_copy.retry()
        if retry_count >= 5:
            send_notification()
            raise

    copy_s3_to_ec2()
