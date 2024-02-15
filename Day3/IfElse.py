print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
# Note : Always make sure statement to be executed should be Inside the block else there will incendation error
if height >= 120 :
  print("You can ride the rollercoaster!")
else :
 print("You can't ride the rollercoaster!")


# To check Number Is even or not
 # Which number do you want to check?
number = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if number%2==0:
   print("This is an even number.")
else:
 print("This is an odd number.")




#  Nested If Else
 
 print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age=int(input("What is your age? "))
if height >= 120 :
  print("You can ride the rollercoaster!")
  if age < 18 : 
   print("Please pay $7.")
  else :
   print("Please pay $12.")
else :
 print("You can't ride the rollercoaster!")


 #  Nested If Elif else
 
 print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age=int(input("What is your age? "))
if height >= 120 :
  print("You can ride the rollercoaster!")
  if age < 12 : 
   print("Please pay $5.")
  elif age<=18 :
   print("Please pay $7.")
  else :
   print("Please pay $12.")
else :
 print("You can't ride the rollercoaster!")



# IF In succession In wants Photo 
 print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age=int(input("What is your age? "))
bill=0
if height >= 120 :
  print("You can ride the rollercoaster!")
  if age < 12 : 
   bill=5
   print("Please pay $5.")
  elif age<=18 :
   bill=7
   print("Please pay $7.")
  else :
   bill=12
   print("Please pay $12.")
  wants_photo=input("Do you want a photo taken? Y or N. ")
  if wants_photo=="Y" :
   bill+=3
   print(f"your final bill is {bill}$" )
else :
 print("You can't ride the rollercoaster!")