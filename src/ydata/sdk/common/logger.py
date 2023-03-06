import logging
import sys
from typing import TextIO


def create_logger(name, stream: TextIO = sys.stdout, level=logging.INFO):
    handler = logging.StreamHandler(stream)
    handler.setFormatter(
        logging.Formatter(
            "%(asctime)s | %(levelname)s | %(module)s:%(lineno)d | %(message)s"
        )
    )

    logger = logging.getLogger(name)
    logger.addHandler(handler)
    logger.setLevel(level)
    logger.propagate = False

    return logger
