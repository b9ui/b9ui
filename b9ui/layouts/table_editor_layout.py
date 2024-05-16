from typing import override

from ludic.attrs import NoAttrs
from ludic.html import div, main
from ludic.types import AnyChildren, Component


class TableEditorLayout(Component[AnyChildren, NoAttrs]):
    @override
    def render(self) -> div:
        return div(
          main(*self.children,
            class_="flex flex-col flex-1 w-full overflow-x-hidden"
          ),
          class_="flex h-full"
        )
        
    