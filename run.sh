#!/bin/bash

DOCKER_COMPOSE="docker-compose -f dockerfiles/docker-compose.local.yml"

build_fn() {
    echo "Building local server..."
    cp src/settings/envs/.local.sample src/settings/envs/.local
    $DOCKER_COMPOSE build
}

populate_fn() {
    echo "Populating database..."
    $DOCKER_COMPOSE up -d
    $DOCKER_COMPOSE exec db sh -c "psql -U postgres -tc \"SELECT 1 FROM pg_database WHERE datname = 'app_db'\" | grep -q 1 || psql -U postgres -c 'CREATE DATABASE app_db'"
    $DOCKER_COMPOSE exec db sh -c "psql -U postgres -f /scripts/init.sql"
    $DOCKER_COMPOSE exec db sh -c "psql -U postgres -f /scripts/create_notifier_fn.sql"
    $DOCKER_COMPOSE exec db sh -c "psql -U postgres -f /scripts/create_trigger.sql"
    $DOCKER_COMPOSE exec db sh -c "psql -U postgres -f /scripts/insert_dummy_users.sql"
    $DOCKER_COMPOSE down
}

populate_users_fn() {
    echo "Populating users..."
    $DOCKER_COMPOSE exec db sh -c "psql -U postgres -f /scripts/insert_dummy_users.sql"
}

start_fn() {
    echo "Starting local server..."
    $DOCKER_COMPOSE up -d
}

build_populate_and_run_detach_fn() {
    echo "Building, populating and running local server in detach mode..."
    build_fn
    populate_fn
    start_fn
}

case "$1" in
    "build")
        build_fn
        ;;
    "populate")
        populate_fn
        ;;
    "start")
        start_fn
        ;;
    "populate_users")
        populate_users_fn
        ;;
    "build_populate_and_run_detach")
        build_populate_and_run_detach_fn
        ;;
    *)
        echo "Usage: $0 {build|populate|start|populate_users|build_populate_and_run_detach}"
        exit 1
        ;;
esac
