import json
import logging
from typing import Any

from .celery import listen
from .databases import db_conn
from .use_cases import registered_users_per_month_use_case

logger = logging.getLogger(__name__)


async def json_response(proto: Any, status_code: int, data: dict) -> None:
    response_body = json.dumps(data)
    proto.response_str(
        status=status_code,
        headers=[("content-type", "application/json")],
        body=response_body,
    )


async def home_handler(score: Any, proto: Any) -> None:
    await json_response(
        proto,
        200,
        await registered_users_per_month_use_case(db_conn),
    )


routes = {
    "/": home_handler,
}


class Application:
    def __init__(self, routes: dict):
        self.routes = routes
        self.start_notification_listener()

    async def __call__(self, scope: Any, proto: Any):
        assert scope.proto == "http"
        path = scope.path
        handler = routes.get(path, "/")
        await handler(scope, proto)  # type: ignore

    def start_notification_listener(self) -> None:
        listen.delay()


app = Application(routes)
