from functools import wraps
from time import sleep


def procrastinate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sleep(2)
        return func(*args, **kwargs)

    return wrapper

