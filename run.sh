#!/bin/bash

DOCKER_COMPOSE="docker-compose -f dockerfiles/docker-compose.local.yml"

case "$1" in
    "build")
        echo "Building local server..."
        cp src/settings/envs/.local.sample src/settings/envs/.local
        $DOCKER_COMPOSE build
        ;;
    "populate")
        echo "Populating database..."
        $DOCKER_COMPOSE up -d
        $DOCKER_COMPOSE exec db sh -c "psql -U postgres -tc \"SELECT 1 FROM pg_database WHERE datname = 'app_db'\" | grep -q 1 || psql -U postgres -c 'CREATE DATABASE app_db'"
        $DOCKER_COMPOSE exec db sh -c "psql -U postgres -f /scripts/init.sql"
        $DOCKER_COMPOSE exec db sh -c "psql -U postgres -f /scripts/create_notifier_fn.sql"
        $DOCKER_COMPOSE exec db sh -c "psql -U postgres -f /scripts/create_trigger.sql"
        $DOCKER_COMPOSE exec db sh -c "psql -U postgres -f /scripts/insert_dummy_users.sql"
        $DOCKER_COMPOSE down
        ;;
    "start")
        echo "Starting local server..."
        $DOCKER_COMPOSE up
        ;;
    "populate_users")
        echo "Populating users..."
        $DOCKER_COMPOSE exec db sh -c "psql -U postgres -f /scripts/insert_dummy_users.sql"
        ;;
    *)
        echo "Invalid command"
        ;;
esac
