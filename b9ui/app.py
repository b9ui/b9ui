import os
import sys
from collections.abc import Callable, Mapping, Sequence
from typing import Any
from starlette.applications import AppType
from starlette.middleware import Middleware
from starlette.routing import BaseRoute, Mount
from starlette.staticfiles import StaticFiles
from starlette.types import Lifespan
from ludic.web.app import LudicApp, TCallable
from b9ui.html import div

from .routing import Router
from .utils.module_loading import autodiscover_modules


APP_PATH = os.environ.get("APP_PATH")
sys.path.append(APP_PATH)


class B9App(LudicApp):

    def __init__(
        self,
        debug: bool = False,
        routes: Sequence[BaseRoute] | None = None,
        middleware: Sequence[Middleware] | None = None,
        exception_handlers: Mapping[Any, TCallable] | None = None,
        on_startup: Sequence[Callable[[], Any]] | None = None,
        on_shutdown: Sequence[Callable[[], Any]] | None = None,
        lifespan: Lifespan[AppType] | None = None,
    ) -> None:
        super().__init__(debug, middleware=middleware)

        default_routes = [
            Mount('/static', StaticFiles(directory=f"{APP_PATH}/static")),
        ]

        routes = default_routes + (routes or [])

        self.router = Router(
            routes, on_startup=on_startup, on_shutdown=on_shutdown, lifespan=lifespan
        )

        self.discovered_modules = autodiscover_modules(self, f"{APP_PATH}/app")


app = B9App(debug=True)


@app.exception_handler(404)
async def not_found() -> div:
    return div(
        div("Page Not Found"),
    )


@app.exception_handler(500)
async def server_error() -> div:
    return div(
        div("Server Error"),
    )
