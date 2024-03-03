from art import logo
import art
from game_data import data
from random import randint
import os
clear = lambda: os.system('cls')

def random_no_gen():
 randoma=randint(0,len(data)-1)
 return randoma

def compare_followers(one,two):
 if one > two:
  return "A"
 else:
   return "B"
print(logo)
random_one=random_no_gen()
random_two=random_no_gen()
ramdom_list=[random_one,random_two]
print(ramdom_list)
print(data[ramdom_list[0]]["name"])
user_answer="A"
compare_result="A"
score=0
while user_answer == compare_result:
    
    print(f"Compare A : {data[ramdom_list[0]]["name"]}, a {data[ramdom_list[0]]["description"]}, from {data[ramdom_list[0]]["country"]}")
    print(art.vs)
    print(f"Against B : {data[ramdom_list[1]]["name"]}, a {data[ramdom_list[1]]["description"]}, from {data[ramdom_list[1]]["country"]}")
    user_answer=input("Who has more followers? Type 'A' or 'B': ")
    compare_result=compare_followers(data[ramdom_list[0]]["follower_count"],data[ramdom_list[1]]["follower_count"])
    if user_answer == compare_result:
        score+=1
        clear()
        print(logo)
        print(f"You're right! Current score: {score}.")
        ramdom_list.remove(ramdom_list[0])
        
        # my logic 
        # if user_answer=="A":
        #     ramdom_list.remove(ramdom_list[0])
        # else:
        #     ramdom_list.remove(ramdom_list[1])
        ramdom_list.append(random_no_gen())
    else:
        
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")





# from game_data import data
# import random
# from art import logo, vs
# from replit import clear

# def get_random_account():
#   """Get data from random account"""
#   return random.choice(data)

# def format_data(account):
#   """Format account into printable format: name, description and country"""
#   name = account["name"]
#   description = account["description"]
#   country = account["country"]
#   # print(f'{name}: {account["follower_count"]}')
#   return f"{name}, a {description}, from {country}"

# def check_answer(guess, a_followers, b_followers):
#   """Checks followers against user's guess 
#   and returns True if they got it right.
#   Or False if they got it wrong.""" 
#   if a_followers > b_followers:
#     return guess == "a"
#   else:
#     return guess == "b"


# def game():
#   print(logo)
#   score = 0
#   game_should_continue = True
#   account_a = get_random_account()
#   account_b = get_random_account()

#   while game_should_continue:
#     account_a = account_b
#     account_b = get_random_account()

#     while account_a == account_b:
#       account_b = get_random_account()

#     print(f"Compare A: {format_data(account_a)}.")
#     print(vs)
#     print(f"Against B: {format_data(account_b)}.")
    
#     guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#     a_follower_count = account_a["follower_count"]
#     b_follower_count = account_b["follower_count"]
#     is_correct = check_answer(guess, a_follower_count, b_follower_count)

#     clear()
#     print(logo)
#     if is_correct:
#       score += 1
#       print(f"You're right! Current score: {score}.")
#     else:
#       game_should_continue = False
#       print(f"Sorry, that's wrong. Final score: {score}")

# game()

# '''

# FAQ: Why does choice B always become choice A in every round, even when A had more followers? 

# Suppose you just started the game and you are comparing the followers of A - Instagram (364k) to B - Selena Gomez (174k). Instagram has more followers, so choice A is correct. However, the subsequent comparison should be between Selena Gomez (the new A) and someone else. The reason is that everything in our list has fewer followers than Instagram. If we were to keep Instagram as part of the comparison (as choice A) then Instagram would stay there for the rest of the game. This would be quite boring. By swapping choice B for A each round, we avoid a situation where the number of followers of choice A keeps going up over the course of the game. Hope that makes sense :-)

# '''



# # Generate a random account from the game data.

# # Format account data into printable format.

# # Ask user for a guess.

# # Check if user is correct.
# ## Get follower count.
# ## If Statement

# # Feedback.

# # Score Keeping.

# # Make game repeatable.

# # Make B become the next A.

# # Add art.

# # Clear screen between rounds.

