from turtle import Turtle



class Paddle(Turtle):
    def __init__(self,cor):
        super().__init__() # Call the parent class initializer
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5) # Stretch to make it a rectangle(100,20)
        self.penup()
        self.goto(cor)

    def go_up(self):
        '''When Up Key(R) W key(L) is Hit'''
        # Move 20 up direction
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def go_down(self):
        '''When Down Key(R) S key(L) is Hit'''
        # Move 20 down direction
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)
        

