from ludic.attrs import Annotated, Alias
from ludic.html import Element
from ludic.types import AnyChildren

from ..attrs import GlobalAttrs


class SvgAttrs(GlobalAttrs, total=False):
    version: str
    xmlns: str
    height: int
    width: int
    viewBox: str
    clip_path: Annotated[str, Alias("clip-path")]
    clip_rule: Annotated[str, Alias("clip-rule")]
    fill: str
    fill_rule: Annotated[str, Alias("fill-rule")]
    stroke: str
    stroke_dasharray: Annotated[str, Alias("stroke-dasharray")]
    stroke_dashoffset: Annotated[str, Alias("stroke-dashoffset")]
    stroke_linecap: Annotated[str, Alias("stroke-linecap")]
    stroke_linejoin: Annotated[str, Alias("stroke-linejoin")]
    stroke_miterlimit: Annotated[str, Alias("stroke-miterlimit")]
    stroke_opacity: Annotated[str, Alias("stroke-opacity")]
    stroke_width: Annotated[str, Alias("stroke-width")]
    transform: str


class CircleAttrs(SvgAttrs, total=False):
    cx: str
    cy: str
    r: str


class PathAttrs(SvgAttrs, total=False):
    d: str


class PolylineAttrs(SvgAttrs, total=False):
    points: str


class svg(Element[AnyChildren, SvgAttrs]):
    html_name = "svg"


class circle(Element[AnyChildren, CircleAttrs]):
    html_name = "circle"


class path(Element[AnyChildren, PathAttrs]):
    html_name = "path"


class polyline(Element[AnyChildren, PolylineAttrs]):
    html_name = "polyline"


class g(Element[AnyChildren, SvgAttrs]):
    html_name = "g"