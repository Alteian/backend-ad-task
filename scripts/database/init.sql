\c app_db

CREATE TABLE IF NOT EXISTS users (
    name TEXT NOT NULL,
    registered_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
