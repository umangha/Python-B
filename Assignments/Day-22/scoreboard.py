from turtle import Turtle

LEFT_SCOREBOARD_POS = (-100,200)
RIGHT_SCOREBOARD_POS = (100,200)

class Scoreboard(Turtle):
    def __init__(self): # Initialize the current class
        super().__init__() # Inherit the parent class
        self.color("white")
        self.penup() # Do not write while moving
        self.hideturtle() # Hides the shape of the turtle
        self.l_score =0 # Left player score
        self.r_score =0 # Right Player score
        self.update_scoreboard() 
    
    def update_scoreboard(self):
        '''Updates the score'''
        self.clear() # overrides the previous score needed because of the overriding of score problem
        self.goto(LEFT_SCOREBOARD_POS) # Shows the score of left player
        self.write(self.l_score,align="center",font=("Courier",80,"normal")) # Writes the score

        self.goto(RIGHT_SCOREBOARD_POS) # Shows the score of right player
        self.write(self.r_score,align="center",font=("Courier",80,"normal")) # Writes the score

    def update_l_score(self):
        '''Update the Left player scores'''
        self.l_score += 1
        self.update_scoreboard()
    
    def update_r_score(self):
        '''Update hte right player scores'''
        self.r_score +=1
        self.update_scoreboard()
