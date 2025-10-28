from turtle import Turtle

# Creating a Tuple for the initial cordinates
INITIAL_CORDINATES=[(0.0,0.0),(-20.0,0.0),(-40.0,0.0)]

# The distance travelled by snake in one move
MOVE_DISTANCE = 20

# Direction
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    """Creates the Snake Body"""
    def __init__(self):
        '''Create Initial 3 segments of the snake'''
        self.segments=[]
        self.create_snake()
        # Holds the head of the snake
        self.head = self.segments[0]
    
    def create_snake(self):
        """Create the Default Snake with 3 segments"""
        for cor in INITIAL_CORDINATES:
            self.add_segments(cor)
            
    
    def add_segments(self,position):
        """Adds a Segment in the Snake(list) takes the position(coordinates) as argument"""
        new_segments= Turtle(shape="square")
        new_segments.color("white")
        # Saying no to the line of the turtle(segment of snake here)
        new_segments.penup()
        # turtle.goto(accepts tuple)
        new_segments.goto(position)
        # INFO: Appending to the segments List()
        self.segments.append(new_segments)

    def extend(self):
        """Use the Tail of the snake position to add a new Position"""
        # turtle.position() returns current(x,y) position in tuple
        self.add_segments(position=self.segments[-1].position())

    def move(self):
        """Move the snake forward by 20"""
        for seg_num in range(len(self.segments)-1,0,-1):
            # IDEA -> Copy the 2nd segment coordinates into 3rd to give illusion of moving 3->2->1
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(x=new_x,y=new_y)

        # 1st segment is always needed to move forward
        self.head.forward(MOVE_DISTANCE)

    # Condition You Cannot Move the head direction in opposite side directly
    def up(self):
        '''Set the turtle head in Up direction = 90 deg '''
        # IF the currect direction of the head i = DOWN(270) then no UP allowed
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        '''Set the turtle head in Down direction = 270 deg '''
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        '''Set the turtle head in left direction = 180deg '''
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        '''Set the turtle head in right direction = 0deg '''
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        '''Snake reset after adding highscore'''
        # To remove the prev snake from the screen
        for seg in self.segments:
            seg.goto(1000,1000)
        
        self.segments.clear() # Empty the list
        self.create_snake()
        # Holds the head of the snake
        self.head = self.segments[0]
