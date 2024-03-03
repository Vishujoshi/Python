import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player=Player()
car=CarManager()
score=Scoreboard()    

screen.onkey(key="Up",fun=player.move_forward)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.gen_cars()
    car.move_cars()
    
    for i in car.all_cars:
        if i.distance(player) < 20:
            
            score.game_over()
            game_is_on=False

    if player.is_at_final_postion():
        player.go_to_start()
        car.level_up()
        score.increase_level()
   

screen.exitonclick()