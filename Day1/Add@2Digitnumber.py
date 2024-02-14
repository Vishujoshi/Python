two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇

# type(two_digit_number)
s=0
r=int(two_digit_number) % 10
a=int(two_digit_number) / 10
s=a+r
print(int(s))

# Or 

two_digit_number = input()

# string[0] function is used locate the character at place 0
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# Add the two integers together
two_digit_number = first_digit + second_digit

print(two_digit_number)