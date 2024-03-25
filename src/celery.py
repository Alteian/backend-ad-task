from celery import Celery

from .listeners import listen_for_changes
from .settings import settings
from .utils import invalidate_cache

redis_host = settings.REDIS_CONN["host"]
redis_port = settings.REDIS_CONN["port"]
redis_db = settings.REDIS_CONN["db"]

celery_app = Celery(
    "tasks",
    broker=f"redis://{redis_host}:{redis_port}/{redis_db}",
    backend=f"redis://{redis_host}:{redis_port}/{redis_db}",
)


@celery_app.task
def listen() -> None:
    listen_for_changes(invalidate_cache)
