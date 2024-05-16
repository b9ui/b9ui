from b9ui.components import Blank
from b9ui.html import div, p


async def index() -> Blank:
    return Blank(
        div(
            p("Hello, World!"),
        ),        
    )

