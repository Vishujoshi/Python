import turtle
from snake import Snake
from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard
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

myscreen.listen()
myscreen.onkey(key="Up" , fun=my_snake.move_up)
myscreen.onkey(key="Down" , fun=my_snake.move_down)
myscreen.onkey(key="Left" , fun=my_snake.move_left)
myscreen.onkey(key="Right" , fun=my_snake.move_right)  

food=Food()
board=Scoreboard()


game_on=True
while game_on:
     myscreen.update()
     time.sleep(0.1)
     my_snake.move()
     if my_snake.head.distance(food)<17:
          food.refresh()
          my_snake.extend()
          # board.keep_score()
          board.keep_score()
     # if abs(my_snake.head.xcor()) > 280 or abs(my_snake.head.ycor()) > 280:    
          # ----Or-----
     if my_snake.head.xcor() > 290 or my_snake.head.xcor() < -290 or my_snake.head.ycor() > 290 or my_snake.head.ycor() < -290 :
          # board.game_over()
          # game_on=False
          my_snake.reset()
          board.reset()
     
     # for tutle in my_snake.tutle_list:
     #      if tutle==my_snake.head:
     #           pass
     #      elif my_snake.head.distance(tutle) < 10:
     #           board.game_over()
     #           game_on=False
     # -------------Same thing using slicing
     for tutle in my_snake.tutle_list[1:]:
          
          if my_snake.head.distance(tutle) < 10:
               my_snake.reset()
               board.reset()









myscreen.exitonclick()