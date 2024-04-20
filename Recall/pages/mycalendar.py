# """The home page of the app."""

from Recall.templates import template

# """Welcome to Reflex! This file showcases the custom component in a basic app."""


import reflex as rx

# from reflex_calendar import *

# class Foo(rx.State):
#     selected_date: str = ""
#     logs: list[str] = []

#     def change_handler(self, var):
#         self.selected_date = var
#         self.add_log(f"Changed selected date: {var}")

#     def active_start_date_change_handler(self, var):
#         if "drill" in var["action"]:
#             return

#         action = var["action"]
#         start_date = var["activeStartDate"]
#         self.add_log(f"Changed active start date to {start_date} ({action})")

#     def click_day_handler(self, day):
#         self.add_log(f"Clicked day {day}")

#     def click_month_handler(self, month):
#         self.add_log(f"Clicked month {month}")

#     def click_decade_handler(self, var):
#         self.add_log(f"Clicked decade {var}")

#     def click_year_handler(self, year):
#         self.add_log(f"Clicked year {year}")

#     def click_week_number_handler(self, var):
#         self.add_log(f"Clicked week number {var['week_number']}")

#     def drill_down_handler(self, view):
#         self.add_log(f"Drilled down to: {view} view")

#     def drill_up_handler(self, view):
#         self.add_log(f"Drilled up to: {view} view")

#     def view_change_handler(self, event):
#         self.add_log(f"View changed to: {event['view']}")

#     def clear_logs(self):
#         self.logs = []

#     def add_log(self, log):
#         self.logs.append(log)
#         if len(self.logs) > 15:
#             self.logs.pop(0)


# def demo():
#     return rx.vstack(
#         rx.heading("Calendar Demo", size="6"),
#         # rx.moment(Foo.selected_date),
#         calendar(
#             go_to_range_start_on_select=True,
#             locale="en-EN",
#             on_active_start_date_change=Foo.active_start_date_change_handler,
#             on_change=Foo.change_handler,
#             on_click_day=Foo.click_day_handler,
#             on_click_month=Foo.click_month_handler,
#             on_click_decade=Foo.click_decade_handler,
#             on_click_year=Foo.click_year_handler,
#             on_click_week_number=Foo.click_week_number_handler,
#             on_drill_down=Foo.drill_down_handler,
#             on_drill_up=Foo.drill_up_handler,
#             # on_view_change=Foo.view_change_handler,
#         ), rx.text(Foo.selected_date),
#         rx.text("HIII"),
#         align="center",
#         width="100%",
#     )


@template(route="/", title="Calendar")
# def mycalendar() -> rx.Component:
#     return rx.center(
#         rx.hstack(
#             demo(),
#             align="center",
#             spacing="7",
#             width="100vw",
#             height="70vh",
#         ),
#         width="100vw",
#         height="100vh",
#     )

def mycalendar() -> rx.Component:
    return rx.center(
        rx.text("HI"),
        width="100vw",
        height="100vh",
    )
