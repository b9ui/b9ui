from typing import override
from b9ui.attrs import NoAttrs 
from b9ui.components import Component
from b9ui.html import html, head, body, aside, div, link, nav, script, title
from b9ui.types import AnyChildren
from lucide import (
  IconPackage, 
  IconHome, 
  IconSettings, 
  IconShoppingCart, 
  IconUserRound,
  IconLineChart
)

from components import NavigationLink


class Layout(Component[AnyChildren, NoAttrs]):
    @override
    def render(self) -> html:
        return html(
            head(
                title("My App"),
                link(href="/static/css/default.css", rel="stylesheet"),
            ),
            body(
                div(
                    div(                        
                        div(
                            div(
                                aside(
                                    nav(
                                        NavigationLink("Acme Inc",
                                            IconPackage(class_="h-5 w-5"),                    
                                            href="#"                
                                        ),
                                        NavigationLink("Dashboard",
                                            IconHome(class_="h-5 w-5"),                    
                                            href="/"                
                                        ),
                                        NavigationLink("Dashboard",
                                            IconShoppingCart(class_="h-5 w-5"),                    
                                            href="#" ,
                                            class_="bg-accent text-accent-foreground"               
                                        ),
                                        NavigationLink("Dashboard",
                                            IconPackage(class_="h-5 w-5"),                    
                                            href="#"                
                                        ),
                                        NavigationLink("Dashboard",
                                            IconUserRound(class_="h-5 w-5"),                    
                                            href="#"                
                                        ),
                                        NavigationLink("Dashboard",
                                            IconLineChart(class_="h-5 w-5"),                    
                                            href="#"                
                                        ),
                                        class_="flex flex-col items-center gap-4 px-2 sm:py-4"
                                    ),
                                    nav(
                                        NavigationLink("Settings",
                                            IconSettings(class_="h-5 w-5"),                    
                                            href="/settings/"                
                                        ),
                                        class_="mt-auto flex flex-col items-center gap-4 px-2 sm:py-4"
                                    ),
                                    class_="fixed inset-y-0 left-0 z-10 hidden w-14 flex-col border-r bg-background sm:flex"
                                ),
                                div(
                                    *self.children,
                                    class_="flex flex-col sm:gap-4 sm:py-4 sm:pl-14"
                                ),
                                class_="flex min-h-screen w-full flex-col bg-muted/40"
                            ),
                        ),
                        class_="w-full h-full theme-zinc"
                    ),
                    class_="relative flex min-h-screen flex-col bg-background"
                ),
                
                script(src="https://unpkg.com/htmx.org@1.9.10"),
                script(src="https://unpkg.com/hyperscript.org@0.9.12"),                
                script(src="https://cdn.tailwindcss.com"),
                class_="min-h-screen bg-background font-sans antialiased __variable_ac79ff",
            ),
            class_="light",
            lang="en", style="color-scheme: light;"
        )
