from typing import cast, override
from ludic.attrs import GlobalAttrs
from ludic.html import table, tbody, thead, tr, th, td
from ludic.types import PrimitiveChildren, BaseElement, ComponentStrict
from ludic.catalog.tables import TableRow as _TableRow
from ludic.catalog.tables import TableHead as _TableHead
from typing_extensions import TypeVar


class TableRow(_TableRow):
    classes = []
    styles = {}

    @override
    def render(self) -> tr:
        return tr(
            *(child if isinstance(child, td) else td(child) for child in self.children),
            **self.attrs,
        )

class TableHead(_TableHead):
    classes = []
    styles = {}

    @override
    def render(self) -> tr:
        return tr(
            *(child if isinstance(child, th) else th(child, class_="p-3 px-4 text-left") for child in self.children),
            **self.attrs,
        )    


THead = TypeVar("THead", bound=BaseElement, default=TableHead)
TRow = TypeVar("TRow", bound=BaseElement, default=TableRow)


class TableAttrs(GlobalAttrs):
    head_attrs: GlobalAttrs
    body_attrs: GlobalAttrs


class Table(ComponentStrict[THead, *tuple[TRow, ...], TableAttrs]):
    classes = ["table"]
    styles = {}

    @property
    def header(self) -> tuple[PrimitiveChildren, ...]:
        if isinstance(self.children[0], TableHead):
            return self.children[0].header
        return ()

    def getlist(self, key: str) -> list[PrimitiveChildren | None]:
        result: list[PrimitiveChildren | None] = []

        for idx, head in enumerate(self.header):
            if key != head:
                continue

            rows: list[TableRow] = cast(list[TableRow], self.children[1:])
            for row in rows:
                if value := row.get_value(idx):
                    result.append(value)

        return result

    @override
    def render(self) -> table:
        return table(
            thead(self.children[0], **self.attrs.get("head_attrs", {})),
            tbody(*self.children[1:], **self.attrs.get("body_attrs", {})),
            **self.attrs_for(table),
        )



