from functools import wraps
from time import sleep
import logging


def procrastinate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sleep(2)
        return func(*args, **kwargs)

    return wrapper

def logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(__name__)
        logger.info(f'Calling function {func.__name__} with args: {args}, kwargs: {kwargs}')
        result = func(*args, **kwargs)
        logger.info(f'Calling function {func.__name__} returned: {result}')
        return result

    return wrapper
