import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("Trtle Crossing Game")
screen.setup(width=600, height=600) # Sets the screen width and height
screen.tracer(0) # Stops the animation

# Initializing the player and car
player = Player()
car = CarManager()



# Catching the Up arrow key stroke of player
screen.listen()
screen.onkeypress(player.move,"Up")


game_is_on = True # Game Status

while game_is_on: # Looping till the game is ongoing
    time.sleep(0.1) # Slows the updating of turtles
    screen.update() # Updates the turtles according to new position 

    car.move_forward()
