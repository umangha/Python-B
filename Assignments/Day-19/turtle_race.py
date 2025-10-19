from turtle import Turtle, Screen
import random

screen = Screen()

# Setting the Screen Width and Height Manually
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="User Turtle",prompt="Choose Your Turtle Color")

# Six colors of rainbow
colors = ["red","orange","yellow","green","blue","purple"]

# List of y-coordinates
y_coordinates = [-80,-50,-20,10,40,70]

# All turtles list
all_turtle = []

# Turtle movement Tracker
turtle_move_status = False


# Creating 6 Turtles
for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    # Go to the required co-ordinates in the screen with respect to the width and height of screen
    new_turtle.goto(x=-230,y=y_coordinates[index])
    all_turtle.append(new_turtle)

# Moving Turtle forward
# Move turtle if the user has inputted his bet
if user_bet:
    turtle_move_status = True

while turtle_move_status:
    for turtle in all_turtle:
        # Focus Here the screen width we set is 250 and size of turtle is (40x40) so radius of turtle is 20. So 250-20=230
        if turtle.xcor() > 230:
            # Game Over Turtle reached the finish line
            turtle_move_status=False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You won the race! Your color is {winning_color}")
            else:
                print(f"You Lost the race! The winning color is {winning_color}")

        # Here 10 is inclusive so the movement of turtle can be from 0 to 10
        new_dist = random.randint(0,10)
        turtle.forward(new_dist)





screen.exitonclick()
