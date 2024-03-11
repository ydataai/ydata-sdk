
from os import environ

LOG_LEVEL = environ.get('LOG_LEVEL', 'WARNING')
DEFAULT_URL = "https://fabric.ydata.ai/api"
BACKOFF = 10  # 10s backoff between requests
TOKEN_VAR = 'YDATA_TOKEN'
