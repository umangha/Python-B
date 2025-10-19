import random
import turtle as t
# import colorgram

# # colorgram.extract(image, number_of_colors)
# colors = colorgram.extract(r'C:\Users\Yujan\OneDrive\Desktop\do\python\Angela Yu\Python Practice\Assignments\Day18\extract_color\p.jpg', 20)

# rgb_list = []
# # Extracting and making the tuple (r,g,b) in list
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_list.append((r,g,b))

# # Obtained list
# print(rgb_list)

# The Color list rgb value
# Remove the first few (r,g,b) combination cause they white background of pic
color_list = [ (219, 153, 107), (133, 171, 195), (222, 72, 88), (215, 131, 149), (24, 119, 152), (241, 208, 98), (121, 177, 149), (38, 119, 84), (20, 165, 204), (219, 83, 76), (140, 86, 62), (131, 83, 102), (175, 185, 215), (21, 168, 123), (161, 209, 166), (174, 154, 74)]

def random_color():
    """Returns a random tuple (r,g,b) of color """
    color = random.choice(color_list)
    print(color)
    return color

def painting():
    """Creates the dotted picture painting"""
    # SIze of dot
    radius = 20
    gap = 50.0
    tim.speed("fastest")
    initial_x_coordinate = tim.xcor()
    for _ in range(10):
        for _ in range(10):
            # Moving the turtle's center towards right side
            updated_x_coordinate = tim.xcor() +  gap
            tim.penup()
            tim.setx(updated_x_coordinate)
            # Random color obtained
            color_obtained = random_color()
            # Set the fill color
            tim.fillcolor(color_obtained)

            tim.pendown()
            
            # start the filling color 
            tim.begin_fill() 

            # Setting the boundary color
            tim.color(color_obtained)
            
            # Drawing the circle
            tim.circle(radius)
            
            # ending the filling of the color
            tim.end_fill() 

            tim.penup()

        # Moving the turtle's center upwards
        y_coordinate = tim.ycor() + gap
        tim.sety(y_coordinate)

        # Resetting the turtle's x-coordinate
        tim.setx(initial_x_coordinate)
            
# 10x10 row of color
# size of dot = 20 and size of space between dot =50

# Object creation of Turtle()
tim = t.Turtle()
# Screen() Object
screen = t.Screen()

# Setting the screen color-mode
screen.colormode(255)

TURTLE_SIZE = 20
# Setting the starting position
tim.penup()
tim.setpos(TURTLE_SIZE/2 - screen.window_width()/2, TURTLE_SIZE/2 - screen.window_height()/2)
tim.pendown()

# Create a circle
painting()


# Exit the drawing interface after a mouse click
screen.exitonclick()
