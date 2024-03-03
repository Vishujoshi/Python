
import turtle
import random
from turtle import Turtle,Screen
turtle.colormode(255)

color_list=[  (237, 245, 240), (212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40)]
speed_list=["fastest","fast","normal","slow","slowest" ]
turtle_color=["red","green","yellow","blue","brown","pink"]
my_screen=Screen()
my_screen.setup(width=500,height=400)
y_cor=[-70,-40,-10,20,50,80]
tutle_list=[]
def make_turtle():
    
    for i in range (0,6):
        
        new_turtle=Turtle()
        new_turtle.penup()
        new_turtle.shape("turtle")
        new_turtle.color(turtle_color[i])
        new_turtle.setpos(-230,y_cor[i])
        tutle_list.append(new_turtle)
make_turtle()

user_choice=turtle.textinput("Make a bet", "Which color frog will win?" )
if user_choice:
     
     is_on = True

while is_on:
        
        for turtle in tutle_list:
            if turtle.xcor()>230:
                is_on=False
                winning_turtle=turtle.pencolor()
                if winning_turtle==user_choice:
                    print(f"You won! {winning_turtle} won the race"  )
                else:
                     print(f"You lost! {winning_turtle} won the race"  )
            
            turtle.forward(random.randint(0,10))    



# def race():
    
#     for i in range (50):
#         my_turtle2.pendown()
#         my_turtle1.pendown()
#         my_turtle.pendown()
#         my_turtle.speed(random.choice(speed_list))
#         my_turtle1.speed(random.choice(speed_list))
#         my_turtle2.speed(random.choice(speed_list))
#         my_turtle2.forward(10)
#         my_turtle1.forward(10)
#         my_turtle.forward(10)
# my_turtle=Turtle()
# my_turtle1=Turtle()

# my_turtle2=Turtle()

# my_turtle1.shape("turtle")
# my_turtle.shape("turtle")
# my_turtle2.shape("turtle")
# my_turtle1.color("red")
# my_turtle.color("green")
# my_turtle1.color("blue")
# my_turtle.penup()
# my_turtle2.penup()
# my_turtle1.penup()
# my_turtle.setpos(-100,0)
# my_turtle1.setpos(-100,30)
# my_turtle2.setpos(-100,60)
# race()



my_screen.exitonclick()