from celery.schedules import crontab


imports = ('app.tasks.test', 
           'app.tasks.test_parallel_tasks'
           )
result_expires = 30
timezone = 'UTC'

accept_content = ['json', 'msgpack', 'yaml']
task_serializer = 'json'
result_serializer = 'json'

beat_schedule = {
    # 'test-celery': {
    #     'task': 'app.tasks.test.print_hello',
    #     # Every minute
    #     'schedule': crontab(hour="*", minute="*"),
    # },
    'execute-add': {
        'task': 'app.tasks.test_parallel_tasks.group_add',
        # Every minute
        'schedule': crontab(minute="*"),
    }
}