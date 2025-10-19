# make a random walk 
import random
import turtle as t

def random_walk():
    """Random Direction changer in right direction"""
    direction_angle = [0,90,180,270]
    for _ in range(100):
        jerry.forward(20)
        angle = random.choice(direction_angle)
        # Change in random direction
        jerry.setheading(angle)
        jerry.color(random.choice(collors_collection))


# Making jerry the turtle
jerry = t.Turtle()
# Screen obj
screen = t.Screen()

# color of turtle 
jerry.color("green")
# Increase the thickness of the line drawn
jerry.pensize(10)
# Change the speed of turtle
jerry.speed(10)

# List of collors
collors_collection = ["black","red","blue","DarkOrange","DarkCyan","chocolate","green","IndianRed1","orange","plum4","salmon4"]

# Random Walk function
random_walk()

# Exits the terminal after a mouse click
screen.exitonclick()
