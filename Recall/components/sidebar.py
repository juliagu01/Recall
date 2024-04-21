"""Sidebar component for the app."""

from Recall import styles

import reflex as rx


def sidebar_header() -> rx.Component:
    """Sidebar header.

    Returns:
        The sidebar header component.
    """
    return rx.hstack(
        # The logo.
        rx.image(src="/favicon.ico", height="2em"),
        rx.link(
            rx.button(
                rx.icon("github"),
                color_scheme="gray",
                variant="soft",
            ),
            href="https://github.com/reflex-dev/reflex",
        ),
        
        align="center",
        width="340%",
        
        padding_x="1em",
        padding_y="2em",
    )


def sidebar_footer() -> rx.Component:
    """Sidebar footer.

    Returns:
        The sidebar footer component.
    """
    return
    


def sidebar_item(text: str, url: str) -> rx.Component:
    """Sidebar item.

    Args:
        text: The text of the item.
        url: The URL of the item.

    Returns:
        rx.Component: The sidebar item component.
    """
    # Whether the item is active.
    active = (rx.State.router.page.path == url.lower()) | (
        (rx.State.router.page.path == "/") & text == "Home"
    )

    return rx.link(
        rx.hstack(
            rx.text(
                text,
                align="center"
            ),
            bg=rx.cond(
                active,
                rx.color("accent", 2),
                "transparent",
            ),
            border=rx.cond(
                active,
                f"1px solid {rx.color('accent', 6)}",
                f"1px solid {rx.color('gray', 6)}",
            ),
            color=rx.cond(
                active,
                styles.accent_text_color,
                styles.text_color,
            ),
            border_radius=styles.border_radius,
            # width="100%",
            padding="1em",
            
        ),
        href=url,
        # width="100%",
        
    )


def sidebar() -> rx.Component:
    """The sidebar.

    Returns:
        The sidebar component.
    """
    # Get all the decorated pages and add them to the sidebar.
    from reflex.page import get_decorated_pages

    custom_order = {"Calendar": 1, "Habits": 2, "Account": 3}
    return rx.box(
        rx.hstack(
            sidebar_header(),
            # rx.spacer(),
            rx.hstack(
                *[
                    sidebar_item(
                        text=page.get("title", page["route"].strip("/").capitalize()),
                        url=page["route"],
                    )
                    for page in sorted(get_decorated_pages(), key=lambda x: custom_order.get(x.get("title", x["route"].strip("/").capitalize()), float('inf')))
                ],
                width="100%",
                overflow_y="auto",
                align_items="end",
                # align_items="flex-start",
                padding="1em",
            ),
            # rx.spacer(),
        ),
        display=["none", "none", "block"],
        height="85px",
        width="100%",
        position="sticky",
        border_bottom=styles.border,
        
    )
