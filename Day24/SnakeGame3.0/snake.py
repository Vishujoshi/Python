import turtle

from turtle import Turtle
import time
positions=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
     

    def __init__(self) :
       
        self.tutle_list=[]
        self.make_snake()
        self.head=self.tutle_list[0]


    
                

    def make_snake(self):
        
        for i in positions:
            self.add_turtle(i)
            
            
    
    def add_turtle(self,position):
            new_turtle=Turtle()
            new_turtle.penup()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.goto(position)
            self.tutle_list.append(new_turtle)
    # move()

    def extend(self):
        self.add_turtle(self.tutle_list[-1].position())
        
    def reset(self):
        for tutle in self.tutle_list:
            tutle.goto(1000,1000)
        self.tutle_list.clear()
        self.make_snake()
        self.head=self.tutle_list[0]
    # myscreen.onkey(key="space",fun=move)
    def move(self):
        for i in range(len(self.tutle_list)-1,0,-1):
            new_x=self.tutle_list[i-1].xcor()
            new_y=self.tutle_list[i-1].ycor()
            self.tutle_list[i].goto(new_x,new_y)
        self.head.forward(20)
        
    def move_left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

    def move_up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)


    def move_down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)









