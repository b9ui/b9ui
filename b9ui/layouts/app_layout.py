from typing import override
from ludic.attrs import NoAttrs
from ludic.html import head, title, style, body, script, div, link
from ludic.types import AnyChildren, Component, NoAttrs
from b9ui.components import SidePanel

from ..html import html


class AppLayout(Component[AnyChildren, NoAttrs]):
    @override
    def render(self) -> html:
        return html(
            head(
                title("My App"),
                style.load(cache=False),
                link(href="/static/css/fonts.css", rel="stylesheet"),
                link(href="/static/css/default.css", rel="stylesheet"),
            ),
            body(
                div(
                    div(
                        div(
                            div(*self.children, 
                                style={"max-height": "calc(0px + 100vh)", "height": "calc(0px + 100vh)"}
                            ),
                        ),
                        class_="min-h-full flex flex-col"
                    ),
                    id="__next"
                ),
                div(                    
                    id="side-panel-area"
                ),
                
                script(src="https://unpkg.com/htmx.org@1.9.10"),
                script(src="https://unpkg.com/hyperscript.org@0.9.12"),                
                script(src="https://cdn.tailwindcss.com"),
            ),
            data_theme="light",
            lang="en", style="color-scheme: light;"
        )
