"""The habits page."""

from Recall.templates import template

import reflex as rx

class ToggleEditViewHabits(rx.State):
    view: str = "Edit"

    habits_data: list[dict[str,str]] = [
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
    }
]

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
            ), rx.spacer(my="3em"),
            rx.foreach(
                ToggleEditViewHabits.habits_data,
                lambda habit: rx.vstack(
                    rx.heading(
                        habit["name"],
                        size="5", 
                        font_family="Lexend",
                        margin_bottom="0.5em",
                        align="left",
                    ), 
                    rx.foreach(
                        habit["labels"].split("|"),
                        lambda item: rx.text(item),
                        size="4", 
                        font_family="Lexend",
                        my="0.5em",
                        align="left",
        
                    ),
                    # rx.text(
                    #     habit["labels"].split("|"),
                    #     my="5px",
                    #     align="start",
                    # ),
                    # *[
                    # rx.text(label, size="5", font_family="Lexend", my="5px", align="left") for label in habit["labels"].split("|")
                    # ],
                    rx.text("Notes", margin_bottom="2em"),
                ),
            ),
            width="40vw",
        ),
        width="100vw",
        justify="center",
    )
