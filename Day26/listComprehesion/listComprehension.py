onelist=[1,3,4]
# newList=[newitem for item in List]
newList=[n+1 for n in onelist]
print(newList)

name="vishal"
namelist=[letter for letter in name]
print(namelist)

rangeList=[num*2 for num in range(1,5)]
print(rangeList)

names=["vishal","Amit","Arun","nitika","abhi","sanam","salim","ayush","avinash"]

short_nameList=[name for name in names if len(name)<=4]
print(short_nameList)

uppercase_namelist=[name.upper() for name in names if len(name)>4]
print(uppercase_namelist)