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
           "Notes",
       ], 
       "responses": [
           "Allergy medicine, Reese's cups", 
           "$10.83",
           "\u00a0"
       ]
   },
   {
       "name": [
           "Sleep quality",
       ],
       "labels": [
           "Rating (1-5):",
           "Notes",
       ], 
       "responses": [
           "5", 
           "\u00a0"
       ]
   },
   {
       "name": [
           "Vacuum",
       ],
       "labels": [
           "Notes",
       ],
       "responses": [
           "\u00a0"
       ]
   },
   {
       "name": [
           "Breakfast",
       ],
       "labels": [
           "Where?",
           "What?",
           "Notes",
       ],
       "responses": [
           "\u00a0", 
           "\u00a0",
           "\u00a0"
       ]
   },
]
          


   def toggle(self):
       self.isEdit = not(self.isEdit)
       print(self.habits_data)
  
   def addHabit(self):
       self.habits_data.append({"name": ["Enter Habit Name"], "labels": ["Notes"], "responses": [""]})
       # print(self.habits_data)

    # for changing habits
   def handleChange(self, habit, value):
    #    print("habit", habit, value, "value")
        for i in range(len(self.habits_data)):
            if(self.habits_data[i]["name"] == habit["name"]):
                self.habits_data[i]["name"][0] = value # Update the first element in the list
    
    # handle submit of habits page
   def handle_submit(self, form_data:list):
       self.isEdit = not(self.isEdit)
       keys = list(form_data.keys())
       for i in range(len(form_data)):
           self.habits_data[i]["name"][0] = keys[i]
       print(self.habits_data)

    #submitting calendar
   def handle_submit_calendar(self, form_data:list):
       keys = list(form_data.keys()) 
       #9 responses in form data, but 
       for i in range(len(form_data)):
           for j in range(len(self.habits_data[i]["responses"])):
                self.habits_data[i]["responses"][j] = keys[i]
       print(self.habits_data)

    #for adding a response
   def handleInputChange(self, habit, response, value):
        for i in range(len(self.habits_data)):
            if(self.habits_data[i]["name"] == habit["name"] and response in self.habits_data[i]["responses"]):
                find_val = self.habits_data[i]["responses"].index(response)
                self.habits_data[i]["responses"][find_val] = value 





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
                                    on_change=lambda value: ToggleEditViewHabits.handleChange(habit, value)
                                ),
                                rx.foreach(
                                    habit["labels"],
                                    lambda label: rx.text(label),
                                    size="4",
                                    font_family="Lexend",
                                    my="0.5em",
                                    align="left",
                                ),
                                
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







