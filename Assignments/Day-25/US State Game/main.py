import turtle
import pandas as pd
from text_on_screen import StateName

screen = turtle.Screen()
screen.title("US States Game")


# File path for the image
image = "Assignments/Day-25/US State Game/blank_states_img.gif"


screen.addshape(image) # Using this image as shape
turtle.shape(image) # Image loaded in the shape of the picture provided


# Importing the Class that displays the text on the turtle screen
text_screen = StateName()
## Getting the Data from the csv
data = pd.read_csv("./Assignments/Day-25/US State Game/50_states.csv")

# Changing the read states df to list
all_state=data.state.tolist()

# List that holds the guessed state name
guessed_states=[]

## Game on Loop
while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Enter a state name:").lower()

    row = data[data["state"].str.lower() == user_answer]

    if len(row) > 0 and user_answer not in guessed_states:
        guessed_states.append(user_answer)
        x = int(row["x"].iloc[0])
        y = int(row["y"].iloc[0])
        text_screen.text_at_xy(text=user_answer, x=x, y=y)
    else:
        print("Wrong state. Try again.")
    
    # Loop Break Condition
    if user_answer== "exit":
        not_guessed_states=[]
        for state in all_state:
            if state not in guessed_states:
                not_guessed_states.append(state)
        not_guessed_df = pd.DataFrame(not_guessed_states)
        not_guessed_df.to_csv("./Assignments/Day-25/US State Game/rem_50_states.csv")
        break


# screen.exitonclick()
print(not_guessed_states)
