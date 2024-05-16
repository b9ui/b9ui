from b9ui.components import Blank
from b9ui.components.button import Button
from b9ui.components.card import Card, CardHeader, CardTitle, CardDescription, CardFooter, CardContent
from b9ui.html import div, main, span, ul, li, time
from lucide import IconTruck

from components import Header


async def index() -> Blank:
    return Blank(
        Header(
        ),
        main(
            div(
                div(
                    Card(
                        CardHeader(
                            CardTitle("Your Orders"),
                            CardDescription(
                                "Introducing Our Dynamic Orders Dashboard for Seamless Management and Insightful Analysis.",
                                class_="max-w-lg text-balance leading-relaxed"
                            ),
                            class_="pb-3"
                        ),
                        CardFooter(
                            Button("Create New Order")
                        ),
                        class_="sm:col-span-2"
                    ),
                    Card(
                        CardHeader(                                
                            CardDescription("This Week"),
                            CardTitle("$1,329", class_="text-4xl"),
                            class_="pb-2"
                        ),
                    ),
                    Card(
                        CardHeader(                                
                            CardDescription("This Month"),
                            CardTitle("$1,329", class_="text-4xl"),
                            class_="pb-2"
                        ),
                    ),
                    class_="grid gap-4 sm:grid-cols-2 md:grid-cols-4 lg:grid-cols-2 xl:grid-cols-4"
                ),
                class_="grid auto-rows-max items-start gap-4 md:gap-8 lg:col-span-2"
            ),
            div(
                Card(
                    CardHeader(
                        div(
                            CardTitle("Order Oe31b70H", class_="group flex items-center gap-2 text-lg"),
                            CardDescription("Date: November 23, 2023"),
                            class_="grid gap-0.5"
                        ),
                        div(
                            Button(
                                IconTruck(class_="h-3.5 w-3.5"),
                                span("Track Order", class_="lg:sr-only xl:not-sr-only xl:whitespace-nowrap"),
                                variant="outline",
                                size="sm",
                                class_="h-8 gap-1"
                            ),
                            class_="ml-auto flex items-center gap-1"
                        ),
                        class_="flex flex-row items-start bg-muted/50"
                    ),
                    CardContent(
                        div(
                            div("Order Details", class_="font-semibold"),
                            ul(
                                li(
                                    span("Glimmer Lamps x 2", class_="text-muted-foreground"),
                                    span("$250.00"),
                                    class_="flex items-center justify-between"
                                ),
                                li(
                                    span("Aqua Filters x 1", class_="text-muted-foreground"),
                                    span("$49.00"),
                                    class_="flex items-center justify-between"
                                ),
                                class_="grid gap-3"
                            ),
                            class_="grid gap-3"
                        ),
                        class_="p-6 text-sm"
                    ),
                    CardFooter(
                        div("Updated",
                            time("November 23, 2023", datetime="2023-11-23"),
                            class_="text-xs text-muted-foreground"
                        ),
                        class_="flex flex-row items-center border-t bg-muted/50 px-6 py-3"
                    ),
                    class_="overflow-hidden"
                ),
            ),
            class_="grid flex-1 items-start gap-4 p-4 sm:px-6 sm:py-0 md:gap-8 lg:grid-cols-3 xl:grid-cols-3"
        )
    )

