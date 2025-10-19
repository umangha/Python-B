# Import from the default Python Module Turtle
from turtle import Turtle, Screen

# Making a obj of class Turtle from Turtle Module
timmy = Turtle()

# Shape of Timmy
timmy.shape("turtle")
timmy.color("green")

# Move turtle forward 100 steps
timmy.forward(100)

# Object creation 
my_screen = Screen()

# Height of the canvas
print(my_screen.canvheight)

# Exits the screen if clicked on
my_screen.exitonclick()