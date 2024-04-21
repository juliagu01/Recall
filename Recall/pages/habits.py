"""The habits page."""

from Recall.templates import template

import reflex as rx




@template(route="/habits", title="Habits")
def habits() -> rx.Component:
    """The Habits page.

    Returns:
        The UI for the Habits page.
    """
    return rx.vstack(
        rx.heading("Habits", size="8"),
        rx.text(
            "You can edit this page in ",
            rx.code("{your_app}/pages/account.py"),
        ), 
        width="100vw",
        align="center",
    )
