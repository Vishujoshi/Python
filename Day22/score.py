from turtle import Turtle

class Score(Turtle):
    def __init__(self) :
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score=0
        self.r_score=0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100,250)
        self.write(f"{self.l_score}", move=False, align='center', font=('Arial', 34, 'normal'))
        self.goto(100,250)
        self.write(f"{self.r_score}", move=False, align='center', font=('Arial', 34, 'normal'))

    def l_point(self):
        self.l_score+=1
        self.update_score()
    
    def r_point(self):
        self.r_score+=1
        self.update_score()
