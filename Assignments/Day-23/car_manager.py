from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5 # Starting speed of cars
MOVE_INCREMENT = 10 # Increasing the speed of the cars each level
X_CORDINATES = 270


class CarManager():
    def __init__(self): # Constructor of CarManager
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE

    def create_car(self):
        '''Create a new car of random color at random y-cor'''
        #Creating a random var to stop creating 10 cars every second 
        random_chance= random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            # Choosing randomly from the colors
            color = random.choice(COLORS)
            new_car.color(color)
            # Creating where the car will be generated
            random_y=random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        '''Move Car in decreasing X-distance'''
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT



    
