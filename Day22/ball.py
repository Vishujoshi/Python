from turtle import Turtle

class Ball(Turtle):
    def __init__(self) :
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1 ,stretch_wid=1)
        self.x=10
        self.y=10
        self.speed=0.1

    def move(self):
        newx=self.xcor()+self.x
        newy=self.ycor()+self.y
        self.goto(newx,newy)
    
    def bounce_y(self):
        self.y*=-1
        
    def bounce_x(self):
        self.x*=-1
        self.speed*=0.9

    def reset(self):
        self.goto(0,0)
        self.speed=0.1
        self.bounce_x()
        