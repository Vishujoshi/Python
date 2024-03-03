
import turtle
import random
from turtle import Turtle,Screen
turtle.colormode(255)
# Extract 6 colors from an image.
# colors = colorgram.extract("E:/Python/Day18/hirst painting challenge/pic.jpg", 10)
# # print(colors)
# rgb=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     newcolor=(r,g,b)
#     rgb.append(newcolor)

# print(rgb)
color_list=[  (237, 245, 240), (212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40)]
def moveforward():
    my_turtle.forward(10)
def movebackward():
    my_turtle.backward(10)

def moveclockwise():
    my_turtle.right(10)

def moveanticlockwise():
    my_turtle.left(10)

def clear():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()

my_turtle=Turtle()

    
my_screen=Screen()
my_screen.listen()
my_screen.onkey(key="w",fun=moveforward)
my_screen.onkey(key="s",fun=movebackward)
my_screen.onkey(key="a",fun=moveanticlockwise)
my_screen.onkey(key="d",fun=moveclockwise)
my_screen.onkey(key="c",fun=clear)
my_screen.exitonclick()