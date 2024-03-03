from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def genPass():
    nr_letters= random.randint(5,8)

    nr_symbols = random.randint(1,3)
    nr_numbers = random.randint(1,3)

    passletters=[random.choice(letters) for i in range(nr_letters)  ]
    passnums=[random.choice(numbers) for i in range(nr_numbers)  ]
    passsym=[random.choice(symbols) for i in range(nr_symbols)  ]

    passList=passletters+passnums+passsym
    random.shuffle(passList)
    password="".join(passList)


    # same below functionality can be achieved using join as above
    # password=""
    # for i in passList:
    #     password=password + i

    # print(password)
    pass_input.insert(0,password)
    # used to copy password automatically
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
content=""
def savePass():
    web=web_input.get()
    email=email_input.get()
    passwrd=pass_input.get()
    if len(web)==0 or len(passwrd)==0:
        messagebox.showinfo(title="Alert", message="Please make sure you have not left any fields empty")
    else: 
        isok=messagebox.askokcancel(title="Details",message=f"Confirm the entered details\n Website: {web} \n email: {email} \n Password : {passwrd}")
        if isok:
            content=web + "|" + email+ "|"+passwrd + "\n"
            with open("E:/Python/Day29/password-manager-start/passwords.txt",mode="a") as file:
                file.write(content)
                # to delete the input entry on screen after add button is pressed
                web_input.delete(0,END)
                pass_input.delete(0,END)
    

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=40,pady=40)

canva=Canvas(height=200,width=200 )
logo_img=PhotoImage(file="E:/Python/Day29/password-manager-start/logo.png")
canva.create_image(100,100,image=logo_img)
canva.grid(row=0,column=1,columnspan=2)
website_label=Label(text="Website: ")
website_label.grid(row=1,column=0)

web_input=Entry(width=40 )
# to show the curson pinging at input
web_input.focus()
web_input.grid(row=1,column=1,columnspan=2)

Email_lable=Label(text="Email/Username: ")
Email_lable.grid(row=2,column=0)
email_input=Entry(width=40)
email_input.insert(0,"vishal_vishi@yahoo.com")
email_input.grid(row=2,column=1,columnspan=2)

Pass_label_lable=Label(text="Password: ")
Pass_label_lable.grid(row=3,column=0)
pass_input=Entry(width=25)
pass_input.grid(row=3,column=1)

gen_btn=Button(text="Generate Password", command=genPass)
gen_btn.grid(row=3,column=2)

Add_btn=Button(text="Add",width=36,command=savePass)
Add_btn.grid(row=4,column=1,columnspan=2)



window.mainloop()