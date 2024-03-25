from src.databases import redis_conn


def invalidate_cache() -> None:
    redis_conn.flushdb()
