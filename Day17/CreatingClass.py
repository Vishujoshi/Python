# class is created by using keyword class 
# pass is used to ignore the funtion and continue further 
class User:
    # init is used as a constructor and used to initializee attributes/variables
    # init function will be called when object is created
    def __init__(self,name,id):
        self.username=name    
        self.id=id
        self.followers=0 
        self.following=0
    
    def follow(self,user):
        self.following+=1
        user.followers+=1

# Creating an object of the class
user1=User("vishal",59)
user2=User("god", 90)
# adding attributes to class
# user1.name="Vishal"
# user1.id ="123"
user1.follow(user2)

print("user1")
print(user1.username)
print(user1.followers)
print(user1.following)
print("user2")
print(user2.username)
print(user2.followers)
print(user2.following)