import random
import os
cls = lambda: os.system('cls')
# def choose_rand_no():
#     randInt=random.randint(1,100)
#     return randInt


print("Welcome to the numuber Guessing Game")
print("I am thinking a number between 1 to 100.")
cls
# print(f"I choose {choose_rand_no()}")

change=0
def check(num,rand_no):
    if num>rand_no:
        print("Too high")
    elif num<rand_no:
        print("Too low")
    else:
        global change
        change=1
        print(f"{num} is correct. You won!")



def play_game():
    randInt=random.randint(1,100)
    print(randInt)
    difficulty=input("Choose a difficulty level -Type e for east and h for hard : ")
    if difficulty=="e":
        attempts=10
        print(f"you have {attempts}  attempts left")
        while attempts>0 :
            guess=int(input("Guess a number : "))
            attempts-=1
            check(guess,randInt)
            if change==1:
                attempts=0
            else:
                if attempts==0:
                    print(f"Game Over! Better luck Next time")
                else:
                    print(f"you have {attempts}  attempts left")
                    
            
    else:
        attempts =5
        print(f"you have {attempts} attempts left")
        while attempts>0 :
            guess=int(input("Guess a number : "))
            attempts-=1
            check(guess,randInt)
            if change==1:
                attempts=0
            else:
                if attempts==0:
                    print(f"Game Over! Better luck Next time")
                else:
                    print(f"you have {attempts}  attempts left")

play_game()
cls
more_play=input("Do you want to play again ? type y for yes , no for no :")
if more_play=="y":
    cls
    play_game()
else:
    cls
    print("Goodbye!")