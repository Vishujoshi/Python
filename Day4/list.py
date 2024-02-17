# List in python

fav_number=[1,2,4,5,6,7]
state_of_india =["Andhra Pradesh", "Himachal Pradesh", "Punjab", "Uttar Pradesh","Jammu","Mizoram", "Tamil Nadu","Haryana"]

print(state_of_india)

print(state_of_india[0])
print(state_of_india[-1])
state_of_india.append("VishalLand")
# -1 is used to print the vlaue at last index 
print(state_of_india[-1])
print(fav_number)
print(type(state_of_india))
print(type(fav_number))


# Nested List In  Python
Nested_list=[state_of_india,fav_number]
print(Nested_list)
# Below command Prints Ist list 5the element in list
print(Nested_list[0][4])
print(f"{len(Nested_list)}")