from typing import override
from b9ui.attrs import NoAttrs
from b9ui.components import Component, Blank
from b9ui.types import AnyChildren
from b9ui.components.input import Input
from lucide import IconSearch


class Search(Component[AnyChildren, NoAttrs]):
    @override
    def render(self) -> Blank:
        return Blank( 
            IconSearch(class_="absolute left-2.5 top-2.5 h-4 w-4 text-muted-foreground"),
            Input(
                type="search",
                placeholder="Search...",
                class_="w-full rounded-lg bg-background pl-8 md:w-[200px] lg:w-[320px]"
            )               
        )
    
