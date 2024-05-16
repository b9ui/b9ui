from b9ui.html import div, nav, h3, main
from b9ui.components import Blank
from b9ui.components.button import Button
from b9ui.components.link import Link
from b9ui.components.card import Card, CardHeader, CardTitle, CardDescription, CardFooter, CardContent

from components import Header


async def index() -> Blank:
    return Blank(
        Header(
        ),
        main(
            div(
                h3("Settings",
                    class_="text-3xl font-semibold"
                ),
                class_="mx-auto grid w-full max-w-6xl gap-2"
            ),
            div(
                nav(
                    Link("General",
                        href="#",
                        class_="font-semibold text-primary"
                    ),
                    Link("Security",
                        href="#"
                    ),
                    Link("Integrations",
                        href="#"
                    ),
                    Link("Support",
                        href="#"
                    ),
                    Link("Organizations",
                        href="#"
                    ),
                    Link("Advanced",
                        href="#"
                    ),
                    class_="grid gap-4 text-sm text-muted-foreground"
                ),
                div(
                    Card(
                        CardHeader(
                            CardTitle("General Settings"),
                            CardDescription("Used to identify your store in the marketplace."),
                            CardContent(),
                            CardFooter(
                                Button("Save"),
                                class_="border-t px-6 py-4"
                            ),
                        ),
                    ),
                    class_="grid gap-6"
                ),
                class_="mx-auto grid w-full max-w-6xl items-start gap-6 md:grid-cols-[180px_1fr] lg:grid-cols-[250px_1fr]"
            ),
            class_="flex min-h-[calc(100vh_-_theme(spacing.16))] flex-1 flex-col gap-4 bg-muted/40 p-4 md:gap-8 md:p-10"
        )
    )