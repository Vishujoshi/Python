from turtle import Screen, Turtle
import turtle
import pandas
screen=Screen()
screen.addshape("E:/Python/Day25/us state game/blank_states_img.gif")
turle=Turtle()
turtle.shape("E:/Python/Day25/us state game/blank_states_img.gif")


def write_state(ans,user_ans):
    turle.hideturtle()
    turle.penup()
    
    turle.goto(int(ans.x),int (ans.y))
    turle.write(f"{user_ans}", move=False, align='left', font=('Arial', 8, 'normal'))


length=0
with open ("E:/Python/Day25/us state game/50_states.csv") as file:
    data=pandas.read_csv(file)
# ans=data[data.state==user_ans]
state_list=data.state.to_list()
guessed_states=[]
missing_sates=[]
while len(guessed_states)<len(state_list):
    user_ans=screen.textinput(title=f"{len(guessed_states)}/50 Correct State", prompt="What is the another state name")
    title_user_ans=user_ans.title()
    
    if title_user_ans=="Exit":
        missing_sates=[state for state in state_list if state not in guessed_states]
        # below for loops can be simplified by ablove list comprehension
        # for state in state_list:
        #     if state not in guessed_states:
        #         missing_sates.append(state)
        statetolearn=pandas.DataFrame(missing_sates)
        statetolearn.to_csv("statesTolearn.csv")
        break
    if title_user_ans in state_list:
        guessed_states.append(title_user_ans)
        ans=data[data.state==title_user_ans]
        write_state(ans,title_user_ans)

# print(type(ans.x))
    

# with open ("E:/Python/Day25/us state game/50_states.csv") as file:
#     data=pandas.read_csv(file)
# print(len(data.state))



# Below function to get screen cordinates on click
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()

# screen.exitonclick()