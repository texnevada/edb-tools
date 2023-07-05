import time

from functools import wraps
from resources.setup_logger import get_log

log = get_log(__name__)


def function_runtime(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        finish = time.perf_counter()
        time_elapsed = round(start - finish, 5)
        log.debug(f"Function took {time_elapsed}s")
        return result
    return wrapper
