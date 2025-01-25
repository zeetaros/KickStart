import logging

loglevels = {
    "CRITICAL": logging.CRITICAL,
    "WARNING": logging.WARNING,
    "INFO": logging.INFO,
    "DEBUG": logging.DEBUG,
    "": logging.INFO
}

def setup_logger(name):
     formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
     handler = logging.StreamHandler()
     handler.setFormatter(formatter)

     logger = logging.getLogger(name)
     # Update log level globally
     logger.setLevel(loglevels["DEBUG"])
     logger.addHandler(handler)
     return logger
