from typing import override
from b9ui.attrs import HyperlinkAttrs
from b9ui.components import Component
from b9ui.components.link import Link
from b9ui.html import span
from b9ui.types import AnyChildren


class NavigationLink(Component[AnyChildren, HyperlinkAttrs]):
    classes = ["flex", "h-9", "w-9", "items-center", "justify-center", "rounded-lg",                
               "transition-colors", "hover:text-foreground", "md:h-8", "md:w-8"]
    variants = {
        "variant": {
            "default": "text-muted-foreground",
            "active": "bg-accent text-accent-foreground",
        }
    }

    @override
    def render(self) -> Link:
        variant = self.variants.get("variant", {}).get(self.attrs.get("variant", "default"))
        if extra_class := self.attrs.get("class_", ""):
            self.attrs["class_"] = f"{variant} {extra_class}"
        else:
            self.attrs["class_"] = f"{variant}"

        return Link(                    
                    span(self.children[0], class_="sr-only"),
                    *self.children[1:],
                    **self.attrs
                )
    
