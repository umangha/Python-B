from turtle import Turtle
import random

# Making the Food class inherit the Turtle Clas
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        
        # Setting the size of turtle as 10x10
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")

        # Goto random point in screeen(600x600)
        self.refresh()
    
    def refresh(self):
        '''Refreshes the position of the food'''
        # Random x and y generating REMEMBER Screen size
        rand_x = random.randint(-280,280)
        rand_y = random.randint(-280,280)
        self.goto(rand_x,rand_y)
