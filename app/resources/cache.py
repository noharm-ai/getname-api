from flask_caching import Cache
from dotenv import load_dotenv
import os

HOUR = 3600

load_dotenv()

config = {
    "CACHE_TYPE": "FileSystemCache",
    "CACHE_DEFAULT_TIMEOUT": int(os.getenv("CACHE_TIMEOUT", 1)) * HOUR,
    "CACHE_DIR": "resources/.cache",
    "CACHE_THRESHOLD": int(os.getenv("CACHE_THRESHOLD", 1000)),
}

cache = Cache()
