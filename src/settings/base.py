import os

from decouple import AutoConfig

config = AutoConfig(os.environ.get("ENV_FILE_PATH"))

DB_CONN = {
    "dbname": config("POSTGRES_DATABASE"),
    "user": config("POSTGRES_USER"),
    "password": config("POSTGRES_PASSWORD"),
    "host": config("POSTGRES_HOST"),
    "port": config("POSTGRES_PORT"),
}

REDIS_CONN = {
    "host": config("REDIS_HOST"),
    "port": config("REDIS_PORT"),
    "db": config("REDIS_DB"),
}
