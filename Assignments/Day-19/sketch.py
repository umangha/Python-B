from turtle import Turtle, Screen

def move_forward():
    """Moves Turtle forward by 10steps """
    # moves the turtle forward by 20 steps
    tim.fd(10)

def move_backward():
    """Moves Turtle backward by 10steps """
    # moves the turtle backward by 20 steps
    tim.backward(10)

def clockwise():
    """Change the direction to Clockwise"""
    tim.right(30)


def counter_clockwise():
    """Change the direction to  Counter Clockwise"""
    tim.left(30)

def clear_screen():
    """Clear Turtle Screen"""
    # screen.reset()

    # Only Erases and resets this particular turtle
    tim.reset()

tim = Turtle()
screen = Screen()
tim.speed("fastest")

# Sets the focus on turtle screen
screen.listen()

# Key Listeners
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")

screen.onkeypress(clockwise,"d")
screen.onkeypress(counter_clockwise,"a")

screen.onkeypress(clear_screen,"c")
# Exit the screen on click
screen.exitonclick()
