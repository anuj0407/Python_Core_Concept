import random
flip = int(input("Enter number of times you want to flip coin: "))
if(flip<=0):
    print("Invalid input")
headCount = 0
tailCount = 0
temp = flip
while(temp > 0):
    toss = random.random()
    if(toss<0.5):
        print ("Tail " ,end = "")
        tailCount += 1
    else:
        print ("Head " ,end = "")
        headCount += 1
    temp -= 1

print()
print(f"Percentage of Head: {(headCount/flip)*100} vs Percentage of Tail: {(tailCount/flip)*100}")


