
from os import environ

LOG_LEVEL = environ.get('LOG_LEVEL', 'WARNING')

BACKOFF = 10  # 10s backoff between requests
