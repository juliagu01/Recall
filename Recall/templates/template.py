"""Common templates used between pages in the app."""

from __future__ import annotations

from Recall import styles
from Recall.components.sidebar import sidebar
from typing import Callable

import reflex as rx

# Meta tags for the app.
default_meta = [
    {
        "name": "viewport",
        "content": "width=device-width, shrink-to-fit=no, initial-scale=1",
    },
]


def menu_item_link(text, href):
    return rx.menu.item(
        rx.link(
            text,
            href=href,
            width="100%",
            color="inherit",
        ),
        _hover={
            "color": styles.accent_color,
            "background_color": styles.accent_text_color,
        },
    )


def menu_button() -> rx.Component:
    """The menu button on the top right of the page.

    Returns:
        The menu button component.
    """
    from reflex.page import get_decorated_pages

    return rx.box(
        rx.menu.root(
            rx.menu.trigger(
                rx.button(
                    rx.icon("menu"),
                    variant="soft",
                )
            ),
            rx.menu.content(
                *[
                    menu_item_link(page["title"], page["route"])
                    for page in sorted(get_decorated_pages(), key=lambda x: (x['index']))
                ]
            ),
        ),
        position="fixed",
        right="2em",
        top="2em",
        z_index="500",
    )


class ThemeState(rx.State):
    """The state for the theme of the app."""

    accent_color: str = "crimson"

    gray_color: str = "gray"



from reflex_calendar import calendar

class Foo(rx.State):
    selected_date: str = ""
    logs: list[str] = []

    def change_handler(self, var):
        self.selected_date = var
        self.add_log(f"Changed selected date: {var}")

    def active_start_date_change_handler(self, var):
        if "drill" in var["action"]:
            return

        action = var["action"]
        start_date = var["activeStartDate"]
        self.add_log(f"Changed active start date to {start_date} ({action})")

    def click_day_handler(self, day):
        self.add_log(f"Clicked day {day}")

    def click_month_handler(self, month):
        self.add_log(f"Clicked month {month}")

    def click_decade_handler(self, var):
        self.add_log(f"Clicked decade {var}")

    def click_year_handler(self, year):
        self.add_log(f"Clicked year {year}")

    def click_week_number_handler(self, var):
        self.add_log(f"Clicked week number {var['week_number']}")

    def drill_down_handler(self, view):
        self.add_log(f"Drilled down to: {view} view")

    def drill_up_handler(self, view):
        self.add_log(f"Drilled up to: {view} view")

    def view_change_handler(self, event):
        self.add_log(f"View changed to: {event['view']}")

    def clear_logs(self):
        self.logs = []

    def add_log(self, log):
        self.logs.append(log)
        if len(self.logs) > 15:
            self.logs.pop(0)

def demo():
    return rx.vstack(
        rx.heading("Calendar Demo", size="6"),
        # rx.moment(Foo.selected_date),
        calendar(
            go_to_range_start_on_select=True,
            locale="en-EN",
            on_active_start_date_change=Foo.active_start_date_change_handler,
            on_change=Foo.change_handler,
            on_click_day=Foo.click_day_handler,
            on_click_month=Foo.click_month_handler,
            on_click_decade=Foo.click_decade_handler,
            on_click_year=Foo.click_year_handler,
            on_click_week_number=Foo.click_week_number_handler,
            on_drill_down=Foo.drill_down_handler,
            on_drill_up=Foo.drill_up_handler,
            # on_view_change=Foo.view_change_handler,
        ), rx.text(Foo.selected_date),
        rx.text("HIII"),
        align="center",
        width="100%",
    )

def template(
    route: str | None = None,
    title: str | None = None,
    # index: int = 0,
    description: str | None = None,
    meta: str | None = None,
    script_tags: list[rx.Component] | None = None,
    on_load: rx.event.EventHandler | list[rx.event.EventHandler] | None = None,
) -> Callable[[Callable[[], rx.Component]], rx.Component]:
    """The template for each page of the app.

    Args:
        route: The route to reach the page.
        title: The title of the page.
        description: The description of the page.
        meta: Additionnal meta to add to the page.
        on_load: The event handler(s) called when the page load.
        script_tags: Scripts to attach to the page.

    Returns:
        The template with the page content.
    """

    def decorator(page_content: Callable[[], rx.Component]) -> rx.Component:
        """The template for each page of the app.

        Args:
            page_content: The content of the page.

        Returns:
            The template with the page content.
        """
        # Get the meta tags for the page.
        all_meta = [*default_meta, *(meta or [])]

        def templated_page():
            return rx.vstack(
                sidebar(),
                demo(),
                rx.box(
                    rx.vstack(
                        page_content(),
                        rx.spacer(),
                        rx.logo(),
                        **styles.template_content_style,
                    ),
                    **styles.template_page_style,
                ),
                # menu_button(),
                align="start",
                background=f"radial-gradient(circle at top right, {rx.color('accent', 2)}, {rx.color('mauve', 1)});",
                position="relative",
            )

        @rx.page(
            route=route,
            title=title,
            description=description,
            meta=all_meta,
            script_tags=script_tags,
            on_load=on_load,
        )
        def theme_wrap():
            return rx.theme(
                templated_page(),
                has_background=True,
                accent_color=ThemeState.accent_color,
                gray_color=ThemeState.gray_color,
            )

        return theme_wrap

    return decorator
