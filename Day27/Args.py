def add(*args):
    sum=0
    for i in args:
        sum+=i
        
    return sum
        
print(add(1,3,4,5,5))


def calculate(n,**kwargs):
    print(kwargs["add"])
    # for key in kwargs: 
    #     print(key)
    # print(kwargs)
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)    
calculate(2,add=2,multiply=3)

class car:
    def __init__(self,**kw) :
        self.model=kw.get("model")
        self.company=kw.get("company")
        self.color=kw.get("color")
        self.speed=kw.get("speed")
        # below line creates error that why we use ge fun to have a optional arguments 
        # optional arguments means its our wish if we want to set value or not 
        # self.sign=kw["sign"]

mycar=car(model="Gtr",color="blue")
print(mycar.model)
print(mycar.color)