import colorgram
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
my_turtle=Turtle()
my_turtle.hideturtle()
my_turtle.penup()

my_turtle.setheading(225)
my_turtle.forward(300)
my_turtle.setheading(0)
# print(my_turtle.pos())
my_turtle.speed("fastest")
y=-212.13
for i in range (10):
    
    for j in range (10):
        # my_turtle.pensize(8)
        # my_turtle.pencolor(random.choice(color_list))
        my_turtle.dot(20,random.choice(color_list))
        my_turtle.penup()
        my_turtle.forward(50)
        my_turtle.pendown()
        
    y+=50
    my_turtle.penup()
    my_turtle.setpos(-212.13,y)
    my_turtle.pendown()
    
my_screen=Screen()
my_screen.exitonclick()