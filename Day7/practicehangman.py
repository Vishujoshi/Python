import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
words=["mouse","pig","dog","elephant", "cat", "tiger","Lizard", "insect", "spider", "donkey, monkey", "pigeon", "rabbit",   "bunnny", "squirl", "cormorant", "beetle", "hornet", "falcon", "iSnake", "sskunk", "goblin", "bugalo", "weasel" ]
random_int=random.randint(0,len(words)-1)
chosen_word=words[random_int]
print(f"random word = {chosen_word} ")
lenght=len(chosen_word)
display=[]
lives=6
for i in range(lenght):
     display+="_"
     
# print(display)
print(f" {" ".join(display)}") 
while lenght >=1 :
    lenght=lenght-1
    guess=input("Guess a letter ? ")
    for i in range(0,len(chosen_word)):
    
     letter=chosen_word[i]
     if letter==guess:
        display[i]=letter

    if guess not in chosen_word:
       lives-=1   
       if lives==0:
          lenght=0
          print("End of game") 


    print(f" {" ".join(display)}") 
    print(stages[lives])

print("End of game")
word=""
for i in display:
   word=word+i

if word==chosen_word:
   print("you won")
else:
   print("you loose")
# word=""
# print(newlist)
# for i in newlist:
#    word+=i + " "

# print(word)