from typing import Any, override

from ludic.attrs import NoAttrs
from ludic.html import (
    header,
    h1,
    p,
)
from ludic.types import (
    ComponentStrict,
    PrimitiveChildren,
)


class Header(ComponentStrict[PrimitiveChildren, NoAttrs]):
    @override
    def render(self) -> header:
        return header(
            h1(f"Example - {self.children[0]}"),
            p("This is an example app 123."),
        )
