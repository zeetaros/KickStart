from celery.schedules import crontab
from kombu import Exchange, Queue


redis_host = "0.0.0.0"
imports = ('app.tasks.test', 
           'app.tasks.test_parallel_tasks'
           )
result_expires = 30
enable_utc = True
timezone = 'UTC'

accept_content = ['json', 'msgpack', 'yaml']
task_serializer = 'json'
result_serializer = 'json'

beat_schedule = {
    'execute-add': {
        'task': 'app.tasks.test_parallel_tasks.group_add',
        # Every minute
        'schedule': crontab(minute="*"),
    }
}

task_queues = (
    Queue("my_queue_1", Exchange("my_exchange_1", type="direct", durable=False), routing_key="my_queue_1"),
    Queue("my_queue_2", Exchange("my_exchange_2", type="direct", durable=False), routing_key="my_queue_2")
)
