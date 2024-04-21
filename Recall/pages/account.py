"""The settings page."""

from Recall.templates import ThemeState, template

import reflex as rx

from datetime import datetime

now = datetime.now()

class accountForm(rx.State):
    submitForm: bool = True
    form_data: dict = {}
    date: str = str(now.strftime('%A'))[0:3] + " "  + \
            str(now.strftime('%B'))[0:3] + " "  + \
            str(now.strftime('%d'))+ " "  + \
            str(now.strftime('%Y'))

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.toggle()
        self.form_data = form_data
        
        

    def toggle(self):
        self.submitForm = not(self.submitForm)


def header()-> rx.Component:
    return rx.hstack(
        rx.heading("Account", size="8", padding_right="2em", font_family="Lexend"),
        rx.hstack(
            rx.text("Dark mode: "),
            rx.color_mode.switch(),
            align="center",
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
                font_family="Lexend",
            ),
        ),
        rx.hstack(
            rx.text("Secondary color: "),
            rx.select(
                [
                    'gray','sky','mint','lime','yellow','amber','gold','bronze'
                ],
                value=ThemeState.gray_color,
                on_change=ThemeState.set_gray_color,
                font_family="Lexend",
            ),
        ),
        
        
        width="100vw",
    )



@template(route="/account", title="Account")
def account() -> rx.Component:
    """The Account page.

    Returns:
        The UI for the Account page.
    """
    
    return (rx.vstack(
        header(),
        rx.cond(
            accountForm.submitForm,
            (rx.form(rx.button("Save", type="submit"),rx.spacer(),
            rx.hstack(
            rx.text("Name:", size = "6", font_family="Lexend"),
            rx.input(placeholder="Joe Bruin", name = "Name"),
            ),
            rx.spacer(),
            rx.text("Member since: " + accountForm.date, size = "4", font_family="Lexend"), 
            on_submit=accountForm.handle_submit,
            reset_on_submission=False,)), #true

            rx.vstack(rx.button("Edit", on_click=accountForm.toggle),
                      rx.hstack(
            rx.text("Name: "+accountForm.form_data["Name"].to_string()[1:-1], size = "6", font_family="Lexend"),
            
            ),
            rx.spacer(),
            rx.text("Member since: " + accountForm.date, size = "4", font_family="Lexend"),
            ) # false
        )
        ), 
        # rx.text(accountForm.form_data.to_string()),
        )