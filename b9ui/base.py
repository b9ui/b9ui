from typing import Generic, cast
from ludic.base import TAttrs, TChildren, BaseElement


class Element(Generic[TChildren, TAttrs], BaseElement):
    """Base class for Ludic elements.

    Args:
        *children (TChild): The children of the element.
        **attrs (Unpack[TAttrs]): The attributes of the element.
    """

    children: tuple[TChildren, ...]
    attrs: TAttrs

    def __init__(
        self,
        *children: TChildren,
        # FIXME: https://github.com/python/typing/issues/1399
        **attributes: Unpack[TAttrs],  # type: ignore
    ) -> None:
        self.attrs = cast(TAttrs, attributes)
        self.children = tuple(self.formatter.extract(*children))