from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import asdict, dataclass
from typing import Any, override
from ludic.attrs import NoAttrs, GlobalAttrs, Annotated
from ludic.catalog.typography import Paragraph
from ludic.html import (
    a,
    div,
    img,
    ul,
    span,
)
from ludic.types import (
    AnyChildren,
    Component
)

from lucide import IconCommand, IconDatabase, IconHome, IconUser
from ..html import button


class NavigationIconButtonAttrs(GlobalAttrs, total=False):
    href: str
    data_state: Annotated[str, "data-state"]

class NavigationIconButton(Component[AnyChildren, NavigationIconButtonAttrs]):
    @override
    def render(self) -> button:
        return button(
          a(
            span(self.children[0],
              class_=" ".join([
                  'transition-colors duration-200',
                  'flex items-center justify-center h-10 w-10 rounded', # Layout
                  'bg-background hover:bg-overlay-hover', # Light mode
                  'text-foreground-lighter hover:text-foreground ', # Dark mode
                ])
            ),
            href=self.attrs.get('href', '#'),
          ),
          data_state=self.attrs.get('data_state', 'closed'),
        )


class NavigationBar(Component[AnyChildren, NoAttrs]):
    @override
    def render(self) -> div:
        return div(
          ul(
            a(
              img(src="/static/img/supabase-logo.svg", alt="Supabase", class_="mx-auto h-[40px] w-6 cursor-pointer rounded"),
              class_="block", href="/",
            ),
            NavigationIconButton(IconHome(), href="/"),
            NavigationIconButton(IconCommand(), href="/dids"),
            NavigationIconButton(IconDatabase(), href="/tables"),
            div(class_="bg-border h-px w-full"),
            class_="flex flex-col space-y-2"
          ),
          ul(
            NavigationIconButton(IconUser()),
            class_="flex flex-col space-y-4 items-center"
          ),
          class_="hide-scrollbar flex w-14 flex-col justify-between p-2 overflow-y-auto border-r bg-background border-default"
        )
    