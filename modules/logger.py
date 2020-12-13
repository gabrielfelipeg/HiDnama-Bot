import logging
import os

LOG_PATH = "./logs.log"
LOG_INITIAL_LEVEL = "DEBUG"
directory_name = os.path.dirname(LOG_PATH)
if not os.path.exists(directory_name):
    os.makedirs(directory_name, exist_ok=True)
logging.basicConfig(
    format = '%(asctime)s|%(levelname)s|%(name)s.%(funcName)s|%(message)s',
    datefmt="%Y-%m-%dT%H:%M:%S%z",
    level = LOG_INITIAL_LEVEL,
    handlers = [
        logging.FileHandler(LOG_PATH, "a", "utf-8"),
        logging.StreamHandler()
    ]
)