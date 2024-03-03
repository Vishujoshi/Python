# we can modify global variable inside function using keyword gloabal to acess global
enemies=1
def fune1():
    print(enemies)
def func():
    global enemies
    enemies+=1
    print(enemies)

fune1()
func()
# though we can use above method but is not preferred and we can use the below method to modify
def corect_fun():
    return enemies+1

print(corect_fun())