from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score
# def move_up():
#    new_y=paddle.ycor() + 20
#    paddle.goto(paddle.xcor(),new_y) 
    
# def move_down():
#    new_y=paddle.ycor() - 20
#    paddle.goto(paddle.xcor(),new_y)   
screen=Screen()
screen.tracer(0)
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball =Ball()
score=Score()

# paddle=Turtle("square")

# paddle.color("white")
# paddle.shapesize(stretch_wid=5,stretch_len=1)
# paddle.penup()
# paddle.goto(350,0)
screen.listen()
screen.onkeypress(key="Up",fun=r_paddle.move_up)
screen.onkeypress(key="Down",fun=r_paddle.move_down)
screen.onkeypress(key="w",fun=l_paddle.move_up)
screen.onkeypress(key="s",fun=l_paddle.move_down)
# screen.onclick(ball.move,btn=1,add=True)
game_on=True

while game_on:
   time.sleep(ball.speed)
   screen.update()
   ball.move()
   

   if ball.ycor()> 280 or ball.ycor() < -280:
      ball.bounce_y()

   if ball.distance(r_paddle)<50 and ball.xcor()>320  or ball.distance(l_paddle)<50 and ball.xcor()<-320 :
      ball.bounce_x()

   if ball.xcor()>380:
        ball.reset()
        score.l_point()
   
   if ball.xcor()<-380:
      ball.reset()
      score.r_point()




screen.exitonclick()