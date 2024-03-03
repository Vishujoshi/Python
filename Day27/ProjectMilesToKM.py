from tkinter import *

window=Tk()
window.title("Mile To KM Coverter")
window.minsize(width=400,height=100)
window.config(padx=100,pady=50)
input=Entry()
input.grid(row=2,column=3)

mile_label=Label(text="Miles")
mile_label.grid(row=2,column=4)
is_equal_lable=Label(text="is equal to")
is_equal_lable.grid(row=3,column=2)

zero_label=Label(text="0")
zero_label.grid(row=3,column=3)


KM_label=Label(text="KM")
KM_label.grid(row=3,column=4)
def cal():
    km=float(input.get())*1.6
    zero_label.config(text=f"{km}")
cal_but=Button(text="Calculate",command=cal)
cal_but.grid(row=4,column=3)
window.mainloop()