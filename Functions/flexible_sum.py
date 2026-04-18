#Fexible summation
def sum(*args):
    total = 0
    for i in args:
        total += i
    return total 

print("sum is: ",sum(4,5,9,2,3,4,5))