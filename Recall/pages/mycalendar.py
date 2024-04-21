# """The home page of the app."""

from Recall.templates import template, ThemeState

# """Welcome to Reflex! This file showcases the custom component in a basic app."""


import reflex as rx

from custom_components.reflex_calendar import calendar

from datetime import datetime

now = datetime.now()

# Get the weekday, month, day, and year from the datetime object
# Concatenate the formatted date


class Foo(rx.State):
    selected_date: str = str(now.strftime('%A'))[0:3] + " "  + \
            str(now.strftime('%B'))[0:3] + " "  + \
            str(now.strftime('%d'))+ " "  + \
            str(now.strftime('%Y'))
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
        YEAR = year

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

class ToggleEditView(rx.State):
    view: str = "Edit" #if it shows edit that means it is in view mode


    def toggle(self):
        if(self.view == "Edit"):
            self.view = "Save"
        else:
            self.view = "Edit"

    

def demo():
    # print("DAY", day)
    # Mapping dictionary for month abbreviations to numeric values
    # Lambda function to convert 3-char abbreviation to numeric month and extract day
    print_date = lambda date: f"{date[0:3]} {date[4:7]} {date[8:10]}"
    
    # time = str(Foo.selected_date)
    return rx.hstack(rx.vstack(
        rx.heading("Calendar", size="6", padding_left="5.25em", 
                   margin_bottom="10px",
                   font_family="Lexend",),
        calendar(
            go_to_range_start_on_select=True,
            calendar_type="gregory",
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
        ), align="start"),
        # Foo.selected_date
        rx.hstack(
            rx.text("Notes for " + print_date(Foo.selected_date),
                    padding_left="10em",
                    padding_right="2.5em",
                    font_family="Lexend",
                    size="8"),
            rx.button(
            ToggleEditView.view,
            color_scheme= ThemeState.gray_color,
            on_click=ToggleEditView.toggle,
        ), 
            
        ),
        
        width="100vw",
        
    )




@template(route="/", title="Calendar")
def mycalendar() -> rx.Component:
    return rx.vstack(
            demo(),
            align="center",
            # spacing="7",
            width="100vw",
            height="70vh",
        )
       