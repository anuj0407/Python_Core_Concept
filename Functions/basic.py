import math
#functions
'''
python have 3 types of functions:
1. built-in functions : these are the functions that are already defined in python and can be used directly without any need of defining them. examples include print(), len(), type(), etc.
2. built-in modules functions : these are the functions that are defined in built-in modules and can be used by importing those modules. examples include math.sqrt(), random.randint(), etc.
3. user-defined functions : these are the functions that are defined by the user as per their requirements.
'''

#built-in functions
print("---- built -in functions ----")
print("Hello World!")
stat = "Learning functions in python"
print(len(stat))

#built-in modules functions
print("---- built -in modules functions ----")
print(math.sqrt(9))
print(math.pow(2, 3))

#user-defined functions
print("---- user-defined functions ----")
def greet(name): #function definition , name is the parameter or argument of the function
    print("Hello, " + name + "!") #function body
    print("Welcome to learning functions in python.") #function body

greet("Anuj")#function call