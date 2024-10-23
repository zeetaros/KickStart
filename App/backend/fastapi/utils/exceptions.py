from email.policy import HTTP
import logging
from functools import wraps
from fastapi import HTTPException, status

logger = logging.getLogger(__name__)


class DocumentNotFoundError(Exception):
    def __init__(self, msg):
        self.msg = msg


def handle_doc_not_found(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except DocumentNotFoundError as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=e.msg,
            )
        except Exception as e:
            raise e

    return wrapper
