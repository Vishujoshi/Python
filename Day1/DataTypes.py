#Data Types
# String Data Type
print ("Hello" + "World")
# Integer Data Type
print (1+2)

# Float Data Type
print(1.2 + 234.55)
# Boolean Data Type - True or False
a=False
print (a)

# type is used used to check the data type 
print(type(a))

# Type casting - To covert data types using inbuilts classes
num_char=len(input("what is your name? "))
print(num_char)
print ("Your name has " +  str(num_char) + " charcaters")


# F-strings int Python

weight=72
height=5.5
name="Vishal"
# print("My Name is " + name  + " height is " + height)
# above line Returns Error so we use F string--
# print("My Name is " + name  + " height is " + height)
#           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~
# TypeError: can only concatenate str (not "float") to str
print(f'My name Is {name}, height is {height} & weight is {weight}')
