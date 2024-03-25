import functools
import logging
from ast import literal_eval
from collections.abc import Callable
from typing import Any

from src.databases import redis_conn

logger = logging.getLogger(__name__)


def cache_result(func: Callable) -> Any:
    @functools.wraps(func)
    async def wrapper(*args: Any, **kwargs: Any):
        cache_key = f"{func.__name__}"

        cached_result = redis_conn.get(cache_key)
        if cached_result:
            result = literal_eval(cached_result.decode())  # type: ignore
            return result
        result = await func(*args, **kwargs)
        redis_conn.set(cache_key, str(result), ex=60 * 60 * 24)

        return result

    return wrapper
