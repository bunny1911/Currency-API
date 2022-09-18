from os import environ
from typing import Callable
from flask import request
from flask_caching import Cache


def make_key(prefix: str) -> Callable[[str], str]:
    def _make_key() -> str:
        return prefix + request.full_path.split("/")[1].lower()

    return _make_key


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
