import math
#  Write a program​ quadratic.py to find the roots of the equation a*x*x+b*x+c.               

def find_root(a,b,c):
    delta = (b**2)-(4*a*c)
    root = []
    root_1 = (-b + math.pow(delta,1/2))/(2*a)
    root_2 = (-b - math.pow(delta,1/2))/(2*a)
    root.append(root_1)
    root.append(root_2)
    return root

#user input for value of a, b, c
print("Quadratic equation: a*x*x + b*x +c")
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

roots = find_root(a,b,c)
print(f"Root 1 of given quadratic equation: {roots[0]}")
print(f"Root 2 of given quadratic equation: {roots[1]}")

