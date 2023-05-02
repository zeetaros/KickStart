import logging

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
loglevels = {
    "CRITICAL": logging.CRITICAL,
    "WARNING": logging.WARNING,
    "INFO": logging.INFO,
    "DEBUG": logging.DEBUG,
    "": logging.INFO
}
logger.setLevel(logging.DEBUG)


def lambda_handler(_event, _context):
    logger.info("Lambda: cc-test-event-consumer1 started!")
    logger.info(f"event body: {_event}")
    logger.debug("Lambda done!")
    