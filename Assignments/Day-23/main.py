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
car_manager = CarManager()
scoreboard = Scoreboard()


# Catching the Up arrow key stroke of player
screen.listen()
screen.onkeypress(player.move,"Up")


game_is_on = True # Game Status

while game_is_on: # Looping till the game is ongoing
    time.sleep(0.1) # Slows the updating of turtles
    screen.update() # Updates the turtles according to new position

    car_manager.create_car() # Creates car
    car_manager.move_car()
    
    # Detect the collision with cars
    for car in car_manager.all_cars:
        # From the center checks the distance between 2 turtles
        if car.distance(player) < 20:
            scoreboard.gameover()
            game_is_on = False

    # Detect if the turtle reaches the top
    if player.is_at_finish_line():
        player.go_to_start_pos()
        car_manager.increase_car_speed()
        scoreboard.increase_level()

# Screen doesnot exits till a mouse click
screen.exitonclick()
