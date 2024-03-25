import psycopg2

from src.settings import settings

db_conn = psycopg2.connect(
    **settings.DB_CONN,
)
