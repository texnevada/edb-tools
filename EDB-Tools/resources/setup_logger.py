import logging
import datetime
import sys

# CRITICAL = 50
# ERROR = 40
# WARNING = 30
# INFO = 20
# DEBUG = 10
# NOTSET = 0

# Set the default encoding for the logging module
if sys.getdefaultencoding() != 'utf-8':
    sys.setdefaultencoding('utf-8')

def get_log(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(20)
    formatter = logging.Formatter('%(asctime)s | [%(levelname)s] | %(name)s: %(message)s')
    stream_formatter = logging.Formatter('%(message)s')

    now = datetime.datetime.now()
    time = now.strftime("%d.%m.%y")
    # For Linux later
    # time = now.strftime("%-d.%-m.%-y")
    file_handler = logging.FileHandler(f"logs/{time}.log")
    file_handler.setLevel(10)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(stream_formatter)
    stream_handler.setLevel(20)
    logger.addHandler(stream_handler)
    return logger
