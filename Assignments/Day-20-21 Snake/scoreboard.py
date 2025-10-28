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

        # Opening the highscore from the file `data.txt`
        with open("data.txt") as save_data:
            self.highscore = int(save_data.read()) 
        
        # self.penup()
        self.displayscore()
      
    def displayscore(self):
        """Display the Scoreboard at the top of the screen """
        self.clear()
        self.goto(DISPLAY_COR)
        self.color(COLOR)
        self.write(f"Score : {self.score} High Score: {self.highscore}",align=ALIGN,font=FONT)
        self.hideturtle()

    def updatescore(self):
        """ Update the Score of the Snake"""
        self.score+=1
        self.displayscore()
    
    # def gameover(self):
    #     self.goto(CENTER)
    #     self.write("Game Over",align=ALIGN,font=FONT)

    def reset_score(self):
        # Keeping track of highscore
        if self.score > self.highscore:
            self.highscore = self.score
        # Resetting the current score
        self.score = 0
        self.save_highscore()
        self.displayscore()

    def save_highscore(self):
        with open("data.txt",mode="w") as save_data:
            save_data.write(str(self.highscore))
        
