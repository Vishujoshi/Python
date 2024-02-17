import random

names_string="Vishal, berlin, Aman, rahul, rajat"

names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
random_int=random.randint(0,len(names)-1)

print(f"{names[random_int]} is going to buy the meal today! ")