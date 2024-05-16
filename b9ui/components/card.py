from typing import override
from b9ui.attrs import NoAttrs
from b9ui.components import Component
from b9ui.html import div, h3, p
from b9ui.types import AnyChildren


class Card(Component[AnyChildren, NoAttrs]):
    classes = ["rounded-xl", "border", "bg-card", "text-card-foreground", "shadow"]
  
    @override
    def render(self) -> div:
        return div(*self.children, **self.attrs)
    

class CardHeader(Component[AnyChildren, NoAttrs]):
    classes = ["flex", "flex-col", "space-y-1.5", "p-6"]

    @override
    def render(self) -> div:
        return div(*self.children, **self.attrs)
    

class CardTitle(Component[AnyChildren, NoAttrs]):
    classes = ["font-semibold", "leading-none", "tracking-tight"]

    @override
    def render(self) -> h3:
        return h3(*self.children, **self.attrs)
    

class CardDescription(Component[AnyChildren, NoAttrs]):
    classes = ["text-sm text-muted-foreground"]

    @override
    def render(self) -> p:
        return p(*self.children, **self.attrs)


class CardContent(Component[AnyChildren, NoAttrs]):
    classes = ["p-6", "pt-0"]

    @override
    def render(self) -> div:
        return div(*self.children, **self.attrs)    
    

class CardFooter(Component[AnyChildren, NoAttrs]):
    classes = ["flex", "items-center", "p-6"]

    @override
    def render(self) -> div:
        return div(*self.children, **self.attrs)    