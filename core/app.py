import logging

from config.log import setup_logging

setup_logging()

logger = logging.getLogger()

def main():
    logger.critical("It works")
