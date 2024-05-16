import inspect
from typing import Any
from collections.abc import Callable
from starlette.routing import get_name
from starlette.routing import Route as StarletteRoute
from starlette.routing import Router as StarletteRouter
from starlette.types import Receive, Scope, Send
from ludic.web.datastructures import URLPath
from ludic.web.endpoints import Endpoint
from ludic.web.requests import Request
from ludic.web.routing import _EndpointHandler as BaseEndpointHandler
from ludic.web.routing import _FunctionHandler as BaseFunctionHandler

from .responses import prepare_response




class FunctionHandler(BaseFunctionHandler): 

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        request = Request(scope, receive)
        response = await prepare_response(self.handler, request)
        await response(scope, receive, send)


class EndpointHandler(BaseEndpointHandler):

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        request = Request(scope, receive)
        handler_name = (
            "get"
            if request.method == "HEAD" and not hasattr(self, "head")
            else request.method.lower()
        )
        handler: Callable[..., Any] = getattr(
            self.handler, handler_name, self.method_not_allowed(scope)
        )
        response = await prepare_response(handler, request)
        await response(scope, receive, send)


class Route(StarletteRoute):
    def __init__(
        self,
        path: str,
        endpoint: Callable[..., Any],
        *,
        name: str | None = None,
        **kwargs: Any,
    ) -> None:
        name = get_name(endpoint) if name is None else name
        wrapped_route = endpoint
        if inspect.isfunction(endpoint) or inspect.ismethod(endpoint):
            wrapped_route = FunctionHandler(endpoint)
        elif inspect.isclass(endpoint) and issubclass(endpoint, Endpoint):
            wrapped_route = EndpointHandler(endpoint)
        if getattr(endpoint, "route", None) is None:
            endpoint.route = self  # type: ignore
        super().__init__(path, wrapped_route, name=name, **kwargs)

    def url_path_for(self, name: str, /, **path_params: Any) -> URLPath:
        result = super().url_path_for(name, **path_params)
        return URLPath(result, result.protocol, result.host)


class Router(StarletteRouter):
    def add_route(
        self,
        path: str,
        endpoint: Callable[..., Any],
        methods: list[str] | None = None,
        name: str | None = None,
        include_in_schema: bool = True,
    ) -> None:
        route = Route(
            path,
            endpoint=endpoint,
            methods=methods,
            name=name,
            include_in_schema=include_in_schema,
        )
        self.routes.append(route)

    def url_path_for(self, name: str, /, **path_params: Any) -> URLPath:
        return super().url_path_for(name, **path_params)  # type: ignore
