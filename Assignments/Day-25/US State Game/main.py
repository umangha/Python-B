import turtle

screen = turtle.Screen()
screen.title("US States Game")

# File path for the image
image = "Assignments/Day-25/US State Game/blank_states_img.gif"

# Using this image as shape
screen.addshape(image)

# Image loaded in the shape of the picture provided
turtle.shape(image)

user_answer = screen.textinput(title="Guess the state",prompt="Enter the State's name: ")

print(user_answer)

screen.exitonclick()

