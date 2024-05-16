from typing import override
from ludic.html import input
from ludic.types import Component, AnyChildren

from ..attrs import InputAttrs


class Input(Component[AnyChildren, InputAttrs]):
    class_name = "flex h-9 border border-input px-3 py-1 text-sm shadow-sm transition-colors file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50"
    input_variants = {
        "text": " ".join([
            ]),
        "search": " ".join([
            ]),
    }

    @override
    def render(self) -> input:
        class_name =  f"{self.class_name} {self.input_variants.get(self.attrs.get('type', 'text'))}"
        if extra_class := self.attrs.get("class_", ""):
            self.attrs["class_"] = f"{extra_class} {class_name}"
        else:
            self.attrs["class_"] = class_name

        return input(*self.children, **self.attrs)


