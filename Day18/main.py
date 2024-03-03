from turtle import Turtle,Screen
import random
import turtle
turtle.colormode(255)
my_turtle=Turtle()
my_turtle.shape("turtle")
my_turtle.color("lawn green")
my_turtle.pensize(1)
my_turtle.speed("fastest")
# my_turtle.forward(100)
# my_turtle.right(90)
# my_turtle.penup()
# my_turtle.pu()
# my_turtle.,up()
# my_turtle.forward(100)

def random_color():
    r=random.randint(0,255)
    b=random.randint(0,255)
    g=random.randint(0,255)
    rgb=(r,b,g)
    return rgb
# 2. Draw a dashed line
# for i in range(0,10):
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)
#     my_turtle.pendown()
    
    
# 1. draw a Square
# for i in range(0,4):
#     my_turtle.forward(10)
#     my_turtle.right(90)
color_list=["green yellow", "dark red","orange","magenta","indigo","red","blue"]
move_list=[0,90,180,270]
def draw_shape(side):
 
    for i in range (round(side)):
        my_turtle.forward(100)
        my_turtle.right(360/side)

def random_movement():
    my_turtle.forward(20)
    my_turtle.setheading(random.choice(move_list))
 
    
        
        


# for i in range(3,11):
#     my_turtle.pencolor(random.choice(color_list))
#     draw_shape(i)

# for i in range(300):
#     my_turtle.color(random_color())
#     random_movement()

def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        my_turtle.color(random_color())
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading()+size_of_gap)

draw_spirograph(5)
# my code for spirograph
# r = 100
# for i in range(100):
#     my_turtle.color(random_color())
#     my_turtle.circle(r)
#     my_turtle.right(10) 
    
    
    

my_screen=Screen()
my_screen.exitonclick()