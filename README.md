
b9ui is a lightweight framework for building HTML pages with a component approach similar to [Next.js](https://nextjs.org/). It is designed so that developers need to write almost no JavaScript to create dynamic web services. 


> [!]

> The framework is in a very early development/testing phase. There are currently a lot of half-functioning features. We welcome your contributions to help progress!


## Requirements

python = "^3.12"
ludic = "^0.4.0"

## Installation


```

pip install “b9ui”

```


Similar to Starlette, you will also want to set up an [ASGI](https://asgi.readthedocs.io/en/latest/) server:


```

pip install uvicorn

```


## Full Example

**app/layout.py**:


```python

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


```

**app/page.py**:


```python

from b9ui.components import Blank
from b9ui.html import div, p


async def index() -> Blank:
    return Blank(
        div(
            p("Hello, World!"),
        ),        
    )


```

To run the application:


```python

uvicorn b9ui.app:app --reload

```


#### More Examples


For more complex usage that includes the full capabilities of the framework, please visit the folder with examples [on GitHub] (https://github.com/b9ui/b9ui/tree/master/examples/).


## Contributing


Any contribution to the framework is welcome! Your help will make it a better resource for the community. If you are ready to contribute, read [contribution guidelines] (https://github.com/b9ui/b9ui/tree/master/CONTRIBUTING.md).