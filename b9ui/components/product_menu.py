from typing import override
from ludic.attrs import NoAttrs, GlobalAttrs
from ludic.html import (
    div,
    ul,
    li,
    span,
    a,
)
from ludic.types import (
    AnyChildren,
    Component
)

from ..html import nav



class MenuGroup(Component[AnyChildren, NoAttrs]):
    @override
    def render(self) -> div:
        
        print(self.children[0])
        return div(
          div(
            div(
              span(
                div(
                  span(self.children[0]),
                  class_="flex flex-col space-y-2",
                ),
                class_="text-sm text-foreground-lighter w-full",
              ),
              class_="flex space-x-3 mb-2 font-normal  px-3",
            ),
            *self.children[1:] ,
            class_="mx-3"
          ),
          class_="my-6 space-y-8"
        )


class MenuItem(Component[AnyChildren, NoAttrs]):
    @override
    def render(self) -> a:
        menu_item = self.children[0]


        return a(
          li(
            span(
              div(
                div(
                  span(menu_item.get("name", ""),
                    class_="truncate",
                  ),
                  class_="flex items-center gap-2 truncate w-full",  
                ),
                class_="flex w-full items-center justify-between gap-1"
              ),
              class_="transition truncate text-sm w-full text-foreground-light group-hover:text-foreground",
            ),
            class_="cursor-pointer flex space-x-3 items-center outline-none focus-visible:ring-1 ring-foreground-muted focus-visible:z-10 group px-3 py-1 font-normal border-default group-hover:border-foreground-muted",
          ),
          href=menu_item.get("url", "#"),
          class_="block",
          target="_self"
        )
    
class Menu(Component[AnyChildren, NoAttrs]):
    @override
    def render(self) -> div:
        return div(*self.children[0])


class ProductMenuAttrs(GlobalAttrs, total=False):
    menu: dict


class ProductMenu(Component[AnyChildren, ProductMenuAttrs]):
    @override
    def render(self) -> div:
        menu_dict = self.attrs.get("menu", {})
        menu_group_title = menu_dict.get("title", "Menu Title")

        return div(
          nav(
            ul(
              MenuGroup(menu_group_title,
                Menu(
                  [MenuItem(m) for m in menu_dict.get("items", [])]
                )
              )
            ),
            role="menu", aria_label="Sidebar", aria_orientation="vertical", aria_labelledby="options-menu"
          ),
          class_="flex flex-col space-y-8 overflow-y-auto"
        )
    
