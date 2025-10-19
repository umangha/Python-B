from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Turn the animation for the Snake Segments moving off
screen.tracer(0)

## What I need? 3 turtles lined up together
snake = Snake()
# Initializing the food
food = Food()

# Initializing the Scoreboard
scoreboard = Scoreboard()


## Snake Movement
# Waits for the key press from keyboard
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# Track Game 
game_on = True

while game_on:
    # Turns the animation back on
    screen.update()

    # Importing the time module to get the little lag animation for the snake movement
    time.sleep(0.1)
    snake.move()

    ## Collision Detection
    # distance() takes either a instance of turtle AKA another turtle or the X,Y value and gives how much distance is between them
    if snake.head.distance(food) < 15:
        food.refresh()

        ## Extend the Snake
        scoreboard.updatescore()

        ## Increase the Snake length
        snake.extend()
    
    ## Check Collision Detection with wall
    if (snake.head.xcor() > 295 or snake.head.xcor() <-295) or (snake.head.ycor() > 295 or snake.head.ycor() < -295):
        game_on = False
        scoreboard.gameover()
    
    ## Detect Collision with any segment of the snake
    ## CONCEPT : Loop through the segment list of the Snake Object if anything has similar distance to the head of the snake then the game is over.

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.gameover()

screen.exitonclick()
