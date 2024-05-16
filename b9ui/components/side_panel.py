from typing import Any, override
from ludic.attrs import NoAttrs
from ludic.html import header, span, form, label, input
from ludic.types import AnyChildren, Component
from b9ui.components.button import Button
from b9ui.html import div



class SidePanel(Component[AnyChildren, NoAttrs]):
    @override
    def render(self) -> div:
        return div(
            header("Add new row to ",
                   span("tenant",
                       class_="text-code font-mono"
                   ),
                class_=" space-y-1 py-4 px-4 bg-overlay sm:px-6 border-b border-overlay "
            ),
            div(
                form(
                    div(
                        div(
                            div(
                                div(
                                    div(
                                        div(
                                            label("ID",
                                                class_="block text-foreground-light text-sm"
                                            ),
                                            span("uuid",
                                                class_="text-foreground-lighter text-sm"
                                            ),
                                            class_="flex flex-col space-y-2 col-span-4"
                                        ),
                                        div(
                                            div(
                                                div(
                                                    input(
                                                        type="text",
                                                        class_="peer/input block box-border w-full rounded-md shadow-sm transition-all text-foreground focus-visible:shadow-md outline-none focus:ring-current focus:ring-2 focus-visible:border-foreground-muted focus-visible:ring-background-control placeholder-foreground-muted bg-foreground/[.026] border border-control text-sm px-4 py-2"
                                                    ),
                                                    class_="relative"
                                                ),
                                            ),
                                            class_="col-span-8"
                                        ),
                                        class_="text-sm grid gap-2 md:grid md:grid-cols-12"
                                    ),
                                    class_="space-y-10 py-6"
                                ),
                                class_="px-4 sm:px-6"
                            ),
                            class_="flex flex-grow flex-col"
                        ),
                        div(
                            div(
                                Button("Cancel", 
                                                     hx_get="/empty",
                                                     hx_target="#side-panel-area",
                                                     type="button"),
                                Button("Save", 
                                                   _="on click set my innerHTML to 'Clicked!'",
                                                   type="text"),                              
                                class_="flex w-full justify-end space-x-3 border-t border-default px-3 py-4"
                            ),
                            class_="flex-shrink"
                        ),
                        class_="flex h-full flex-col"
                    ),
                    class_="h-full"
                ),


                class_=" relative flex-1 overflow-y-auto "
            ),
            id="side-panel-editor",
            role="dialog", aria_describedby="radix-:r2e:", aria_labelledby="radix-:r2d:",
            data_state="open",
            class_=" z-40 bg-overlay flex flex-col fixed inset-y-0 h-full lg:h-screen border-l border-overlay shadow-xl  w-screen max-w-2xl h-full  right-0 data-open:animate-panel-slide-right-out data-closed:animate-panel-slide-right-in  transition-all duration-100 ease-in ",          
            style={"pointer-events": "auto"},
        )
    