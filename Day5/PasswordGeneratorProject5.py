import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
str=""

for i in range(0,nr_letters):
    random_letters=random.randint(0,len(letters)-1)
    str=str + letters[random_letters]
for i in range(0,nr_symbols):
    random_symbols=random.randint(0,len(symbols)-1)
    str=str + symbols[random_symbols]
for i in range(0,nr_numbers):
    # 2nd method to select random number from list 
    str=str + random.choice(numbers)
# print(str)


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
  
# passlist=list(str.strip(""))
# Covert string to a list ----------------IIIIIIIMMMMMMMPPPPPPPPPPPTTTTTTTTTTT
passlist=list(str)

# // or we can use the method above to shuffle-------------------IIIIIIIMMMMMMMPPPPPPPPPPPTTTTTTTTTTT
random.shuffle(passlist)
# print(passlist)
# covert list to string----------------IIIIIIIMMMMMMMPPPPPPPPPPPTTTTTTTTTTT
password=""
for i in passlist:
    password=password + i

# print(password)
print(f"Your password Is {password}")