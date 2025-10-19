"""importing the default turtle graphics package"""
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

# Changing the shape to turtle
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")


# Screen Doesnot exit till the screen is clicked
screen = Screen()
screen.exitonclick()
