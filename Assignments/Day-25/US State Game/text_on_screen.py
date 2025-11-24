from turtle import Turtle

FONT = ("Arial", 5, "bold")

class StateName(Turtle):
    def __init__(self):
        self.turtle = Turtle(visible=False) # Make the turtle invisible
        self.turtle.speed("fastest")
    
    def text_at_xy(self,x,y,text):
        '''At the x and y cordinates show the text'''
        self.turtle.penup() # Stop drawing that line
        self.turtle.goto(x,y)
        self.turtle.write(text,font=FONT)

