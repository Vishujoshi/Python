import random
import PracticeModeule as Practice

rand_int1=random.randint(1,3)
rand_int2=random.randint(1,3)

# random number B/W 0-1 ie 0.212,0.21; 0.313
random_float=random.random()
print (f"your  first random int is {rand_int1}")
print (f"your  first random int is {random_float}")
# Can use the mmodule using below commands I.e  -m ModuleName.function or varaible
print(f"vlaue of Pi is {Practice.pi}")

love_score=random.randint(1,100)
print(f"Your love score is {love_score}")