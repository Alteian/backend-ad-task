ARG BASE_IMAGE=python:3.12-slim

FROM $BASE_IMAGE AS base

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . .

EXPOSE 8000

FROM base AS local-stage

RUN chmod +x /app/scripts/start/local.sh

ENTRYPOINT ["/app/scripts/start/local.sh"]

FROM base AS celery-stage

RUN chmod +x /app/scripts/start/celery.sh

ENTRYPOINT ["/app/scripts/start/celery.sh"]
