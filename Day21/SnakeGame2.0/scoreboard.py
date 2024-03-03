from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) :
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.score=0
        self.update_score()
        

    def update_score(self):
        
        self.write(f"Score : {self.score}",move=False, align='center', font=('Arial', 20, 'normal'))

    def keep_score(self):
            self.score+=1
            self.clear()
            self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",move=False, align='center', font=('Arial', 20, 'normal'))