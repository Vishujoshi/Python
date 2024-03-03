# Local vs global scope in Python
#  # global namespace
var_a = 75
def A_func():
     """This is global function and can be used anywhere """
     var_b=25
     print(var_a)
     print(var_b)
     
     def fun2():
          """This is local function to A-_func"""
          print("this is fun ")
          var_c=32
          print(var_a)
          print(var_b)
          print(var_c)
          
     fun2()
     

A_func()    
    
print(var_a)
# below throws error as var_b is local to functiion
# print(var_b)
# below throws error as fun2 is local to functiion
# fun2()

# --------NOTE---variables inside loops are not considered local scope and can be accessed outside