from abc import ABCMeta, abstractmethod
from ludic.base import BaseElement, Element
from ludic.types import NoAttrs, TAttrs, TChildren

from ludic.components import Component, Blank
from .body import Body
from .header import Header 
from .page import Page
from .navigation_bar import NavigationBar
from .product_menu import ProductMenu
from .product_menu_bar import ProductMenuBar
from .side_panel import SidePanel


class Component(Element[TChildren, TAttrs], metaclass=ABCMeta):
    """Base class for components.

    A component subclasses an :class:`Element` and represents any element
    that can be rendered in Ludic.

    Example usage:

        class PersonAttrs(Attributes):
            age: NotRequired[int]

        class Person(Component[PersonAttrs]):
            @override
            def render(self) -> dl:
                return dl(
                    dt("Name"),
                    dd(self.attrs["name"]),
                    dt("Age"),
                    dd(self.attrs.get("age", "N/A")),
                )

    Now the component can be used in any other component or element:

        >>> div(Person(name="John Doe", age=30), id="person-detail")

    """

    @abstractmethod
    def render(self) -> BaseElement:
        """Render the component as an instance of :class:`BaseElement`."""