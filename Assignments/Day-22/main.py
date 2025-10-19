from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

LEFT_POSITION = (-350,0)
RIGHT_POSITION = (350,0)

screen = Screen()
screen.bgcolor("black")
## Setting the screen size
screen.setup(width=800,height=600)
## Change the Screen title
screen.title("PingPong")
# Animation is off
screen.tracer(0)

# Initializing the left and right paddle object
l_paddle = Paddle(LEFT_POSITION)
r_paddle = Paddle(RIGHT_POSITION)

# Initializing the Ball
ball = Ball()

# Initializing the scoreboard
scoreboard = Scoreboard()

# For the left paddle
screen.listen() # Listen for on key events
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

# For the right paddle 
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

## Required to turn on the animation (After turning off to tracer) if the game is still on 
game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed) # Required to show the moment of ball
    screen.update()
    ball.move()

    # Collision Detection with up and down wall
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()
    
    # Collision with the paddles
    if (ball.distance(l_paddle) < 50 and ball.xcor() <= -330) or (ball.distance(r_paddle) < 50 and ball.xcor() >=330):
        ball.bounce_x()
    
    # Condition if the ball becomes a goal
    # Left paddle misses
    if ball.xcor() <= -400:
        # Trying to change the direction of the ball towards the side of scorer
        ball.reset_pos()
        scoreboard.update_r_score()

    # Right Paddle misses
    if ball.xcor() >= 400:
        # Trying to change the direction of the ball towards the side of scorer
        ball.reset_pos()
        scoreboard.update_l_score()
        
        
        
screen.exitonclick()
