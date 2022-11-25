import sys
from loguru import logger as logrus

def setup(LOGGER_PATH: str):
    logrus.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
    logrus.add(LOGGER_PATH + "/log.log")
