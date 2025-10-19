import turtle as t
import random

# The Color list rgb value
# Remove the first few (r,g,b) combination cause they white background of pic
color_list = [ (219, 153, 107), (133, 171, 195), (222, 72, 88), (215, 131, 149), (24, 119, 152), (241, 208, 98), (121, 177, 149), (38, 119, 84), (20, 165, 204), (219, 83, 76), (140, 86, 62), (131, 83, 102), (175, 185, 215), (21, 168, 123), (161, 209, 166), (174, 154, 74)]

# Object of Turtle Class
tim = t.Turtle()


tim.speed("fastest")

# No drawing of line
tim.penup()

# Hides the turtle from view
tim.hideturtle()

# Screen Class Object
screen = t.Screen()

# Setting the color mode to rgb 255 by default its 0
screen.colormode(255)

# Changing the direction of turtle
tim.setheading(225)
tim.forward(250)
# Back to default direction of turtle
tim.setheading(0)

no_of_dots = 100


for dot in range(1,no_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    # Check if the row has 10 dots then move back to default position 
    if dot % 10 == 0:
        # Turtle Direction Turns Up
        tim.setheading(90)
        tim.forward(50)

        # Turn turtle direction to left
        tim.setheading(180)
        # Move Back to the default starting positions of dot
        tim.forward(500)

        # Setting back the heading to default direction
        tim.setheading(0)













screen.exitonclick()
