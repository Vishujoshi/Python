from turtle import Turtle
with open("E:/Python/Day24/SnakeGame3.0/data.txt" , mode="r") as file:
     highscore=file.read()
class Scoreboard(Turtle):
    def __init__(self) :
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.score=0
        self.high_score=int(highscore)
        self.update_score()
        

    def update_score(self):
        self.clear()
        
        self.write(f"Score : {self.score} High Score: {self.high_score}",move=False, align='center', font=('Arial', 20, 'normal'))
    
    def reset(self):
         if self.score>self.high_score:
              self.high_score=self.score
              with open("E:/Python/Day24/SnakeGame3.0/data.txt" , mode="w") as file:
                file.write(f"{self.score}")
         self.score=0
         self.update_score()
         


    def keep_score(self):
            self.score+=1
            # self.clear()
            self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",move=False, align='center', font=('Arial', 20, 'normal'))