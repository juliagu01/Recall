"""The habits page."""

from Recall.templates import template

import reflex as rx

habits_data: list[dict[str, str]] = [
    {
        "name": "Target run",
        "labels": "Items?|Spending?",
    },
    {
        "name": "Sleep quality",
        "labels": "Rating (1-5):",
    },
    {
        "name": "Vacuum",
        "labels": "",
    },
]


class ToggleEditViewHabits(rx.State):
    view: str = "Edit"

    def toggle(self):
        if (self.view == "Edit"):
            self.view = "Save"
        else:
            self.view = "Edit"


@template(route="/habits", title="Habits")
def habits() -> rx.Component:
    """The Habits page.

    Returns:
        The UI for the Habits page.
    """
    return rx.hstack(
        rx.vstack(
            rx.hstack(
                rx.heading(
                    "Habits", 
                    size="6", 
                    font_family="Lexend",
                ),
                rx.button(
                    ToggleEditViewHabits.view,
                    on_click=ToggleEditViewHabits.toggle,
                ),
                width="100%",
                justify="between",
            ),
            rx.foreach(
                habits_data,
                lambda habit: rx.vstack(
                    rx.heading(
                        habit["name"],
                        size="5", 
                        font_family="Lexend",
                    ),
                    rx.text(
                        habit["labels"],
                    ),
#                    rx.heading(
#                        habit["name"],
#                        size="5", 
#                        font_family="Lexend",
#                    ),
#                    rx.foreach(
#                        habit["labels"].split("|").append("Notes:"),
#                        lambda label: rx.text(
#                            label
#                        ),
#                    ),
                ),
            ),
            rx.text(
                "You can edit this page in ",
                rx.code("{your_app}/pages/account.py"),
            ), 
            width="40vw",
            align="center",
        ),
        width="100vw",
        justify="center",
    )
