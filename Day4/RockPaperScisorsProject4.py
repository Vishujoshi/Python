import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Lets play Rock paper Scissors")
user_input=input("Choose 1 for Rock, 2 for paper, 3 for scissors \n")
if user_input=="1":
 print(rock)
elif user_input=="2":
 print(paper)
else:
 print(scissors)

print("Computer Choose")
computer_choice=random.randint(1,3)
strCC=str(computer_choice)
print(computer_choice)

if strCC=="1":
 print(rock)
elif strCC=="2":
 print(paper)
else:
 print(scissors)

if user_input=="1" and strCC == "1" or user_input=="3" and strCC == "3" or user_input=="2" and strCC == "2" :
  print("draw")
elif user_input=="1" and strCC=="2" or user_input=="2" and strCC=="3" or user_input=="3" and strCC=="1":
 print("Computer Won!!!!")
else:
 print("You won!!!!")