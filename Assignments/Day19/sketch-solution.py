from turtle import Turtle, Screen

def forward():
    """Move the Turtle Forward"""
    tim.fd(10)

def backward():
    """Move the Turtle Backward"""
    tim.back(10)

def clockwise():
    """Move the Turtle Clockwise"""
    # Adding 10 to the current directio in clockwise
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def anti_clockwise():
    """Move the Turtle Anti Clockwise"""
    # Adding 10 to the current direction in anti-clockwise
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clear():
    """Resets the Screen"""
    screen.reset()


tim=Turtle()
screen = Screen()

tim.speed("fastest")

screen.listen()
screen.onkey(forward,"w")
screen.onkey(backward,"s")
screen.onkey(clockwise,"d")
screen.onkey(anti_clockwise,"a")
screen.onkey(clear,"c")

screen.exitonclick()
