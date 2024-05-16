from ludic.types import ComponentStrict, PrimitiveChildren
from b9ui.attrs import ButtonAttrs
from ..html import button


class Button(ComponentStrict[PrimitiveChildren, ButtonAttrs]):
    classes = ["inline-flex", "items-center", "justify-center", "whitespace-nowrap", "rounded-md", "text-sm", "font-medium", 
               "transition-colors", "focus-visible:outline-none", "focus-visible:ring-1", 
               "focus-visible:ring-ring", "disabled:pointer-events-none", "disabled:opacity-50"]
    variants = {
        "variant": {
            "default": "bg-primary text-primary-foreground shadow hover:bg-primary/90",
            "destructive": "bg-destructive text-destructive-foreground shadow-sm hover:bg-destructive/90",
            "outline": "border border-input bg-background shadow-sm hover:bg-accent hover:text-accent-foreground",
            "secondary": "bg-secondary text-secondary-foreground shadow-sm hover:bg-secondary/80",
            "ghost": "hover:bg-accent hover:text-accent-foreground",
            "link": "text-primary underline-offset-4 hover:underline",
        },
        "size": {
            "default": "h-9 px-4 py-2",
            "sm": "h-8 rounded-md px-3 text-xs",
            "lg": "h-10 rounded-md px-8",
            "icon": "h-9 w-9",
        }
    }


    def render(self) -> button:
        button_variant = self.variants.get("variant", {}).get(self.attrs.get("variant", "default"))
        button_size = self.variants.get("size", {}).get(self.attrs.get("size", "default"))

        if extra_class := self.attrs.get("class_", ""):
            self.attrs["class_"] = f"{button_variant} {button_size} {extra_class}"
        else:
            self.attrs["class_"] = f"{button_variant} {button_size}"
        return button(*self.children, **self.attrs)
