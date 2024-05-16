from typing import override
from b9ui.attrs import HyperlinkAttrs
from b9ui.components import Component
from b9ui.components.breadcrumb import Breadcrumb, BreadcrumbList, BreadcrumbItem, BreadcrumbLink, BreadcrumbPage

from b9ui.html import header, div
from b9ui.types import AnyChildren


class Header(Component[AnyChildren, HyperlinkAttrs]):
    @override
    def render(self) -> header:
        from components import Search
        
        return header(
            Breadcrumb(
                BreadcrumbList(                    
                    BreadcrumbLink("Dashboard", href="#"),  
                    BreadcrumbLink("Orders", href="#"),                     
                    BreadcrumbItem(
                        BreadcrumbPage("Recent Orders"),
                    ),                    
                ),
                class_="hidden md:flex"
            ),
            div(
                Search(),
                class_="relative ml-auto flex-1 md:grow-0"
            ),
            class_="sticky top-0 z-30 flex h-14 items-center gap-4 border-b bg-background px-4 sm:static sm:h-auto sm:border-0 sm:bg-transparent sm:px-6"
        )
    
