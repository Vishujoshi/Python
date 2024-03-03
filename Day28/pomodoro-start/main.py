from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep=0
timer=0
mark=""
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canva.itemconfig(time_text,text="00:00")
    check_lable.config(text="")
    title_lable.config(text="Timer")
    global rep 
    rep=0
    global mark
    mark=""
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep
    long_breakC=LONG_BREAK_MIN*60
    shortBreakC=SHORT_BREAK_MIN*60
    WorkMINC=WORK_MIN*60
    rep+=1
    global mark
    if rep%8==0:
        countdown(long_breakC)
        title_lable.config(text="Long Break",fg=RED)
        mark+="✔️"
            
        check_lable.config(text=mark)
    elif rep%2==0:
        countdown(shortBreakC)
        title_lable.config(text="Break",fg=PINK)
        mark+="✔️"
            
        check_lable.config(text=mark)
    else:   
        countdown(WorkMINC)
        title_lable.config(text="Work",fg=GREEN)
        
        
        
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    min=math.floor(count/60)
    if min<10:
        min=f"0{min}"
    sec=count%60
   
    if sec<10:
        sec=f"0{sec}"
    canva.itemconfig(time_text, text=f"{min}:{sec}")
    
    if count>0:
        global timer
        timer=window.after(10,countdown,count-1)
    else:
        start_timer()
        
        # mark=""
        # work_session=math.floor(rep/2)
        # for i in range(work_session):
        #     mark+="✔️"
            
        # check_lable.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)


title_lable=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,34,"bold")  )
title_lable.grid(row=0,column=1)
canva=Canvas(width=200,height=224 , bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="E:/Python/Day28/pomodoro-start/tomato.png")
canva.create_image(100,112,image=tomato_img)
time_text=canva.create_text(100,132,text="00:00" ,font=(FONT_NAME,34,"bold") ,fill="white")
canva.grid(row=1,column=1)

start_btn=Button(text="Start",command=start_timer)
start_btn.grid(row=2,column=0)

reset_btn=Button(text="Reset",command=reset)
reset_btn.grid(row=2,column=2)

check_lable=Label(fg=GREEN,bg=YELLOW)
check_lable.grid(row=3,column=1)

window.mainloop()