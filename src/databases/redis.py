import redis

from src.settings import settings

redis_conn = redis.Redis(**settings.REDIS_CONN)
