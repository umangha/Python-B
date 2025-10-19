import random
import turtle as t

def rand_color():
    """Returns Tuple of RGB random color combo"""
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def make_spirograph(gap_size):
    """Takes the gap_size or the angle to make a spirograph"""

    radius=100
    # Speed of drawing
    kachuwa.speed("fastest")
    
    # here the gap is between the circles and it stops after the required number of gaps has been made so it is used in for loop (360/gap_size)
    for i in range(int(360/gap_size)):
        kachuwa.color(rand_color())
        kachuwa.circle(radius)
        # heading() -> Which direction it is pointing towards
        # setheading() -> change the heading
        kachuwa.setheading(kachuwa.heading()+gap_size)

# Making turtle and screen object
kachuwa = t.Turtle()
screen = t.Screen()

# Setting the colormode to accept rgb
screen.colormode(255)

# Calling the main function
make_spirograph(5)

# Doesnot exit till clicked
screen.exitonclick()
