logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(asctime)s - [%(levelname)s] - %(name)s:%(funcName)s:%(lineno)s - %(module)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M%S",
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["default"],
    },
    "loggers": {
        "boto3": {
            "level": "WARNING",
        },
        "botocore": {
            "level": "WARNING",
        },
    },
}
