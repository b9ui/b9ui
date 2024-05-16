from typing import override
from ludic.attrs import NoAttrs
from ludic.html import ol
from ludic.types import AnyChildren, Component
from b9ui.components.link import Link
from b9ui.html import span, svg, li, nav
from ludic.components import Blank


class Breadcrumb(Component[AnyChildren, NoAttrs]):
    @override
    def render(self) -> nav:
        return nav(
            *self.children,
            aria_label="breadcrumb"
        )

class BreadcrumbList(Component[AnyChildren, NoAttrs]):
    @override
    def render(self) -> ol:
        return ol(
            *self.children,
            class_="flex flex-wrap items-center gap-1.5 break-words text-sm text-muted-foreground sm:gap-2.5"
        )    
    
class BreadcrumbItem(Component[AnyChildren, NoAttrs]):
    @override
    def render(self) -> li:
        return li(
            *self.children,
            class_="inline-flex items-center gap-1.5"
        )       


class BreadcrumbLink(Component[AnyChildren, NoAttrs]):
    @override
    def render(self) -> Blank:
        return Blank(
            li(
                Link(*self.children, **self.attrs,
                    class_="transition-colors hover:text-foreground"
                ),
                class_="inline-flex items-center gap-1.5"
            ),
            li(
                svg.svg(
                    svg.path(
                        d="M6.1584 3.13508C6.35985 2.94621 6.67627 2.95642 6.86514 3.15788L10.6151 7.15788C10.7954 7.3502 10.7954 7.64949 10.6151 7.84182L6.86514 11.8418C6.67627 12.0433 6.35985 12.0535 6.1584 11.8646C5.95694 11.6757 5.94673 11.3593 6.1356 11.1579L9.565 7.49985L6.1356 3.84182C5.94673 3.64036 5.95694 3.32394 6.1584 3.13508Z",
                        fill="currentColor", fill_rule="evenodd", clip_rule="evenodd"
                    ),
                    width="15", height="15", viewBox="0 0 15 15", fill="none"
                ),
                role="presentation", 
                aria_hidden="true", 
                class_="[&amp;>svg]:size-3.5"
            )
        )



class BreadcrumbPage(Component[AnyChildren, NoAttrs]):
    @override
    def render(self) -> span:
        return span(
            *self.children,
            aria_current="paage",
            aria_disabled="true",
            role="link",
            class_="font-normal text-foreground"
        ) 
        
    