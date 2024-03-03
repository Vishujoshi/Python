COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random
class CarManager:
    def __init__(self) :
        
        self.all_cars=[]
        self.car_speed =STARTING_MOVE_DISTANCE

    def gen_cars(self):
        randomdigit=random.randint(0,6)
        if randomdigit == 1:
            newcar=Turtle()
            newcar.shape("square")
            newcar.penup()
            newcar.shapesize(stretch_len=2,stretch_wid=1)
            newcar.color(random.choice(COLORS))
            newcar_y=random.randint(-250,250)
            newcar.goto(300,newcar_y)
            self.all_cars.append(newcar)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT