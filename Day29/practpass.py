
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= random.randint(8,10)

nr_symbols = random.randint(2,4)
nr_numbers = random.randint(2,4)

passletters=[random.choice(letters) for i in range(nr_letters)  ]
passnums=[random.choice(numbers) for i in range(nr_numbers)  ]
passsym=[random.choice(symbols) for i in range(nr_symbols)  ]

passList=passletters+passnums+passsym
random.shuffle(passList)




password=""
for i in passList:
    password=password + i

print(password)
# print(f"Your password Is {password}")