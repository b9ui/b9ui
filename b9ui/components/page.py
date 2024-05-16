from typing import override
from ludic.html import head, title, style, body, script, div, link
from ludic.types import AnyChildren, Component, NoAttrs

from ..html import html


class Page(Component[AnyChildren, NoAttrs]):
    styles = {
    }

    @override
    def render(self) -> html:
        return html(
            head(
                title("Ludic Example"),
                style.load(cache=False),
                link(href="/static/css/default.css", rel="stylesheet"),
            ),
            body(
                div(*self.children, id="__next"),
                script(src="https://unpkg.com/htmx.org@1.9.10"),
                script(src="https://cdn.tailwindcss.com"),
            ),
            lang="en", style="color-scheme: light;", data_theme="light"
        )
