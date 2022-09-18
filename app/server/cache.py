from os import environ
from flask_caching import Cache


CACHE_HOST: str = environ.get("CACHE_HOST")

if CACHE_HOST is None:
    # Use default
    CACHE_HOST = "localhost:11211"

# Create cache object
cache = Cache(
    config={
        "CACHE_TYPE": "MemcachedCache",
        "CACHE_DEFAULT_TIMEOUT": 300,
        "CACHE_MEMCACHED_SERVERS": [CACHE_HOST]
    }
)
