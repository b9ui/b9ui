from typing import Any, override

from ludic.attrs import NoAttrs
from ludic.catalog.typography import Paragraph
from ludic.html import (
    div,
    main,
)
from ludic.types import (
    AnyChildren,
    Component,
)



class Body(Component[AnyChildren, NoAttrs]):
    @override
    def render(self) -> div:
        return div(
                div(
                    div(                        
                      main(
                          main(
                              div(*self.children,
                                  class_="w-full mx-auto my-16 space-y-16 max-w-7xl"
                              ),
                              class_="flex-1 overflow-y-auto",
                              style="max-height: 100vh;",
                          ),
                          class_="flex flex-col flex-1 w-full overflow-x-hidden"
                      ),
                      class_="flex h-full"
                    )
                ),
                class_="min-h-full flex flex-col",
        )
    