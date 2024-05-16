from typing import override
from ludic.html import span



class Toast(span):
    id: str = "toast"
    target: str = f"#{id}"
    styles = {
        target: {
            "background": "#E1F0DA",
            "margin": "10px 20px",
            "opacity": "0",
            "transition": "opacity 3s ease-out",
        },
        f"{target}.htmx-settling": {
            "opacity": "100",
        },
    }

    @override
    def render(self) -> span:
        return span(*self.children, id=self.id)