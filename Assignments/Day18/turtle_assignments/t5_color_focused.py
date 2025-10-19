# make a random walk and generating color in RGB
import random
import turtle as t

def random_color():
    '''Returns tuple of random rgb color '''
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def random_walk():
    """Random Direction changer in right direction"""
    direction_angle = [0,90,180,270]
    for _ in range(100):
        jerry.forward(20)
        angle = random.choice(direction_angle)
        # Change in random direction
        jerry.setheading(angle)
        jerry.color(random_color())



# Making jerry the turtle
jerry = t.Turtle()
# Screen obj
screen = t.Screen()

# Changing the color mode of turtle package as a whole. Range of color is 0 to 255 RGB
screen.colormode(255)

# color of turtle
jerry.color("green")
# Increase the thickness of the line drawn
jerry.pensize(10)
# Change the speed of turtle
jerry.speed(10)



# Random Walk function
random_walk()

# Exits the terminal after a mouse click
screen.exitonclick()
