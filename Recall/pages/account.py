"""The settings page."""

from Recall.templates import ThemeState, template

import reflex as rx


@template(route="/account", title="Account")
def account() -> rx.Component:
    """The Account page.

    Returns:
        The UI for the Account page.
    """
    return rx.vstack(
        rx.heading("Account", size="8"),
        rx.hstack(
            rx.text("Dark mode: "),
            rx.color_mode.switch(),
        ),
        rx.hstack(
            rx.text("Primary color: "),
            rx.select(
                [
                    "tomato",
                    "red",
                    "ruby",
                    "crimson",
                    "pink",
                    "plum",
                    "purple",
                    "violet",
                    "iris",
                    "indigo",
                    "blue",
                    "cyan",
                    "teal",
                    "jade",
                    "green",
                    "grass",
                    "brown",
                    "orange",
                    "sky",
                    "mint",
                    "lime",
                    "yellow",
                    "amber",
                    "gold",
                    "bronze",
                    "gray",
                ],
                value=ThemeState.accent_color,
                on_change=ThemeState.set_accent_color,
            ),
        ),
        rx.hstack(
            rx.text("Secondary color: "),
            rx.select(
                [
                    "gray",
                    "mauve",
                    "slate",
                    "sage",
                    "olive",
                    "sand",
                ],
                value=ThemeState.gray_color,
                on_change=ThemeState.set_gray_color,
            ),
        ),
        rx.text(
            "You can edit this page in ",
            rx.code("{your_app}/pages/account.py"),
            size="1",
        ),
    )
