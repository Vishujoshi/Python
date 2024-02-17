def greet():
  print("Hello")
  print("my name is - vishal")
  print("hru")

greet()

# passing values in function
def greety(name):
  print(f"Hello {name}")
  print(f"my name is - {name}")
  print(f"hru {name}")
  

greety("Vishal")
# passing 2 parameterd
def greety(name,location):
  print(f"Hello {name}")
  print(f"i  am from  - {location}")
 
  
# positional Arguments
greety("Vishal","India")
#Keyword arguments
greety(location="Vishal",name="India")