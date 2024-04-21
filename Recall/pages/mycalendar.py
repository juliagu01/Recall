# """The home page of the app."""

from Recall.templates import template, ThemeState

# """Welcome to Reflex! This file showcases the custom component in a basic app."""


import reflex as rx

from custom_components.reflex_calendar import calendar

from datetime import datetime

from Recall.pages.habits import ToggleEditViewHabits

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

class ViewState(rx.State):
    edit: bool = True

    def toggle(self):
       self.edit = not(self.edit)

    
          
    # def handle_submit(self, form_data:list):
    #    self.isEdit = not(self.isEdit)
    #    keys = list(form_data.keys())
    #    for i in range(len(form_data)):
    #        self.habits_data[i]["name"][0] = keys[i]
    #    print(self.habits_data)

    

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
        rx.vstack(
            rx.hstack(
                rx.text("Notes for " + print_date(Foo.selected_date),
                        font_family="Lexend",
                        size="8"),
                ),rx.spacer(margin_top="10px"),

                # rx.cond(ViewState.edit,
                    # rx.button(
                    # "Edit",
                    # color_scheme= ThemeState.gray_color,
                    # on_click=ViewState.toggle,
                    # ),
                    # rx.button(
                    # "Save",
                    # color_scheme= ThemeState.gray_color,
                    # on_click=ViewState.toggle,
                    # )
                # )
                # ,
                rx.cond(ViewState.edit,
                    # true
                    rx.vstack(
                       rx.foreach(
                           ToggleEditViewHabits.habits_data,
                           lambda habit: rx.vstack(
                               rx.heading(
                                   habit["name"][0],
                                   size="6",
                                   font_family="Lexend",
                                   margin_bottom="0.5em",
                                   align="left",
                               ), rx.hstack(
                               rx.vstack(
                                rx.foreach(
                                    habit["labels"],
                                    lambda label: rx.text(label),
                                    size="4",
                                    font_family="Lexend",
                                    my="0.5em",
                                    align="left",
                               )), rx.vstack(
                                rx.foreach(
                                   habit["responses"],
                                   lambda response: rx.text(response, color_scheme=ThemeState.accent_color),
                                   size="4",
                                   font_family="Lexend",
                                   my="0.5em",
                                   align="left",
                               )))
                           )
                       ), rx.button(
                                "Edit",
                                color_scheme= ThemeState.gray_color,
                                on_click=ViewState.toggle,
                                ))
                    ,

                    #false
                    rx.vstack(
                       rx.foreach(
                           ToggleEditViewHabits.habits_data,
                           lambda habit: rx.vstack(
                               rx.heading(
                                   habit["name"][0],
                                   size="6",
                                   font_family="Lexend",
                                   margin_bottom="0.5em",
                                   align="left",
                               ), rx.hstack(
                               rx.vstack(
                                rx.foreach(
                                    habit["labels"],
                                    lambda label: rx.text(label),
                                    size="5",
                                    font_family="Lexend",
                                    my="4em",
                                    align="left",
                               )), rx.vstack(
                                rx.foreach(
                                   habit["responses"],
                                   lambda response: 
                                   rx.input( value=response,
                                    name=response,
                                    on_change=lambda value: ToggleEditViewHabits.handleInputChange(habit, response, value)),
                                   size="4",
                                   font_family="Lexend",
                                   my="0.5em",
                                   align="left",
                               ))),
                           )
                       ), rx.button(
                    "Save",
                    color_scheme= ThemeState.gray_color,
                    on_click=ViewState.toggle,
                    ))
                    ,
                ),
            
            padding_left="10em",
            padding_right="2.5em",
            
                
            
        ),
        
    ), 






@template(route="/", title="Calendar")
def mycalendar() -> rx.Component:
    return rx.vstack(
            demo(),
            align="center",
            # spacing="7",
            width="100vw",
            height="70vh",
            margin_bottom = "15em", 
        )
       