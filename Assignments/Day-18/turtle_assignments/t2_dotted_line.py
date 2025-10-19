'''Import Class Turtle and Screen from turtle package'''
from turtle import Turtle, Screen

# making a obj
jack = Turtle()

# Turtle shape
jack.shape("turtle")
jack.color("green")

# Make a dotted line

for i in range(20):
    jack.forward(10)
    # No drawing line
    jack.penup()

    jack.forward(10)
    # Start Drawing line again
    jack.pendown()



# Screen object
screen = Screen()
# Holds the screen till its clicked
screen.exitonclick()
