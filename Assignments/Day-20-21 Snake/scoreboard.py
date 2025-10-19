from turtle import Turtle

CENTER = (0,0)
DISPLAY_COR = (0,270)
ALIGN = "center"
COLOR= "white"
FONT = ("Arial", 16, "normal")
class Scoreboard(Turtle):
    """ Tracking the score of the snake"""
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.penup()
        self.displayscore()
      
    def displayscore(self):
        """Display the Scoreboard at the top of the screen """
        self.clear()
        self.goto(DISPLAY_COR)
        self.color(COLOR)
        self.write(f"Score :{self.score}",align=ALIGN,font=FONT)
        self.hideturtle()

    def updatescore(self):
        """ Update the Score of the Snake"""
        self.score+=1
        self.displayscore()
    
    def gameover(self):
        self.goto(CENTER)
        self.write("Game Over",align=ALIGN,font=FONT)
