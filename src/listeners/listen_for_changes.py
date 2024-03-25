import logging
import time
from collections.abc import Callable

import psycopg2

from src.databases import db_conn

logger = logging.getLogger(__name__)


def listen_for_changes(fn: Callable) -> None:
    conn = db_conn
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    curs = conn.cursor()
    curs.execute("LISTEN users_changes")
    while True:
        time.sleep(1)  # Not ideal, but good enough for this example
        conn.poll()
        if conn.notifies:
            fn()
            conn.notifies.clear()
