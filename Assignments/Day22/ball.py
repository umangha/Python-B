from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__() # Call the parent Class A.K.A Turtle class
        self.shape('circle')
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.penup() # To not draw
        self.ball_speed= 0.1 # Default
        # Default is (0,0) -> center
    
    def move(self):
        '''Moves the ball in x and y direction'''
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
    
    def bounce_y(self):
        '''When the Collision detection with Up or Down Wall changes the y-dir of ball'''
        self.y_move = self.y_move * -1

    def bounce_x(self):
        '''When the Collision detection with left or right paddle changes the x-dir of ball'''
        self.x_move = self.x_move * -1
        self.ball_speed *= 0.8 # Increase the speed of the ball lesser it is better but cannot be negative
    
    def reset_pos(self):
        '''Reset the ball to center and change ball direction'''
        # Ball goes to the center of the screen 
        self.goto(0,0)
        
        # Reset the ball speed to default
        self.ball_speed = 0.1

        # Reverse the direciton of the ball towards the scorer
        self.bounce_x()
        
        



        

