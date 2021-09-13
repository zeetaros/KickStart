CELERY_BROKER_URL = env('CELERY_BROKER_URL', default='amqp://guest:guest@localhost:5672//')
CELERY_RESULT_BACKEND = 'django-db+sqlite:///results.sqlite'