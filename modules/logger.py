import logging
import os

class Logger:
    
    def __init__(self):
        LOG_PATH = "./logs.log"
        directory_name = os.path.dirname(LOG_PATH)
        if not os.path.exists(directory_name):
            os.makedirs(directory_name, exist_ok=True)
        logging.basicConfig(
            filename = LOG_PATH,
            format = '%(asctime)s|%(levelname)s|%(name)s.%(funcName)s|%(message)s',
            datefmt="%Y-%m-%dT%H:%M:%S%z",
            level = logging.DEBUG
        )