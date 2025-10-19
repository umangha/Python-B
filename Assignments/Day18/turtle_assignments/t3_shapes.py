# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
# Random color for each shapes and sides length is 100
# Every shapes should be overlayed
# Degree of turn for each shapes is according to (360/sides of shapes).
# For Example: square (360/4 = 90) and pentagon (360/4 = 72)

'''Import Class Turtle and Screen from turtle package'''
from turtle import Turtle, Screen
import random

def draw_shape(sides):
    '''Takes no of sides and angle of turn and draws a shape with random color'''
    angle = 360 / sides
    jack.color(random.choice(collors_collection))
    for _ in range(sides):
        jack.forward(150)
        jack.rt(angle)


# making a obj
jack = Turtle()
# Screen object
screen = Screen()

TURTLE_SIZE = 20

# List of collors
collors_collection = ["black","red","blue","DarkOrange","DarkCyan","chocolate","green","IndianRed1","orange","plum4","salmon4"]


# Setting the starting position
jack.penup()
jack.setpos(0, screen.window_height()/2 - TURTLE_SIZE/2)
jack.pendown()

# Turtle shape
jack.shape("turtle")
jack.pensize(10)


# In for loop range excludes 11 so it is upto 10
for sides in range(3,11):
    draw_shape(sides)



# Holds the screen till its clicked
screen.exitonclick()
