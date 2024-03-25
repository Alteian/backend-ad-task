#!/bin/bash

set -ex
celery -A src.celery worker --loglevel=info --concurrency=1
