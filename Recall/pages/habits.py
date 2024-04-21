"""The habits page."""


from Recall.templates import template
import reflex as rx


class ToggleEditViewHabits(rx.State):
   isEdit: bool = True


   habits_data: list[dict[str,list[str]]] = [
   {
       "name": [
           "Target run"
       ],
       "labels": [
           "Items?",
           "Spending?",
       ],
   },
   {
       "name": [
           "Sleep quality",
       ],
       "labels": [
           "Rating (1-5):",
       ],
   },
   {
       "name": [
           "Vacuum",
       ],
       "labels": [
       ],
   },
   {
       "name": [
           "Breakfast",
       ],
       "labels": [
           "Where?",
           "What?",
       ],
   },
]
          


   def toggle(self):
       self.isEdit = not(self.isEdit)
       print(self.habits_data)
  
   def addHabit(self):
       self.habits_data.append({"name": ["Enter Habit Name"], "labels": []})
       # print(self.habits_data)


   def handleInputChange(self, habit, value):
    #    print("habit", habit, value, "value")
        for i in range(len(self.habits_data)):
            if(self.habits_data[i]["name"] == habit["name"]):
                self.habits_data[i]["name"][0] = value # Update the first element in the list
          
   def handle_submit(self, form_data:list):
       self.isEdit = not(self.isEdit)
       keys = list(form_data.keys())
       for i in range(len(form_data)):
           self.habits_data[i]["name"][0] = keys[i]
       print(self.habits_data)






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
                   margin_bottom="0.5em",
               ),
  
                   width="100%",
                   justify="between",
           ),
               
               rx.spacer(my="3em"),
              
                   rx.cond(
                       ToggleEditViewHabits.isEdit,
                       #opt 1:true
                       rx.vstack(
                       rx.foreach(
                           ToggleEditViewHabits.habits_data,
                           lambda habit: rx.vstack(
                               rx.heading(
                                   habit["name"][0],
                                   size="5",
                                   font_family="Lexend",
                                   margin_bottom="0.5em",
                                   align="left",
                               ),
                               rx.foreach(
                                   habit["labels"],
                                   lambda label: rx.text(label),
                                   size="4",
                                   font_family="Lexend",
                                   my="0.5em",
                                   align="left",
                               ),
                               rx.text("Notes:", margin_bottom="2em"),
                           )
                       ), 
                       rx.button(
                           "Edit",
                           on_click=ToggleEditViewHabits.toggle,
                       )),
                       #opt 2: false
                       rx.vstack( rx.button("Add Habit", on_click=ToggleEditViewHabits.addHabit),
                        rx.form(
                        rx.foreach(
                            ToggleEditViewHabits.habits_data,
                            lambda habit: rx.vstack(
                                rx.input(
                                    value=habit["name"][0],
                                    name=habit["name"][0],
                                    on_change=lambda value: ToggleEditViewHabits.handleInputChange(habit, value)
                                ),
                                rx.foreach(
                                    habit["labels"],
                                    lambda label: rx.text(label),
                                    size="4",
                                    font_family="Lexend",
                                    my="0.5em",
                                    align="left",
                                ),
                                rx.text("Notes:", margin_bottom="2em"),
                            )
                        ), 
                            rx.button(
                            "Save",
                            type="submit"
                        )
                        , on_submit=ToggleEditViewHabits.handle_submit,
                            reset_on_submit=False,
                       ) # form closed
                       )
                  
              
           ),

           width="40vw",
       ),
       width="100vw",
       justify="center",
   )







