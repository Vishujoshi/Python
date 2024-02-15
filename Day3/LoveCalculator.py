# 💪 This is a difficult challenge! 💪
# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs.

# Then check for the number of times the letters in the word LOVE occurs.

# Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is *x*, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:

# "Your score is *y*, you are alright together."
# Otherwise, the message will just be their score. e.g.:

# "Your score is *z*."
# e.g.

# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# T occurs 0 times

# R occurs 1 time

# U occurs 2 times

# E occurs 2 times

# Total = 5

# L occurs 1 time

# O occurs 0 times

# V occurs 0 times

# E occurs 2 times

# Total = 3

# Love Score = 53

# Print: "Your score is 53."



print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
both_name=name1 + name2
lower_both_name=both_name.lower()
t=lower_both_name.count("t")
r=lower_both_name.count("r")
u=lower_both_name.count("u")
e=lower_both_name.count("e")

first_digit=t+r+u+e

l=lower_both_name.count("l")
o=lower_both_name.count("o")
v=lower_both_name.count("v")
e=lower_both_name.count("e")

second_digit=l+o+v+e

score=str(first_digit)+str(second_digit)
final_score=int(score)
if final_score<10 or final_score>90 : 
 print(f"Your score is {score}, you go together like coke and mentos.")
elif final_score >40 and final_score<50:
 print(f"Your score is {score}, you are alright together.")
else:
 print(f"Your score is {score}.")