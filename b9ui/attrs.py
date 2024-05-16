from typing import Annotated, Literal
from ludic.attrs import HtmxAttrs, HtmlAndEventAttrs, Alias, HyperlinkAttrs
from ludic.base import Attrs, NoAttrs
from ludic.styles import CSSProperties


class GlobalAttrs(HtmxAttrs, HtmlAndEventAttrs, total=False):
    _: str
    aria_current: Annotated[str, "aria-current"]
    aria_disabled: Annotated[str, "aria-disabled"]
    aria_hidden: Annotated[str, "aria-hidden"]
    aria_label: Annotated[str, "aria-label"]
    aria_labelledby: Annotated[str, "aria-labelledby"]    
    aria_orientation: Annotated[str, "aria-orientation"]
    data_orientation: Annotated[str, "data-orientation"]
    role: str
    

class HtmlTagAttrs(Attrs, total=False):
    xmlns: str
    lang: str
    class_: Annotated[str, Alias("class")]
    style: CSSProperties
    data_theme: Annotated[str, Alias("data-theme")]


class ButtonAttrs(GlobalAttrs, total=False):    
    autofocus: bool
    disabled: bool
    form: str
    formaction: str
    formenctype: Literal[
        "application/x-www-form-urlencoded", "multipart/form-data", "text/plain"
    ]
    formmethod: Literal["get", "post"]
    formnovalidate: bool
    formtarget: str
    popovertarget: str
    popovertargetaction: Literal["show", "hide", "toggle"]
    name: str
    type: Literal["primary", "secondary", "default", "alternative", "outline", "dashed", "link", "text", "danger", "warning"]
    variant: Literal["default", "destructive", "outline", "secondary", "ghost", "link"]
    size: Literal["default", "sm", "lg", "icon"]
    
    htmltype: Literal["submit", "reset", "button"]

    value: str
    data_state: Annotated[str, "data-state"]


class DivAttrs(GlobalAttrs, total=False):
    aria_describedby: Annotated[str, "aria-describedby"]
    aria_labelledby: Annotated[str, "aria-labelledby"]
    role: str
    data_state: Annotated[str, "data-state"]


class InputAttrs(GlobalAttrs, total=False):
    accept: str
    alt: str
    autcomplete: Literal["on", "off"]
    autofocus: bool
    checked: bool
    dirname: str
    disabled: bool
    form: str
    formaction: str
    formenctype: Literal[
        "application/x-www-form-urlencoded", "multipart/form-data", "text/plain"
    ]
    formmethod: Literal["get", "post"]
    formnovalidate: bool
    formtarget: str
    height: int
    list: str
    max: int
    maxlength: int
    min: int
    minlength: int
    multiple: bool
    name: str
    pattern: str
    placeholder: str
    popovertarget: str
    popovertargetaction: Literal["show", "hide", "toggle"]
    readonly: bool
    required: bool
    size: int
    src: str
    step: int
    type: Literal[
        "checkbox",
        "button",
        "color",
        "date",
        "datetime-local",
        "email",
        "file",
        "hidden",
        "image",
        "month",
        "number",
        "password",
        "radio",
        "range",
        "reset",
        "search",
        "submit",
        "tel",
        "text",
        "time",
        "url",
        "week",
    ]
    value: str
    width: int


class LiAttrs(GlobalAttrs, total=False):
    value: int    


class UlAttrs(GlobalAttrs, total=False):
    role: str
    data_orientation: Annotated[str, "data-orientation"]
    aria_label: Annotated[str, "aria-label"]
    aria_orientation: Annotated[str, "aria-orientation"]
    aria_labelledby: Annotated[str, "aria-labelledby"]