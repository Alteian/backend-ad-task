FROM python:3.12-slim

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . .

EXPOSE 8000

RUN chmod +x /app/scripts/start/local.sh

ENTRYPOINT ["/app/scripts/start/local.sh"]
