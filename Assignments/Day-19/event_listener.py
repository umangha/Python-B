from turtle import Turtle,Screen

def move_forwards():
    """Forward 10 Steps"""
    tim.forward(10)

tim = Turtle()
screen = Screen()

screen.listen()
screen.onkey(fun=move_forwards,key="space")

screen.exitonclick()
