from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
DIRECTION = 90 # Facing NORTH (UP)


class Player(Turtle): # Inheriting the Turtle Class
    def __init__(self): # Constructor method
        super().__init__() # Calling the constructor method of Paren Turtle Class
        self.shape("turtle")
        self.color("white")
        self.seth(DIRECTION) # Make the Turtle Face UP
        self.penup() # Stop Drawing the line
        self.go_to_start_pos()
    
    def go_to_start_pos(self):
        '''Turtle goes to the starting position'''
        self.goto(STARTING_POSITION)
    
    def move(self):
        '''Make the turtle move UP'''
        # new_y = self.ycor() + MOVE_DISTANCE
        # # Check if the turtle reached the finish line
        # if new_y >= FINISH_LINE_Y:
        #     self.start_pos()
        # else:
        #     # Move the turtle to the new position
        #     self.goto(self.xcor(),new_y)
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
