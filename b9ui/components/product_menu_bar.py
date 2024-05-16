from typing import override
from ludic.attrs import NoAttrs, GlobalAttrs
from ludic.html import (
    div,
    h4,
    p,
)
from ludic.types import (
    AnyChildren,
    Component
)

from .product_menu import ProductMenu

class ProductMenuBarAttrs(GlobalAttrs, total=False):
    menu: dict


class ProductMenuBar(Component[AnyChildren, ProductMenuBarAttrs]):
    @override
    def render(self) -> div:
        
        menu_dict = self.attrs.get("menu", {})

        return div(
          div(
            h4(menu_dict.get("title", ""), class_="text-lg"),
            style="minHeight: '3rem'",
            class_="dark:border-dark flex max-h-12 items-center border-b px-6",
          ),
          div(
            ProductMenu(
                menu=self.attrs.get("menu", {})
            ),
            style="maxHeight: 'calc(100vh - 96px)'",
            class_="flex-grow overflow-y-auto"
          ),
          class_=" ".join([
              'hide-scrollbar flex w-64 flex-col border-r', # Layout
              'bg-background',
              'border-default ',
            ]),
        )
    