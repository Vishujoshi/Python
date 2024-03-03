import turtle
from snake import Snake
from turtle import Turtle,Screen
import time
turtle.colormode(255)

myscreen=Screen()
myscreen.setup(width=600,height=600)
myscreen.bgcolor("black")
myscreen.title("Snake Game")
myscreen.tracer(0)
turtle_color=["red","green","yellow","blue","brown","pink"]
positions=[(0,0),(-20,0),(-40,0)]
tutle_list=[]
my_snake=Snake()


  


game_on=True
while game_on:
     myscreen.update()
     time.sleep(0.1)
     my_snake.move()
     myscreen.listen()
     myscreen.onkey(key="Up" , fun=my_snake.move_up)
     myscreen.onkey(key="Down" , fun=my_snake.move_down)
     myscreen.onkey(key="Left" , fun=my_snake.move_left)
     myscreen.onkey(key="Right" , fun=my_snake.move_right)









myscreen.exitonclick()