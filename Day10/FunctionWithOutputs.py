
import os
cls = lambda: os.system('cls')
print("Welcome to line Formatter")
input_string=input("Enter your String in any format \n ")

def format_fun(string):
     cls()
     if string== "":
      return "you didnot provide valid inputs"
     formted_string=string.title()
     return formted_string

print(format_fun(input_string))