import sys
import logging
from loguru import logger

def setup(LOGGER_PATH: str):
    logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
    logger.add(LOGGER_PATH + "/log.log")
