from typing import override
from b9ui.attrs import NoAttrs 
from b9ui.components import Component
from b9ui.html import html, head, body, div, link, script, title
from b9ui.types import AnyChildren


class Layout(Component[AnyChildren, NoAttrs]):
    @override
    def render(self) -> html:
        return html(
            head(
                title("Hello, World! App"),
                link(href="/static/css/default.css", rel="stylesheet"),
            ),
            body(
                div(
                    div(
                        div(
                            div(
                                div(*self.children,
                                    class_="pb-24 flex flex-col justify-between w-full"
                                ),                                
                                class_="w-full flex justify-center"
                            ),
                            class_="py-16 overflow-auto flex flex-row"
                        ),                                                
                        class_="app text-stone-700 dark:text-gray-100 bg-white dark:bg-stone-900 min-h-screen"
                    ),
                    class_="display: contents"
                ),                
                script(src="https://unpkg.com/htmx.org@1.9.10"),
                script(src="https://unpkg.com/hyperscript.org@0.9.12"),                
                script(src="https://cdn.tailwindcss.com"),
                class_="min-h-screen bg-background font-sans antialiased __className_aaf875",
            ),
            class_="light",
            lang="en", style="color-scheme: light;"
        )
