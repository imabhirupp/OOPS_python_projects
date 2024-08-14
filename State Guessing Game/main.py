import turtle,pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()                                                                                             # collects all the states as a list
guessed_state = []

while len(guessed_state) < 50:

    answer_state = screen.textinput(f"{len(guessed_state)} the States",
                                    "What's another State's Name?").title()                                                      # .title() is used to make the first letter of a string capitalise

    if answer_state == "Exit":                                                                                                   # To exit if the user enters exit
        missing_states = []
        # missing_states = [states for states in all_states if states is not in guessed_state]                                   # Alternative code lines using list comprehension
        for states in all_states:
            if states is not in guessed_state:                                                                                   # To check if the states is not in the guessed_state list
                missing_states.append(states)                                                                                    # Adding the state to missing_states list
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)                                                                              # Creating a data-frame with the missing states list
        new_data.to_csv("Missed_out_states.csv")                                                                                 # Saving the data-frame as a csv file

        break

    if answer_state in all_states:                                                                                               # check if answer_state is in the all_state list using 'in'
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]                                                                            # storing the row data of that state
        t.goto(state_data.x.item(), state_data.y.item())                                                                         # tapping into the x-cor and y-cor of the state and using item to only get the value of the x and y coordinates and not their index numbers
        t.write(answer_state)                                                                                                    # writing the name of the answer_state on the screen to avoid the extra data if we use the direct state name





screen.exitonclick()
