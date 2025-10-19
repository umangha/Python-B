from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5 # Starting speed of cars
MOVE_INCREMENT = 10 # Increasing the speed of the cars each level
X_CORDINATES = 270


class CarManager(Turtle):
    def __init__(self): # Constructor of CarManager
        super().__init__() # Calling the parent class Turtle
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=2)
        # Choosing randomly from the colors
        color = random.choice(COLORS)
        self.color(color)
        self.x_cordinates = X_CORDINATES
        self.y_cordinates = random.randint(-230,230)
        self.penup() # No to drawing
        self.setheading(180) # Face towards the left side
        self.goto(self.x_cordinates , self.y_cordinates)


    def move_forward(self):
        '''Move the Car forward'''
        self.forward(STARTING_MOVE_DISTANCE)
    
