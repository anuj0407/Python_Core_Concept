#lambda function : used for one - liner small operations

add = lambda x,y : x+y
print(add(4,10))

# HIGHER-ORDER FUNCTIONS
# Definition: A function that accepts another function as an argument OR returns a function.
# First-Order: Operates on data (numbers, strings).
# Higher-Order: Operates on other functions.
# Examples: map(), filter(), sorted(), and custom functions that return lambdas

# Making a calculator by using lambda function in a function named as calci
# calci will be the higher - order - function

def calci(operation):
    if(operation == "+"):
        return lambda a,b: a+b
    elif(operation == "-"):
        return lambda a,b: a-b
    elif(operation == "*"):
        return lambda a,b: a*b
    elif(operation == "/"):
        return lambda a,b: a/b
    else:
        return lambda a,b: "Invalid Operation!"
    
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
operation = input("Enter a operation(+ , - , * , /): ")
func = calci(operation)
print(func(a,b))
    

