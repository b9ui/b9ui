import inspect
from collections.abc import Callable
from typing import Any, ParamSpec, TypeVar, get_origin

from starlette._utils import is_async_callable
from starlette.concurrency import run_in_threadpool
from starlette.datastructures import FormData, Headers, QueryParams
from starlette.requests import Request
from starlette.responses import (
    FileResponse,
    HTMLResponse,
    JSONResponse,
    PlainTextResponse,
    RedirectResponse,
    Response,
    StreamingResponse,
)
from starlette.websockets import WebSocket

from ludic.types import BaseElement
from ludic.web import datastructures as ds
from ludic.web.parsers import BaseParser
from ludic.web.responses import LudicResponse, extract_from_request, run_in_threadpool_safe

def custom_prepare_response(handler, request, raw_response):
    discovered_modules = request.app.discovered_modules
    handler_module = f"{handler.__module__}"
    module_parts = handler_module.split(".")
    module_parts_len = len(module_parts)

    if handler_module.endswith("page"):
        for i in range(module_parts_len):
            current_module_name = ".".join(module_parts[:module_parts_len - i])

            if current_module_name.endswith(".page"):
                layout_module_name = current_module_name.replace(".page", ".layout")
            else:
                layout_module_name = f"{current_module_name}.layout"
                
            if layout_module_name in discovered_modules.keys():
                layout_module = discovered_modules.get(layout_module_name, None)

                if layout_module:
                    layout_cls = getattr(layout_module, "Layout")

                    raw_response = layout_cls(raw_response)

    return raw_response


async def prepare_response(
    handler: Callable[..., Any],
    request: Request,
    status_code: int | None = None,
    headers: Headers | None = None,
) -> Response:
    """Prepares response for the given handler and request.

    Args:
        handler: The handler to prepare the response for.
        request: The request to prepare the response for.
        status_code: The status code to use for the response.
        headers: The headers to use for the response.

    Returns:
        The prepared response.
    """
    handler_kw = await extract_from_request(handler, request)
    is_async = is_async_callable(handler)

    if is_async:
        with BaseElement.formatter:
            raw_response = await handler(**handler_kw)
    else:
        raw_response = await run_in_threadpool_safe(handler, **handler_kw)

    raw_response = custom_prepare_response(handler, request, raw_response)

    if isinstance(raw_response, tuple):
        if len(raw_response) == 2:
            raw_response, status_or_headers = raw_response
            if isinstance(status_or_headers, dict):
                headers = ds.Headers(status_or_headers)
            else:
                status_code = status_or_headers
        elif len(raw_response) == 3:
            raw_response, status_code, headers = raw_response
            headers = ds.Headers(headers)
        else:
            raise ValueError(f"Invalid response tuple: {raw_response}")

    if raw_response is None:
        raw_response = ""

    response: Response
    if isinstance(raw_response, BaseElement):
        response = LudicResponse(
            raw_response, status_code=status_code or 200, headers=headers
        )
    elif isinstance(raw_response, str | bool | int | float):
        response = PlainTextResponse(
            str(raw_response), status_code=status_code or 200, headers=headers
        )
    elif isinstance(raw_response, Response):
        response = raw_response
    else:
        raise ValueError(f"Invalid response type: {type(raw_response)}")

    return response