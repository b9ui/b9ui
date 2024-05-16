from typing import override
from ludic.attrs import HyperlinkAttrs
from ludic.html import a
from ludic.types import AnyChildren, Component


class Link(Component[AnyChildren, HyperlinkAttrs]):
    @override
    def render(self) -> a:
        return a(
            *self.children,
            **self.attrs
        )
    