from turtle import Turtle
from random import randint
import random
color=["red","green","yellow","blue","brown","pink"]
class Food(Turtle):
    def __init__(self) :
        super().__init__()
        self.shape("circle")
        self.penup()
        
        self.color(random.choice(color))
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.refresh()

    def refresh(self):
        x=randint(-280,280)
        y=randint(-280,280)
        self.goto(x,y)
        