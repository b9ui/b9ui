from typing import override
from ludic.attrs import GlobalAttrs
from ludic.html import div, main
from ludic.types import AnyChildren, Component

from ..components import NavigationBar, ProductMenuBar


class ProjectLayoutAttrs(GlobalAttrs, total=False):
    menu: dict


class ProjectLayout(Component[AnyChildren, ProjectLayoutAttrs]):
    @override
    def render(self) -> div:
        return div(
          NavigationBar(),
          ProductMenuBar(menu=self.attrs.get("menu", {})),
          main(*self.children,
            class_="flex flex-col flex-1 w-full overflow-x-hidden"
          ),
          class_="flex h-full"
        )
        
    