import art
def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2


# def calculate(one,operand,two):
#     if operand=="+":
#       output = add(one,two)
#       return output
#     if operand=="-":
#       output = subtract(one,two)
#       return output
#     if operand=="*":
#       output = multiply(one,two)
#       return output
#     if operand=="/":
#       output = divide(one,two)
#       return output
operations={
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}
# calculator Function Here is recurrsion function
def calculator():
    print(art.logo)
    number1=float(input("Enter 1st number \n"))
    contin=True
    while contin:
        for operator in operations:
            print(operator)
        operator_choosed=input("Choose the Operotor from above :  ")
        number2=float(input("Enter next number \n "))
        operations_function=operations[operator_choosed]
        answer=operations_function(number1,number2)
        print(f"{number1} {operator_choosed} {number2} = {operations_function(number1,number2)}")
        if input(f"Wourld you like continue at {answer} or exit ? type y or n to start a new calulation: ")=="y":
            number1=answer
        else:
            contin=False
            calculator()

calculator()

