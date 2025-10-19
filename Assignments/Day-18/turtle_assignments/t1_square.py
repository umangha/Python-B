"""Importing Turtle graphics"""
from turtle import Turtle, Screen

# Creating a class of Turtle()
kachuwa = Turtle()

# Making a green turtle
kachuwa.shape("turtle")
kachuwa.color("green")

# length of square
LENGTH = 100

# Shows the current position of turtle
print(f"Starting position of turtle: {kachuwa.position()}")

for i in range(4):
    kachuwa.forward(LENGTH)
    kachuwa.rt(90)

# For holding the screen in place until clicked
screen = Screen()
screen.exitonclick()
